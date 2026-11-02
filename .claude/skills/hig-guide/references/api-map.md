# API map: guidance to implementation

339 references pulled from every page's 'Developer documentation' section: the exact SwiftUI, UIKit, AppKit, and framework-specific API that implements each piece of guidance, plus the frameworks and guides a page points to. Entries marked framework/guide are the framework itself (AVFoundation, App Intents) or an Apple how-to, not a single symbol.

Use this to go from a design decision straight to the right API instead of guessing at a class or modifier name. When reviewing code, check the symbol used against what the HIG actually names here — a hand-rolled view where a system API exists is itself worth flagging.

---

## By component

**Accessibility** <sub>[Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)</sub>
- [Building accessible apps](https://developer.apple.com/accessibility/) <sub>framework/guide</sub>
- [Accessibility](https://developer.apple.com/documentation/accessibility) <sub>framework/guide</sub>
- [Overview of Accessibility Nutrition Labels](https://devcms.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels) <sub>framework/guide</sub>

**Action sheets** <sub>[Action sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets)</sub>
- [confirmationDialog(_:isPresented:titleVisibility:actions:)](https://developer.apple.com/documentation/swiftui/view/confirmationdialog(_:ispresented:titlevisibility:actions:)-46zbb) — SwiftUI
- [UIAlertController.Style.actionSheet](https://developer.apple.com/documentation/uikit/uialertcontroller/style/actionsheet) — UIKit

**Activity rings** <sub>[Activity rings](https://developer.apple.com/design/human-interface-guidelines/activity-rings)</sub>
- [HKActivityRingView](https://developer.apple.com/documentation/healthkitui/hkactivityringview) — HealthKit

**Activity views** <sub>[Activity views](https://developer.apple.com/design/human-interface-guidelines/activity-views)</sub>
- [UIActivityViewController](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller) — UIKit
- [UIActivity](https://developer.apple.com/documentation/uikit/uiactivity) — UIKit
- [App Extension Support](https://developer.apple.com/documentation/foundation/app-extension-support) — Foundation

**AirPlay** <sub>[AirPlay](https://developer.apple.com/design/human-interface-guidelines/airplay)</sub>
- [AVFoundation](https://developer.apple.com/documentation/avfoundation) <sub>framework/guide</sub>
- [AVKit](https://developer.apple.com/documentation/avkit) <sub>framework/guide</sub>

**Alerts** <sub>[Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts)</sub>
- [alert(_:isPresented:actions:)](https://developer.apple.com/documentation/swiftui/view/alert(_:ispresented:actions:)-1bkka) — SwiftUI
- [UIAlertController](https://developer.apple.com/documentation/uikit/uialertcontroller) — UIKit
- [NSAlert](https://developer.apple.com/documentation/appkit/nsalert) — AppKit

**Always On** <sub>[Always On](https://developer.apple.com/design/human-interface-guidelines/always-on)</sub>
- [Designing your app for the Always On state](https://developer.apple.com/documentation/watchos-apps/designing-your-app-for-the-always-on-state) — watchOS apps

**App Clips** <sub>[App Clips](https://developer.apple.com/design/human-interface-guidelines/app-clips)</sub>
- [App Clips](https://developer.apple.com/documentation/appclip) <sub>framework/guide</sub>
- [App Store Connect](https://appstoreconnect.apple.com/) <sub>framework/guide</sub>

**App Shortcuts** <sub>[App Shortcuts](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts)</sub>
- [App Intents](https://developer.apple.com/documentation/appintents) <sub>framework/guide</sub>
- [SiriKit](https://developer.apple.com/documentation/sirikit) <sub>framework/guide</sub>
- [Getting started with the App Intents framework](https://developer.apple.com/documentation/appintents/getting-started-with-the-app-intents-framework) — App Intents
- [Defining app entities for your custom data types](https://developer.apple.com/documentation/appintents/defining-app-entities-for-your-custom-data-types) — App Intents

**App icons** <sub>[App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons)</sub>
- [Creating your app icon using Icon Composer](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer) <sub>framework/guide</sub>
- [Configuring your app icon using an asset catalog](https://developer.apple.com/documentation/xcode/configuring-your-app-icon) <sub>framework/guide</sub>

**Apple Pay** <sub>[Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay)</sub>
- [Apple Pay](https://developer.apple.com/documentation/passkit/apple-pay) — PassKit
- [Apple Pay on the Web](https://developer.apple.com/documentation/applepayontheweb) <sub>framework/guide</sub>
- [WKInterfacePaymentButton](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton) — WatchKit

**Apple Pencil and Scribble** <sub>[Apple Pencil and Scribble](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble)</sub>
- [PencilKit](https://developer.apple.com/documentation/pencilkit) <sub>framework/guide</sub>
- [PaperKit](https://developer.apple.com/documentation/paperkit) <sub>framework/guide</sub>

**Augmented reality** <sub>[Augmented reality](https://developer.apple.com/design/human-interface-guidelines/augmented-reality)</sub>
- [ARKit](https://developer.apple.com/documentation/arkit) <sub>framework/guide</sub>

**Boxes** <sub>[Boxes](https://developer.apple.com/design/human-interface-guidelines/boxes)</sub>
- [GroupBox](https://developer.apple.com/documentation/swiftui/groupbox) — SwiftUI
- [NSBox](https://developer.apple.com/documentation/appkit/nsbox) — AppKit

**Buttons** <sub>[Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons)</sub>
- [Button](https://developer.apple.com/documentation/swiftui/button) — SwiftUI
- [UIButton](https://developer.apple.com/documentation/uikit/uibutton) — UIKit
- [NSButton](https://developer.apple.com/documentation/appkit/nsbutton) — AppKit

**Camera Control** <sub>[Camera Control](https://developer.apple.com/design/human-interface-guidelines/camera-control)</sub>
- [Enhancing your app experience with the Camera Control](https://developer.apple.com/documentation/avfoundation/enhancing-your-app-experience-with-the-camera-control) — AVFoundation
- [AVCaptureControl](https://developer.apple.com/documentation/avfoundation/avcapturecontrol) — AVFoundation
- [LockedCameraCapture](https://developer.apple.com/documentation/lockedcameracapture) <sub>framework/guide</sub>

**CarPlay** <sub>[CarPlay](https://developer.apple.com/design/human-interface-guidelines/carplay)</sub>
- [CarPlay App Programming Guide](https://developer.apple.com/carplay/documentation/CarPlay-App-Programming-Guide.pdf) <sub>framework/guide</sub>

**CareKit** <sub>[CareKit](https://developer.apple.com/design/human-interface-guidelines/carekit)</sub>
- [CareKit](https://carekit-apple.github.io/CareKit/documentation/carekit) <sub>framework/guide</sub>
- [Research & Care > Developers](https://www.researchandcare.org/developers/) <sub>framework/guide</sub>
- [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy) — HealthKit
- [HealthKit](https://developer.apple.com/documentation/healthkit) <sub>framework/guide</sub>
- [ResearchKit GitHub project](https://github.com/ResearchKit/ResearchKit) <sub>framework/guide</sub>

**Charting data** <sub>[Charting data](https://developer.apple.com/design/human-interface-guidelines/charting-data)</sub>
- [Swift Charts](https://developer.apple.com/documentation/charts) <sub>framework/guide</sub>

**Charts** <sub>[Charts](https://developer.apple.com/design/human-interface-guidelines/charts)</sub>
- [Swift Charts](https://developer.apple.com/documentation/charts) <sub>framework/guide</sub>

**Collaboration and sharing** <sub>[Collaboration and sharing](https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing)</sub>
- [Shared with You](https://developer.apple.com/documentation/sharedwithyou) <sub>framework/guide</sub>
- [ShareLink](https://developer.apple.com/documentation/swiftui/sharelink) — SwiftUI

**Collections** <sub>[Collections](https://developer.apple.com/design/human-interface-guidelines/collections)</sub>
- [UICollectionView](https://developer.apple.com/documentation/uikit/uicollectionview) — UIKit
- [NSCollectionView](https://developer.apple.com/documentation/appkit/nscollectionview) — AppKit

**Color** <sub>[Color](https://developer.apple.com/design/human-interface-guidelines/color)</sub>
- [Color](https://developer.apple.com/documentation/swiftui/color) — SwiftUI
- [UIColor](https://developer.apple.com/documentation/uikit/uicolor) — UIKit
- [Color](https://developer.apple.com/documentation/appkit/color) — AppKit

**Color wells** <sub>[Color wells](https://developer.apple.com/design/human-interface-guidelines/color-wells)</sub>
- [UIColorWell](https://developer.apple.com/documentation/uikit/uicolorwell) — UIKit
- [UIColorPickerViewController](https://developer.apple.com/documentation/uikit/uicolorpickerviewcontroller) — UIKit
- [NSColorWell](https://developer.apple.com/documentation/appkit/nscolorwell) — AppKit
- [Color Programming Topics](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/DrawColor/DrawColor.html) <sub>framework/guide</sub>

**Column views** <sub>[Column views](https://developer.apple.com/design/human-interface-guidelines/column-views)</sub>
- [NSBrowser](https://developer.apple.com/documentation/appkit/nsbrowser) — AppKit

**Combo boxes** <sub>[Combo boxes](https://developer.apple.com/design/human-interface-guidelines/combo-boxes)</sub>
- [NSComboBox](https://developer.apple.com/documentation/appkit/nscombobox) — AppKit

**Complications** <sub>[Complications](https://developer.apple.com/design/human-interface-guidelines/complications)</sub>
- [WidgetKit](https://developer.apple.com/documentation/widgetkit) <sub>framework/guide</sub>

**Context menus** <sub>[Context menus](https://developer.apple.com/design/human-interface-guidelines/context-menus)</sub>
- [contextMenu(menuItems:)](https://developer.apple.com/documentation/swiftui/view/contextmenu(menuitems:)) — SwiftUI
- [UIContextMenuInteraction](https://developer.apple.com/documentation/uikit/uicontextmenuinteraction) — UIKit
- [popUpContextMenu(_:with:for:)](https://developer.apple.com/documentation/appkit/nsmenu/popupcontextmenu(_:with:for:)) — AppKit

**Controls** <sub>[Controls](https://developer.apple.com/design/human-interface-guidelines/controls)</sub>
- [LockedCameraCapture](https://developer.apple.com/documentation/lockedcameracapture) <sub>framework/guide</sub>
- [WidgetKit](https://developer.apple.com/documentation/widgetkit) <sub>framework/guide</sub>

**Designing for games** <sub>[Designing for games](https://developer.apple.com/design/human-interface-guidelines/designing-for-games)</sub>
- [Games Pathway](https://developer.apple.com/games/get-started/) <sub>framework/guide</sub>
- [Create games for Apple platforms](https://developer.apple.com/games/) <sub>framework/guide</sub>

**Designing for iOS** <sub>[Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios)</sub>
- [iOS Pathway](https://developer.apple.com/ios/get-started/) <sub>framework/guide</sub>

**Designing for iPadOS** <sub>[Designing for iPadOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados)</sub>
- [iPadOS Pathway](https://developer.apple.com/ipados/get-started/) <sub>framework/guide</sub>

**Designing for macOS** <sub>[Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos)</sub>
- [macOS Pathway](https://developer.apple.com/macos/get-started/) <sub>framework/guide</sub>

**Designing for tvOS** <sub>[Designing for tvOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos)</sub>
- [tvOS Pathway](https://developer.apple.com/tvos/get-started/) <sub>framework/guide</sub>

**Designing for visionOS** <sub>[Designing for visionOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos)</sub>
- [visionOS Pathway](https://developer.apple.com/visionos/get-started/) <sub>framework/guide</sub>
- [Creating your first visionOS app](https://developer.apple.com/documentation/visionos/creating-your-first-visionos-app) <sub>framework/guide</sub>

**Designing for watchOS** <sub>[Designing for watchOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos)</sub>
- [watchOS Pathway](https://developer.apple.com/watchos/get-started/) <sub>framework/guide</sub>

**Digit entry views** <sub>[Digit entry views](https://developer.apple.com/design/human-interface-guidelines/digit-entry-views)</sub>
- [TVDigitEntryViewController](https://developer.apple.com/documentation/tvuikit/tvdigitentryviewcontroller) — TVUIKit

**Digital Crown** <sub>[Digital Crown](https://developer.apple.com/design/human-interface-guidelines/digital-crown)</sub>
- [WKCrownDelegate](https://developer.apple.com/documentation/watchkit/wkcrowndelegate) — WatchKit

**Disclosure controls** <sub>[Disclosure controls](https://developer.apple.com/design/human-interface-guidelines/disclosure-controls)</sub>
- [DisclosureGroup](https://developer.apple.com/documentation/swiftui/disclosuregroup) — SwiftUI
- [NSButton.BezelStyle.disclosure](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/disclosure) — AppKit
- [NSButton.BezelStyle.pushDisclosure](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/pushdisclosure) — AppKit

**Dock menus** <sub>[Dock menus](https://developer.apple.com/design/human-interface-guidelines/dock-menus)</sub>
- [applicationDockMenu(_:)](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationdockmenu(_:)) — AppKit

**Drag and drop** <sub>[Drag and drop](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop)</sub>
- [Drag and drop](https://developer.apple.com/documentation/uikit/drag-and-drop) — UIKit
- [Drag and Drop](https://developer.apple.com/documentation/appkit/drag-and-drop) — AppKit
- [File Provider](https://developer.apple.com/documentation/fileprovider) <sub>framework/guide</sub>

**Edit menus** <sub>[Edit menus](https://developer.apple.com/design/human-interface-guidelines/edit-menus)</sub>
- [UIEditMenuInteraction](https://developer.apple.com/documentation/uikit/uieditmenuinteraction) — UIKit
- [NSMenu](https://developer.apple.com/documentation/appkit/nsmenu) — AppKit

**Entering data** <sub>[Entering data](https://developer.apple.com/design/human-interface-guidelines/entering-data)</sub>
- [Input events](https://developer.apple.com/documentation/swiftui/input-events) — SwiftUI

**Eyes** <sub>[Eyes](https://developer.apple.com/design/human-interface-guidelines/eyes)</sub>
- [Adopting best practices for privacy and user preferences](https://developer.apple.com/documentation/visionos/adopting-best-practices-for-privacy) — visionOS

**Feedback** <sub>[Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback)</sub>
- [Animation and haptics](https://developer.apple.com/documentation/uikit/animation-and-haptics) — UIKit

**File management** <sub>[File management](https://developer.apple.com/design/human-interface-guidelines/file-management)</sub>
- [Documents](https://developer.apple.com/documentation/swiftui/documents) — SwiftUI

**Focus and selection** <sub>[Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection)</sub>
- [Focus Attributes](https://developer.apple.com/documentation/tvml/focus-attributes) — TVML
- [Focus-based navigation](https://developer.apple.com/documentation/uikit/focus-based-navigation) — UIKit
- [About focus interactions for Apple TV](https://developer.apple.com/documentation/uikit/about-focus-interactions-for-apple-tv) — UIKit

**Game Center** <sub>[Game Center](https://developer.apple.com/design/human-interface-guidelines/game-center)</sub>
- [GameKit](https://developer.apple.com/documentation/gamekit) <sub>framework/guide</sub>
- [Creating activities for your game](https://developer.apple.com/documentation/gamekit/creating-activities-for-your-game) <sub>framework/guide</sub>
- [Creating engaging challenges from leaderboards](https://developer.apple.com/documentation/gamekit/creating-engaging-challenges-from-leaderboards) <sub>framework/guide</sub>
- [Create games for Apple platforms](https://developer.apple.com/games/) <sub>framework/guide</sub>
- [Game Porting Toolkit](https://developer.apple.com/games/game-porting-toolkit/) <sub>framework/guide</sub>

**Game controls** <sub>[Game controls](https://developer.apple.com/design/human-interface-guidelines/game-controls)</sub>
- [Create games for Apple platforms](https://developer.apple.com/games/) <sub>framework/guide</sub>
- [Touch Controller](https://developer.apple.com/documentation/touchcontroller) <sub>framework/guide</sub>
- [Game Controller](https://developer.apple.com/documentation/gamecontroller) <sub>framework/guide</sub>

**Gauges** <sub>[Gauges](https://developer.apple.com/design/human-interface-guidelines/gauges)</sub>
- [Gauge](https://developer.apple.com/documentation/swiftui/gauge) — SwiftUI
- [NSLevelIndicator](https://developer.apple.com/documentation/appkit/nslevelindicator) — AppKit

**Generative AI** <sub>[Generative AI](https://developer.apple.com/design/human-interface-guidelines/generative-ai)</sub>
- [Apple Intelligence and machine learning](https://developer.apple.com/documentation/technologyoverviews/ai-machine-learning) <sub>framework/guide</sub>
- [Foundation Models](https://developer.apple.com/documentation/foundationmodels) <sub>framework/guide</sub>
- [Core AI](https://developer.apple.com/documentation/coreai) <sub>framework/guide</sub>

**Gestures** <sub>[Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures)</sub>
- [Gestures](https://developer.apple.com/documentation/swiftui/gestures) — SwiftUI
- [UITouch](https://developer.apple.com/documentation/uikit/uitouch) — UIKit

**Going full screen** <sub>[Going full screen](https://developer.apple.com/design/human-interface-guidelines/going-full-screen)</sub>
- [fullScreenCover(item:onDismiss:content:)](https://developer.apple.com/documentation/swiftui/view/fullscreencover(item:ondismiss:content:)) — SwiftUI
- [NSScreen](https://developer.apple.com/documentation/appkit/nsscreen) — AppKit
- [NSWindow.CollectionBehavior](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior-swift.struct) — AppKit
- [Managing your game window for Metal in macOS](https://developer.apple.com/documentation/metal/managing-your-game-window-for-metal-in-macos) — Swift, Objective-C

**Gyroscope and accelerometer** <sub>[Gyroscope and accelerometer](https://developer.apple.com/design/human-interface-guidelines/gyro-and-accelerometer)</sub>
- [Getting processed device-motion data](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data) — Core Motion

**HealthKit** <sub>[HealthKit](https://developer.apple.com/design/human-interface-guidelines/healthkit)</sub>
- [HealthKit](https://developer.apple.com/documentation/healthkit) <sub>framework/guide</sub>
- [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy) — HealthKit

**Home Screen quick actions** <sub>[Home Screen quick actions](https://developer.apple.com/design/human-interface-guidelines/home-screen-quick-actions)</sub>
- [Add Home Screen quick actions](https://developer.apple.com/documentation/uikit/add-home-screen-quick-actions) — UIKit

**HomeKit** <sub>[HomeKit](https://developer.apple.com/design/human-interface-guidelines/homekit)</sub>
- [HomeKit](https://developer.apple.com/documentation/homekit) <sub>framework/guide</sub>

**ID Verifier** <sub>[ID Verifier](https://developer.apple.com/design/human-interface-guidelines/id-verifier)</sub>
- [Adopting the Verifier API in your iPhone app](https://developer.apple.com/documentation/proximityreader/adopting-the-verifier-api-in-your-iphone-app) — ProximityReader

**Image views** <sub>[Image views](https://developer.apple.com/design/human-interface-guidelines/image-views)</sub>
- [Image](https://developer.apple.com/documentation/swiftui/image) — SwiftUI
- [UIImageView](https://developer.apple.com/documentation/uikit/uiimageview) — UIKit
- [NSImageView](https://developer.apple.com/documentation/appkit/nsimageview) — AppKit

**Image wells** <sub>[Image wells](https://developer.apple.com/design/human-interface-guidelines/image-wells)</sub>
- [NSImageView](https://developer.apple.com/documentation/appkit/nsimageview) — AppKit

**Images** <sub>[Images](https://developer.apple.com/design/human-interface-guidelines/images)</sub>
- [Drawing sharp layer-based content in visionOS](https://developer.apple.com/documentation/visionos/drawing-sharp-layer-based-content) — visionOS
- [Images](https://developer.apple.com/documentation/swiftui/images) — SwiftUI
- [UIImageView](https://developer.apple.com/documentation/uikit/uiimageview) — UIKit
- [NSImageView](https://developer.apple.com/documentation/appkit/nsimageview) — AppKit

**Immersive experiences** <sub>[Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences)</sub>
- [Creating fully immersive experiences in your app](https://developer.apple.com/documentation/visionos/creating-fully-immersive-experiences) — visionOS
- [Incorporating real-world surroundings in an immersive experience](https://developer.apple.com/documentation/visionos/incorporating-real-world-surroundings-in-an-immersive-experience) — visionOS
- [ImmersionStyle](https://developer.apple.com/documentation/swiftui/immersionstyle) — visionOS
- [Immersive spaces](https://developer.apple.com/documentation/swiftui/immersive-spaces) — SwiftUI

**In-app purchase** <sub>[In-app purchase](https://developer.apple.com/design/human-interface-guidelines/in-app-purchase)</sub>
- [In-App Purchase](https://developer.apple.com/documentation/storekit/in-app-purchase) — StoreKit

**Inclusion** <sub>[Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion)</sub>
- [Localization](https://developer.apple.com/documentation/xcode/localization) — Xcode

**Keyboards** <sub>[Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards)</sub>
- [KeyboardShortcut](https://developer.apple.com/documentation/swiftui/keyboardshortcut) — SwiftUI
- [Input events](https://developer.apple.com/documentation/swiftui/input-events) — SwiftUI
- [Handling key presses made on a physical keyboard](https://developer.apple.com/documentation/uikit/handling-key-presses-made-on-a-physical-keyboard) — UIKit
- [Mouse, Keyboard, and Trackpad](https://developer.apple.com/documentation/appkit/mouse-keyboard-and-trackpad) — AppKit

**Labels** <sub>[Labels](https://developer.apple.com/design/human-interface-guidelines/labels)</sub>
- [Label](https://developer.apple.com/documentation/swiftui/label) — SwiftUI
- [Text](https://developer.apple.com/documentation/swiftui/text) — SwiftUI
- [UILabel](https://developer.apple.com/documentation/uikit/uilabel) — UIKit
- [NSTextField](https://developer.apple.com/documentation/appkit/nstextfield) — AppKit

**Launching** <sub>[Launching](https://developer.apple.com/design/human-interface-guidelines/launching)</sub>
- [Specifying your app’s launch screen](https://developer.apple.com/documentation/xcode/specifying-your-apps-launch-screen) — Xcode
- [Responding to the launch of your app](https://developer.apple.com/documentation/uikit/responding-to-the-launch-of-your-app) — UIKit

**Layout** <sub>[Layout](https://developer.apple.com/design/human-interface-guidelines/layout)</sub>
- [Composing custom layouts with SwiftUI](https://developer.apple.com/documentation/swiftui/composing-custom-layouts-with-swiftui) — SwiftUI

**Lists and tables** <sub>[Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables)</sub>
- [List](https://developer.apple.com/documentation/swiftui/list) — SwiftUI
- [Tables](https://developer.apple.com/documentation/swiftui/tables) — SwiftUI
- [UITableView](https://developer.apple.com/documentation/uikit/uitableview) — UIKit
- [NSTableView](https://developer.apple.com/documentation/appkit/nstableview) — AppKit

**Live Activities** <sub>[Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities)</sub>
- [ActivityKit](https://developer.apple.com/documentation/activitykit) <sub>framework/guide</sub>
- [SwiftUI](https://developer.apple.com/documentation/swiftui) <sub>framework/guide</sub>
- [WidgetKit](https://developer.apple.com/documentation/widgetkit) <sub>framework/guide</sub>
- [Developing a WidgetKit strategy](https://developer.apple.com/documentation/widgetkit/developing-a-widgetkit-strategy) — WidgetKit

**Live Photos** <sub>[Live Photos](https://developer.apple.com/design/human-interface-guidelines/live-photos)</sub>
- [PHLivePhoto](https://developer.apple.com/documentation/photos/phlivephoto) — PhotoKit
- [LivePhotosKit JS](https://developer.apple.com/documentation/livephotoskitjs) — LivePhotosKit JS

**Loading** <sub>[Loading](https://developer.apple.com/design/human-interface-guidelines/loading)</sub>
- [Background Assets](https://developer.apple.com/documentation/backgroundassets) <sub>framework/guide</sub>

**Lockups** <sub>[Lockups](https://developer.apple.com/design/human-interface-guidelines/lockups)</sub>
- [TVLockupView](https://developer.apple.com/documentation/tvuikit/tvlockupview) — TVUIKit
- [TVLockupHeaderFooterView](https://developer.apple.com/documentation/tvuikit/tvlockupheaderfooterview) — TVUIKit

**Mac Catalyst** <sub>[Mac Catalyst](https://developer.apple.com/design/human-interface-guidelines/mac-catalyst)</sub>
- [Mac Catalyst](https://developer.apple.com/documentation/uikit/mac-catalyst) — UIKit

**Machine learning** <sub>[Machine learning](https://developer.apple.com/design/human-interface-guidelines/machine-learning)</sub>
- [Apple Intelligence and machine learning](https://developer.apple.com/documentation/technologyoverviews/ai-machine-learning) <sub>framework/guide</sub>
- [Create ML](https://developer.apple.com/documentation/createml) <sub>framework/guide</sub>
- [Core ML](https://developer.apple.com/documentation/coreml) <sub>framework/guide</sub>

**Managing accounts** <sub>[Managing accounts](https://developer.apple.com/design/human-interface-guidelines/managing-accounts)</sub>
- [Supporting passkeys](https://developer.apple.com/documentation/authenticationservices/supporting-passkeys) — Authentication Services

**Managing notifications** <sub>[Managing notifications](https://developer.apple.com/design/human-interface-guidelines/managing-notifications)</sub>
- [User Notifications](https://developer.apple.com/documentation/usernotifications) <sub>framework/guide</sub>

**Maps** <sub>[Maps](https://developer.apple.com/design/human-interface-guidelines/maps)</sub>
- [MapKit](https://developer.apple.com/documentation/mapkit) <sub>framework/guide</sub>
- [MapKit JS](https://developer.apple.com/documentation/mapkitjs) <sub>framework/guide</sub>
- [Indoor Mapping Data Format](https://register.apple.com/resources/imdf/) <sub>framework/guide</sub>

**Materials** <sub>[Materials](https://developer.apple.com/design/human-interface-guidelines/materials)</sub>
- [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass) <sub>framework/guide</sub>
- [glassEffect(_:in:)](https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:)) — SwiftUI
- [Material](https://developer.apple.com/documentation/swiftui/material) — SwiftUI
- [UIVisualEffectView](https://developer.apple.com/documentation/uikit/uivisualeffectview) — UIKit
- [NSVisualEffectView](https://developer.apple.com/documentation/appkit/nsvisualeffectview) — AppKit

**Menus** <sub>[Menus](https://developer.apple.com/design/human-interface-guidelines/menus)</sub>
- [Menu](https://developer.apple.com/documentation/swiftui/menu) — SwiftUI
- [Menus and shortcuts](https://developer.apple.com/documentation/uikit/menus-and-shortcuts) — UIKit
- [Menus](https://developer.apple.com/documentation/appkit/menus) — AppKit

**Modality** <sub>[Modality](https://developer.apple.com/design/human-interface-guidelines/modality)</sub>
- [Presentation modifiers](https://developer.apple.com/documentation/swiftui/view-presentation) — SwiftUI
- [UIModalPresentationStyle](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle) — UIKit
- [Modal Windows and Panels](https://developer.apple.com/documentation/appkit/modal-windows-and-panels) — AppKit

**Motion** <sub>[Motion](https://developer.apple.com/design/human-interface-guidelines/motion)</sub>
- [Animating views and transitions](https://developer.apple.com/tutorials/swiftui/animating-views-and-transitions) — SwiftUI

**Multitasking** <sub>[Multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking)</sub>
- [Responding to the launch of your app](https://developer.apple.com/documentation/uikit/responding-to-the-launch-of-your-app) — UIKit
- [Multitasking on iPad, Mac, and Apple Vision Pro](https://developer.apple.com/documentation/uikit/multitasking-on-ipad-mac-and-apple-vision-pro) — UIKit

**NFC** <sub>[NFC](https://developer.apple.com/design/human-interface-guidelines/nfc)</sub>
- [Core NFC](https://developer.apple.com/documentation/corenfc) <sub>framework/guide</sub>

**Nearby interactions** <sub>[Nearby interactions](https://developer.apple.com/design/human-interface-guidelines/nearby-interactions)</sub>
- [Nearby Interaction](https://developer.apple.com/documentation/nearbyinteraction) <sub>framework/guide</sub>

**Notifications** <sub>[Notifications](https://developer.apple.com/design/human-interface-guidelines/notifications)</sub>
- [Asking permission to use notifications](https://developer.apple.com/documentation/usernotifications/asking-permission-to-use-notifications) — User Notifications
- [User Notifications UI](https://developer.apple.com/documentation/usernotificationsui) <sub>framework/guide</sub>
- [User Notifications](https://developer.apple.com/documentation/usernotifications) <sub>framework/guide</sub>

**Offering help** <sub>[Offering help](https://developer.apple.com/design/human-interface-guidelines/offering-help)</sub>
- [TipKit](https://developer.apple.com/documentation/tipkit) <sub>framework/guide</sub>
- [NSHelpManager](https://developer.apple.com/documentation/appkit/nshelpmanager) — AppKit

**Ornaments** <sub>[Ornaments](https://developer.apple.com/design/human-interface-guidelines/ornaments)</sub>
- [ornament(visibility:attachmentAnchor:contentAlignment:ornament:)](https://developer.apple.com/documentation/swiftui/view/ornament(visibility:attachmentanchor:contentalignment:ornament:)) — SwiftUI

**Outline views** <sub>[Outline views](https://developer.apple.com/design/human-interface-guidelines/outline-views)</sub>
- [OutlineGroup](https://developer.apple.com/documentation/swiftui/outlinegroup) — SwiftUI
- [NSOutlineView](https://developer.apple.com/documentation/appkit/nsoutlineview) — AppKit

**Page controls** <sub>[Page controls](https://developer.apple.com/design/human-interface-guidelines/page-controls)</sub>
- [PageTabViewStyle](https://developer.apple.com/documentation/swiftui/pagetabviewstyle) — SwiftUI
- [UIPageControl](https://developer.apple.com/documentation/uikit/uipagecontrol) — UIKit

**Panels** <sub>[Panels](https://developer.apple.com/design/human-interface-guidelines/panels)</sub>
- [NSPanel](https://developer.apple.com/documentation/appkit/nspanel) — AppKit
- [hudWindow](https://developer.apple.com/documentation/appkit/nswindow/stylemask-swift.struct/hudwindow) — AppKit

**Path controls** <sub>[Path controls](https://developer.apple.com/design/human-interface-guidelines/path-controls)</sub>
- [NSPathControl](https://developer.apple.com/documentation/appkit/nspathcontrol) — AppKit

**Photo editing** <sub>[Photo editing](https://developer.apple.com/design/human-interface-guidelines/photo-editing)</sub>
- [App extensions](https://developer.apple.com/app-extensions/) <sub>framework/guide</sub>
- [PhotoKit](https://developer.apple.com/documentation/photokit) <sub>framework/guide</sub>

**Pickers** <sub>[Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers)</sub>
- [Picker](https://developer.apple.com/documentation/swiftui/picker) — SwiftUI
- [UIDatePicker](https://developer.apple.com/documentation/uikit/uidatepicker) — UIKit
- [UIPickerView](https://developer.apple.com/documentation/uikit/uipickerview) — UIKit
- [NSDatePicker](https://developer.apple.com/documentation/appkit/nsdatepicker) — AppKit

**Playing audio** <sub>[Playing audio](https://developer.apple.com/design/human-interface-guidelines/playing-audio)</sub>
- [Configuring your app for media playback](https://developer.apple.com/documentation/avfoundation/configuring-your-app-for-media-playback) — AVFoundation
- [AVAudioSession](https://developer.apple.com/documentation/avfaudio/avaudiosession) — AVFAudio
- [MusicKit](https://developer.apple.com/documentation/musickit) — MusicKit

**Playing haptics** <sub>[Playing haptics](https://developer.apple.com/design/human-interface-guidelines/playing-haptics)</sub>
- [Core Haptics](https://developer.apple.com/documentation/corehaptics) <sub>framework/guide</sub>

**Playing video** <sub>[Playing video](https://developer.apple.com/design/human-interface-guidelines/playing-video)</sub>
- [Configuring your app for media playback](https://developer.apple.com/documentation/avfoundation/configuring-your-app-for-media-playback) — AVFoundation
- [AVKit](https://developer.apple.com/documentation/avkit) <sub>framework/guide</sub>
- [HTTP Live Streaming](https://developer.apple.com/streaming/) <sub>framework/guide</sub>

**Pointing devices** <sub>[Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices)</sub>
- [Input events](https://developer.apple.com/documentation/swiftui/input-events) — SwiftUI
- [Pointer interactions](https://developer.apple.com/documentation/uikit/pointer-interactions) — UIKit
- [Mouse, Keyboard, and Trackpad](https://developer.apple.com/documentation/appkit/mouse-keyboard-and-trackpad) — AppKit

**Pop-up buttons** <sub>[Pop-up buttons](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons)</sub>
- [MenuPickerStyle](https://developer.apple.com/documentation/swiftui/menupickerstyle) — SwiftUI
- [changesSelectionAsPrimaryAction](https://developer.apple.com/documentation/uikit/uibutton/changesselectionasprimaryaction) — UIKit
- [NSPopUpButton](https://developer.apple.com/documentation/appkit/nspopupbutton) — AppKit

**Popovers** <sub>[Popovers](https://developer.apple.com/design/human-interface-guidelines/popovers)</sub>
- [popover(isPresented:attachmentAnchor:arrowEdge:content:)](https://developer.apple.com/documentation/swiftui/view/popover(ispresented:attachmentanchor:arrowedge:content:)) — SwiftUI
- [UIPopoverPresentationController](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller) — UIKit
- [NSPopover](https://developer.apple.com/documentation/appkit/nspopover) — AppKit

**Printing** <sub>[Printing](https://developer.apple.com/design/human-interface-guidelines/printing)</sub>
- [UIPrintInteractionController](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller) — UIKit
- [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) — AppKit

**Privacy** <sub>[Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy)</sub>
- [Requesting access to protected resources](https://developer.apple.com/documentation/uikit/requesting-access-to-protected-resources) — UIKit
- [Security](https://developer.apple.com/documentation/security) <sub>framework/guide</sub>
- [Requesting authorization to use location services](https://developer.apple.com/documentation/corelocation/requesting-authorization-to-use-location-services) — CoreLocation
- [App Tracking Transparency](https://developer.apple.com/documentation/apptrackingtransparency) <sub>framework/guide</sub>

**Progress indicators** <sub>[Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators)</sub>
- [ProgressView](https://developer.apple.com/documentation/swiftui/progressview) — SwiftUI
- [UIProgressView](https://developer.apple.com/documentation/uikit/uiprogressview) — UIKit
- [UIActivityIndicatorView](https://developer.apple.com/documentation/uikit/uiactivityindicatorview) — UIKit
- [UIRefreshControl](https://developer.apple.com/documentation/uikit/uirefreshcontrol) — UIKit
- [NSProgressIndicator](https://developer.apple.com/documentation/appkit/nsprogressindicator) — AppKit

**Pull-down buttons** <sub>[Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons)</sub>
- [MenuPickerStyle](https://developer.apple.com/documentation/swiftui/menupickerstyle) — SwiftUI
- [showsMenuAsPrimaryAction](https://developer.apple.com/documentation/uikit/uicontrol/showsmenuasprimaryaction) — UIKit
- [pullsDown](https://developer.apple.com/documentation/appkit/nspopupbutton/pullsdown) — AppKit

**Rating indicators** <sub>[Rating indicators](https://developer.apple.com/design/human-interface-guidelines/rating-indicators)</sub>
- [NSLevelIndicator.Style.rating](https://developer.apple.com/documentation/appkit/nslevelindicator/style/rating) — AppKit

**Ratings and reviews** <sub>[Ratings and reviews](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews)</sub>
- [RequestReviewAction](https://developer.apple.com/documentation/storekit/requestreviewaction) — StoreKit

**ResearchKit** <sub>[ResearchKit](https://developer.apple.com/design/human-interface-guidelines/researchkit)</sub>
- [Research & Care > Developers](https://www.researchandcare.org/developers/) <sub>framework/guide</sub>
- [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy) — HealthKit
- [ResearchKit GitHub project](https://github.com/ResearchKit/ResearchKit) <sub>framework/guide</sub>

**Right to left** <sub>[Right to left](https://developer.apple.com/design/human-interface-guidelines/right-to-left)</sub>
- [Localization](https://developer.apple.com/localization/) <sub>framework/guide</sub>
- [Preparing views for localization](https://developer.apple.com/documentation/swiftui/preparing-views-for-localization) — SwiftUI

**SF Symbols** <sub>[SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols)</sub>
- [Symbols](https://developer.apple.com/documentation/symbols) — Symbols framework
- [Configuring and displaying symbol images in your UI](https://developer.apple.com/documentation/uikit/configuring-and-displaying-symbol-images-in-your-ui) — UIKit
- [Creating custom symbol images for your app](https://developer.apple.com/documentation/uikit/creating-custom-symbol-images-for-your-app) — UIKit

**Scroll views** <sub>[Scroll views](https://developer.apple.com/design/human-interface-guidelines/scroll-views)</sub>
- [ScrollView](https://developer.apple.com/documentation/swiftui/scrollview) — SwiftUI
- [UIScrollView](https://developer.apple.com/documentation/uikit/uiscrollview) — UIKit
- [NSScrollView](https://developer.apple.com/documentation/appkit/nsscrollview) — AppKit
- [WKPageOrientation](https://developer.apple.com/documentation/watchkit/wkpageorientation) — WatchKit
- [look](https://developer.apple.com/documentation/swiftui/scrollinputkind/look) — SwiftUI

**Search fields** <sub>[Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields)</sub>
- [Adding a search interface to your app](https://developer.apple.com/documentation/swiftui/adding-a-search-interface-to-your-app) — SwiftUI
- [searchable(text:placement:prompt:)](https://developer.apple.com/documentation/swiftui/view/searchable(text:placement:prompt:)) — SwiftUI
- [UISearchBar](https://developer.apple.com/documentation/uikit/uisearchbar) — UIKit
- [UISearchTextField](https://developer.apple.com/documentation/uikit/uisearchtextfield) — UIKit
- [NSSearchField](https://developer.apple.com/documentation/appkit/nssearchfield) — AppKit

**Searching** <sub>[Searching](https://developer.apple.com/design/human-interface-guidelines/searching)</sub>
- [Adding your app’s content to Spotlight indexes](https://developer.apple.com/documentation/corespotlight/adding-your-app-s-content-to-spotlight-indexes) — Core Spotlight

**Segmented controls** <sub>[Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls)</sub>
- [segmented](https://developer.apple.com/documentation/swiftui/pickerstyle/segmented) — SwiftUI
- [UISegmentedControl](https://developer.apple.com/documentation/uikit/uisegmentedcontrol) — UIKit
- [NSSegmentedControl](https://developer.apple.com/documentation/appkit/nssegmentedcontrol) — AppKit

**Settings** <sub>[Settings](https://developer.apple.com/design/human-interface-guidelines/settings)</sub>
- [Settings](https://developer.apple.com/documentation/swiftui/settings) — SwiftUI
- [UserDefaults](https://developer.apple.com/documentation/foundation/userdefaults) — Foundation
- [Preference Panes](https://developer.apple.com/documentation/preferencepanes) <sub>framework/guide</sub>

**SharePlay** <sub>[SharePlay](https://developer.apple.com/design/human-interface-guidelines/shareplay)</sub>
- [Group Activities](https://developer.apple.com/documentation/groupactivities) <sub>framework/guide</sub>

**ShazamKit** <sub>[ShazamKit](https://developer.apple.com/design/human-interface-guidelines/shazamkit)</sub>
- [ShazamKit](https://developer.apple.com/documentation/shazamkit) <sub>framework/guide</sub>

**Sheets** <sub>[Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets)</sub>
- [sheet(item:onDismiss:content:)](https://developer.apple.com/documentation/swiftui/view/sheet(item:ondismiss:content:)) — SwiftUI
- [UISheetPresentationController](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller) — UIKit
- [presentAsSheet(_:)](https://developer.apple.com/documentation/appkit/nsviewcontroller/presentassheet(_:)) — AppKit

**Sidebars** <sub>[Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars)</sub>
- [sidebarAdaptable](https://developer.apple.com/documentation/swiftui/tabviewstyle/sidebaradaptable) — SwiftUI
- [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview) — SwiftUI
- [sidebar](https://developer.apple.com/documentation/swiftui/liststyle/sidebar) — SwiftUI
- [UICollectionLayoutListConfiguration](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct) — UIKit
- [NSSplitViewController](https://developer.apple.com/documentation/appkit/nssplitviewcontroller) — AppKit

**Sign in with Apple** <sub>[Sign in with Apple](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple)</sub>
- [Authentication Services](https://developer.apple.com/documentation/authenticationservices) <sub>framework/guide</sub>
- [Displaying Sign in with Apple buttons on the web](https://developer.apple.com/documentation/signinwithapple/displaying-sign-in-with-apple-buttons-on-the-web) — Sign in with Apple

**Siri** <sub>[Siri](https://developer.apple.com/design/human-interface-guidelines/siri)</sub>
- [App Intents](https://developer.apple.com/documentation/appintents) <sub>framework/guide</sub>
- [App schema domains](https://developer.apple.com/documentation/appintents/app-schema-domains) <sub>framework/guide</sub>
- [Apple Intelligence and Siri AI](https://developer.apple.com/documentation/appintents/apple-intelligence-and-siri-ai) <sub>framework/guide</sub>

**Sliders** <sub>[Sliders](https://developer.apple.com/design/human-interface-guidelines/sliders)</sub>
- [Slider](https://developer.apple.com/documentation/swiftui/slider) — SwiftUI
- [UISlider](https://developer.apple.com/documentation/uikit/uislider) — UIKit
- [NSSlider](https://developer.apple.com/documentation/appkit/nsslider) — AppKit

**Snippets** <sub>[Snippets](https://developer.apple.com/design/human-interface-guidelines/snippets)</sub>
- [App Intents](https://developer.apple.com/documentation/appintents) <sub>framework/guide</sub>

**Spatial layout** <sub>[Spatial layout](https://developer.apple.com/design/human-interface-guidelines/spatial-layout)</sub>
- [Presenting windows and spaces](https://developer.apple.com/documentation/visionos/presenting-windows-and-spaces) — visionOS
- [Positioning and sizing windows](https://developer.apple.com/documentation/visionos/positioning-and-sizing-windows) — visionOS
- [Adding 3D content to your app](https://developer.apple.com/documentation/visionos/adding-3d-content-to-your-app) — visionOS

**Split views** <sub>[Split views](https://developer.apple.com/design/human-interface-guidelines/split-views)</sub>
- [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview) — SwiftUI
- [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller) — UIKit
- [NSSplitViewController](https://developer.apple.com/documentation/appkit/nssplitviewcontroller) — AppKit

**Status bars** <sub>[Status bars](https://developer.apple.com/design/human-interface-guidelines/status-bars)</sub>
- [UIStatusBarStyle](https://developer.apple.com/documentation/uikit/uistatusbarstyle) — UIKit
- [preferredStatusBarStyle](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredstatusbarstyle) — UIKit

**Steppers** <sub>[Steppers](https://developer.apple.com/design/human-interface-guidelines/steppers)</sub>
- [UIStepper](https://developer.apple.com/documentation/uikit/uistepper) — UIKit
- [NSStepper](https://developer.apple.com/documentation/appkit/nsstepper) — AppKit

**Tab bars** <sub>[Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars)</sub>
- [TabView](https://developer.apple.com/documentation/swiftui/tabview) — SwiftUI
- [TabViewBottomAccessoryPlacement](https://developer.apple.com/documentation/swiftui/tabviewbottomaccessoryplacement) — SwiftUI
- [Enhancing your app’s content with tab navigation](https://developer.apple.com/documentation/swiftui/enhancing-your-app-content-with-tab-navigation) — SwiftUI
- [UITabBar](https://developer.apple.com/documentation/uikit/uitabbar) — UIKit
- [Elevating your iPad app with a tab bar and sidebar](https://developer.apple.com/documentation/uikit/elevating-your-ipad-app-with-a-tab-bar-and-sidebar) — UIKit

**Tab views** <sub>[Tab views](https://developer.apple.com/design/human-interface-guidelines/tab-views)</sub>
- [TabView](https://developer.apple.com/documentation/swiftui/tabview) — SwiftUI
- [NSTabView](https://developer.apple.com/documentation/appkit/nstabview) — AppKit

**Tap to Pay on iPhone** <sub>[Tap to Pay on iPhone](https://developer.apple.com/design/human-interface-guidelines/tap-to-pay-on-iphone)</sub>
- [Adding support for Tap to Pay on iPhone to your app](https://developer.apple.com/documentation/proximityreader/adding-support-for-tap-to-pay-on-iphone-to-your-app) — ProximityReader

**Text fields** <sub>[Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields)</sub>
- [TextField](https://developer.apple.com/documentation/swiftui/textfield) — SwiftUI
- [SecureField](https://developer.apple.com/documentation/swiftui/securefield) — SwiftUI
- [UITextField](https://developer.apple.com/documentation/uikit/uitextfield) — UIKit
- [NSTextField](https://developer.apple.com/documentation/appkit/nstextfield) — AppKit

**Text views** <sub>[Text views](https://developer.apple.com/design/human-interface-guidelines/text-views)</sub>
- [Text](https://developer.apple.com/documentation/swiftui/text) — SwiftUI
- [UITextView](https://developer.apple.com/documentation/uikit/uitextview) — UIKit
- [NSTextView](https://developer.apple.com/documentation/appkit/nstextview) — AppKit

**The menu bar** <sub>[The menu bar](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar)</sub>
- [CommandMenu](https://developer.apple.com/documentation/swiftui/commandmenu) — SwiftUI
- [Adding menus and shortcuts to the menu bar and user interface](https://developer.apple.com/documentation/uikit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface) — UIKit
- [NSStatusBar](https://developer.apple.com/documentation/appkit/nsstatusbar) — AppKit

**Toggles** <sub>[Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles)</sub>
- [Toggle](https://developer.apple.com/documentation/swiftui/toggle) — SwiftUI
- [UISwitch](https://developer.apple.com/documentation/uikit/uiswitch) — UIKit
- [NSButton.ButtonType.toggle](https://developer.apple.com/documentation/appkit/nsbutton/buttontype/toggle) — AppKit
- [NSSwitch](https://developer.apple.com/documentation/appkit/nsswitch) — AppKit

**Token fields** <sub>[Token fields](https://developer.apple.com/design/human-interface-guidelines/token-fields)</sub>
- [NSTokenField](https://developer.apple.com/documentation/appkit/nstokenfield) — AppKit

**Toolbars** <sub>[Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars)</sub>
- [Toolbars](https://developer.apple.com/documentation/swiftui/toolbars) — SwiftUI
- [UIToolbar](https://developer.apple.com/documentation/uikit/uitoolbar) — UIKit
- [NSToolbar](https://developer.apple.com/documentation/appkit/nstoolbar) — AppKit

**Typography** <sub>[Typography](https://developer.apple.com/design/human-interface-guidelines/typography)</sub>
- [Text input and output](https://developer.apple.com/documentation/swiftui/text-input-and-output) — SwiftUI
- [Text display and fonts](https://developer.apple.com/documentation/uikit/text-display-and-fonts) — UIKit
- [Fonts](https://developer.apple.com/documentation/appkit/fonts) — AppKit

**Undo and redo** <sub>[Undo and redo](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo)</sub>
- [UndoManager](https://developer.apple.com/documentation/foundation/undomanager) — Foundation

**Virtual keyboards** <sub>[Virtual keyboards](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards)</sub>
- [keyboardType(_:)](https://developer.apple.com/documentation/swiftui/view/keyboardtype(_:)) — SwiftUI
- [textContentType(_:)](https://developer.apple.com/documentation/swiftui/view/textcontenttype(_:)) — SwiftUI
- [UIKeyboardType](https://developer.apple.com/documentation/uikit/uikeyboardtype) — UIKit

**VoiceOver** <sub>[VoiceOver](https://developer.apple.com/design/human-interface-guidelines/voiceover)</sub>
- [Accessibility](https://developer.apple.com/documentation/accessibility) <sub>framework/guide</sub>
- [VoiceOver](https://developer.apple.com/documentation/accessibility/voiceover) <sub>framework/guide</sub>
- [Supporting VoiceOver in your app](https://developer.apple.com/documentation/uikit/supporting-voiceover-in-your-app) <sub>framework/guide</sub>

**Wallet** <sub>[Wallet](https://developer.apple.com/design/human-interface-guidelines/wallet)</sub>
- [FinanceKitUI](https://developer.apple.com/documentation/financekitui) <sub>framework/guide</sub>
- [FinanceKit](https://developer.apple.com/documentation/financekit) <sub>framework/guide</sub>
- [PassKit (Apple Pay and Wallet)](https://developer.apple.com/documentation/passkit) <sub>framework/guide</sub>
- [Wallet Passes](https://developer.apple.com/documentation/walletpasses) <sub>framework/guide</sub>
- [Wallet Orders](https://developer.apple.com/documentation/walletorders) <sub>framework/guide</sub>

**Watch faces** <sub>[Watch faces](https://developer.apple.com/design/human-interface-guidelines/watch-faces)</sub>
- [Sharing an Apple Watch face](https://developer.apple.com/documentation/clockkit/sharing-an-apple-watch-face) — ClockKit

**Web views** <sub>[Web views](https://developer.apple.com/design/human-interface-guidelines/web-views)</sub>
- [WKWebView](https://developer.apple.com/documentation/webkit/wkwebview) — WebKit

**Widgets** <sub>[Widgets](https://developer.apple.com/design/human-interface-guidelines/widgets)</sub>
- [WidgetKit](https://developer.apple.com/documentation/widgetkit) <sub>framework/guide</sub>
- [Developing a WidgetKit strategy](https://developer.apple.com/documentation/widgetkit/developing-a-widgetkit-strategy) — WidgetKit

**Windows** <sub>[Windows](https://developer.apple.com/design/human-interface-guidelines/windows)</sub>
- [Windows](https://developer.apple.com/documentation/swiftui/windows) — SwiftUI
- [WindowGroup](https://developer.apple.com/documentation/swiftui/windowgroup) — SwiftUI
- [UIWindow](https://developer.apple.com/documentation/uikit/uiwindow) — UIKit
- [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) — AppKit

**Workouts** <sub>[Workouts](https://developer.apple.com/design/human-interface-guidelines/workouts)</sub>
- [WorkoutKit](https://developer.apple.com/documentation/workoutkit) <sub>framework/guide</sub>
- [Workouts and activity rings](https://developer.apple.com/documentation/healthkit/workouts-and-activity-rings) — HealthKit

**iCloud** <sub>[iCloud](https://developer.apple.com/design/human-interface-guidelines/icloud)</sub>
- [CloudKit](https://developer.apple.com/documentation/cloudkit) <sub>framework/guide</sub>
- [GameSave](https://developer.apple.com/documentation/gamesave) <sub>framework/guide</sub>

**iMessage apps and stickers** <sub>[iMessage apps and stickers](https://developer.apple.com/design/human-interface-guidelines/imessage-apps-and-stickers)</sub>
- [Messages](https://developer.apple.com/documentation/messages) <sub>framework/guide</sub>
- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](https://developer.apple.com/documentation/messages/adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime) — Messages

---

## By framework

Same data, grouped the other direction — everything the HIG cites for a given framework.

### AVFAudio
- [AVAudioSession](https://developer.apple.com/documentation/avfaudio/avaudiosession) — Playing audio ([Playing audio](https://developer.apple.com/design/human-interface-guidelines/playing-audio))

### AVFoundation
- [Enhancing your app experience with the Camera Control](https://developer.apple.com/documentation/avfoundation/enhancing-your-app-experience-with-the-camera-control) — Camera Control ([Camera Control](https://developer.apple.com/design/human-interface-guidelines/camera-control))
- [AVCaptureControl](https://developer.apple.com/documentation/avfoundation/avcapturecontrol) — Camera Control ([Camera Control](https://developer.apple.com/design/human-interface-guidelines/camera-control))
- [Configuring your app for media playback](https://developer.apple.com/documentation/avfoundation/configuring-your-app-for-media-playback) — Playing audio ([Playing audio](https://developer.apple.com/design/human-interface-guidelines/playing-audio))
- [Configuring your app for media playback](https://developer.apple.com/documentation/avfoundation/configuring-your-app-for-media-playback) — Playing video ([Playing video](https://developer.apple.com/design/human-interface-guidelines/playing-video))

### App Intents
- [Getting started with the App Intents framework](https://developer.apple.com/documentation/appintents/getting-started-with-the-app-intents-framework) — App Shortcuts ([App Shortcuts](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts))
- [Defining app entities for your custom data types](https://developer.apple.com/documentation/appintents/defining-app-entities-for-your-custom-data-types) — App Shortcuts ([App Shortcuts](https://developer.apple.com/design/human-interface-guidelines/app-shortcuts))

### AppKit
- [NSAlert](https://developer.apple.com/documentation/appkit/nsalert) — Alerts ([Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts))
- [NSBox](https://developer.apple.com/documentation/appkit/nsbox) — Boxes ([Boxes](https://developer.apple.com/design/human-interface-guidelines/boxes))
- [NSButton](https://developer.apple.com/documentation/appkit/nsbutton) — Buttons ([Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons))
- [NSCollectionView](https://developer.apple.com/documentation/appkit/nscollectionview) — Collections ([Collections](https://developer.apple.com/design/human-interface-guidelines/collections))
- [NSColorWell](https://developer.apple.com/documentation/appkit/nscolorwell) — Color wells ([Color wells](https://developer.apple.com/design/human-interface-guidelines/color-wells))
- [Color](https://developer.apple.com/documentation/appkit/color) — Color ([Color](https://developer.apple.com/design/human-interface-guidelines/color))
- [NSBrowser](https://developer.apple.com/documentation/appkit/nsbrowser) — Column views ([Column views](https://developer.apple.com/design/human-interface-guidelines/column-views))
- [NSComboBox](https://developer.apple.com/documentation/appkit/nscombobox) — Combo boxes ([Combo boxes](https://developer.apple.com/design/human-interface-guidelines/combo-boxes))
- [popUpContextMenu(_:with:for:)](https://developer.apple.com/documentation/appkit/nsmenu/popupcontextmenu(_:with:for:)) — Context menus ([Context menus](https://developer.apple.com/design/human-interface-guidelines/context-menus))
- [NSButton.BezelStyle.disclosure](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/disclosure) — Disclosure controls ([Disclosure controls](https://developer.apple.com/design/human-interface-guidelines/disclosure-controls))
- [NSButton.BezelStyle.pushDisclosure](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/pushdisclosure) — Disclosure controls ([Disclosure controls](https://developer.apple.com/design/human-interface-guidelines/disclosure-controls))
- [applicationDockMenu(_:)](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationdockmenu(_:)) — Dock menus ([Dock menus](https://developer.apple.com/design/human-interface-guidelines/dock-menus))
- [Drag and Drop](https://developer.apple.com/documentation/appkit/drag-and-drop) — Drag and drop ([Drag and drop](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop))
- [NSMenu](https://developer.apple.com/documentation/appkit/nsmenu) — Edit menus ([Edit menus](https://developer.apple.com/design/human-interface-guidelines/edit-menus))
- [NSLevelIndicator](https://developer.apple.com/documentation/appkit/nslevelindicator) — Gauges ([Gauges](https://developer.apple.com/design/human-interface-guidelines/gauges))
- [NSScreen](https://developer.apple.com/documentation/appkit/nsscreen) — Going full screen ([Going full screen](https://developer.apple.com/design/human-interface-guidelines/going-full-screen))
- [NSWindow.CollectionBehavior](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior-swift.struct) — Going full screen ([Going full screen](https://developer.apple.com/design/human-interface-guidelines/going-full-screen))
- [NSImageView](https://developer.apple.com/documentation/appkit/nsimageview) — Image views ([Image views](https://developer.apple.com/design/human-interface-guidelines/image-views))
- [NSImageView](https://developer.apple.com/documentation/appkit/nsimageview) — Image wells ([Image wells](https://developer.apple.com/design/human-interface-guidelines/image-wells))
- [NSImageView](https://developer.apple.com/documentation/appkit/nsimageview) — Images ([Images](https://developer.apple.com/design/human-interface-guidelines/images))
- [Mouse, Keyboard, and Trackpad](https://developer.apple.com/documentation/appkit/mouse-keyboard-and-trackpad) — Keyboards ([Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards))
- [NSTextField](https://developer.apple.com/documentation/appkit/nstextfield) — Labels ([Labels](https://developer.apple.com/design/human-interface-guidelines/labels))
- [NSTableView](https://developer.apple.com/documentation/appkit/nstableview) — Lists and tables ([Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables))
- [NSVisualEffectView](https://developer.apple.com/documentation/appkit/nsvisualeffectview) — Materials ([Materials](https://developer.apple.com/design/human-interface-guidelines/materials))
- [Menus](https://developer.apple.com/documentation/appkit/menus) — Menus ([Menus](https://developer.apple.com/design/human-interface-guidelines/menus))
- [Modal Windows and Panels](https://developer.apple.com/documentation/appkit/modal-windows-and-panels) — Modality ([Modality](https://developer.apple.com/design/human-interface-guidelines/modality))
- [NSHelpManager](https://developer.apple.com/documentation/appkit/nshelpmanager) — Offering help ([Offering help](https://developer.apple.com/design/human-interface-guidelines/offering-help))
- [NSOutlineView](https://developer.apple.com/documentation/appkit/nsoutlineview) — Outline views ([Outline views](https://developer.apple.com/design/human-interface-guidelines/outline-views))
- [NSPanel](https://developer.apple.com/documentation/appkit/nspanel) — Panels ([Panels](https://developer.apple.com/design/human-interface-guidelines/panels))
- [hudWindow](https://developer.apple.com/documentation/appkit/nswindow/stylemask-swift.struct/hudwindow) — Panels ([Panels](https://developer.apple.com/design/human-interface-guidelines/panels))
- [NSPathControl](https://developer.apple.com/documentation/appkit/nspathcontrol) — Path controls ([Path controls](https://developer.apple.com/design/human-interface-guidelines/path-controls))
- [NSDatePicker](https://developer.apple.com/documentation/appkit/nsdatepicker) — Pickers ([Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers))
- [Mouse, Keyboard, and Trackpad](https://developer.apple.com/documentation/appkit/mouse-keyboard-and-trackpad) — Pointing devices ([Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices))
- [NSPopUpButton](https://developer.apple.com/documentation/appkit/nspopupbutton) — Pop-up buttons ([Pop-up buttons](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons))
- [NSPopover](https://developer.apple.com/documentation/appkit/nspopover) — Popovers ([Popovers](https://developer.apple.com/design/human-interface-guidelines/popovers))
- [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) — Printing ([Printing](https://developer.apple.com/design/human-interface-guidelines/printing))
- [NSProgressIndicator](https://developer.apple.com/documentation/appkit/nsprogressindicator) — Progress indicators ([Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators))
- [pullsDown](https://developer.apple.com/documentation/appkit/nspopupbutton/pullsdown) — Pull-down buttons ([Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons))
- [NSLevelIndicator.Style.rating](https://developer.apple.com/documentation/appkit/nslevelindicator/style/rating) — Rating indicators ([Rating indicators](https://developer.apple.com/design/human-interface-guidelines/rating-indicators))
- [NSScrollView](https://developer.apple.com/documentation/appkit/nsscrollview) — Scroll views ([Scroll views](https://developer.apple.com/design/human-interface-guidelines/scroll-views))
- [NSSearchField](https://developer.apple.com/documentation/appkit/nssearchfield) — Search fields ([Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields))
- [NSSegmentedControl](https://developer.apple.com/documentation/appkit/nssegmentedcontrol) — Segmented controls ([Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls))
- [presentAsSheet(_:)](https://developer.apple.com/documentation/appkit/nsviewcontroller/presentassheet(_:)) — Sheets ([Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets))
- [NSSplitViewController](https://developer.apple.com/documentation/appkit/nssplitviewcontroller) — Sidebars ([Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars))
- [NSSlider](https://developer.apple.com/documentation/appkit/nsslider) — Sliders ([Sliders](https://developer.apple.com/design/human-interface-guidelines/sliders))
- [NSSplitViewController](https://developer.apple.com/documentation/appkit/nssplitviewcontroller) — Split views ([Split views](https://developer.apple.com/design/human-interface-guidelines/split-views))
- [NSStepper](https://developer.apple.com/documentation/appkit/nsstepper) — Steppers ([Steppers](https://developer.apple.com/design/human-interface-guidelines/steppers))
- [NSTabView](https://developer.apple.com/documentation/appkit/nstabview) — Tab views ([Tab views](https://developer.apple.com/design/human-interface-guidelines/tab-views))
- [NSTextField](https://developer.apple.com/documentation/appkit/nstextfield) — Text fields ([Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields))
- [NSTextView](https://developer.apple.com/documentation/appkit/nstextview) — Text views ([Text views](https://developer.apple.com/design/human-interface-guidelines/text-views))
- [NSStatusBar](https://developer.apple.com/documentation/appkit/nsstatusbar) — The menu bar ([The menu bar](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar))
- [NSButton.ButtonType.toggle](https://developer.apple.com/documentation/appkit/nsbutton/buttontype/toggle) — Toggles ([Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles))
- [NSSwitch](https://developer.apple.com/documentation/appkit/nsswitch) — Toggles ([Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles))
- [NSTokenField](https://developer.apple.com/documentation/appkit/nstokenfield) — Token fields ([Token fields](https://developer.apple.com/design/human-interface-guidelines/token-fields))
- [NSToolbar](https://developer.apple.com/documentation/appkit/nstoolbar) — Toolbars ([Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars))
- [Fonts](https://developer.apple.com/documentation/appkit/fonts) — Typography ([Typography](https://developer.apple.com/design/human-interface-guidelines/typography))
- [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) — Windows ([Windows](https://developer.apple.com/design/human-interface-guidelines/windows))

### Authentication Services
- [Supporting passkeys](https://developer.apple.com/documentation/authenticationservices/supporting-passkeys) — Managing accounts ([Managing accounts](https://developer.apple.com/design/human-interface-guidelines/managing-accounts))

### ClockKit
- [Sharing an Apple Watch face](https://developer.apple.com/documentation/clockkit/sharing-an-apple-watch-face) — Watch faces ([Watch faces](https://developer.apple.com/design/human-interface-guidelines/watch-faces))

### Core Motion
- [Getting processed device-motion data](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data) — Gyroscope and accelerometer ([Gyroscope and accelerometer](https://developer.apple.com/design/human-interface-guidelines/gyro-and-accelerometer))

### Core Spotlight
- [Adding your app’s content to Spotlight indexes](https://developer.apple.com/documentation/corespotlight/adding-your-app-s-content-to-spotlight-indexes) — Searching ([Searching](https://developer.apple.com/design/human-interface-guidelines/searching))

### CoreLocation
- [Requesting authorization to use location services](https://developer.apple.com/documentation/corelocation/requesting-authorization-to-use-location-services) — Privacy ([Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy))

### Foundation
- [App Extension Support](https://developer.apple.com/documentation/foundation/app-extension-support) — Activity views ([Activity views](https://developer.apple.com/design/human-interface-guidelines/activity-views))
- [UserDefaults](https://developer.apple.com/documentation/foundation/userdefaults) — Settings ([Settings](https://developer.apple.com/design/human-interface-guidelines/settings))
- [UndoManager](https://developer.apple.com/documentation/foundation/undomanager) — Undo and redo ([Undo and redo](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo))

### HealthKit
- [HKActivityRingView](https://developer.apple.com/documentation/healthkitui/hkactivityringview) — Activity rings ([Activity rings](https://developer.apple.com/design/human-interface-guidelines/activity-rings))
- [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy) — CareKit ([CareKit](https://developer.apple.com/design/human-interface-guidelines/carekit))
- [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy) — HealthKit ([HealthKit](https://developer.apple.com/design/human-interface-guidelines/healthkit))
- [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy) — ResearchKit ([ResearchKit](https://developer.apple.com/design/human-interface-guidelines/researchkit))
- [Workouts and activity rings](https://developer.apple.com/documentation/healthkit/workouts-and-activity-rings) — Workouts ([Workouts](https://developer.apple.com/design/human-interface-guidelines/workouts))

### LivePhotosKit JS
- [LivePhotosKit JS](https://developer.apple.com/documentation/livephotoskitjs) — Live Photos ([Live Photos](https://developer.apple.com/design/human-interface-guidelines/live-photos))

### Messages
- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](https://developer.apple.com/documentation/messages/adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime) — iMessage apps and stickers ([iMessage apps and stickers](https://developer.apple.com/design/human-interface-guidelines/imessage-apps-and-stickers))

### MusicKit
- [MusicKit](https://developer.apple.com/documentation/musickit) — Playing audio ([Playing audio](https://developer.apple.com/design/human-interface-guidelines/playing-audio))

### PassKit
- [Apple Pay](https://developer.apple.com/documentation/passkit/apple-pay) — Apple Pay ([Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay))

### PhotoKit
- [PHLivePhoto](https://developer.apple.com/documentation/photos/phlivephoto) — Live Photos ([Live Photos](https://developer.apple.com/design/human-interface-guidelines/live-photos))

### ProximityReader
- [Adopting the Verifier API in your iPhone app](https://developer.apple.com/documentation/proximityreader/adopting-the-verifier-api-in-your-iphone-app) — ID Verifier ([ID Verifier](https://developer.apple.com/design/human-interface-guidelines/id-verifier))
- [Adding support for Tap to Pay on iPhone to your app](https://developer.apple.com/documentation/proximityreader/adding-support-for-tap-to-pay-on-iphone-to-your-app) — Tap to Pay on iPhone ([Tap to Pay on iPhone](https://developer.apple.com/design/human-interface-guidelines/tap-to-pay-on-iphone))

### Sign in with Apple
- [Displaying Sign in with Apple buttons on the web](https://developer.apple.com/documentation/signinwithapple/displaying-sign-in-with-apple-buttons-on-the-web) — Sign in with Apple ([Sign in with Apple](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple))

### StoreKit
- [In-App Purchase](https://developer.apple.com/documentation/storekit/in-app-purchase) — In-app purchase ([In-app purchase](https://developer.apple.com/design/human-interface-guidelines/in-app-purchase))
- [RequestReviewAction](https://developer.apple.com/documentation/storekit/requestreviewaction) — Ratings and reviews ([Ratings and reviews](https://developer.apple.com/design/human-interface-guidelines/ratings-and-reviews))

### Swift, Objective-C
- [Managing your game window for Metal in macOS](https://developer.apple.com/documentation/metal/managing-your-game-window-for-metal-in-macos) — Going full screen ([Going full screen](https://developer.apple.com/design/human-interface-guidelines/going-full-screen))

### SwiftUI
- [confirmationDialog(_:isPresented:titleVisibility:actions:)](https://developer.apple.com/documentation/swiftui/view/confirmationdialog(_:ispresented:titlevisibility:actions:)-46zbb) — Action sheets ([Action sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets))
- [alert(_:isPresented:actions:)](https://developer.apple.com/documentation/swiftui/view/alert(_:ispresented:actions:)-1bkka) — Alerts ([Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts))
- [GroupBox](https://developer.apple.com/documentation/swiftui/groupbox) — Boxes ([Boxes](https://developer.apple.com/design/human-interface-guidelines/boxes))
- [Button](https://developer.apple.com/documentation/swiftui/button) — Buttons ([Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons))
- [ShareLink](https://developer.apple.com/documentation/swiftui/sharelink) — Collaboration and sharing ([Collaboration and sharing](https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing))
- [Color](https://developer.apple.com/documentation/swiftui/color) — Color ([Color](https://developer.apple.com/design/human-interface-guidelines/color))
- [contextMenu(menuItems:)](https://developer.apple.com/documentation/swiftui/view/contextmenu(menuitems:)) — Context menus ([Context menus](https://developer.apple.com/design/human-interface-guidelines/context-menus))
- [DisclosureGroup](https://developer.apple.com/documentation/swiftui/disclosuregroup) — Disclosure controls ([Disclosure controls](https://developer.apple.com/design/human-interface-guidelines/disclosure-controls))
- [Input events](https://developer.apple.com/documentation/swiftui/input-events) — Entering data ([Entering data](https://developer.apple.com/design/human-interface-guidelines/entering-data))
- [Documents](https://developer.apple.com/documentation/swiftui/documents) — File management ([File management](https://developer.apple.com/design/human-interface-guidelines/file-management))
- [Gauge](https://developer.apple.com/documentation/swiftui/gauge) — Gauges ([Gauges](https://developer.apple.com/design/human-interface-guidelines/gauges))
- [Gestures](https://developer.apple.com/documentation/swiftui/gestures) — Gestures ([Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures))
- [fullScreenCover(item:onDismiss:content:)](https://developer.apple.com/documentation/swiftui/view/fullscreencover(item:ondismiss:content:)) — Going full screen ([Going full screen](https://developer.apple.com/design/human-interface-guidelines/going-full-screen))
- [Image](https://developer.apple.com/documentation/swiftui/image) — Image views ([Image views](https://developer.apple.com/design/human-interface-guidelines/image-views))
- [Images](https://developer.apple.com/documentation/swiftui/images) — Images ([Images](https://developer.apple.com/design/human-interface-guidelines/images))
- [Immersive spaces](https://developer.apple.com/documentation/swiftui/immersive-spaces) — Immersive experiences ([Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences))
- [KeyboardShortcut](https://developer.apple.com/documentation/swiftui/keyboardshortcut) — Keyboards ([Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards))
- [Input events](https://developer.apple.com/documentation/swiftui/input-events) — Keyboards ([Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards))
- [Label](https://developer.apple.com/documentation/swiftui/label) — Labels ([Labels](https://developer.apple.com/design/human-interface-guidelines/labels))
- [Text](https://developer.apple.com/documentation/swiftui/text) — Labels ([Labels](https://developer.apple.com/design/human-interface-guidelines/labels))
- [Composing custom layouts with SwiftUI](https://developer.apple.com/documentation/swiftui/composing-custom-layouts-with-swiftui) — Layout ([Layout](https://developer.apple.com/design/human-interface-guidelines/layout))
- [List](https://developer.apple.com/documentation/swiftui/list) — Lists and tables ([Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables))
- [Tables](https://developer.apple.com/documentation/swiftui/tables) — Lists and tables ([Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables))
- [glassEffect(_:in:)](https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:)) — Materials ([Materials](https://developer.apple.com/design/human-interface-guidelines/materials))
- [Material](https://developer.apple.com/documentation/swiftui/material) — Materials ([Materials](https://developer.apple.com/design/human-interface-guidelines/materials))
- [Menu](https://developer.apple.com/documentation/swiftui/menu) — Menus ([Menus](https://developer.apple.com/design/human-interface-guidelines/menus))
- [Presentation modifiers](https://developer.apple.com/documentation/swiftui/view-presentation) — Modality ([Modality](https://developer.apple.com/design/human-interface-guidelines/modality))
- [Animating views and transitions](https://developer.apple.com/tutorials/swiftui/animating-views-and-transitions) — Motion ([Motion](https://developer.apple.com/design/human-interface-guidelines/motion))
- [ornament(visibility:attachmentAnchor:contentAlignment:ornament:)](https://developer.apple.com/documentation/swiftui/view/ornament(visibility:attachmentanchor:contentalignment:ornament:)) — Ornaments ([Ornaments](https://developer.apple.com/design/human-interface-guidelines/ornaments))
- [OutlineGroup](https://developer.apple.com/documentation/swiftui/outlinegroup) — Outline views ([Outline views](https://developer.apple.com/design/human-interface-guidelines/outline-views))
- [PageTabViewStyle](https://developer.apple.com/documentation/swiftui/pagetabviewstyle) — Page controls ([Page controls](https://developer.apple.com/design/human-interface-guidelines/page-controls))
- [Picker](https://developer.apple.com/documentation/swiftui/picker) — Pickers ([Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers))
- [Input events](https://developer.apple.com/documentation/swiftui/input-events) — Pointing devices ([Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices))
- [MenuPickerStyle](https://developer.apple.com/documentation/swiftui/menupickerstyle) — Pop-up buttons ([Pop-up buttons](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons))
- [popover(isPresented:attachmentAnchor:arrowEdge:content:)](https://developer.apple.com/documentation/swiftui/view/popover(ispresented:attachmentanchor:arrowedge:content:)) — Popovers ([Popovers](https://developer.apple.com/design/human-interface-guidelines/popovers))
- [ProgressView](https://developer.apple.com/documentation/swiftui/progressview) — Progress indicators ([Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators))
- [MenuPickerStyle](https://developer.apple.com/documentation/swiftui/menupickerstyle) — Pull-down buttons ([Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons))
- [Preparing views for localization](https://developer.apple.com/documentation/swiftui/preparing-views-for-localization) — Right to left ([Right to left](https://developer.apple.com/design/human-interface-guidelines/right-to-left))
- [ScrollView](https://developer.apple.com/documentation/swiftui/scrollview) — Scroll views ([Scroll views](https://developer.apple.com/design/human-interface-guidelines/scroll-views))
- [look](https://developer.apple.com/documentation/swiftui/scrollinputkind/look) — Scroll views ([Scroll views](https://developer.apple.com/design/human-interface-guidelines/scroll-views))
- [Adding a search interface to your app](https://developer.apple.com/documentation/swiftui/adding-a-search-interface-to-your-app) — Search fields ([Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields))
- [searchable(text:placement:prompt:)](https://developer.apple.com/documentation/swiftui/view/searchable(text:placement:prompt:)) — Search fields ([Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields))
- [segmented](https://developer.apple.com/documentation/swiftui/pickerstyle/segmented) — Segmented controls ([Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls))
- [Settings](https://developer.apple.com/documentation/swiftui/settings) — Settings ([Settings](https://developer.apple.com/design/human-interface-guidelines/settings))
- [sheet(item:onDismiss:content:)](https://developer.apple.com/documentation/swiftui/view/sheet(item:ondismiss:content:)) — Sheets ([Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets))
- [sidebarAdaptable](https://developer.apple.com/documentation/swiftui/tabviewstyle/sidebaradaptable) — Sidebars ([Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars))
- [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview) — Sidebars ([Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars))
- [sidebar](https://developer.apple.com/documentation/swiftui/liststyle/sidebar) — Sidebars ([Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars))
- [Slider](https://developer.apple.com/documentation/swiftui/slider) — Sliders ([Sliders](https://developer.apple.com/design/human-interface-guidelines/sliders))
- [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview) — Split views ([Split views](https://developer.apple.com/design/human-interface-guidelines/split-views))
- [TabView](https://developer.apple.com/documentation/swiftui/tabview) — Tab bars ([Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars))
- [TabViewBottomAccessoryPlacement](https://developer.apple.com/documentation/swiftui/tabviewbottomaccessoryplacement) — Tab bars ([Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars))
- [Enhancing your app’s content with tab navigation](https://developer.apple.com/documentation/swiftui/enhancing-your-app-content-with-tab-navigation) — Tab bars ([Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars))
- [TabView](https://developer.apple.com/documentation/swiftui/tabview) — Tab views ([Tab views](https://developer.apple.com/design/human-interface-guidelines/tab-views))
- [TextField](https://developer.apple.com/documentation/swiftui/textfield) — Text fields ([Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields))
- [SecureField](https://developer.apple.com/documentation/swiftui/securefield) — Text fields ([Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields))
- [Text](https://developer.apple.com/documentation/swiftui/text) — Text views ([Text views](https://developer.apple.com/design/human-interface-guidelines/text-views))
- [CommandMenu](https://developer.apple.com/documentation/swiftui/commandmenu) — The menu bar ([The menu bar](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar))
- [Toggle](https://developer.apple.com/documentation/swiftui/toggle) — Toggles ([Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles))
- [Toolbars](https://developer.apple.com/documentation/swiftui/toolbars) — Toolbars ([Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars))
- [Text input and output](https://developer.apple.com/documentation/swiftui/text-input-and-output) — Typography ([Typography](https://developer.apple.com/design/human-interface-guidelines/typography))
- [keyboardType(_:)](https://developer.apple.com/documentation/swiftui/view/keyboardtype(_:)) — Virtual keyboards ([Virtual keyboards](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards))
- [textContentType(_:)](https://developer.apple.com/documentation/swiftui/view/textcontenttype(_:)) — Virtual keyboards ([Virtual keyboards](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards))
- [Windows](https://developer.apple.com/documentation/swiftui/windows) — Windows ([Windows](https://developer.apple.com/design/human-interface-guidelines/windows))
- [WindowGroup](https://developer.apple.com/documentation/swiftui/windowgroup) — Windows ([Windows](https://developer.apple.com/design/human-interface-guidelines/windows))

### Symbols framework
- [Symbols](https://developer.apple.com/documentation/symbols) — SF Symbols ([SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols))

### TVML
- [Focus Attributes](https://developer.apple.com/documentation/tvml/focus-attributes) — Focus and selection ([Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection))

### TVUIKit
- [TVDigitEntryViewController](https://developer.apple.com/documentation/tvuikit/tvdigitentryviewcontroller) — Digit entry views ([Digit entry views](https://developer.apple.com/design/human-interface-guidelines/digit-entry-views))
- [TVLockupView](https://developer.apple.com/documentation/tvuikit/tvlockupview) — Lockups ([Lockups](https://developer.apple.com/design/human-interface-guidelines/lockups))
- [TVLockupHeaderFooterView](https://developer.apple.com/documentation/tvuikit/tvlockupheaderfooterview) — Lockups ([Lockups](https://developer.apple.com/design/human-interface-guidelines/lockups))

### UIKit
- [UIAlertController.Style.actionSheet](https://developer.apple.com/documentation/uikit/uialertcontroller/style/actionsheet) — Action sheets ([Action sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets))
- [UIActivityViewController](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller) — Activity views ([Activity views](https://developer.apple.com/design/human-interface-guidelines/activity-views))
- [UIActivity](https://developer.apple.com/documentation/uikit/uiactivity) — Activity views ([Activity views](https://developer.apple.com/design/human-interface-guidelines/activity-views))
- [UIAlertController](https://developer.apple.com/documentation/uikit/uialertcontroller) — Alerts ([Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts))
- [UIButton](https://developer.apple.com/documentation/uikit/uibutton) — Buttons ([Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons))
- [UICollectionView](https://developer.apple.com/documentation/uikit/uicollectionview) — Collections ([Collections](https://developer.apple.com/design/human-interface-guidelines/collections))
- [UIColorWell](https://developer.apple.com/documentation/uikit/uicolorwell) — Color wells ([Color wells](https://developer.apple.com/design/human-interface-guidelines/color-wells))
- [UIColorPickerViewController](https://developer.apple.com/documentation/uikit/uicolorpickerviewcontroller) — Color wells ([Color wells](https://developer.apple.com/design/human-interface-guidelines/color-wells))
- [UIColor](https://developer.apple.com/documentation/uikit/uicolor) — Color ([Color](https://developer.apple.com/design/human-interface-guidelines/color))
- [UIContextMenuInteraction](https://developer.apple.com/documentation/uikit/uicontextmenuinteraction) — Context menus ([Context menus](https://developer.apple.com/design/human-interface-guidelines/context-menus))
- [Drag and drop](https://developer.apple.com/documentation/uikit/drag-and-drop) — Drag and drop ([Drag and drop](https://developer.apple.com/design/human-interface-guidelines/drag-and-drop))
- [UIEditMenuInteraction](https://developer.apple.com/documentation/uikit/uieditmenuinteraction) — Edit menus ([Edit menus](https://developer.apple.com/design/human-interface-guidelines/edit-menus))
- [Animation and haptics](https://developer.apple.com/documentation/uikit/animation-and-haptics) — Feedback ([Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback))
- [Focus-based navigation](https://developer.apple.com/documentation/uikit/focus-based-navigation) — Focus and selection ([Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection))
- [About focus interactions for Apple TV](https://developer.apple.com/documentation/uikit/about-focus-interactions-for-apple-tv) — Focus and selection ([Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection))
- [UITouch](https://developer.apple.com/documentation/uikit/uitouch) — Gestures ([Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures))
- [Add Home Screen quick actions](https://developer.apple.com/documentation/uikit/add-home-screen-quick-actions) — Home Screen quick actions ([Home Screen quick actions](https://developer.apple.com/design/human-interface-guidelines/home-screen-quick-actions))
- [UIImageView](https://developer.apple.com/documentation/uikit/uiimageview) — Image views ([Image views](https://developer.apple.com/design/human-interface-guidelines/image-views))
- [UIImageView](https://developer.apple.com/documentation/uikit/uiimageview) — Images ([Images](https://developer.apple.com/design/human-interface-guidelines/images))
- [Handling key presses made on a physical keyboard](https://developer.apple.com/documentation/uikit/handling-key-presses-made-on-a-physical-keyboard) — Keyboards ([Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards))
- [UILabel](https://developer.apple.com/documentation/uikit/uilabel) — Labels ([Labels](https://developer.apple.com/design/human-interface-guidelines/labels))
- [Responding to the launch of your app](https://developer.apple.com/documentation/uikit/responding-to-the-launch-of-your-app) — Launching ([Launching](https://developer.apple.com/design/human-interface-guidelines/launching))
- [UITableView](https://developer.apple.com/documentation/uikit/uitableview) — Lists and tables ([Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables))
- [Mac Catalyst](https://developer.apple.com/documentation/uikit/mac-catalyst) — Mac Catalyst ([Mac Catalyst](https://developer.apple.com/design/human-interface-guidelines/mac-catalyst))
- [UIVisualEffectView](https://developer.apple.com/documentation/uikit/uivisualeffectview) — Materials ([Materials](https://developer.apple.com/design/human-interface-guidelines/materials))
- [Menus and shortcuts](https://developer.apple.com/documentation/uikit/menus-and-shortcuts) — Menus ([Menus](https://developer.apple.com/design/human-interface-guidelines/menus))
- [UIModalPresentationStyle](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle) — Modality ([Modality](https://developer.apple.com/design/human-interface-guidelines/modality))
- [Responding to the launch of your app](https://developer.apple.com/documentation/uikit/responding-to-the-launch-of-your-app) — Multitasking ([Multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking))
- [Multitasking on iPad, Mac, and Apple Vision Pro](https://developer.apple.com/documentation/uikit/multitasking-on-ipad-mac-and-apple-vision-pro) — Multitasking ([Multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking))
- [UIPageControl](https://developer.apple.com/documentation/uikit/uipagecontrol) — Page controls ([Page controls](https://developer.apple.com/design/human-interface-guidelines/page-controls))
- [UIDatePicker](https://developer.apple.com/documentation/uikit/uidatepicker) — Pickers ([Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers))
- [UIPickerView](https://developer.apple.com/documentation/uikit/uipickerview) — Pickers ([Pickers](https://developer.apple.com/design/human-interface-guidelines/pickers))
- [Pointer interactions](https://developer.apple.com/documentation/uikit/pointer-interactions) — Pointing devices ([Pointing devices](https://developer.apple.com/design/human-interface-guidelines/pointing-devices))
- [changesSelectionAsPrimaryAction](https://developer.apple.com/documentation/uikit/uibutton/changesselectionasprimaryaction) — Pop-up buttons ([Pop-up buttons](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons))
- [UIPopoverPresentationController](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller) — Popovers ([Popovers](https://developer.apple.com/design/human-interface-guidelines/popovers))
- [UIPrintInteractionController](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller) — Printing ([Printing](https://developer.apple.com/design/human-interface-guidelines/printing))
- [Requesting access to protected resources](https://developer.apple.com/documentation/uikit/requesting-access-to-protected-resources) — Privacy ([Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy))
- [UIProgressView](https://developer.apple.com/documentation/uikit/uiprogressview) — Progress indicators ([Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators))
- [UIActivityIndicatorView](https://developer.apple.com/documentation/uikit/uiactivityindicatorview) — Progress indicators ([Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators))
- [UIRefreshControl](https://developer.apple.com/documentation/uikit/uirefreshcontrol) — Progress indicators ([Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators))
- [showsMenuAsPrimaryAction](https://developer.apple.com/documentation/uikit/uicontrol/showsmenuasprimaryaction) — Pull-down buttons ([Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons))
- [UIScrollView](https://developer.apple.com/documentation/uikit/uiscrollview) — Scroll views ([Scroll views](https://developer.apple.com/design/human-interface-guidelines/scroll-views))
- [UISearchBar](https://developer.apple.com/documentation/uikit/uisearchbar) — Search fields ([Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields))
- [UISearchTextField](https://developer.apple.com/documentation/uikit/uisearchtextfield) — Search fields ([Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields))
- [UISegmentedControl](https://developer.apple.com/documentation/uikit/uisegmentedcontrol) — Segmented controls ([Segmented controls](https://developer.apple.com/design/human-interface-guidelines/segmented-controls))
- [Configuring and displaying symbol images in your UI](https://developer.apple.com/documentation/uikit/configuring-and-displaying-symbol-images-in-your-ui) — SF Symbols ([SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols))
- [Creating custom symbol images for your app](https://developer.apple.com/documentation/uikit/creating-custom-symbol-images-for-your-app) — SF Symbols ([SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols))
- [UISheetPresentationController](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller) — Sheets ([Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets))
- [UICollectionLayoutListConfiguration](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct) — Sidebars ([Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars))
- [UISlider](https://developer.apple.com/documentation/uikit/uislider) — Sliders ([Sliders](https://developer.apple.com/design/human-interface-guidelines/sliders))
- [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller) — Split views ([Split views](https://developer.apple.com/design/human-interface-guidelines/split-views))
- [UIStatusBarStyle](https://developer.apple.com/documentation/uikit/uistatusbarstyle) — Status bars ([Status bars](https://developer.apple.com/design/human-interface-guidelines/status-bars))
- [preferredStatusBarStyle](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredstatusbarstyle) — Status bars ([Status bars](https://developer.apple.com/design/human-interface-guidelines/status-bars))
- [UIStepper](https://developer.apple.com/documentation/uikit/uistepper) — Steppers ([Steppers](https://developer.apple.com/design/human-interface-guidelines/steppers))
- [UITabBar](https://developer.apple.com/documentation/uikit/uitabbar) — Tab bars ([Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars))
- [Elevating your iPad app with a tab bar and sidebar](https://developer.apple.com/documentation/uikit/elevating-your-ipad-app-with-a-tab-bar-and-sidebar) — Tab bars ([Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars))
- [UITextField](https://developer.apple.com/documentation/uikit/uitextfield) — Text fields ([Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields))
- [UITextView](https://developer.apple.com/documentation/uikit/uitextview) — Text views ([Text views](https://developer.apple.com/design/human-interface-guidelines/text-views))
- [Adding menus and shortcuts to the menu bar and user interface](https://developer.apple.com/documentation/uikit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface) — The menu bar ([The menu bar](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar))
- [UISwitch](https://developer.apple.com/documentation/uikit/uiswitch) — Toggles ([Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles))
- [UIToolbar](https://developer.apple.com/documentation/uikit/uitoolbar) — Toolbars ([Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars))
- [Text display and fonts](https://developer.apple.com/documentation/uikit/text-display-and-fonts) — Typography ([Typography](https://developer.apple.com/design/human-interface-guidelines/typography))
- [UIKeyboardType](https://developer.apple.com/documentation/uikit/uikeyboardtype) — Virtual keyboards ([Virtual keyboards](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards))
- [UIWindow](https://developer.apple.com/documentation/uikit/uiwindow) — Windows ([Windows](https://developer.apple.com/design/human-interface-guidelines/windows))

### User Notifications
- [Asking permission to use notifications](https://developer.apple.com/documentation/usernotifications/asking-permission-to-use-notifications) — Notifications ([Notifications](https://developer.apple.com/design/human-interface-guidelines/notifications))

### WatchKit
- [WKInterfacePaymentButton](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton) — Apple Pay ([Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay))
- [WKCrownDelegate](https://developer.apple.com/documentation/watchkit/wkcrowndelegate) — Digital Crown ([Digital Crown](https://developer.apple.com/design/human-interface-guidelines/digital-crown))
- [WKPageOrientation](https://developer.apple.com/documentation/watchkit/wkpageorientation) — Scroll views ([Scroll views](https://developer.apple.com/design/human-interface-guidelines/scroll-views))

### WebKit
- [WKWebView](https://developer.apple.com/documentation/webkit/wkwebview) — Web views ([Web views](https://developer.apple.com/design/human-interface-guidelines/web-views))

### WidgetKit
- [Developing a WidgetKit strategy](https://developer.apple.com/documentation/widgetkit/developing-a-widgetkit-strategy) — Live Activities ([Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities))
- [Developing a WidgetKit strategy](https://developer.apple.com/documentation/widgetkit/developing-a-widgetkit-strategy) — Widgets ([Widgets](https://developer.apple.com/design/human-interface-guidelines/widgets))

### Xcode
- [Localization](https://developer.apple.com/documentation/xcode/localization) — Inclusion ([Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion))
- [Specifying your app’s launch screen](https://developer.apple.com/documentation/xcode/specifying-your-apps-launch-screen) — Launching ([Launching](https://developer.apple.com/design/human-interface-guidelines/launching))

### visionOS
- [Adopting best practices for privacy and user preferences](https://developer.apple.com/documentation/visionos/adopting-best-practices-for-privacy) — Eyes ([Eyes](https://developer.apple.com/design/human-interface-guidelines/eyes))
- [Drawing sharp layer-based content in visionOS](https://developer.apple.com/documentation/visionos/drawing-sharp-layer-based-content) — Images ([Images](https://developer.apple.com/design/human-interface-guidelines/images))
- [Creating fully immersive experiences in your app](https://developer.apple.com/documentation/visionos/creating-fully-immersive-experiences) — Immersive experiences ([Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences))
- [Incorporating real-world surroundings in an immersive experience](https://developer.apple.com/documentation/visionos/incorporating-real-world-surroundings-in-an-immersive-experience) — Immersive experiences ([Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences))
- [ImmersionStyle](https://developer.apple.com/documentation/swiftui/immersionstyle) — Immersive experiences ([Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences))
- [Presenting windows and spaces](https://developer.apple.com/documentation/visionos/presenting-windows-and-spaces) — Spatial layout ([Spatial layout](https://developer.apple.com/design/human-interface-guidelines/spatial-layout))
- [Positioning and sizing windows](https://developer.apple.com/documentation/visionos/positioning-and-sizing-windows) — Spatial layout ([Spatial layout](https://developer.apple.com/design/human-interface-guidelines/spatial-layout))
- [Adding 3D content to your app](https://developer.apple.com/documentation/visionos/adding-3d-content-to-your-app) — Spatial layout ([Spatial layout](https://developer.apple.com/design/human-interface-guidelines/spatial-layout))

### watchOS apps
- [Designing your app for the Always On state](https://developer.apple.com/documentation/watchos-apps/designing-your-app-for-the-always-on-state) — Always On ([Always On](https://developer.apple.com/design/human-interface-guidelines/always-on))
