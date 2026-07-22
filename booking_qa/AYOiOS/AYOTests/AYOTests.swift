import XCTest
class AYOTests: XCTestCase {
    override func setUpWithError() throws { }
    override func tearDownWithError() throws { }
}

extension AYOTests {
    func testLaunch() throws {
        let app = XCUIApplication()
        app.launch()
        XCUIDevice.shared.orientation = .portrait
        XCTAssertTrue(app.buttons["Allow"].waitForExistence(timeout: 5) == false)
    }
}
