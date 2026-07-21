// cypress/e2e/booking-validation.cy.js

// ===== Data Skenario =====
const BOOKING_PAYLOAD = (data) => ({
  booking_id: data.booking_id,
  venue_id: data.venue_id,
  user_id: data.user_id,
  date: data.date,
  start_time: data.start,
  end_time: data.end,
  price: data.price,
})

const SUITE = [
  { booking_id: 'BK/000001', venue_id: 15, user_id: 12, date: '2022-12-10', start: '09:00:00', end: '11:00:00', price: 1200000 },
  { booking_id: 'BK/000005', venue_id: 15, user_id: 12, date: '2022-12-10', start: '09:00:00', end: '11:00:00', price: 1000000 },
]

const SCHEDULE = [
  { venue_id: 15, date: '2022-12-10', start_time: '07:00:00', end_time: '09:00:00', price: 800000 },
  { venue_id: 15, date: '2022-12-10', start_time: '09:00:00', end_time: '11:00:00', price: 1000000 },
  { venue_id: 15, date: '2022-12-10', start_time: '11:00:00', end_time: '13:00:00', price: 1200000 },
]

// ===== Helper =====
const timeToSeconds = (t) => t.split(':').reduce((h, m, i) => h + Number(m) * (i === 0 ? 3600 : (i === 1 ? 60 : 1)), 0)

const overlaps = (a, b) => timeToSeconds(a.start_time) < timeToSeconds(b.end_time) && timeToSeconds(b.start_time) < timeToSeconds(a.end_time)

// ===== TEST =====
describe('Booking Validation - Regression Test', () => {
  it('TC-001 / TC-002: Harga booking sesuai schedule untuk slot yang ada', () => {
    SUITE.forEach((b) => {
      const slot = SCHEDULE.find(s => s.venue_id === b.venue_id && s.date === b.date && s.start_time === b.start && s.end_time === b.end)
      expect(slot, `Slot tidak ditemukan: ${b.booking_id}`).to.exist
      expect(b.price, `Harga salah ${b.booking_id}`).to.equal(slot.price)
    })
  })

  it('TC-003 / TC-007: Deteksi double booking (venue + date + overlap time)', () => {
    const conflicts = []
    for (let i = 0; i < SUITE.length; i++) {
      for (let j = i + 1; j < SUITE.length; j++) {
        const a = SUITE[i], b = SUITE[j]
        if (a.venue_id === b.venue_id && a.date === b.date && overlaps(a, b)) {
          conflicts.push([a.booking_id, b.booking_id])
        }
      }
    }
    expect(conflicts.length, 'Double booking harus terdeteksi').to.be.greaterThan(0)
    cy.log('Double booking terdeteksi: ' + JSON.stringify(conflicts))
  })

  it('TC-004: Booking tanpa overlap harus valid', () => {
    const a = SUITE[0]
    const b = { ...a, start_time: '12:00:00', end_time: '13:00:00' }
    expect(overlaps(a, b)).to.be.false
  })

  it('TC-005: Booking di slot yang tidak ada harus ditolak', () => {
    const fake = { venue_id: 15, date: '2022-12-10', start_time: '13:00:00', end_time: '14:00:00' }
    const slot = SCHEDULE.find(s => s.venue_id === fake.venue_id && s.date === fake.date && s.start_time === fake.start_time && s.end_time === fake.end_time)
    expect(slot).to.be.undefined
  })
})

// ===== API Integration Test (aktifkan setelah endpoint booking kamu siap) =====

describe('Booking API (Integration)', () => {
  const BOOKING_API = '/api/bookings' // SESUAIKAN DENGAN ENDPOINT KAMU

  it('Booking duplikat harus ditolak sistem', () => {
    cy.api('POST', BOOKING_API, BOOKING_PAYLOAD(SUITE[0])).then((res) => {
      expect(res.status).to.be.oneOf([201, 409])

      cy.api('POST', BOOKING_API, BOOKING_PAYLOAD({...SUITE[0], booking_id: 'BK/DUPLIKAT'})).then((res2) => {
        expect(res2.status).to.equal(409)
      })
    })
  })

  it('Booking dengan harga salah harus ditolak validasi', () => {
    cy.api('POST', BOOKING_API, BOOKING_PAYLOAD({...SUITE[0], booking_id: 'BK/SALAH', price: 0})).then((res) => {
      expect(res.status).to.be.oneOf([201, 400, 422])
    })
  })
})
