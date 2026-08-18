# API map: guidance to implementation

339 references pulled from every page's 'Developer documentation' section: the exact SwiftUI, UIKit, AppKit, and framework-specific API that implements each piece of guidance, plus the frameworks and guides a page points to. Entries marked framework/guide are the framework itself (AVFoundation, App Intents) or an Apple how-to, not a single symbol.

Use this to go from a design decision straight to the right API instead of guessing at a class or modifier name. When reviewing code, check the symbol used against what the HIG actually names here — a hand-rolled view where a system API exists is itself worth flagging.

---

## By component

**Accessibility** <sub>`pages/accessibility.md`</sub>
- [Building accessible apps](https://developer.apple.com/accessibility/) <sub>framework/guide</sub>
- [Accessibility](https://developer.apple.com/documentation/accessibility) <sub>framework/guide</sub>
- [Overview of Accessibility Nutrition Labels](https://devcms.apple.com/help/app-store-connect/manage-app-accessibility/overview-of-accessibility-nutrition-labels) <sub>framework/guide</sub>

**Action sheets** <sub>`pages/action-sheets.md`</sub>
- [confirmationDialog(_:isPresented:titleVisibility:actions:)](https://developer.apple.com/documentation/swiftui/view/confirmationdialog(_:ispresented:titlevisibility:actions:)-46zbb) — SwiftUI
- [UIAlertController.Style.actionSheet](https://developer.apple.com/documentation/uikit/uialertcontroller/style/actionsheet) — UIKit

**Activity rings** <sub>`pages/activity-rings.md`</sub>
- [HKActivityRingView](https://developer.apple.com/documentation/healthkitui/hkactivityringview) — HealthKit

**Activity views** <sub>`pages/activity-views.md`</sub>
- [UIActivityViewController](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller) — UIKit
- [UIActivity](https://developer.apple.com/documentation/uikit/uiactivity) — UIKit
- [App Extension Support](https://developer.apple.com/documentation/foundation/app-extension-support) — Foundation

**AirPlay** <sub>`pages/airplay.md`</sub>
- [AVFoundation](https://developer.apple.com/documentation/avfoundation) <sub>framework/guide</sub>
- [AVKit](https://developer.apple.com/documentation/avkit) <sub>framework/guide</sub>

**Alerts** <sub>`pages/alerts.md`</sub>
- [alert(_:isPresented:actions:)](https://developer.apple.com/documentation/swiftui/view/alert(_:ispresented:actions:)-1bkka) — SwiftUI
- [UIAlertController](https://developer.apple.com/documentation/uikit/uialertcontroller) — UIKit
- [NSAlert](https://developer.apple.com/documentation/appkit/nsalert) — AppKit

**Always On** <sub>`pages/always-on.md`</sub>
- [Designing your app for the Always On state](https://developer.apple.com/documentation/watchos-apps/designing-your-app-for-the-always-on-state) — watchOS apps

**App Clips** <sub>`pages/app-clips.md`</sub>
- [App Clips](https://developer.apple.com/documentation/appclip) <sub>framework/guide</sub>
- [App Store Connect](https://appstoreconnect.apple.com/) <sub>framework/guide</sub>

**App Shortcuts** <sub>`pages/app-shortcuts.md`</sub>
- [App Intents](https://developer.apple.com/documentation/appintents) <sub>framework/guide</sub>
- [SiriKit](https://developer.apple.com/documentation/sirikit) <sub>framework/guide</sub>
- [Getting started with the App Intents framework](https://developer.apple.com/documentation/appintents/getting-started-with-the-app-intents-framework) — App Intents
- [Defining app entities for your custom data types](https://developer.apple.com/documentation/appintents/defining-app-entities-for-your-custom-data-types) — App Intents

**App icons** <sub>`pages/app-icons.md`</sub>
- [Creating your app icon using Icon Composer](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer) <sub>framework/guide</sub>
- [Configuring your app icon using an asset catalog](https://developer.apple.com/documentation/xcode/configuring-your-app-icon) <sub>framework/guide</sub>

**Apple Pay** <sub>`pages/apple-pay.md`</sub>
- [Apple Pay](https://developer.apple.com/documentation/passkit/apple-pay) — PassKit
- [Apple Pay on the Web](https://developer.apple.com/documentation/applepayontheweb) <sub>framework/guide</sub>
- [WKInterfacePaymentButton](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton) — WatchKit

**Apple Pencil and Scribble** <sub>`pages/apple-pencil-and-scribble.md`</sub>
- [PencilKit](https://developer.apple.com/documentation/pencilkit) <sub>framework/guide</sub>
- [PaperKit](https://developer.apple.com/documentation/paperkit) <sub>framework/guide</sub>

**Augmented reality** <sub>`pages/augmented-reality.md`</sub>
- [ARKit](https://developer.apple.com/documentation/arkit) <sub>framework/guide</sub>

**Boxes** <sub>`pages/boxes.md`</sub>
- [GroupBox](https://developer.apple.com/documentation/swiftui/groupbox) — SwiftUI
- [NSBox](https://developer.apple.com/documentation/appkit/nsbox) — AppKit

**Buttons** <sub>`pages/buttons.md`</sub>
- [Button](https://developer.apple.com/documentation/swiftui/button) — SwiftUI
- [UIButton](https://developer.apple.com/documentation/uikit/uibutton) — UIKit
- [NSButton](https://developer.apple.com/documentation/appkit/nsbutton) — AppKit

**Camera Control** <sub>`pages/camera-control.md`</sub>
- [Enhancing your app experience with the Camera Control](https://developer.apple.com/documentation/avfoundation/enhancing-your-app-experience-with-the-camera-control) — AVFoundation
- [AVCaptureControl](https://developer.apple.com/documentation/avfoundation/avcapturecontrol) — AVFoundation
- [LockedCameraCapture](https://developer.apple.com/documentation/lockedcameracapture) <sub>framework/guide</sub>

**CarPlay** <sub>`pages/carplay.md`</sub>
- [CarPlay App Programming Guide](https://developer.apple.com/carplay/documentation/CarPlay-App-Programming-Guide.pdf) <sub>framework/guide</sub>

**CareKit** <sub>`pages/carekit.md`</sub>
- [CareKit](https://carekit-apple.github.io/CareKit/documentation/carekit) <sub>framework/guide</sub>
- [Research & Care > Developers](https://www.researchandcare.org/developers/) <sub>framework/guide</sub>
- [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy) — HealthKit
- [HealthKit](https://developer.apple.com/documentation/healthkit) <sub>framework/guide</sub>
- [ResearchKit GitHub project](https://github.com/ResearchKit/ResearchKit) <sub>framework/guide</sub>

**Charting data** <sub>`pages/charting-data.md`</sub>
- [Swift Charts](https://developer.apple.com/documentation/charts) <sub>framework/guide</sub>

**Charts** <sub>`pages/charts.md`</sub>
- [Swift Charts](https://developer.apple.com/documentation/charts) <sub>framework/guide</sub>

**Collaboration and sharing** <sub>`pages/collaboration-and-sharing.md`</sub>
- [Shared with You](https://developer.apple.com/documentation/sharedwithyou) <sub>framework/guide</sub>
- [ShareLink](https://developer.apple.com/documentation/swiftui/sharelink) — SwiftUI

**Collections** <sub>`pages/collections.md`</sub>
- [UICollectionView](https://developer.apple.com/documentation/uikit/uicollectionview) — UIKit
- [NSCollectionView](https://developer.apple.com/documentation/appkit/nscollectionview) — AppKit

**Color** <sub>`pages/color.md`</sub>
- [Color](https://developer.apple.com/documentation/swiftui/color) — SwiftUI
- [UIColor](https://developer.apple.com/documentation/uikit/uicolor) — UIKit
- [Color](https://developer.apple.com/documentation/appkit/color) — AppKit

**Color wells** <sub>`pages/color-wells.md`</sub>
- [UIColorWell](https://developer.apple.com/documentation/uikit/uicolorwell) — UIKit
- [UIColorPickerViewController](https://developer.apple.com/documentation/uikit/uicolorpickerviewcontroller) — UIKit
- [NSColorWell](https://developer.apple.com/documentation/appkit/nscolorwell) — AppKit
- [Color Programming Topics](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/DrawColor/DrawColor.html) <sub>framework/guide</sub>

**Column views** <sub>`pages/column-views.md`</sub>
- [NSBrowser](https://developer.apple.com/documentation/appkit/nsbrowser) — AppKit

**Combo boxes** <sub>`pages/combo-boxes.md`</sub>
- [NSComboBox](https://developer.apple.com/documentation/appkit/nscombobox) — AppKit

**Complications** <sub>`pages/complications.md`</sub>
- [WidgetKit](https://developer.apple.com/documentation/widgetkit) <sub>framework/guide</sub>

**Context menus** <sub>`pages/context-menus.md`</sub>
- [contextMenu(menuItems:)](https://developer.apple.com/documentation/swiftui/view/contextmenu(menuitems:)) — SwiftUI
- [UIContextMenuInteraction](https://developer.apple.com/documentation/uikit/uicontextmenuinteraction) — UIKit
- [popUpContextMenu(_:with:for:)](https://developer.apple.com/documentation/appkit/nsmenu/popupcontextmenu(_:with:for:)) — AppKit

**Controls** <sub>`pages/controls.md`</sub>
- [LockedCameraCapture](https://developer.apple.com/documentation/lockedcameracapture) <sub>framework/guide</sub>
- [WidgetKit](https://developer.apple.com/documentation/widgetkit) <sub>framework/guide</sub>

**Designing for games** <sub>`pages/designing-for-games.md`</sub>
- [Games Pathway](https://developer.apple.com/games/get-started/) <sub>framework/guide</sub>
- [Create games for Apple platforms](https://developer.apple.com/games/) <sub>framework/guide</sub>

**Designing for iOS** <sub>`pages/designing-for-ios.md`</sub>
- [iOS Pathway](https://developer.apple.com/ios/get-started/) <sub>framework/guide</sub>

**Designing for iPadOS** <sub>`pages/designing-for-ipados.md`</sub>
- [iPadOS Pathway](https://developer.apple.com/ipados/get-started/) <sub>framework/guide</sub>

**Designing for macOS** <sub>`pages/designing-for-macos.md`</sub>
- [macOS Pathway](https://developer.apple.com/macos/get-started/) <sub>framework/guide</sub>

**Designing for tvOS** <sub>`pages/designing-for-tvos.md`</sub>
- [tvOS Pathway](https://developer.apple.com/tvos/get-started/) <sub>framework/guide</sub>

**Designing for visionOS** <sub>`pages/designing-for-visionos.md`</sub>
- [visionOS Pathway](https://developer.apple.com/visionos/get-started/) <sub>framework/guide</sub>
- [Creating your first visionOS app](https://developer.apple.com/documentation/visionos/creating-your-first-visionos-app) <sub>framework/guide</sub>

**Designing for watchOS** <sub>`pages/designing-for-watchos.md`</sub>
- [watchOS Pathway](https://developer.apple.com/watchos/get-started/) <sub>framework/guide</sub>

**Digit entry views** <sub>`pages/digit-entry-views.md`</sub>
- [TVDigitEntryViewController](https://developer.apple.com/documentation/tvuikit/tvdigitentryviewcontroller) — TVUIKit

**Digital Crown** <sub>`pages/digital-crown.md`</sub>
- [WKCrownDelegate](https://developer.apple.com/documentation/watchkit/wkcrowndelegate) — WatchKit

**Disclosure controls** <sub>`pages/disclosure-controls.md`</sub>
- [DisclosureGroup](https://developer.apple.com/documentation/swiftui/disclosuregroup) — SwiftUI
- [NSButton.BezelStyle.disclosure](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/disclosure) — AppKit
- [NSButton.BezelStyle.pushDisclosure](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/pushdisclosure) — AppKit

**Dock menus** <sub>`pages/dock-menus.md`</sub>
- [applicationDockMenu(_:)](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationdockmenu(_:)) — AppKit

**Drag and drop** <sub>`pages/drag-and-drop.md`</sub>
- [Drag and drop](https://developer.apple.com/documentation/uikit/drag-and-drop) — UIKit
- [Drag and Drop](https://developer.apple.com/documentation/appkit/drag-and-drop) — AppKit
- [File Provider](https://developer.apple.com/documentation/fileprovider) <sub>framework/guide</sub>

**Edit menus** <sub>`pages/edit-menus.md`</sub>
- [UIEditMenuInteraction](https://developer.apple.com/documentation/uikit/uieditmenuinteraction) — UIKit
- [NSMenu](https://developer.apple.com/documentation/appkit/nsmenu) — AppKit

**Entering data** <sub>`pages/entering-data.md`</sub>
- [Input events](https://developer.apple.com/documentation/swiftui/input-events) — SwiftUI

**Eyes** <sub>`pages/eyes.md`</sub>
- [Adopting best practices for privacy and user preferences](https://developer.apple.com/documentation/visionos/adopting-best-practices-for-privacy) — visionOS

**Feedback** <sub>`pages/feedback.md`</sub>
- [Animation and haptics](https://developer.apple.com/documentation/uikit/animation-and-haptics) — UIKit

**File management** <sub>`pages/file-management.md`</sub>
- [Documents](https://developer.apple.com/documentation/swiftui/documents) — SwiftUI

**Focus and selection** <sub>`pages/focus-and-selection.md`</sub>
- [Focus Attributes](https://developer.apple.com/documentation/tvml/focus-attributes) — TVML
- [Focus-based navigation](https://developer.apple.com/documentation/uikit/focus-based-navigation) — UIKit
- [About focus interactions for Apple TV](https://developer.apple.com/documentation/uikit/about-focus-interactions-for-apple-tv) — UIKit

**Game Center** <sub>`pages/game-center.md`</sub>
- [GameKit](https://developer.apple.com/documentation/gamekit) <sub>framework/guide</sub>
- [Creating activities for your game](https://developer.apple.com/documentation/gamekit/creating-activities-for-your-game) <sub>framework/guide</sub>
- [Creating engaging challenges from leaderboards](https://developer.apple.com/documentation/gamekit/creating-engaging-challenges-from-leaderboards) <sub>framework/guide</sub>
- [Create games for Apple platforms](https://developer.apple.com/games/) <sub>framework/guide</sub>
- [Game Porting Toolkit](https://developer.apple.com/games/game-porting-toolkit/) <sub>framework/guide</sub>

**Game controls** <sub>`pages/game-controls.md`</sub>
- [Create games for Apple platforms](https://developer.apple.com/games/) <sub>framework/guide</sub>
- [Touch Controller](https://developer.apple.com/documentation/touchcontroller) <sub>framework/guide</sub>
- [Game Controller](https://developer.apple.com/documentation/gamecontroller) <sub>framework/guide</sub>

**Gauges** <sub>`pages/gauges.md`</sub>
- [Gauge](https://developer.apple.com/documentation/swiftui/gauge) — SwiftUI
- [NSLevelIndicator](https://developer.apple.com/documentation/appkit/nslevelindicator) — AppKit

**Generative AI** <sub>`pages/generative-ai.md`</sub>
- [Apple Intelligence and machine learning](https://developer.apple.com/documentation/technologyoverviews/ai-machine-learning) <sub>framework/guide</sub>
- [Foundation Models](https://developer.apple.com/documentation/foundationmodels) <sub>framework/guide</sub>
- [Core AI](https://developer.apple.com/documentation/coreai) <sub>framework/guide</sub>

**Gestures** <sub>`pages/gestures.md`</sub>
- [Gestures](https://developer.apple.com/documentation/swiftui/gestures) — SwiftUI
- [UITouch](https://developer.apple.com/documentation/uikit/uitouch) — UIKit

**Going full screen** <sub>`pages/going-full-screen.md`</sub>
- [fullScreenCover(item:onDismiss:content:)](https://developer.apple.com/documentation/swiftui/view/fullscreencover(item:ondismiss:content:)) — SwiftUI
- [NSScreen](https://developer.apple.com/documentation/appkit/nsscreen) — AppKit
- [NSWindow.CollectionBehavior](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior-swift.struct) — AppKit
- [Managing your game window for Metal in macOS](https://developer.apple.com/documentation/metal/managing-your-game-window-for-metal-in-macos) — Swift, Objective-C

**Gyroscope and accelerometer** <sub>`pages/gyro-and-accelerometer.md`</sub>
- [Getting processed device-motion data](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data) — Core Motion

**HealthKit** <sub>`pages/healthkit.md`</sub>
- [HealthKit](https://developer.apple.com/documentation/healthkit) <sub>framework/guide</sub>
- [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy) — HealthKit

**Home Screen quick actions** <sub>`pages/home-screen-quick-actions.md`</sub>
- [Add Home Screen quick actions](https://developer.apple.com/documentation/uikit/add-home-screen-quick-actions) — UIKit

**HomeKit** <sub>`pages/homekit.md`</sub>
- [HomeKit](https://developer.apple.com/documentation/homekit) <sub>framework/guide</sub>

**ID Verifier** <sub>`pages/id-verifier.md`</sub>
- [Adopting the Verifier API in your iPhone app](https://developer.apple.com/documentation/proximityreader/adopting-the-verifier-api-in-your-iphone-app) — ProximityReader

**Image views** <sub>`pages/image-views.md`</sub>
- [Image](https://developer.apple.com/documentation/swiftui/image) — SwiftUI
- [UIImageView](https://developer.apple.com/documentation/uikit/uiimageview) — UIKit
- [NSImageView](https://developer.apple.com/documentation/appkit/nsimageview) — AppKit

**Image wells** <sub>`pages/image-wells.md`</sub>
- [NSImageView](https://developer.apple.com/documentation/appkit/nsimageview) — AppKit

**Images** <sub>`pages/images.md`</sub>
- [Drawing sharp layer-based content in visionOS](https://developer.apple.com/documentation/visionos/drawing-sharp-layer-based-content) — visionOS
- [Images](https://developer.apple.com/documentation/swiftui/images) — SwiftUI
- [UIImageView](https://developer.apple.com/documentation/uikit/uiimageview) — UIKit
- [NSImageView](https://developer.apple.com/documentation/appkit/nsimageview) — AppKit

**Immersive experiences** <sub>`pages/immersive-experiences.md`</sub>
- [Creating fully immersive experiences in your app](https://developer.apple.com/documentation/visionos/creating-fully-immersive-experiences) — visionOS
- [Incorporating real-world surroundings in an immersive experience](https://developer.apple.com/documentation/visionos/incorporating-real-world-surroundings-in-an-immersive-experience) — visionOS
- [ImmersionStyle](https://developer.apple.com/documentation/swiftui/immersionstyle) — visionOS
- [Immersive spaces](https://developer.apple.com/documentation/swiftui/immersive-spaces) — SwiftUI

**In-app purchase** <sub>`pages/in-app-purchase.md`</sub>
- [In-App Purchase](https://developer.apple.com/documentation/storekit/in-app-purchase) — StoreKit

**Inclusion** <sub>`pages/inclusion.md`</sub>
- [Localization](https://developer.apple.com/documentation/xcode/localization) — Xcode

**Keyboards** <sub>`pages/keyboards.md`</sub>
- [KeyboardShortcut](https://developer.apple.com/documentation/swiftui/keyboardshortcut) — SwiftUI
- [Input events](https://developer.apple.com/documentation/swiftui/input-events) — SwiftUI
- [Handling key presses made on a physical keyboard](https://developer.apple.com/documentation/uikit/handling-key-presses-made-on-a-physical-keyboard) — UIKit
- [Mouse, Keyboard, and Trackpad](https://developer.apple.com/documentation/appkit/mouse-keyboard-and-trackpad) — AppKit

**Labels** <sub>`pages/labels.md`</sub>
- [Label](https://developer.apple.com/documentation/swiftui/label) — SwiftUI
- [Text](https://developer.apple.com/documentation/swiftui/text) — SwiftUI
- [UILabel](https://developer.apple.com/documentation/uikit/uilabel) — UIKit
- [NSTextField](https://developer.apple.com/documentation/appkit/nstextfield) — AppKit

**Launching** <sub>`pages/launching.md`</sub>
- [Specifying your app’s launch screen](https://developer.apple.com/documentation/xcode/specifying-your-apps-launch-screen) — Xcode
- [Responding to the launch of your app](https://developer.apple.com/documentation/uikit/responding-to-the-launch-of-your-app) — UIKit

**Layout** <sub>`pages/layout.md`</sub>
- [Composing custom layouts with SwiftUI](https://developer.apple.com/documentation/swiftui/composing-custom-layouts-with-swiftui) — SwiftUI

**Lists and tables** <sub>`pages/lists-and-tables.md`</sub>
- [List](https://developer.apple.com/documentation/swiftui/list) — SwiftUI
- [Tables](https://developer.apple.com/documentation/swiftui/tables) — SwiftUI
- [UITableView](https://developer.apple.com/documentation/uikit/uitableview) — UIKit
- [NSTableView](https://developer.apple.com/documentation/appkit/nstableview) — AppKit

**Live Activities** <sub>`pages/live-activities.md`</sub>
- [ActivityKit](https://developer.apple.com/documentation/activitykit) <sub>framework/guide</sub>
- [SwiftUI](https://developer.apple.com/documentation/swiftui) <sub>framework/guide</sub>
- [WidgetKit](https://developer.apple.com/documentation/widgetkit) <sub>framework/guide</sub>
- [Developing a WidgetKit strategy](https://developer.apple.com/documentation/widgetkit/developing-a-widgetkit-strategy) — WidgetKit

**Live Photos** <sub>`pages/live-photos.md`</sub>
- [PHLivePhoto](https://developer.apple.com/documentation/photos/phlivephoto) — PhotoKit
- [LivePhotosKit JS](https://developer.apple.com/documentation/livephotoskitjs) — LivePhotosKit JS

**Loading** <sub>`pages/loading.md`</sub>
- [Background Assets](https://developer.apple.com/documentation/backgroundassets) <sub>framework/guide</sub>

**Lockups** <sub>`pages/lockups.md`</sub>
- [TVLockupView](https://developer.apple.com/documentation/tvuikit/tvlockupview) — TVUIKit
- [TVLockupHeaderFooterView](https://developer.apple.com/documentation/tvuikit/tvlockupheaderfooterview) — TVUIKit

**Mac Catalyst** <sub>`pages/mac-catalyst.md`</sub>
- [Mac Catalyst](https://developer.apple.com/documentation/uikit/mac-catalyst) — UIKit

**Machine learning** <sub>`pages/machine-learning.md`</sub>
- [Apple Intelligence and machine learning](https://developer.apple.com/documentation/technologyoverviews/ai-machine-learning) <sub>framework/guide</sub>
- [Create ML](https://developer.apple.com/documentation/createml) <sub>framework/guide</sub>
- [Core ML](https://developer.apple.com/documentation/coreml) <sub>framework/guide</sub>

**Managing accounts** <sub>`pages/managing-accounts.md`</sub>
- [Supporting passkeys](https://developer.apple.com/documentation/authenticationservices/supporting-passkeys) — Authentication Services

**Managing notifications** <sub>`pages/managing-notifications.md`</sub>
- [User Notifications](https://developer.apple.com/documentation/usernotifications) <sub>framework/guide</sub>

**Maps** <sub>`pages/maps.md`</sub>
- [MapKit](https://developer.apple.com/documentation/mapkit) <sub>framework/guide</sub>
- [MapKit JS](https://developer.apple.com/documentation/mapkitjs) <sub>framework/guide</sub>
- [Indoor Mapping Data Format](https://register.apple.com/resources/imdf/) <sub>framework/guide</sub>

**Materials** <sub>`pages/materials.md`</sub>
- [Adopting Liquid Glass](https://developer.apple.com/documentation/technologyoverviews/adopting-liquid-glass) <sub>framework/guide</sub>
- [glassEffect(_:in:)](https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:)) — SwiftUI
- [Material](https://developer.apple.com/documentation/swiftui/material) — SwiftUI
- [UIVisualEffectView](https://developer.apple.com/documentation/uikit/uivisualeffectview) — UIKit
- [NSVisualEffectView](https://developer.apple.com/documentation/appkit/nsvisualeffectview) — AppKit

**Menus** <sub>`pages/menus.md`</sub>
- [Menu](https://developer.apple.com/documentation/swiftui/menu) — SwiftUI
- [Menus and shortcuts](https://developer.apple.com/documentation/uikit/menus-and-shortcuts) — UIKit
- [Menus](https://developer.apple.com/documentation/appkit/menus) — AppKit

**Modality** <sub>`pages/modality.md`</sub>
- [Presentation modifiers](https://developer.apple.com/documentation/swiftui/view-presentation) — SwiftUI
- [UIModalPresentationStyle](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle) — UIKit
- [Modal Windows and Panels](https://developer.apple.com/documentation/appkit/modal-windows-and-panels) — AppKit

**Motion** <sub>`pages/motion.md`</sub>
- [Animating views and transitions](https://developer.apple.com/tutorials/swiftui/animating-views-and-transitions) — SwiftUI

**Multitasking** <sub>`pages/multitasking.md`</sub>
- [Responding to the launch of your app](https://developer.apple.com/documentation/uikit/responding-to-the-launch-of-your-app) — UIKit
- [Multitasking on iPad, Mac, and Apple Vision Pro](https://developer.apple.com/documentation/uikit/multitasking-on-ipad-mac-and-apple-vision-pro) — UIKit

**NFC** <sub>`pages/nfc.md`</sub>
- [Core NFC](https://developer.apple.com/documentation/corenfc) <sub>framework/guide</sub>

**Nearby interactions** <sub>`pages/nearby-interactions.md`</sub>
- [Nearby Interaction](https://developer.apple.com/documentation/nearbyinteraction) <sub>framework/guide</sub>

**Notifications** <sub>`pages/notifications.md`</sub>
- [Asking permission to use notifications](https://developer.apple.com/documentation/usernotifications/asking-permission-to-use-notifications) — User Notifications
- [User Notifications UI](https://developer.apple.com/documentation/usernotificationsui) <sub>framework/guide</sub>
- [User Notifications](https://developer.apple.com/documentation/usernotifications) <sub>framework/guide</sub>

**Offering help** <sub>`pages/offering-help.md`</sub>
- [TipKit](https://developer.apple.com/documentation/tipkit) <sub>framework/guide</sub>
- [NSHelpManager](https://developer.apple.com/documentation/appkit/nshelpmanager) — AppKit

**Ornaments** <sub>`pages/ornaments.md`</sub>
- [ornament(visibility:attachmentAnchor:contentAlignment:ornament:)](https://developer.apple.com/documentation/swiftui/view/ornament(visibility:attachmentanchor:contentalignment:ornament:)) — SwiftUI

**Outline views** <sub>`pages/outline-views.md`</sub>
- [OutlineGroup](https://developer.apple.com/documentation/swiftui/outlinegroup) — SwiftUI
- [NSOutlineView](https://developer.apple.com/documentation/appkit/nsoutlineview) — AppKit

**Page controls** <sub>`pages/page-controls.md`</sub>
- [PageTabViewStyle](https://developer.apple.com/documentation/swiftui/pagetabviewstyle) — SwiftUI
- [UIPageControl](https://developer.apple.com/documentation/uikit/uipagecontrol) — UIKit

**Panels** <sub>`pages/panels.md`</sub>
- [NSPanel](https://developer.apple.com/documentation/appkit/nspanel) — AppKit
- [hudWindow](https://developer.apple.com/documentation/appkit/nswindow/stylemask-swift.struct/hudwindow) — AppKit

**Path controls** <sub>`pages/path-controls.md`</sub>
- [NSPathControl](https://developer.apple.com/documentation/appkit/nspathcontrol) — AppKit

**Photo editing** <sub>`pages/photo-editing.md`</sub>
- [App extensions](https://developer.apple.com/app-extensions/) <sub>framework/guide</sub>
- [PhotoKit](https://developer.apple.com/documentation/photokit) <sub>framework/guide</sub>

**Pickers** <sub>`pages/pickers.md`</sub>
- [Picker](https://developer.apple.com/documentation/swiftui/picker) — SwiftUI
- [UIDatePicker](https://developer.apple.com/documentation/uikit/uidatepicker) — UIKit
- [UIPickerView](https://developer.apple.com/documentation/uikit/uipickerview) — UIKit
- [NSDatePicker](https://developer.apple.com/documentation/appkit/nsdatepicker) — AppKit

**Playing audio** <sub>`pages/playing-audio.md`</sub>
- [Configuring your app for media playback](https://developer.apple.com/documentation/avfoundation/configuring-your-app-for-media-playback) — AVFoundation
- [AVAudioSession](https://developer.apple.com/documentation/avfaudio/avaudiosession) — AVFAudio
- [MusicKit](https://developer.apple.com/documentation/musickit) — MusicKit

**Playing haptics** <sub>`pages/playing-haptics.md`</sub>
- [Core Haptics](https://developer.apple.com/documentation/corehaptics) <sub>framework/guide</sub>

**Playing video** <sub>`pages/playing-video.md`</sub>
- [Configuring your app for media playback](https://developer.apple.com/documentation/avfoundation/configuring-your-app-for-media-playback) — AVFoundation
- [AVKit](https://developer.apple.com/documentation/avkit) <sub>framework/guide</sub>
- [HTTP Live Streaming](https://developer.apple.com/streaming/) <sub>framework/guide</sub>

**Pointing devices** <sub>`pages/pointing-devices.md`</sub>
- [Input events](https://developer.apple.com/documentation/swiftui/input-events) — SwiftUI
- [Pointer interactions](https://developer.apple.com/documentation/uikit/pointer-interactions) — UIKit
- [Mouse, Keyboard, and Trackpad](https://developer.apple.com/documentation/appkit/mouse-keyboard-and-trackpad) — AppKit

**Pop-up buttons** <sub>`pages/pop-up-buttons.md`</sub>
- [MenuPickerStyle](https://developer.apple.com/documentation/swiftui/menupickerstyle) — SwiftUI
- [changesSelectionAsPrimaryAction](https://developer.apple.com/documentation/uikit/uibutton/changesselectionasprimaryaction) — UIKit
- [NSPopUpButton](https://developer.apple.com/documentation/appkit/nspopupbutton) — AppKit

**Popovers** <sub>`pages/popovers.md`</sub>
- [popover(isPresented:attachmentAnchor:arrowEdge:content:)](https://developer.apple.com/documentation/swiftui/view/popover(ispresented:attachmentanchor:arrowedge:content:)) — SwiftUI
- [UIPopoverPresentationController](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller) — UIKit
- [NSPopover](https://developer.apple.com/documentation/appkit/nspopover) — AppKit

**Printing** <sub>`pages/printing.md`</sub>
- [UIPrintInteractionController](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller) — UIKit
- [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) — AppKit

**Privacy** <sub>`pages/privacy.md`</sub>
- [Requesting access to protected resources](https://developer.apple.com/documentation/uikit/requesting-access-to-protected-resources) — UIKit
- [Security](https://developer.apple.com/documentation/security) <sub>framework/guide</sub>
- [Requesting authorization to use location services](https://developer.apple.com/documentation/corelocation/requesting-authorization-to-use-location-services) — CoreLocation
- [App Tracking Transparency](https://developer.apple.com/documentation/apptrackingtransparency) <sub>framework/guide</sub>

**Progress indicators** <sub>`pages/progress-indicators.md`</sub>
- [ProgressView](https://developer.apple.com/documentation/swiftui/progressview) — SwiftUI
- [UIProgressView](https://developer.apple.com/documentation/uikit/uiprogressview) — UIKit
- [UIActivityIndicatorView](https://developer.apple.com/documentation/uikit/uiactivityindicatorview) — UIKit
- [UIRefreshControl](https://developer.apple.com/documentation/uikit/uirefreshcontrol) — UIKit
- [NSProgressIndicator](https://developer.apple.com/documentation/appkit/nsprogressindicator) — AppKit

**Pull-down buttons** <sub>`pages/pull-down-buttons.md`</sub>
- [MenuPickerStyle](https://developer.apple.com/documentation/swiftui/menupickerstyle) — SwiftUI
- [showsMenuAsPrimaryAction](https://developer.apple.com/documentation/uikit/uicontrol/showsmenuasprimaryaction) — UIKit
- [pullsDown](https://developer.apple.com/documentation/appkit/nspopupbutton/pullsdown) — AppKit

**Rating indicators** <sub>`pages/rating-indicators.md`</sub>
- [NSLevelIndicator.Style.rating](https://developer.apple.com/documentation/appkit/nslevelindicator/style/rating) — AppKit

**Ratings and reviews** <sub>`pages/ratings-and-reviews.md`</sub>
- [RequestReviewAction](https://developer.apple.com/documentation/storekit/requestreviewaction) — StoreKit

**ResearchKit** <sub>`pages/researchkit.md`</sub>
- [Research & Care > Developers](https://www.researchandcare.org/developers/) <sub>framework/guide</sub>
- [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy) — HealthKit
- [ResearchKit GitHub project](https://github.com/ResearchKit/ResearchKit) <sub>framework/guide</sub>

**Right to left** <sub>`pages/right-to-left.md`</sub>
- [Localization](https://developer.apple.com/localization/) <sub>framework/guide</sub>
- [Preparing views for localization](https://developer.apple.com/documentation/swiftui/preparing-views-for-localization) — SwiftUI

**SF Symbols** <sub>`pages/sf-symbols.md`</sub>
- [Symbols](https://developer.apple.com/documentation/symbols) — Symbols framework
- [Configuring and displaying symbol images in your UI](https://developer.apple.com/documentation/uikit/configuring-and-displaying-symbol-images-in-your-ui) — UIKit
- [Creating custom symbol images for your app](https://developer.apple.com/documentation/uikit/creating-custom-symbol-images-for-your-app) — UIKit

**Scroll views** <sub>`pages/scroll-views.md`</sub>
- [ScrollView](https://developer.apple.com/documentation/swiftui/scrollview) — SwiftUI
- [UIScrollView](https://developer.apple.com/documentation/uikit/uiscrollview) — UIKit
- [NSScrollView](https://developer.apple.com/documentation/appkit/nsscrollview) — AppKit
- [WKPageOrientation](https://developer.apple.com/documentation/watchkit/wkpageorientation) — WatchKit
- [look](https://developer.apple.com/documentation/swiftui/scrollinputkind/look) — SwiftUI

**Search fields** <sub>`pages/search-fields.md`</sub>
- [Adding a search interface to your app](https://developer.apple.com/documentation/swiftui/adding-a-search-interface-to-your-app) — SwiftUI
- [searchable(text:placement:prompt:)](https://developer.apple.com/documentation/swiftui/view/searchable(text:placement:prompt:)) — SwiftUI
- [UISearchBar](https://developer.apple.com/documentation/uikit/uisearchbar) — UIKit
- [UISearchTextField](https://developer.apple.com/documentation/uikit/uisearchtextfield) — UIKit
- [NSSearchField](https://developer.apple.com/documentation/appkit/nssearchfield) — AppKit

**Searching** <sub>`pages/searching.md`</sub>
- [Adding your app’s content to Spotlight indexes](https://developer.apple.com/documentation/corespotlight/adding-your-app-s-content-to-spotlight-indexes) — Core Spotlight

**Segmented controls** <sub>`pages/segmented-controls.md`</sub>
- [segmented](https://developer.apple.com/documentation/swiftui/pickerstyle/segmented) — SwiftUI
- [UISegmentedControl](https://developer.apple.com/documentation/uikit/uisegmentedcontrol) — UIKit
- [NSSegmentedControl](https://developer.apple.com/documentation/appkit/nssegmentedcontrol) — AppKit

**Settings** <sub>`pages/settings.md`</sub>
- [Settings](https://developer.apple.com/documentation/swiftui/settings) — SwiftUI
- [UserDefaults](https://developer.apple.com/documentation/foundation/userdefaults) — Foundation
- [Preference Panes](https://developer.apple.com/documentation/preferencepanes) <sub>framework/guide</sub>

**SharePlay** <sub>`pages/shareplay.md`</sub>
- [Group Activities](https://developer.apple.com/documentation/groupactivities) <sub>framework/guide</sub>

**ShazamKit** <sub>`pages/shazamkit.md`</sub>
- [ShazamKit](https://developer.apple.com/documentation/shazamkit) <sub>framework/guide</sub>

**Sheets** <sub>`pages/sheets.md`</sub>
- [sheet(item:onDismiss:content:)](https://developer.apple.com/documentation/swiftui/view/sheet(item:ondismiss:content:)) — SwiftUI
- [UISheetPresentationController](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller) — UIKit
- [presentAsSheet(_:)](https://developer.apple.com/documentation/appkit/nsviewcontroller/presentassheet(_:)) — AppKit

**Sidebars** <sub>`pages/sidebars.md`</sub>
- [sidebarAdaptable](https://developer.apple.com/documentation/swiftui/tabviewstyle/sidebaradaptable) — SwiftUI
- [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview) — SwiftUI
- [sidebar](https://developer.apple.com/documentation/swiftui/liststyle/sidebar) — SwiftUI
- [UICollectionLayoutListConfiguration](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct) — UIKit
- [NSSplitViewController](https://developer.apple.com/documentation/appkit/nssplitviewcontroller) — AppKit

**Sign in with Apple** <sub>`pages/sign-in-with-apple.md`</sub>
- [Authentication Services](https://developer.apple.com/documentation/authenticationservices) <sub>framework/guide</sub>
- [Displaying Sign in with Apple buttons on the web](https://developer.apple.com/documentation/signinwithapple/displaying-sign-in-with-apple-buttons-on-the-web) — Sign in with Apple

**Siri** <sub>`pages/siri.md`</sub>
- [App Intents](https://developer.apple.com/documentation/appintents) <sub>framework/guide</sub>
- [App schema domains](https://developer.apple.com/documentation/appintents/app-schema-domains) <sub>framework/guide</sub>
- [Apple Intelligence and Siri AI](https://developer.apple.com/documentation/appintents/apple-intelligence-and-siri-ai) <sub>framework/guide</sub>

**Sliders** <sub>`pages/sliders.md`</sub>
- [Slider](https://developer.apple.com/documentation/swiftui/slider) — SwiftUI
- [UISlider](https://developer.apple.com/documentation/uikit/uislider) — UIKit
- [NSSlider](https://developer.apple.com/documentation/appkit/nsslider) — AppKit

**Snippets** <sub>`pages/snippets.md`</sub>
- [App Intents](https://developer.apple.com/documentation/appintents) <sub>framework/guide</sub>

**Spatial layout** <sub>`pages/spatial-layout.md`</sub>
- [Presenting windows and spaces](https://developer.apple.com/documentation/visionos/presenting-windows-and-spaces) — visionOS
- [Positioning and sizing windows](https://developer.apple.com/documentation/visionos/positioning-and-sizing-windows) — visionOS
- [Adding 3D content to your app](https://developer.apple.com/documentation/visionos/adding-3d-content-to-your-app) — visionOS

**Split views** <sub>`pages/split-views.md`</sub>
- [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview) — SwiftUI
- [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller) — UIKit
- [NSSplitViewController](https://developer.apple.com/documentation/appkit/nssplitviewcontroller) — AppKit

**Status bars** <sub>`pages/status-bars.md`</sub>
- [UIStatusBarStyle](https://developer.apple.com/documentation/uikit/uistatusbarstyle) — UIKit
- [preferredStatusBarStyle](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredstatusbarstyle) — UIKit

**Steppers** <sub>`pages/steppers.md`</sub>
- [UIStepper](https://developer.apple.com/documentation/uikit/uistepper) — UIKit
- [NSStepper](https://developer.apple.com/documentation/appkit/nsstepper) — AppKit

**Tab bars** <sub>`pages/tab-bars.md`</sub>
- [TabView](https://developer.apple.com/documentation/swiftui/tabview) — SwiftUI
- [TabViewBottomAccessoryPlacement](https://developer.apple.com/documentation/swiftui/tabviewbottomaccessoryplacement) — SwiftUI
- [Enhancing your app’s content with tab navigation](https://developer.apple.com/documentation/swiftui/enhancing-your-app-content-with-tab-navigation) — SwiftUI
- [UITabBar](https://developer.apple.com/documentation/uikit/uitabbar) — UIKit
- [Elevating your iPad app with a tab bar and sidebar](https://developer.apple.com/documentation/uikit/elevating-your-ipad-app-with-a-tab-bar-and-sidebar) — UIKit

**Tab views** <sub>`pages/tab-views.md`</sub>
- [TabView](https://developer.apple.com/documentation/swiftui/tabview) — SwiftUI
- [NSTabView](https://developer.apple.com/documentation/appkit/nstabview) — AppKit

**Tap to Pay on iPhone** <sub>`pages/tap-to-pay-on-iphone.md`</sub>
- [Adding support for Tap to Pay on iPhone to your app](https://developer.apple.com/documentation/proximityreader/adding-support-for-tap-to-pay-on-iphone-to-your-app) — ProximityReader

**Text fields** <sub>`pages/text-fields.md`</sub>
- [TextField](https://developer.apple.com/documentation/swiftui/textfield) — SwiftUI
- [SecureField](https://developer.apple.com/documentation/swiftui/securefield) — SwiftUI
- [UITextField](https://developer.apple.com/documentation/uikit/uitextfield) — UIKit
- [NSTextField](https://developer.apple.com/documentation/appkit/nstextfield) — AppKit

**Text views** <sub>`pages/text-views.md`</sub>
- [Text](https://developer.apple.com/documentation/swiftui/text) — SwiftUI
- [UITextView](https://developer.apple.com/documentation/uikit/uitextview) — UIKit
- [NSTextView](https://developer.apple.com/documentation/appkit/nstextview) — AppKit

**The menu bar** <sub>`pages/the-menu-bar.md`</sub>
- [CommandMenu](https://developer.apple.com/documentation/swiftui/commandmenu) — SwiftUI
- [Adding menus and shortcuts to the menu bar and user interface](https://developer.apple.com/documentation/uikit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface) — UIKit
- [NSStatusBar](https://developer.apple.com/documentation/appkit/nsstatusbar) — AppKit

**Toggles** <sub>`pages/toggles.md`</sub>
- [Toggle](https://developer.apple.com/documentation/swiftui/toggle) — SwiftUI
- [UISwitch](https://developer.apple.com/documentation/uikit/uiswitch) — UIKit
- [NSButton.ButtonType.toggle](https://developer.apple.com/documentation/appkit/nsbutton/buttontype/toggle) — AppKit
- [NSSwitch](https://developer.apple.com/documentation/appkit/nsswitch) — AppKit

**Token fields** <sub>`pages/token-fields.md`</sub>
- [NSTokenField](https://developer.apple.com/documentation/appkit/nstokenfield) — AppKit

**Toolbars** <sub>`pages/toolbars.md`</sub>
- [Toolbars](https://developer.apple.com/documentation/swiftui/toolbars) — SwiftUI
- [UIToolbar](https://developer.apple.com/documentation/uikit/uitoolbar) — UIKit
- [NSToolbar](https://developer.apple.com/documentation/appkit/nstoolbar) — AppKit

**Typography** <sub>`pages/typography.md`</sub>
- [Text input and output](https://developer.apple.com/documentation/swiftui/text-input-and-output) — SwiftUI
- [Text display and fonts](https://developer.apple.com/documentation/uikit/text-display-and-fonts) — UIKit
- [Fonts](https://developer.apple.com/documentation/appkit/fonts) — AppKit

**Undo and redo** <sub>`pages/undo-and-redo.md`</sub>
- [UndoManager](https://developer.apple.com/documentation/foundation/undomanager) — Foundation

**Virtual keyboards** <sub>`pages/virtual-keyboards.md`</sub>
- [keyboardType(_:)](https://developer.apple.com/documentation/swiftui/view/keyboardtype(_:)) — SwiftUI
- [textContentType(_:)](https://developer.apple.com/documentation/swiftui/view/textcontenttype(_:)) — SwiftUI
- [UIKeyboardType](https://developer.apple.com/documentation/uikit/uikeyboardtype) — UIKit

**VoiceOver** <sub>`pages/voiceover.md`</sub>
- [Accessibility](https://developer.apple.com/documentation/accessibility) <sub>framework/guide</sub>
- [VoiceOver](https://developer.apple.com/documentation/accessibility/voiceover) <sub>framework/guide</sub>
- [Supporting VoiceOver in your app](https://developer.apple.com/documentation/uikit/supporting-voiceover-in-your-app) <sub>framework/guide</sub>

**Wallet** <sub>`pages/wallet.md`</sub>
- [FinanceKitUI](https://developer.apple.com/documentation/financekitui) <sub>framework/guide</sub>
- [FinanceKit](https://developer.apple.com/documentation/financekit) <sub>framework/guide</sub>
- [PassKit (Apple Pay and Wallet)](https://developer.apple.com/documentation/passkit) <sub>framework/guide</sub>
- [Wallet Passes](https://developer.apple.com/documentation/walletpasses) <sub>framework/guide</sub>
- [Wallet Orders](https://developer.apple.com/documentation/walletorders) <sub>framework/guide</sub>

**Watch faces** <sub>`pages/watch-faces.md`</sub>
- [Sharing an Apple Watch face](https://developer.apple.com/documentation/clockkit/sharing-an-apple-watch-face) — ClockKit

**Web views** <sub>`pages/web-views.md`</sub>
- [WKWebView](https://developer.apple.com/documentation/webkit/wkwebview) — WebKit

**Widgets** <sub>`pages/widgets.md`</sub>
- [WidgetKit](https://developer.apple.com/documentation/widgetkit) <sub>framework/guide</sub>
- [Developing a WidgetKit strategy](https://developer.apple.com/documentation/widgetkit/developing-a-widgetkit-strategy) — WidgetKit

**Windows** <sub>`pages/windows.md`</sub>
- [Windows](https://developer.apple.com/documentation/swiftui/windows) — SwiftUI
- [WindowGroup](https://developer.apple.com/documentation/swiftui/windowgroup) — SwiftUI
- [UIWindow](https://developer.apple.com/documentation/uikit/uiwindow) — UIKit
- [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) — AppKit

**Workouts** <sub>`pages/workouts.md`</sub>
- [WorkoutKit](https://developer.apple.com/documentation/workoutkit) <sub>framework/guide</sub>
- [Workouts and activity rings](https://developer.apple.com/documentation/healthkit/workouts-and-activity-rings) — HealthKit

**iCloud** <sub>`pages/icloud.md`</sub>
- [CloudKit](https://developer.apple.com/documentation/cloudkit) <sub>framework/guide</sub>
- [GameSave](https://developer.apple.com/documentation/gamesave) <sub>framework/guide</sub>

**iMessage apps and stickers** <sub>`pages/imessage-apps-and-stickers.md`</sub>
- [Messages](https://developer.apple.com/documentation/messages) <sub>framework/guide</sub>
- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](https://developer.apple.com/documentation/messages/adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime) — Messages

---

## By framework

Same data, grouped the other direction — everything the HIG cites for a given framework.

### AVFAudio
- [AVAudioSession](https://developer.apple.com/documentation/avfaudio/avaudiosession) — Playing audio (`pages/playing-audio.md`)

### AVFoundation
- [Enhancing your app experience with the Camera Control](https://developer.apple.com/documentation/avfoundation/enhancing-your-app-experience-with-the-camera-control) — Camera Control (`pages/camera-control.md`)
- [AVCaptureControl](https://developer.apple.com/documentation/avfoundation/avcapturecontrol) — Camera Control (`pages/camera-control.md`)
- [Configuring your app for media playback](https://developer.apple.com/documentation/avfoundation/configuring-your-app-for-media-playback) — Playing audio (`pages/playing-audio.md`)
- [Configuring your app for media playback](https://developer.apple.com/documentation/avfoundation/configuring-your-app-for-media-playback) — Playing video (`pages/playing-video.md`)

### App Intents
- [Getting started with the App Intents framework](https://developer.apple.com/documentation/appintents/getting-started-with-the-app-intents-framework) — App Shortcuts (`pages/app-shortcuts.md`)
- [Defining app entities for your custom data types](https://developer.apple.com/documentation/appintents/defining-app-entities-for-your-custom-data-types) — App Shortcuts (`pages/app-shortcuts.md`)

### AppKit
- [NSAlert](https://developer.apple.com/documentation/appkit/nsalert) — Alerts (`pages/alerts.md`)
- [NSBox](https://developer.apple.com/documentation/appkit/nsbox) — Boxes (`pages/boxes.md`)
- [NSButton](https://developer.apple.com/documentation/appkit/nsbutton) — Buttons (`pages/buttons.md`)
- [NSCollectionView](https://developer.apple.com/documentation/appkit/nscollectionview) — Collections (`pages/collections.md`)
- [NSColorWell](https://developer.apple.com/documentation/appkit/nscolorwell) — Color wells (`pages/color-wells.md`)
- [Color](https://developer.apple.com/documentation/appkit/color) — Color (`pages/color.md`)
- [NSBrowser](https://developer.apple.com/documentation/appkit/nsbrowser) — Column views (`pages/column-views.md`)
- [NSComboBox](https://developer.apple.com/documentation/appkit/nscombobox) — Combo boxes (`pages/combo-boxes.md`)
- [popUpContextMenu(_:with:for:)](https://developer.apple.com/documentation/appkit/nsmenu/popupcontextmenu(_:with:for:)) — Context menus (`pages/context-menus.md`)
- [NSButton.BezelStyle.disclosure](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/disclosure) — Disclosure controls (`pages/disclosure-controls.md`)
- [NSButton.BezelStyle.pushDisclosure](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/pushdisclosure) — Disclosure controls (`pages/disclosure-controls.md`)
- [applicationDockMenu(_:)](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationdockmenu(_:)) — Dock menus (`pages/dock-menus.md`)
- [Drag and Drop](https://developer.apple.com/documentation/appkit/drag-and-drop) — Drag and drop (`pages/drag-and-drop.md`)
- [NSMenu](https://developer.apple.com/documentation/appkit/nsmenu) — Edit menus (`pages/edit-menus.md`)
- [NSLevelIndicator](https://developer.apple.com/documentation/appkit/nslevelindicator) — Gauges (`pages/gauges.md`)
- [NSScreen](https://developer.apple.com/documentation/appkit/nsscreen) — Going full screen (`pages/going-full-screen.md`)
- [NSWindow.CollectionBehavior](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior-swift.struct) — Going full screen (`pages/going-full-screen.md`)
- [NSImageView](https://developer.apple.com/documentation/appkit/nsimageview) — Image views (`pages/image-views.md`)
- [NSImageView](https://developer.apple.com/documentation/appkit/nsimageview) — Image wells (`pages/image-wells.md`)
- [NSImageView](https://developer.apple.com/documentation/appkit/nsimageview) — Images (`pages/images.md`)
- [Mouse, Keyboard, and Trackpad](https://developer.apple.com/documentation/appkit/mouse-keyboard-and-trackpad) — Keyboards (`pages/keyboards.md`)
- [NSTextField](https://developer.apple.com/documentation/appkit/nstextfield) — Labels (`pages/labels.md`)
- [NSTableView](https://developer.apple.com/documentation/appkit/nstableview) — Lists and tables (`pages/lists-and-tables.md`)
- [NSVisualEffectView](https://developer.apple.com/documentation/appkit/nsvisualeffectview) — Materials (`pages/materials.md`)
- [Menus](https://developer.apple.com/documentation/appkit/menus) — Menus (`pages/menus.md`)
- [Modal Windows and Panels](https://developer.apple.com/documentation/appkit/modal-windows-and-panels) — Modality (`pages/modality.md`)
- [NSHelpManager](https://developer.apple.com/documentation/appkit/nshelpmanager) — Offering help (`pages/offering-help.md`)
- [NSOutlineView](https://developer.apple.com/documentation/appkit/nsoutlineview) — Outline views (`pages/outline-views.md`)
- [NSPanel](https://developer.apple.com/documentation/appkit/nspanel) — Panels (`pages/panels.md`)
- [hudWindow](https://developer.apple.com/documentation/appkit/nswindow/stylemask-swift.struct/hudwindow) — Panels (`pages/panels.md`)
- [NSPathControl](https://developer.apple.com/documentation/appkit/nspathcontrol) — Path controls (`pages/path-controls.md`)
- [NSDatePicker](https://developer.apple.com/documentation/appkit/nsdatepicker) — Pickers (`pages/pickers.md`)
- [Mouse, Keyboard, and Trackpad](https://developer.apple.com/documentation/appkit/mouse-keyboard-and-trackpad) — Pointing devices (`pages/pointing-devices.md`)
- [NSPopUpButton](https://developer.apple.com/documentation/appkit/nspopupbutton) — Pop-up buttons (`pages/pop-up-buttons.md`)
- [NSPopover](https://developer.apple.com/documentation/appkit/nspopover) — Popovers (`pages/popovers.md`)
- [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) — Printing (`pages/printing.md`)
- [NSProgressIndicator](https://developer.apple.com/documentation/appkit/nsprogressindicator) — Progress indicators (`pages/progress-indicators.md`)
- [pullsDown](https://developer.apple.com/documentation/appkit/nspopupbutton/pullsdown) — Pull-down buttons (`pages/pull-down-buttons.md`)
- [NSLevelIndicator.Style.rating](https://developer.apple.com/documentation/appkit/nslevelindicator/style/rating) — Rating indicators (`pages/rating-indicators.md`)
- [NSScrollView](https://developer.apple.com/documentation/appkit/nsscrollview) — Scroll views (`pages/scroll-views.md`)
- [NSSearchField](https://developer.apple.com/documentation/appkit/nssearchfield) — Search fields (`pages/search-fields.md`)
- [NSSegmentedControl](https://developer.apple.com/documentation/appkit/nssegmentedcontrol) — Segmented controls (`pages/segmented-controls.md`)
- [presentAsSheet(_:)](https://developer.apple.com/documentation/appkit/nsviewcontroller/presentassheet(_:)) — Sheets (`pages/sheets.md`)
- [NSSplitViewController](https://developer.apple.com/documentation/appkit/nssplitviewcontroller) — Sidebars (`pages/sidebars.md`)
- [NSSlider](https://developer.apple.com/documentation/appkit/nsslider) — Sliders (`pages/sliders.md`)
- [NSSplitViewController](https://developer.apple.com/documentation/appkit/nssplitviewcontroller) — Split views (`pages/split-views.md`)
- [NSStepper](https://developer.apple.com/documentation/appkit/nsstepper) — Steppers (`pages/steppers.md`)
- [NSTabView](https://developer.apple.com/documentation/appkit/nstabview) — Tab views (`pages/tab-views.md`)
- [NSTextField](https://developer.apple.com/documentation/appkit/nstextfield) — Text fields (`pages/text-fields.md`)
- [NSTextView](https://developer.apple.com/documentation/appkit/nstextview) — Text views (`pages/text-views.md`)
- [NSStatusBar](https://developer.apple.com/documentation/appkit/nsstatusbar) — The menu bar (`pages/the-menu-bar.md`)
- [NSButton.ButtonType.toggle](https://developer.apple.com/documentation/appkit/nsbutton/buttontype/toggle) — Toggles (`pages/toggles.md`)
- [NSSwitch](https://developer.apple.com/documentation/appkit/nsswitch) — Toggles (`pages/toggles.md`)
- [NSTokenField](https://developer.apple.com/documentation/appkit/nstokenfield) — Token fields (`pages/token-fields.md`)
- [NSToolbar](https://developer.apple.com/documentation/appkit/nstoolbar) — Toolbars (`pages/toolbars.md`)
- [Fonts](https://developer.apple.com/documentation/appkit/fonts) — Typography (`pages/typography.md`)
- [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) — Windows (`pages/windows.md`)

### Authentication Services
- [Supporting passkeys](https://developer.apple.com/documentation/authenticationservices/supporting-passkeys) — Managing accounts (`pages/managing-accounts.md`)

### ClockKit
- [Sharing an Apple Watch face](https://developer.apple.com/documentation/clockkit/sharing-an-apple-watch-face) — Watch faces (`pages/watch-faces.md`)

### Core Motion
- [Getting processed device-motion data](https://developer.apple.com/documentation/coremotion/getting-processed-device-motion-data) — Gyroscope and accelerometer (`pages/gyro-and-accelerometer.md`)

### Core Spotlight
- [Adding your app’s content to Spotlight indexes](https://developer.apple.com/documentation/corespotlight/adding-your-app-s-content-to-spotlight-indexes) — Searching (`pages/searching.md`)

### CoreLocation
- [Requesting authorization to use location services](https://developer.apple.com/documentation/corelocation/requesting-authorization-to-use-location-services) — Privacy (`pages/privacy.md`)

### Foundation
- [App Extension Support](https://developer.apple.com/documentation/foundation/app-extension-support) — Activity views (`pages/activity-views.md`)
- [UserDefaults](https://developer.apple.com/documentation/foundation/userdefaults) — Settings (`pages/settings.md`)
- [UndoManager](https://developer.apple.com/documentation/foundation/undomanager) — Undo and redo (`pages/undo-and-redo.md`)

### HealthKit
- [HKActivityRingView](https://developer.apple.com/documentation/healthkitui/hkactivityringview) — Activity rings (`pages/activity-rings.md`)
- [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy) — CareKit (`pages/carekit.md`)
- [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy) — HealthKit (`pages/healthkit.md`)
- [Protecting user privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy) — ResearchKit (`pages/researchkit.md`)
- [Workouts and activity rings](https://developer.apple.com/documentation/healthkit/workouts-and-activity-rings) — Workouts (`pages/workouts.md`)

### LivePhotosKit JS
- [LivePhotosKit JS](https://developer.apple.com/documentation/livephotoskitjs) — Live Photos (`pages/live-photos.md`)

### Messages
- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](https://developer.apple.com/documentation/messages/adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime) — iMessage apps and stickers (`pages/imessage-apps-and-stickers.md`)

### MusicKit
- [MusicKit](https://developer.apple.com/documentation/musickit) — Playing audio (`pages/playing-audio.md`)

### PassKit
- [Apple Pay](https://developer.apple.com/documentation/passkit/apple-pay) — Apple Pay (`pages/apple-pay.md`)

### PhotoKit
- [PHLivePhoto](https://developer.apple.com/documentation/photos/phlivephoto) — Live Photos (`pages/live-photos.md`)

### ProximityReader
- [Adopting the Verifier API in your iPhone app](https://developer.apple.com/documentation/proximityreader/adopting-the-verifier-api-in-your-iphone-app) — ID Verifier (`pages/id-verifier.md`)
- [Adding support for Tap to Pay on iPhone to your app](https://developer.apple.com/documentation/proximityreader/adding-support-for-tap-to-pay-on-iphone-to-your-app) — Tap to Pay on iPhone (`pages/tap-to-pay-on-iphone.md`)

### Sign in with Apple
- [Displaying Sign in with Apple buttons on the web](https://developer.apple.com/documentation/signinwithapple/displaying-sign-in-with-apple-buttons-on-the-web) — Sign in with Apple (`pages/sign-in-with-apple.md`)

### StoreKit
- [In-App Purchase](https://developer.apple.com/documentation/storekit/in-app-purchase) — In-app purchase (`pages/in-app-purchase.md`)
- [RequestReviewAction](https://developer.apple.com/documentation/storekit/requestreviewaction) — Ratings and reviews (`pages/ratings-and-reviews.md`)

### Swift, Objective-C
- [Managing your game window for Metal in macOS](https://developer.apple.com/documentation/metal/managing-your-game-window-for-metal-in-macos) — Going full screen (`pages/going-full-screen.md`)

### SwiftUI
- [confirmationDialog(_:isPresented:titleVisibility:actions:)](https://developer.apple.com/documentation/swiftui/view/confirmationdialog(_:ispresented:titlevisibility:actions:)-46zbb) — Action sheets (`pages/action-sheets.md`)
- [alert(_:isPresented:actions:)](https://developer.apple.com/documentation/swiftui/view/alert(_:ispresented:actions:)-1bkka) — Alerts (`pages/alerts.md`)
- [GroupBox](https://developer.apple.com/documentation/swiftui/groupbox) — Boxes (`pages/boxes.md`)
- [Button](https://developer.apple.com/documentation/swiftui/button) — Buttons (`pages/buttons.md`)
- [ShareLink](https://developer.apple.com/documentation/swiftui/sharelink) — Collaboration and sharing (`pages/collaboration-and-sharing.md`)
- [Color](https://developer.apple.com/documentation/swiftui/color) — Color (`pages/color.md`)
- [contextMenu(menuItems:)](https://developer.apple.com/documentation/swiftui/view/contextmenu(menuitems:)) — Context menus (`pages/context-menus.md`)
- [DisclosureGroup](https://developer.apple.com/documentation/swiftui/disclosuregroup) — Disclosure controls (`pages/disclosure-controls.md`)
- [Input events](https://developer.apple.com/documentation/swiftui/input-events) — Entering data (`pages/entering-data.md`)
- [Documents](https://developer.apple.com/documentation/swiftui/documents) — File management (`pages/file-management.md`)
- [Gauge](https://developer.apple.com/documentation/swiftui/gauge) — Gauges (`pages/gauges.md`)
- [Gestures](https://developer.apple.com/documentation/swiftui/gestures) — Gestures (`pages/gestures.md`)
- [fullScreenCover(item:onDismiss:content:)](https://developer.apple.com/documentation/swiftui/view/fullscreencover(item:ondismiss:content:)) — Going full screen (`pages/going-full-screen.md`)
- [Image](https://developer.apple.com/documentation/swiftui/image) — Image views (`pages/image-views.md`)
- [Images](https://developer.apple.com/documentation/swiftui/images) — Images (`pages/images.md`)
- [Immersive spaces](https://developer.apple.com/documentation/swiftui/immersive-spaces) — Immersive experiences (`pages/immersive-experiences.md`)
- [KeyboardShortcut](https://developer.apple.com/documentation/swiftui/keyboardshortcut) — Keyboards (`pages/keyboards.md`)
- [Input events](https://developer.apple.com/documentation/swiftui/input-events) — Keyboards (`pages/keyboards.md`)
- [Label](https://developer.apple.com/documentation/swiftui/label) — Labels (`pages/labels.md`)
- [Text](https://developer.apple.com/documentation/swiftui/text) — Labels (`pages/labels.md`)
- [Composing custom layouts with SwiftUI](https://developer.apple.com/documentation/swiftui/composing-custom-layouts-with-swiftui) — Layout (`pages/layout.md`)
- [List](https://developer.apple.com/documentation/swiftui/list) — Lists and tables (`pages/lists-and-tables.md`)
- [Tables](https://developer.apple.com/documentation/swiftui/tables) — Lists and tables (`pages/lists-and-tables.md`)
- [glassEffect(_:in:)](https://developer.apple.com/documentation/swiftui/view/glasseffect(_:in:)) — Materials (`pages/materials.md`)
- [Material](https://developer.apple.com/documentation/swiftui/material) — Materials (`pages/materials.md`)
- [Menu](https://developer.apple.com/documentation/swiftui/menu) — Menus (`pages/menus.md`)
- [Presentation modifiers](https://developer.apple.com/documentation/swiftui/view-presentation) — Modality (`pages/modality.md`)
- [Animating views and transitions](https://developer.apple.com/tutorials/swiftui/animating-views-and-transitions) — Motion (`pages/motion.md`)
- [ornament(visibility:attachmentAnchor:contentAlignment:ornament:)](https://developer.apple.com/documentation/swiftui/view/ornament(visibility:attachmentanchor:contentalignment:ornament:)) — Ornaments (`pages/ornaments.md`)
- [OutlineGroup](https://developer.apple.com/documentation/swiftui/outlinegroup) — Outline views (`pages/outline-views.md`)
- [PageTabViewStyle](https://developer.apple.com/documentation/swiftui/pagetabviewstyle) — Page controls (`pages/page-controls.md`)
- [Picker](https://developer.apple.com/documentation/swiftui/picker) — Pickers (`pages/pickers.md`)
- [Input events](https://developer.apple.com/documentation/swiftui/input-events) — Pointing devices (`pages/pointing-devices.md`)
- [MenuPickerStyle](https://developer.apple.com/documentation/swiftui/menupickerstyle) — Pop-up buttons (`pages/pop-up-buttons.md`)
- [popover(isPresented:attachmentAnchor:arrowEdge:content:)](https://developer.apple.com/documentation/swiftui/view/popover(ispresented:attachmentanchor:arrowedge:content:)) — Popovers (`pages/popovers.md`)
- [ProgressView](https://developer.apple.com/documentation/swiftui/progressview) — Progress indicators (`pages/progress-indicators.md`)
- [MenuPickerStyle](https://developer.apple.com/documentation/swiftui/menupickerstyle) — Pull-down buttons (`pages/pull-down-buttons.md`)
- [Preparing views for localization](https://developer.apple.com/documentation/swiftui/preparing-views-for-localization) — Right to left (`pages/right-to-left.md`)
- [ScrollView](https://developer.apple.com/documentation/swiftui/scrollview) — Scroll views (`pages/scroll-views.md`)
- [look](https://developer.apple.com/documentation/swiftui/scrollinputkind/look) — Scroll views (`pages/scroll-views.md`)
- [Adding a search interface to your app](https://developer.apple.com/documentation/swiftui/adding-a-search-interface-to-your-app) — Search fields (`pages/search-fields.md`)
- [searchable(text:placement:prompt:)](https://developer.apple.com/documentation/swiftui/view/searchable(text:placement:prompt:)) — Search fields (`pages/search-fields.md`)
- [segmented](https://developer.apple.com/documentation/swiftui/pickerstyle/segmented) — Segmented controls (`pages/segmented-controls.md`)
- [Settings](https://developer.apple.com/documentation/swiftui/settings) — Settings (`pages/settings.md`)
- [sheet(item:onDismiss:content:)](https://developer.apple.com/documentation/swiftui/view/sheet(item:ondismiss:content:)) — Sheets (`pages/sheets.md`)
- [sidebarAdaptable](https://developer.apple.com/documentation/swiftui/tabviewstyle/sidebaradaptable) — Sidebars (`pages/sidebars.md`)
- [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview) — Sidebars (`pages/sidebars.md`)
- [sidebar](https://developer.apple.com/documentation/swiftui/liststyle/sidebar) — Sidebars (`pages/sidebars.md`)
- [Slider](https://developer.apple.com/documentation/swiftui/slider) — Sliders (`pages/sliders.md`)
- [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview) — Split views (`pages/split-views.md`)
- [TabView](https://developer.apple.com/documentation/swiftui/tabview) — Tab bars (`pages/tab-bars.md`)
- [TabViewBottomAccessoryPlacement](https://developer.apple.com/documentation/swiftui/tabviewbottomaccessoryplacement) — Tab bars (`pages/tab-bars.md`)
- [Enhancing your app’s content with tab navigation](https://developer.apple.com/documentation/swiftui/enhancing-your-app-content-with-tab-navigation) — Tab bars (`pages/tab-bars.md`)
- [TabView](https://developer.apple.com/documentation/swiftui/tabview) — Tab views (`pages/tab-views.md`)
- [TextField](https://developer.apple.com/documentation/swiftui/textfield) — Text fields (`pages/text-fields.md`)
- [SecureField](https://developer.apple.com/documentation/swiftui/securefield) — Text fields (`pages/text-fields.md`)
- [Text](https://developer.apple.com/documentation/swiftui/text) — Text views (`pages/text-views.md`)
- [CommandMenu](https://developer.apple.com/documentation/swiftui/commandmenu) — The menu bar (`pages/the-menu-bar.md`)
- [Toggle](https://developer.apple.com/documentation/swiftui/toggle) — Toggles (`pages/toggles.md`)
- [Toolbars](https://developer.apple.com/documentation/swiftui/toolbars) — Toolbars (`pages/toolbars.md`)
- [Text input and output](https://developer.apple.com/documentation/swiftui/text-input-and-output) — Typography (`pages/typography.md`)
- [keyboardType(_:)](https://developer.apple.com/documentation/swiftui/view/keyboardtype(_:)) — Virtual keyboards (`pages/virtual-keyboards.md`)
- [textContentType(_:)](https://developer.apple.com/documentation/swiftui/view/textcontenttype(_:)) — Virtual keyboards (`pages/virtual-keyboards.md`)
- [Windows](https://developer.apple.com/documentation/swiftui/windows) — Windows (`pages/windows.md`)
- [WindowGroup](https://developer.apple.com/documentation/swiftui/windowgroup) — Windows (`pages/windows.md`)

### Symbols framework
- [Symbols](https://developer.apple.com/documentation/symbols) — SF Symbols (`pages/sf-symbols.md`)

### TVML
- [Focus Attributes](https://developer.apple.com/documentation/tvml/focus-attributes) — Focus and selection (`pages/focus-and-selection.md`)

### TVUIKit
- [TVDigitEntryViewController](https://developer.apple.com/documentation/tvuikit/tvdigitentryviewcontroller) — Digit entry views (`pages/digit-entry-views.md`)
- [TVLockupView](https://developer.apple.com/documentation/tvuikit/tvlockupview) — Lockups (`pages/lockups.md`)
- [TVLockupHeaderFooterView](https://developer.apple.com/documentation/tvuikit/tvlockupheaderfooterview) — Lockups (`pages/lockups.md`)

### UIKit
- [UIAlertController.Style.actionSheet](https://developer.apple.com/documentation/uikit/uialertcontroller/style/actionsheet) — Action sheets (`pages/action-sheets.md`)
- [UIActivityViewController](https://developer.apple.com/documentation/uikit/uiactivityviewcontroller) — Activity views (`pages/activity-views.md`)
- [UIActivity](https://developer.apple.com/documentation/uikit/uiactivity) — Activity views (`pages/activity-views.md`)
- [UIAlertController](https://developer.apple.com/documentation/uikit/uialertcontroller) — Alerts (`pages/alerts.md`)
- [UIButton](https://developer.apple.com/documentation/uikit/uibutton) — Buttons (`pages/buttons.md`)
- [UICollectionView](https://developer.apple.com/documentation/uikit/uicollectionview) — Collections (`pages/collections.md`)
- [UIColorWell](https://developer.apple.com/documentation/uikit/uicolorwell) — Color wells (`pages/color-wells.md`)
- [UIColorPickerViewController](https://developer.apple.com/documentation/uikit/uicolorpickerviewcontroller) — Color wells (`pages/color-wells.md`)
- [UIColor](https://developer.apple.com/documentation/uikit/uicolor) — Color (`pages/color.md`)
- [UIContextMenuInteraction](https://developer.apple.com/documentation/uikit/uicontextmenuinteraction) — Context menus (`pages/context-menus.md`)
- [Drag and drop](https://developer.apple.com/documentation/uikit/drag-and-drop) — Drag and drop (`pages/drag-and-drop.md`)
- [UIEditMenuInteraction](https://developer.apple.com/documentation/uikit/uieditmenuinteraction) — Edit menus (`pages/edit-menus.md`)
- [Animation and haptics](https://developer.apple.com/documentation/uikit/animation-and-haptics) — Feedback (`pages/feedback.md`)
- [Focus-based navigation](https://developer.apple.com/documentation/uikit/focus-based-navigation) — Focus and selection (`pages/focus-and-selection.md`)
- [About focus interactions for Apple TV](https://developer.apple.com/documentation/uikit/about-focus-interactions-for-apple-tv) — Focus and selection (`pages/focus-and-selection.md`)
- [UITouch](https://developer.apple.com/documentation/uikit/uitouch) — Gestures (`pages/gestures.md`)
- [Add Home Screen quick actions](https://developer.apple.com/documentation/uikit/add-home-screen-quick-actions) — Home Screen quick actions (`pages/home-screen-quick-actions.md`)
- [UIImageView](https://developer.apple.com/documentation/uikit/uiimageview) — Image views (`pages/image-views.md`)
- [UIImageView](https://developer.apple.com/documentation/uikit/uiimageview) — Images (`pages/images.md`)
- [Handling key presses made on a physical keyboard](https://developer.apple.com/documentation/uikit/handling-key-presses-made-on-a-physical-keyboard) — Keyboards (`pages/keyboards.md`)
- [UILabel](https://developer.apple.com/documentation/uikit/uilabel) — Labels (`pages/labels.md`)
- [Responding to the launch of your app](https://developer.apple.com/documentation/uikit/responding-to-the-launch-of-your-app) — Launching (`pages/launching.md`)
- [UITableView](https://developer.apple.com/documentation/uikit/uitableview) — Lists and tables (`pages/lists-and-tables.md`)
- [Mac Catalyst](https://developer.apple.com/documentation/uikit/mac-catalyst) — Mac Catalyst (`pages/mac-catalyst.md`)
- [UIVisualEffectView](https://developer.apple.com/documentation/uikit/uivisualeffectview) — Materials (`pages/materials.md`)
- [Menus and shortcuts](https://developer.apple.com/documentation/uikit/menus-and-shortcuts) — Menus (`pages/menus.md`)
- [UIModalPresentationStyle](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle) — Modality (`pages/modality.md`)
- [Responding to the launch of your app](https://developer.apple.com/documentation/uikit/responding-to-the-launch-of-your-app) — Multitasking (`pages/multitasking.md`)
- [Multitasking on iPad, Mac, and Apple Vision Pro](https://developer.apple.com/documentation/uikit/multitasking-on-ipad-mac-and-apple-vision-pro) — Multitasking (`pages/multitasking.md`)
- [UIPageControl](https://developer.apple.com/documentation/uikit/uipagecontrol) — Page controls (`pages/page-controls.md`)
- [UIDatePicker](https://developer.apple.com/documentation/uikit/uidatepicker) — Pickers (`pages/pickers.md`)
- [UIPickerView](https://developer.apple.com/documentation/uikit/uipickerview) — Pickers (`pages/pickers.md`)
- [Pointer interactions](https://developer.apple.com/documentation/uikit/pointer-interactions) — Pointing devices (`pages/pointing-devices.md`)
- [changesSelectionAsPrimaryAction](https://developer.apple.com/documentation/uikit/uibutton/changesselectionasprimaryaction) — Pop-up buttons (`pages/pop-up-buttons.md`)
- [UIPopoverPresentationController](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller) — Popovers (`pages/popovers.md`)
- [UIPrintInteractionController](https://developer.apple.com/documentation/uikit/uiprintinteractioncontroller) — Printing (`pages/printing.md`)
- [Requesting access to protected resources](https://developer.apple.com/documentation/uikit/requesting-access-to-protected-resources) — Privacy (`pages/privacy.md`)
- [UIProgressView](https://developer.apple.com/documentation/uikit/uiprogressview) — Progress indicators (`pages/progress-indicators.md`)
- [UIActivityIndicatorView](https://developer.apple.com/documentation/uikit/uiactivityindicatorview) — Progress indicators (`pages/progress-indicators.md`)
- [UIRefreshControl](https://developer.apple.com/documentation/uikit/uirefreshcontrol) — Progress indicators (`pages/progress-indicators.md`)
- [showsMenuAsPrimaryAction](https://developer.apple.com/documentation/uikit/uicontrol/showsmenuasprimaryaction) — Pull-down buttons (`pages/pull-down-buttons.md`)
- [UIScrollView](https://developer.apple.com/documentation/uikit/uiscrollview) — Scroll views (`pages/scroll-views.md`)
- [UISearchBar](https://developer.apple.com/documentation/uikit/uisearchbar) — Search fields (`pages/search-fields.md`)
- [UISearchTextField](https://developer.apple.com/documentation/uikit/uisearchtextfield) — Search fields (`pages/search-fields.md`)
- [UISegmentedControl](https://developer.apple.com/documentation/uikit/uisegmentedcontrol) — Segmented controls (`pages/segmented-controls.md`)
- [Configuring and displaying symbol images in your UI](https://developer.apple.com/documentation/uikit/configuring-and-displaying-symbol-images-in-your-ui) — SF Symbols (`pages/sf-symbols.md`)
- [Creating custom symbol images for your app](https://developer.apple.com/documentation/uikit/creating-custom-symbol-images-for-your-app) — SF Symbols (`pages/sf-symbols.md`)
- [UISheetPresentationController](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller) — Sheets (`pages/sheets.md`)
- [UICollectionLayoutListConfiguration](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct) — Sidebars (`pages/sidebars.md`)
- [UISlider](https://developer.apple.com/documentation/uikit/uislider) — Sliders (`pages/sliders.md`)
- [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller) — Split views (`pages/split-views.md`)
- [UIStatusBarStyle](https://developer.apple.com/documentation/uikit/uistatusbarstyle) — Status bars (`pages/status-bars.md`)
- [preferredStatusBarStyle](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredstatusbarstyle) — Status bars (`pages/status-bars.md`)
- [UIStepper](https://developer.apple.com/documentation/uikit/uistepper) — Steppers (`pages/steppers.md`)
- [UITabBar](https://developer.apple.com/documentation/uikit/uitabbar) — Tab bars (`pages/tab-bars.md`)
- [Elevating your iPad app with a tab bar and sidebar](https://developer.apple.com/documentation/uikit/elevating-your-ipad-app-with-a-tab-bar-and-sidebar) — Tab bars (`pages/tab-bars.md`)
- [UITextField](https://developer.apple.com/documentation/uikit/uitextfield) — Text fields (`pages/text-fields.md`)
- [UITextView](https://developer.apple.com/documentation/uikit/uitextview) — Text views (`pages/text-views.md`)
- [Adding menus and shortcuts to the menu bar and user interface](https://developer.apple.com/documentation/uikit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface) — The menu bar (`pages/the-menu-bar.md`)
- [UISwitch](https://developer.apple.com/documentation/uikit/uiswitch) — Toggles (`pages/toggles.md`)
- [UIToolbar](https://developer.apple.com/documentation/uikit/uitoolbar) — Toolbars (`pages/toolbars.md`)
- [Text display and fonts](https://developer.apple.com/documentation/uikit/text-display-and-fonts) — Typography (`pages/typography.md`)
- [UIKeyboardType](https://developer.apple.com/documentation/uikit/uikeyboardtype) — Virtual keyboards (`pages/virtual-keyboards.md`)
- [UIWindow](https://developer.apple.com/documentation/uikit/uiwindow) — Windows (`pages/windows.md`)

### User Notifications
- [Asking permission to use notifications](https://developer.apple.com/documentation/usernotifications/asking-permission-to-use-notifications) — Notifications (`pages/notifications.md`)

### WatchKit
- [WKInterfacePaymentButton](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton) — Apple Pay (`pages/apple-pay.md`)
- [WKCrownDelegate](https://developer.apple.com/documentation/watchkit/wkcrowndelegate) — Digital Crown (`pages/digital-crown.md`)
- [WKPageOrientation](https://developer.apple.com/documentation/watchkit/wkpageorientation) — Scroll views (`pages/scroll-views.md`)

### WebKit
- [WKWebView](https://developer.apple.com/documentation/webkit/wkwebview) — Web views (`pages/web-views.md`)

### WidgetKit
- [Developing a WidgetKit strategy](https://developer.apple.com/documentation/widgetkit/developing-a-widgetkit-strategy) — Live Activities (`pages/live-activities.md`)
- [Developing a WidgetKit strategy](https://developer.apple.com/documentation/widgetkit/developing-a-widgetkit-strategy) — Widgets (`pages/widgets.md`)

### Xcode
- [Localization](https://developer.apple.com/documentation/xcode/localization) — Inclusion (`pages/inclusion.md`)
- [Specifying your app’s launch screen](https://developer.apple.com/documentation/xcode/specifying-your-apps-launch-screen) — Launching (`pages/launching.md`)

### visionOS
- [Adopting best practices for privacy and user preferences](https://developer.apple.com/documentation/visionos/adopting-best-practices-for-privacy) — Eyes (`pages/eyes.md`)
- [Drawing sharp layer-based content in visionOS](https://developer.apple.com/documentation/visionos/drawing-sharp-layer-based-content) — Images (`pages/images.md`)
- [Creating fully immersive experiences in your app](https://developer.apple.com/documentation/visionos/creating-fully-immersive-experiences) — Immersive experiences (`pages/immersive-experiences.md`)
- [Incorporating real-world surroundings in an immersive experience](https://developer.apple.com/documentation/visionos/incorporating-real-world-surroundings-in-an-immersive-experience) — Immersive experiences (`pages/immersive-experiences.md`)
- [ImmersionStyle](https://developer.apple.com/documentation/swiftui/immersionstyle) — Immersive experiences (`pages/immersive-experiences.md`)
- [Presenting windows and spaces](https://developer.apple.com/documentation/visionos/presenting-windows-and-spaces) — Spatial layout (`pages/spatial-layout.md`)
- [Positioning and sizing windows](https://developer.apple.com/documentation/visionos/positioning-and-sizing-windows) — Spatial layout (`pages/spatial-layout.md`)
- [Adding 3D content to your app](https://developer.apple.com/documentation/visionos/adding-3d-content-to-your-app) — Spatial layout (`pages/spatial-layout.md`)

### watchOS apps
- [Designing your app for the Always On state](https://developer.apple.com/documentation/watchos-apps/designing-your-app-for-the-always-on-state) — Always On (`pages/always-on.md`)
