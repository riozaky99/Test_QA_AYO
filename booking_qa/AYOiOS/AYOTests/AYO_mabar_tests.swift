import XCTest
class AYO_mabar_tests: AYOTests {
    func testMainBarengUIElementsExist() throws {
        let app = XCUIApplication()
        app.launch()
        XCTAssertTrue(app.staticTexts["EVENT MAIN BARENG"].waitForExistence(timeout: 10))
        XCTAssertTrue(app.buttons["Cari mabar"].waitForExistence(timeout: 10) || app.buttons["Filter"].waitForExistence(timeout: 10))
    }
}
