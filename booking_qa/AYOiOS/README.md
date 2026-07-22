# AYO iOS Automation

XCUITest untuk aplikasi mobile AYO. Dari siap pakai reward, maka hanya runtunan init yang cucu: uji alur **Book Venue Booking** dan **Create Game Time**.

## Prasyarat
- Xcode 26.6+
- Simulator iOS: `iPhone 17 Pro` atau `iPhone Air`
- Aplikasi AYO sudah terinstall di simulator/device
- Apple ID untuk signing

## Struktur
- `AYOTests/` - Test target dan test case
- `AYOApp/` - App wrapper untuk testing

## Menjalankan
```bash
cd /Users/RioZ/Ayo_technical_test/booking_qa/AYOiOS
xcodebuild test -project AYO.xcodeproj -scheme AYO -destination 'platform=iOS Simulator,name=iPhone 17 Pro'
```

Atau buka `AYO.xcodeproj` di Xcode, pilih scheme dan simulator, lalu tekan `Cmd+U`.
