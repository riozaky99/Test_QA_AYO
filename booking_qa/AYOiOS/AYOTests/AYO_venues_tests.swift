import XCTest
class AYO_venues_tests: AYOTests {
    let app = XCUIApplication()
    func testVenuesListingElementsExist() throws {
        app.launch()
        XCTAssertTrue(app.staticTexts["BOOKING LAPANGAN ONLINE TERBAIK"].waitForExistence(timeout: 10))
        XCTAssertTrue(app.buttons["Pilih Cabang Olahraga"].waitForExistence(timeout: 10))
    }
}
