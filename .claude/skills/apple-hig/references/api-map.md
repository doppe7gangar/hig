# API map: guidance to implementation

240 symbol references pulled from every page's 'Developer documentation' section — the exact SwiftUI, UIKit, AppKit, and framework-specific API that implements each piece of guidance.

Use this to go from a design decision straight to the right API instead of guessing at a class or modifier name. When reviewing code, check the symbol used against what the HIG actually names here — a hand-rolled view where a system API exists is itself worth flagging.

---

## By component

**Action sheets** <sub>`pages/action-sheets.md`</sub>
- [confirmationDialog(_:isPresented:titleVisibility:actions:)](https://developer.apple.com/documentation/SwiftUI/View/confirmationDialog(_:isPresented:titleVisibility:actions:)-46zbb) — SwiftUI
- [UIAlertController.Style.actionSheet](https://developer.apple.com/documentation/UIKit/UIAlertController/Style/actionSheet) — UIKit

**Activity rings** <sub>`pages/activity-rings.md`</sub>
- [HKActivityRingView](https://developer.apple.com/documentation/HealthKitUI/HKActivityRingView) — HealthKit

**Activity views** <sub>`pages/activity-views.md`</sub>
- [UIActivityViewController](https://developer.apple.com/documentation/UIKit/UIActivityViewController) — UIKit
- [UIActivity](https://developer.apple.com/documentation/UIKit/UIActivity) — UIKit
- [App Extension Support](https://developer.apple.com/documentation/Foundation/app-extension-support) — Foundation

**Alerts** <sub>`pages/alerts.md`</sub>
- [alert(_:isPresented:actions:)](https://developer.apple.com/documentation/SwiftUI/View/alert(_:isPresented:actions:)-1bkka) — SwiftUI
- [UIAlertController](https://developer.apple.com/documentation/UIKit/UIAlertController) — UIKit
- [NSAlert](https://developer.apple.com/documentation/AppKit/NSAlert) — AppKit

**Always On** <sub>`pages/always-on.md`</sub>
- [Designing your app for the Always On state](https://developer.apple.com/documentation/watchOS-Apps/designing-your-app-for-the-always-on-state) — watchOS apps

**App Shortcuts** <sub>`pages/app-shortcuts.md`</sub>
- [Getting started with the App Intents framework](https://developer.apple.com/documentation/AppIntents/getting-started-with-the-app-intents-framework) — App Intents
- [Defining app entities for your custom data types](https://developer.apple.com/documentation/AppIntents/defining-app-entities-for-your-custom-data-types) — App Intents

**Apple Pay** <sub>`pages/apple-pay.md`</sub>
- [Apple Pay](https://developer.apple.com/documentation/PassKit/apple-pay) — PassKit
- [WKInterfacePaymentButton](https://developer.apple.com/documentation/WatchKit/WKInterfacePaymentButton) — WatchKit

**Boxes** <sub>`pages/boxes.md`</sub>
- [GroupBox](https://developer.apple.com/documentation/SwiftUI/GroupBox) — SwiftUI
- [NSBox](https://developer.apple.com/documentation/AppKit/NSBox) — AppKit

**Buttons** <sub>`pages/buttons.md`</sub>
- [Button](https://developer.apple.com/documentation/SwiftUI/Button) — SwiftUI
- [UIButton](https://developer.apple.com/documentation/UIKit/UIButton) — UIKit
- [NSButton](https://developer.apple.com/documentation/AppKit/NSButton) — AppKit

**Camera Control** <sub>`pages/camera-control.md`</sub>
- [Enhancing your app experience with the Camera Control](https://developer.apple.com/documentation/AVFoundation/enhancing-your-app-experience-with-the-camera-control) — AVFoundation
- [AVCaptureControl](https://developer.apple.com/documentation/AVFoundation/AVCaptureControl) — AVFoundation

**CareKit** <sub>`pages/carekit.md`</sub>
- [Protecting user privacy](https://developer.apple.com/documentation/HealthKit/protecting-user-privacy) — HealthKit

**Collaboration and sharing** <sub>`pages/collaboration-and-sharing.md`</sub>
- [ShareLink](https://developer.apple.com/documentation/SwiftUI/ShareLink) — SwiftUI

**Collections** <sub>`pages/collections.md`</sub>
- [UICollectionView](https://developer.apple.com/documentation/UIKit/UICollectionView) — UIKit
- [NSCollectionView](https://developer.apple.com/documentation/AppKit/NSCollectionView) — AppKit

**Color** <sub>`pages/color.md`</sub>
- [Color](https://developer.apple.com/documentation/SwiftUI/Color) — SwiftUI
- [UIColor](https://developer.apple.com/documentation/UIKit/UIColor) — UIKit
- [Color](https://developer.apple.com/documentation/AppKit/color) — AppKit

**Color wells** <sub>`pages/color-wells.md`</sub>
- [UIColorWell](https://developer.apple.com/documentation/UIKit/UIColorWell) — UIKit
- [UIColorPickerViewController](https://developer.apple.com/documentation/UIKit/UIColorPickerViewController) — UIKit
- [NSColorWell](https://developer.apple.com/documentation/AppKit/NSColorWell) — AppKit

**Column views** <sub>`pages/column-views.md`</sub>
- [NSBrowser](https://developer.apple.com/documentation/AppKit/NSBrowser) — AppKit

**Combo boxes** <sub>`pages/combo-boxes.md`</sub>
- [NSComboBox](https://developer.apple.com/documentation/AppKit/NSComboBox) — AppKit

**Context menus** <sub>`pages/context-menus.md`</sub>
- [contextMenu(menuItems:)](https://developer.apple.com/documentation/SwiftUI/View/contextMenu(menuItems:)) — SwiftUI
- [UIContextMenuInteraction](https://developer.apple.com/documentation/UIKit/UIContextMenuInteraction) — UIKit
- [popUpContextMenu(_:with:for:)](https://developer.apple.com/documentation/AppKit/NSMenu/popUpContextMenu(_:with:for:)) — AppKit

**Digit entry views** <sub>`pages/digit-entry-views.md`</sub>
- [TVDigitEntryViewController](https://developer.apple.com/documentation/TVUIKit/TVDigitEntryViewController) — TVUIKit

**Digital Crown** <sub>`pages/digital-crown.md`</sub>
- [WKCrownDelegate](https://developer.apple.com/documentation/WatchKit/WKCrownDelegate) — WatchKit

**Disclosure controls** <sub>`pages/disclosure-controls.md`</sub>
- [DisclosureGroup](https://developer.apple.com/documentation/SwiftUI/DisclosureGroup) — SwiftUI
- [NSButton.BezelStyle.disclosure](https://developer.apple.com/documentation/AppKit/NSButton/BezelStyle-swift.enum/disclosure) — AppKit
- [NSButton.BezelStyle.pushDisclosure](https://developer.apple.com/documentation/AppKit/NSButton/BezelStyle-swift.enum/pushDisclosure) — AppKit

**Dock menus** <sub>`pages/dock-menus.md`</sub>
- [applicationDockMenu(_:)](https://developer.apple.com/documentation/AppKit/NSApplicationDelegate/applicationDockMenu(_:)) — AppKit

**Drag and drop** <sub>`pages/drag-and-drop.md`</sub>
- [Drag and drop](https://developer.apple.com/documentation/UIKit/drag-and-drop) — UIKit
- [Drag and Drop](https://developer.apple.com/documentation/AppKit/drag-and-drop) — AppKit

**Edit menus** <sub>`pages/edit-menus.md`</sub>
- [UIEditMenuInteraction](https://developer.apple.com/documentation/UIKit/UIEditMenuInteraction) — UIKit
- [NSMenu](https://developer.apple.com/documentation/AppKit/NSMenu) — AppKit

**Entering data** <sub>`pages/entering-data.md`</sub>
- [Input events](https://developer.apple.com/documentation/SwiftUI/Input-events) — SwiftUI

**Eyes** <sub>`pages/eyes.md`</sub>
- [Adopting best practices for privacy and user preferences](https://developer.apple.com/documentation/visionOS/adopting-best-practices-for-privacy) — visionOS

**Feedback** <sub>`pages/feedback.md`</sub>
- [Animation and haptics](https://developer.apple.com/documentation/UIKit/animation-and-haptics) — UIKit

**File management** <sub>`pages/file-management.md`</sub>
- [Documents](https://developer.apple.com/documentation/SwiftUI/Documents) — SwiftUI

**Focus and selection** <sub>`pages/focus-and-selection.md`</sub>
- [Focus Attributes](https://developer.apple.com/documentation/TVML/focus-attributes) — TVML
- [Focus-based navigation](https://developer.apple.com/documentation/UIKit/focus-based-navigation) — UIKit
- [About focus interactions for Apple TV](https://developer.apple.com/documentation/UIKit/about-focus-interactions-for-apple-tv) — UIKit

**Gauges** <sub>`pages/gauges.md`</sub>
- [Gauge](https://developer.apple.com/documentation/SwiftUI/Gauge) — SwiftUI
- [NSLevelIndicator](https://developer.apple.com/documentation/AppKit/NSLevelIndicator) — AppKit

**Gestures** <sub>`pages/gestures.md`</sub>
- [Gestures](https://developer.apple.com/documentation/SwiftUI/Gestures) — SwiftUI
- [UITouch](https://developer.apple.com/documentation/UIKit/UITouch) — UIKit

**Going full screen** <sub>`pages/going-full-screen.md`</sub>
- [fullScreenCover(item:onDismiss:content:)](https://developer.apple.com/documentation/SwiftUI/View/fullScreenCover(item:onDismiss:content:)) — SwiftUI
- [NSScreen](https://developer.apple.com/documentation/AppKit/NSScreen) — AppKit
- [NSWindow.CollectionBehavior](https://developer.apple.com/documentation/AppKit/NSWindow/CollectionBehavior-swift.struct) — AppKit
- [Managing your game window for Metal in macOS](https://developer.apple.com/documentation/Metal/managing-your-game-window-for-metal-in-macos) — Swift, Objective-C

**Gyroscope and accelerometer** <sub>`pages/gyro-and-accelerometer.md`</sub>
- [Getting processed device-motion data](https://developer.apple.com/documentation/CoreMotion/getting-processed-device-motion-data) — Core Motion

**HealthKit** <sub>`pages/healthkit.md`</sub>
- [Protecting user privacy](https://developer.apple.com/documentation/HealthKit/protecting-user-privacy) — HealthKit

**Home Screen quick actions** <sub>`pages/home-screen-quick-actions.md`</sub>
- [Add Home Screen quick actions](https://developer.apple.com/documentation/UIKit/add-home-screen-quick-actions) — UIKit

**ID Verifier** <sub>`pages/id-verifier.md`</sub>
- [Adopting the Verifier API in your iPhone app](https://developer.apple.com/documentation/ProximityReader/adopting-the-verifier-api-in-your-iphone-app) — ProximityReader

**Image views** <sub>`pages/image-views.md`</sub>
- [Image](https://developer.apple.com/documentation/SwiftUI/Image) — SwiftUI
- [UIImageView](https://developer.apple.com/documentation/UIKit/UIImageView) — UIKit
- [NSImageView](https://developer.apple.com/documentation/AppKit/NSImageView) — AppKit

**Image wells** <sub>`pages/image-wells.md`</sub>
- [NSImageView](https://developer.apple.com/documentation/AppKit/NSImageView) — AppKit

**Images** <sub>`pages/images.md`</sub>
- [Drawing sharp layer-based content in visionOS](https://developer.apple.com/documentation/visionOS/drawing-sharp-layer-based-content) — visionOS
- [Images](https://developer.apple.com/documentation/SwiftUI/Images) — SwiftUI
- [UIImageView](https://developer.apple.com/documentation/UIKit/UIImageView) — UIKit
- [NSImageView](https://developer.apple.com/documentation/AppKit/NSImageView) — AppKit

**Immersive experiences** <sub>`pages/immersive-experiences.md`</sub>
- [Creating fully immersive experiences in your app](https://developer.apple.com/documentation/visionOS/creating-fully-immersive-experiences) — visionOS
- [Incorporating real-world surroundings in an immersive experience](https://developer.apple.com/documentation/visionOS/incorporating-real-world-surroundings-in-an-immersive-experience) — visionOS
- [ImmersionStyle](https://developer.apple.com/documentation/SwiftUI/ImmersionStyle) — visionOS
- [Immersive spaces](https://developer.apple.com/documentation/SwiftUI/Immersive-spaces) — SwiftUI

**In-app purchase** <sub>`pages/in-app-purchase.md`</sub>
- [In-App Purchase](https://developer.apple.com/documentation/StoreKit/in-app-purchase) — StoreKit

**Inclusion** <sub>`pages/inclusion.md`</sub>
- [Localization](https://developer.apple.com/documentation/Xcode/localization) — Xcode

**Keyboards** <sub>`pages/keyboards.md`</sub>
- [KeyboardShortcut](https://developer.apple.com/documentation/SwiftUI/KeyboardShortcut) — SwiftUI
- [Input events](https://developer.apple.com/documentation/SwiftUI/Input-events) — SwiftUI
- [Handling key presses made on a physical keyboard](https://developer.apple.com/documentation/UIKit/handling-key-presses-made-on-a-physical-keyboard) — UIKit
- [Mouse, Keyboard, and Trackpad](https://developer.apple.com/documentation/AppKit/mouse-keyboard-and-trackpad) — AppKit

**Labels** <sub>`pages/labels.md`</sub>
- [Label](https://developer.apple.com/documentation/SwiftUI/Label) — SwiftUI
- [Text](https://developer.apple.com/documentation/SwiftUI/Text) — SwiftUI
- [UILabel](https://developer.apple.com/documentation/UIKit/UILabel) — UIKit
- [NSTextField](https://developer.apple.com/documentation/AppKit/NSTextField) — AppKit

**Launching** <sub>`pages/launching.md`</sub>
- [Specifying your app’s launch screen](https://developer.apple.com/documentation/Xcode/specifying-your-apps-launch-screen) — Xcode
- [Responding to the launch of your app](https://developer.apple.com/documentation/UIKit/responding-to-the-launch-of-your-app) — UIKit

**Layout** <sub>`pages/layout.md`</sub>
- [Composing custom layouts with SwiftUI](https://developer.apple.com/documentation/SwiftUI/composing-custom-layouts-with-swiftui) — SwiftUI

**Lists and tables** <sub>`pages/lists-and-tables.md`</sub>
- [List](https://developer.apple.com/documentation/SwiftUI/List) — SwiftUI
- [Tables](https://developer.apple.com/documentation/SwiftUI/Tables) — SwiftUI
- [UITableView](https://developer.apple.com/documentation/UIKit/UITableView) — UIKit
- [NSTableView](https://developer.apple.com/documentation/AppKit/NSTableView) — AppKit

**Live Activities** <sub>`pages/live-activities.md`</sub>
- [Developing a WidgetKit strategy](https://developer.apple.com/documentation/WidgetKit/Developing-a-WidgetKit-strategy) — WidgetKit

**Live Photos** <sub>`pages/live-photos.md`</sub>
- [PHLivePhoto](https://developer.apple.com/documentation/Photos/PHLivePhoto) — PhotoKit
- [LivePhotosKit JS](https://developer.apple.com/documentation/LivePhotosKitJS) — LivePhotosKit JS

**Lockups** <sub>`pages/lockups.md`</sub>
- [TVLockupView](https://developer.apple.com/documentation/TVUIKit/TVLockupView) — TVUIKit
- [TVLockupHeaderFooterView](https://developer.apple.com/documentation/TVUIKit/TVLockupHeaderFooterView) — TVUIKit

**Mac Catalyst** <sub>`pages/mac-catalyst.md`</sub>
- [Mac Catalyst](https://developer.apple.com/documentation/UIKit/mac-catalyst) — UIKit

**Managing accounts** <sub>`pages/managing-accounts.md`</sub>
- [Supporting passkeys](https://developer.apple.com/documentation/AuthenticationServices/supporting-passkeys) — Authentication Services

**Materials** <sub>`pages/materials.md`</sub>
- [glassEffect(_:in:)](https://developer.apple.com/documentation/SwiftUI/View/glassEffect(_:in:)) — SwiftUI
- [Material](https://developer.apple.com/documentation/SwiftUI/Material) — SwiftUI
- [UIVisualEffectView](https://developer.apple.com/documentation/UIKit/UIVisualEffectView) — UIKit
- [NSVisualEffectView](https://developer.apple.com/documentation/AppKit/NSVisualEffectView) — AppKit

**Menus** <sub>`pages/menus.md`</sub>
- [Menu](https://developer.apple.com/documentation/SwiftUI/Menu) — SwiftUI
- [Menus and shortcuts](https://developer.apple.com/documentation/UIKit/menus-and-shortcuts) — UIKit
- [Menus](https://developer.apple.com/documentation/AppKit/menus) — AppKit

**Modality** <sub>`pages/modality.md`</sub>
- [Presentation modifiers](https://developer.apple.com/documentation/SwiftUI/View-Presentation) — SwiftUI
- [UIModalPresentationStyle](https://developer.apple.com/documentation/UIKit/UIModalPresentationStyle) — UIKit
- [Modal Windows and Panels](https://developer.apple.com/documentation/AppKit/modal-windows-and-panels) — AppKit

**Motion** <sub>`pages/motion.md`</sub>
- [Animating views and transitions](https://developer.apple.com/tutorials/SwiftUI/animating-views-and-transitions) — SwiftUI

**Multitasking** <sub>`pages/multitasking.md`</sub>
- [Responding to the launch of your app](https://developer.apple.com/documentation/UIKit/responding-to-the-launch-of-your-app) — UIKit
- [Multitasking on iPad, Mac, and Apple Vision Pro](https://developer.apple.com/documentation/UIKit/multitasking-on-ipad-mac-and-apple-vision-pro) — UIKit

**Notifications** <sub>`pages/notifications.md`</sub>
- [Asking permission to use notifications](https://developer.apple.com/documentation/UserNotifications/asking-permission-to-use-notifications) — User Notifications

**Offering help** <sub>`pages/offering-help.md`</sub>
- [NSHelpManager](https://developer.apple.com/documentation/AppKit/NSHelpManager) — AppKit

**Ornaments** <sub>`pages/ornaments.md`</sub>
- [ornament(visibility:attachmentAnchor:contentAlignment:ornament:)](https://developer.apple.com/documentation/SwiftUI/View/ornament(visibility:attachmentAnchor:contentAlignment:ornament:)) — SwiftUI

**Outline views** <sub>`pages/outline-views.md`</sub>
- [OutlineGroup](https://developer.apple.com/documentation/SwiftUI/OutlineGroup) — SwiftUI
- [NSOutlineView](https://developer.apple.com/documentation/AppKit/NSOutlineView) — AppKit

**Page controls** <sub>`pages/page-controls.md`</sub>
- [PageTabViewStyle](https://developer.apple.com/documentation/SwiftUI/PageTabViewStyle) — SwiftUI
- [UIPageControl](https://developer.apple.com/documentation/UIKit/UIPageControl) — UIKit

**Panels** <sub>`pages/panels.md`</sub>
- [NSPanel](https://developer.apple.com/documentation/AppKit/NSPanel) — AppKit
- [hudWindow](https://developer.apple.com/documentation/AppKit/NSWindow/StyleMask-swift.struct/hudWindow) — AppKit

**Path controls** <sub>`pages/path-controls.md`</sub>
- [NSPathControl](https://developer.apple.com/documentation/AppKit/NSPathControl) — AppKit

**Pickers** <sub>`pages/pickers.md`</sub>
- [Picker](https://developer.apple.com/documentation/SwiftUI/Picker) — SwiftUI
- [UIDatePicker](https://developer.apple.com/documentation/UIKit/UIDatePicker) — UIKit
- [UIPickerView](https://developer.apple.com/documentation/UIKit/UIPickerView) — UIKit
- [NSDatePicker](https://developer.apple.com/documentation/AppKit/NSDatePicker) — AppKit

**Playing audio** <sub>`pages/playing-audio.md`</sub>
- [Configuring your app for media playback](https://developer.apple.com/documentation/AVFoundation/configuring-your-app-for-media-playback) — AVFoundation
- [AVAudioSession](https://developer.apple.com/documentation/AVFAudio/AVAudioSession) — AVFAudio
- [MusicKit](https://developer.apple.com/documentation/MusicKit) — MusicKit

**Playing video** <sub>`pages/playing-video.md`</sub>
- [Configuring your app for media playback](https://developer.apple.com/documentation/AVFoundation/configuring-your-app-for-media-playback) — AVFoundation

**Pointing devices** <sub>`pages/pointing-devices.md`</sub>
- [Input events](https://developer.apple.com/documentation/SwiftUI/Input-events) — SwiftUI
- [Pointer interactions](https://developer.apple.com/documentation/UIKit/pointer-interactions) — UIKit
- [Mouse, Keyboard, and Trackpad](https://developer.apple.com/documentation/AppKit/mouse-keyboard-and-trackpad) — AppKit

**Pop-up buttons** <sub>`pages/pop-up-buttons.md`</sub>
- [MenuPickerStyle](https://developer.apple.com/documentation/SwiftUI/MenuPickerStyle) — SwiftUI
- [changesSelectionAsPrimaryAction](https://developer.apple.com/documentation/UIKit/UIButton/changesSelectionAsPrimaryAction) — UIKit
- [NSPopUpButton](https://developer.apple.com/documentation/AppKit/NSPopUpButton) — AppKit

**Popovers** <sub>`pages/popovers.md`</sub>
- [popover(isPresented:attachmentAnchor:arrowEdge:content:)](https://developer.apple.com/documentation/SwiftUI/View/popover(isPresented:attachmentAnchor:arrowEdge:content:)) — SwiftUI
- [UIPopoverPresentationController](https://developer.apple.com/documentation/UIKit/UIPopoverPresentationController) — UIKit
- [NSPopover](https://developer.apple.com/documentation/AppKit/NSPopover) — AppKit

**Printing** <sub>`pages/printing.md`</sub>
- [UIPrintInteractionController](https://developer.apple.com/documentation/UIKit/UIPrintInteractionController) — UIKit
- [NSDocument](https://developer.apple.com/documentation/AppKit/NSDocument) — AppKit

**Privacy** <sub>`pages/privacy.md`</sub>
- [Requesting access to protected resources](https://developer.apple.com/documentation/UIKit/requesting-access-to-protected-resources) — UIKit
- [Requesting authorization to use location services](https://developer.apple.com/documentation/CoreLocation/requesting-authorization-to-use-location-services) — CoreLocation

**Progress indicators** <sub>`pages/progress-indicators.md`</sub>
- [ProgressView](https://developer.apple.com/documentation/SwiftUI/ProgressView) — SwiftUI
- [UIProgressView](https://developer.apple.com/documentation/UIKit/UIProgressView) — UIKit
- [UIActivityIndicatorView](https://developer.apple.com/documentation/UIKit/UIActivityIndicatorView) — UIKit
- [UIRefreshControl](https://developer.apple.com/documentation/UIKit/UIRefreshControl) — UIKit
- [NSProgressIndicator](https://developer.apple.com/documentation/AppKit/NSProgressIndicator) — AppKit

**Pull-down buttons** <sub>`pages/pull-down-buttons.md`</sub>
- [MenuPickerStyle](https://developer.apple.com/documentation/SwiftUI/MenuPickerStyle) — SwiftUI
- [showsMenuAsPrimaryAction](https://developer.apple.com/documentation/UIKit/UIControl/showsMenuAsPrimaryAction) — UIKit
- [pullsDown](https://developer.apple.com/documentation/AppKit/NSPopUpButton/pullsDown) — AppKit

**Rating indicators** <sub>`pages/rating-indicators.md`</sub>
- [NSLevelIndicator.Style.rating](https://developer.apple.com/documentation/AppKit/NSLevelIndicator/Style/rating) — AppKit

**Ratings and reviews** <sub>`pages/ratings-and-reviews.md`</sub>
- [RequestReviewAction](https://developer.apple.com/documentation/StoreKit/RequestReviewAction) — StoreKit

**ResearchKit** <sub>`pages/researchkit.md`</sub>
- [Protecting user privacy](https://developer.apple.com/documentation/HealthKit/protecting-user-privacy) — HealthKit

**Right to left** <sub>`pages/right-to-left.md`</sub>
- [Preparing views for localization](https://developer.apple.com/documentation/SwiftUI/Preparing-views-for-localization) — SwiftUI

**SF Symbols** <sub>`pages/sf-symbols.md`</sub>
- [Symbols](https://developer.apple.com/documentation/Symbols) — Symbols framework
- [Configuring and displaying symbol images in your UI](https://developer.apple.com/documentation/UIKit/configuring-and-displaying-symbol-images-in-your-ui) — UIKit
- [Creating custom symbol images for your app](https://developer.apple.com/documentation/UIKit/creating-custom-symbol-images-for-your-app) — UIKit

**Scroll views** <sub>`pages/scroll-views.md`</sub>
- [ScrollView](https://developer.apple.com/documentation/SwiftUI/ScrollView) — SwiftUI
- [UIScrollView](https://developer.apple.com/documentation/UIKit/UIScrollView) — UIKit
- [NSScrollView](https://developer.apple.com/documentation/AppKit/NSScrollView) — AppKit
- [WKPageOrientation](https://developer.apple.com/documentation/WatchKit/WKPageOrientation) — WatchKit
- [look](https://developer.apple.com/documentation/SwiftUI/ScrollInputKind/look) — SwiftUI

**Search fields** <sub>`pages/search-fields.md`</sub>
- [Adding a search interface to your app](https://developer.apple.com/documentation/SwiftUI/Adding-a-search-interface-to-your-app) — SwiftUI
- [searchable(text:placement:prompt:)](https://developer.apple.com/documentation/SwiftUI/View/searchable(text:placement:prompt:)) — SwiftUI
- [UISearchBar](https://developer.apple.com/documentation/UIKit/UISearchBar) — UIKit
- [UISearchTextField](https://developer.apple.com/documentation/UIKit/UISearchTextField) — UIKit
- [NSSearchField](https://developer.apple.com/documentation/AppKit/NSSearchField) — AppKit

**Searching** <sub>`pages/searching.md`</sub>
- [Adding your app’s content to Spotlight indexes](https://developer.apple.com/documentation/CoreSpotlight/adding-your-app-s-content-to-spotlight-indexes) — Core Spotlight

**Segmented controls** <sub>`pages/segmented-controls.md`</sub>
- [segmented](https://developer.apple.com/documentation/SwiftUI/PickerStyle/segmented) — SwiftUI
- [UISegmentedControl](https://developer.apple.com/documentation/UIKit/UISegmentedControl) — UIKit
- [NSSegmentedControl](https://developer.apple.com/documentation/AppKit/NSSegmentedControl) — AppKit

**Settings** <sub>`pages/settings.md`</sub>
- [Settings](https://developer.apple.com/documentation/SwiftUI/Settings) — SwiftUI
- [UserDefaults](https://developer.apple.com/documentation/Foundation/UserDefaults) — Foundation

**Sheets** <sub>`pages/sheets.md`</sub>
- [sheet(item:onDismiss:content:)](https://developer.apple.com/documentation/SwiftUI/View/sheet(item:onDismiss:content:)) — SwiftUI
- [UISheetPresentationController](https://developer.apple.com/documentation/UIKit/UISheetPresentationController) — UIKit
- [presentAsSheet(_:)](https://developer.apple.com/documentation/AppKit/NSViewController/presentAsSheet(_:)) — AppKit

**Sidebars** <sub>`pages/sidebars.md`</sub>
- [sidebarAdaptable](https://developer.apple.com/documentation/SwiftUI/TabViewStyle/sidebarAdaptable) — SwiftUI
- [NavigationSplitView](https://developer.apple.com/documentation/SwiftUI/NavigationSplitView) — SwiftUI
- [sidebar](https://developer.apple.com/documentation/SwiftUI/ListStyle/sidebar) — SwiftUI
- [UICollectionLayoutListConfiguration](https://developer.apple.com/documentation/UIKit/UICollectionLayoutListConfiguration-swift.struct) — UIKit
- [NSSplitViewController](https://developer.apple.com/documentation/AppKit/NSSplitViewController) — AppKit

**Sign in with Apple** <sub>`pages/sign-in-with-apple.md`</sub>
- [Displaying Sign in with Apple buttons on the web](https://developer.apple.com/documentation/signinwithapple/displaying-sign-in-with-apple-buttons-on-the-web) — Sign in with Apple

**Sliders** <sub>`pages/sliders.md`</sub>
- [Slider](https://developer.apple.com/documentation/SwiftUI/Slider) — SwiftUI
- [UISlider](https://developer.apple.com/documentation/UIKit/UISlider) — UIKit
- [NSSlider](https://developer.apple.com/documentation/AppKit/NSSlider) — AppKit

**Spatial layout** <sub>`pages/spatial-layout.md`</sub>
- [Presenting windows and spaces](https://developer.apple.com/documentation/visionOS/presenting-windows-and-spaces) — visionOS
- [Positioning and sizing windows](https://developer.apple.com/documentation/visionOS/positioning-and-sizing-windows) — visionOS
- [Adding 3D content to your app](https://developer.apple.com/documentation/visionOS/adding-3d-content-to-your-app) — visionOS

**Split views** <sub>`pages/split-views.md`</sub>
- [NavigationSplitView](https://developer.apple.com/documentation/SwiftUI/NavigationSplitView) — SwiftUI
- [UISplitViewController](https://developer.apple.com/documentation/UIKit/UISplitViewController) — UIKit
- [NSSplitViewController](https://developer.apple.com/documentation/AppKit/NSSplitViewController) — AppKit

**Status bars** <sub>`pages/status-bars.md`</sub>
- [UIStatusBarStyle](https://developer.apple.com/documentation/UIKit/UIStatusBarStyle) — UIKit
- [preferredStatusBarStyle](https://developer.apple.com/documentation/UIKit/UIViewController/preferredStatusBarStyle) — UIKit

**Steppers** <sub>`pages/steppers.md`</sub>
- [UIStepper](https://developer.apple.com/documentation/UIKit/UIStepper) — UIKit
- [NSStepper](https://developer.apple.com/documentation/AppKit/NSStepper) — AppKit

**Tab bars** <sub>`pages/tab-bars.md`</sub>
- [TabView](https://developer.apple.com/documentation/SwiftUI/TabView) — SwiftUI
- [TabViewBottomAccessoryPlacement](https://developer.apple.com/documentation/SwiftUI/TabViewBottomAccessoryPlacement) — SwiftUI
- [Enhancing your app’s content with tab navigation](https://developer.apple.com/documentation/SwiftUI/Enhancing-your-app-content-with-tab-navigation) — SwiftUI
- [UITabBar](https://developer.apple.com/documentation/UIKit/UITabBar) — UIKit
- [Elevating your iPad app with a tab bar and sidebar](https://developer.apple.com/documentation/UIKit/elevating-your-ipad-app-with-a-tab-bar-and-sidebar) — UIKit

**Tab views** <sub>`pages/tab-views.md`</sub>
- [TabView](https://developer.apple.com/documentation/SwiftUI/TabView) — SwiftUI
- [NSTabView](https://developer.apple.com/documentation/AppKit/NSTabView) — AppKit

**Tap to Pay on iPhone** <sub>`pages/tap-to-pay-on-iphone.md`</sub>
- [Adding support for Tap to Pay on iPhone to your app](https://developer.apple.com/documentation/ProximityReader/adding-support-for-tap-to-pay-on-iphone-to-your-app) — ProximityReader

**Text fields** <sub>`pages/text-fields.md`</sub>
- [TextField](https://developer.apple.com/documentation/SwiftUI/TextField) — SwiftUI
- [SecureField](https://developer.apple.com/documentation/SwiftUI/SecureField) — SwiftUI
- [UITextField](https://developer.apple.com/documentation/UIKit/UITextField) — UIKit
- [NSTextField](https://developer.apple.com/documentation/AppKit/NSTextField) — AppKit

**Text views** <sub>`pages/text-views.md`</sub>
- [Text](https://developer.apple.com/documentation/SwiftUI/Text) — SwiftUI
- [UITextView](https://developer.apple.com/documentation/UIKit/UITextView) — UIKit
- [NSTextView](https://developer.apple.com/documentation/AppKit/NSTextView) — AppKit

**The menu bar** <sub>`pages/the-menu-bar.md`</sub>
- [CommandMenu](https://developer.apple.com/documentation/SwiftUI/CommandMenu) — SwiftUI
- [Adding menus and shortcuts to the menu bar and user interface](https://developer.apple.com/documentation/UIKit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface) — UIKit
- [NSStatusBar](https://developer.apple.com/documentation/AppKit/NSStatusBar) — AppKit

**Toggles** <sub>`pages/toggles.md`</sub>
- [Toggle](https://developer.apple.com/documentation/SwiftUI/Toggle) — SwiftUI
- [UISwitch](https://developer.apple.com/documentation/UIKit/UISwitch) — UIKit
- [NSButton.ButtonType.toggle](https://developer.apple.com/documentation/AppKit/NSButton/ButtonType/toggle) — AppKit
- [NSSwitch](https://developer.apple.com/documentation/AppKit/NSSwitch) — AppKit

**Token fields** <sub>`pages/token-fields.md`</sub>
- [NSTokenField](https://developer.apple.com/documentation/AppKit/NSTokenField) — AppKit

**Toolbars** <sub>`pages/toolbars.md`</sub>
- [Toolbars](https://developer.apple.com/documentation/SwiftUI/Toolbars) — SwiftUI
- [UIToolbar](https://developer.apple.com/documentation/UIKit/UIToolbar) — UIKit
- [NSToolbar](https://developer.apple.com/documentation/AppKit/NSToolbar) — AppKit

**Typography** <sub>`pages/typography.md`</sub>
- [Text input and output](https://developer.apple.com/documentation/SwiftUI/Text-input-and-output) — SwiftUI
- [Text display and fonts](https://developer.apple.com/documentation/UIKit/text-display-and-fonts) — UIKit
- [Fonts](https://developer.apple.com/documentation/AppKit/fonts) — AppKit

**Undo and redo** <sub>`pages/undo-and-redo.md`</sub>
- [UndoManager](https://developer.apple.com/documentation/Foundation/UndoManager) — Foundation

**Virtual keyboards** <sub>`pages/virtual-keyboards.md`</sub>
- [keyboardType(_:)](https://developer.apple.com/documentation/SwiftUI/View/keyboardType(_:)) — SwiftUI
- [textContentType(_:)](https://developer.apple.com/documentation/SwiftUI/View/textContentType(_:)) — SwiftUI
- [UIKeyboardType](https://developer.apple.com/documentation/UIKit/UIKeyboardType) — UIKit

**Watch faces** <sub>`pages/watch-faces.md`</sub>
- [Sharing an Apple Watch face](https://developer.apple.com/documentation/ClockKit/sharing-an-apple-watch-face) — ClockKit

**Web views** <sub>`pages/web-views.md`</sub>
- [WKWebView](https://developer.apple.com/documentation/WebKit/WKWebView) — WebKit

**Widgets** <sub>`pages/widgets.md`</sub>
- [Developing a WidgetKit strategy](https://developer.apple.com/documentation/WidgetKit/Developing-a-WidgetKit-strategy) — WidgetKit

**Windows** <sub>`pages/windows.md`</sub>
- [Windows](https://developer.apple.com/documentation/SwiftUI/Windows) — SwiftUI
- [WindowGroup](https://developer.apple.com/documentation/SwiftUI/WindowGroup) — SwiftUI
- [UIWindow](https://developer.apple.com/documentation/UIKit/UIWindow) — UIKit
- [NSWindow](https://developer.apple.com/documentation/AppKit/NSWindow) — AppKit

**Workouts** <sub>`pages/workouts.md`</sub>
- [Workouts and activity rings](https://developer.apple.com/documentation/HealthKit/workouts-and-activity-rings) — HealthKit

**iMessage apps and stickers** <sub>`pages/imessage-apps-and-stickers.md`</sub>
- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](https://developer.apple.com/documentation/Messages/adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime) — Messages

---

## By framework

Same data, grouped the other direction — everything the HIG cites for a given framework.

### AVFAudio
- [AVAudioSession](https://developer.apple.com/documentation/AVFAudio/AVAudioSession) — Playing audio (`pages/playing-audio.md`)

### AVFoundation
- [Enhancing your app experience with the Camera Control](https://developer.apple.com/documentation/AVFoundation/enhancing-your-app-experience-with-the-camera-control) — Camera Control (`pages/camera-control.md`)
- [AVCaptureControl](https://developer.apple.com/documentation/AVFoundation/AVCaptureControl) — Camera Control (`pages/camera-control.md`)
- [Configuring your app for media playback](https://developer.apple.com/documentation/AVFoundation/configuring-your-app-for-media-playback) — Playing audio (`pages/playing-audio.md`)
- [Configuring your app for media playback](https://developer.apple.com/documentation/AVFoundation/configuring-your-app-for-media-playback) — Playing video (`pages/playing-video.md`)

### App Intents
- [Getting started with the App Intents framework](https://developer.apple.com/documentation/AppIntents/getting-started-with-the-app-intents-framework) — App Shortcuts (`pages/app-shortcuts.md`)
- [Defining app entities for your custom data types](https://developer.apple.com/documentation/AppIntents/defining-app-entities-for-your-custom-data-types) — App Shortcuts (`pages/app-shortcuts.md`)

### AppKit
- [NSAlert](https://developer.apple.com/documentation/AppKit/NSAlert) — Alerts (`pages/alerts.md`)
- [NSBox](https://developer.apple.com/documentation/AppKit/NSBox) — Boxes (`pages/boxes.md`)
- [NSButton](https://developer.apple.com/documentation/AppKit/NSButton) — Buttons (`pages/buttons.md`)
- [NSCollectionView](https://developer.apple.com/documentation/AppKit/NSCollectionView) — Collections (`pages/collections.md`)
- [NSColorWell](https://developer.apple.com/documentation/AppKit/NSColorWell) — Color wells (`pages/color-wells.md`)
- [Color](https://developer.apple.com/documentation/AppKit/color) — Color (`pages/color.md`)
- [NSBrowser](https://developer.apple.com/documentation/AppKit/NSBrowser) — Column views (`pages/column-views.md`)
- [NSComboBox](https://developer.apple.com/documentation/AppKit/NSComboBox) — Combo boxes (`pages/combo-boxes.md`)
- [popUpContextMenu(_:with:for:)](https://developer.apple.com/documentation/AppKit/NSMenu/popUpContextMenu(_:with:for:)) — Context menus (`pages/context-menus.md`)
- [NSButton.BezelStyle.disclosure](https://developer.apple.com/documentation/AppKit/NSButton/BezelStyle-swift.enum/disclosure) — Disclosure controls (`pages/disclosure-controls.md`)
- [NSButton.BezelStyle.pushDisclosure](https://developer.apple.com/documentation/AppKit/NSButton/BezelStyle-swift.enum/pushDisclosure) — Disclosure controls (`pages/disclosure-controls.md`)
- [applicationDockMenu(_:)](https://developer.apple.com/documentation/AppKit/NSApplicationDelegate/applicationDockMenu(_:)) — Dock menus (`pages/dock-menus.md`)
- [Drag and Drop](https://developer.apple.com/documentation/AppKit/drag-and-drop) — Drag and drop (`pages/drag-and-drop.md`)
- [NSMenu](https://developer.apple.com/documentation/AppKit/NSMenu) — Edit menus (`pages/edit-menus.md`)
- [NSLevelIndicator](https://developer.apple.com/documentation/AppKit/NSLevelIndicator) — Gauges (`pages/gauges.md`)
- [NSScreen](https://developer.apple.com/documentation/AppKit/NSScreen) — Going full screen (`pages/going-full-screen.md`)
- [NSWindow.CollectionBehavior](https://developer.apple.com/documentation/AppKit/NSWindow/CollectionBehavior-swift.struct) — Going full screen (`pages/going-full-screen.md`)
- [NSImageView](https://developer.apple.com/documentation/AppKit/NSImageView) — Image views (`pages/image-views.md`)
- [NSImageView](https://developer.apple.com/documentation/AppKit/NSImageView) — Image wells (`pages/image-wells.md`)
- [NSImageView](https://developer.apple.com/documentation/AppKit/NSImageView) — Images (`pages/images.md`)
- [Mouse, Keyboard, and Trackpad](https://developer.apple.com/documentation/AppKit/mouse-keyboard-and-trackpad) — Keyboards (`pages/keyboards.md`)
- [NSTextField](https://developer.apple.com/documentation/AppKit/NSTextField) — Labels (`pages/labels.md`)
- [NSTableView](https://developer.apple.com/documentation/AppKit/NSTableView) — Lists and tables (`pages/lists-and-tables.md`)
- [NSVisualEffectView](https://developer.apple.com/documentation/AppKit/NSVisualEffectView) — Materials (`pages/materials.md`)
- [Menus](https://developer.apple.com/documentation/AppKit/menus) — Menus (`pages/menus.md`)
- [Modal Windows and Panels](https://developer.apple.com/documentation/AppKit/modal-windows-and-panels) — Modality (`pages/modality.md`)
- [NSHelpManager](https://developer.apple.com/documentation/AppKit/NSHelpManager) — Offering help (`pages/offering-help.md`)
- [NSOutlineView](https://developer.apple.com/documentation/AppKit/NSOutlineView) — Outline views (`pages/outline-views.md`)
- [NSPanel](https://developer.apple.com/documentation/AppKit/NSPanel) — Panels (`pages/panels.md`)
- [hudWindow](https://developer.apple.com/documentation/AppKit/NSWindow/StyleMask-swift.struct/hudWindow) — Panels (`pages/panels.md`)
- [NSPathControl](https://developer.apple.com/documentation/AppKit/NSPathControl) — Path controls (`pages/path-controls.md`)
- [NSDatePicker](https://developer.apple.com/documentation/AppKit/NSDatePicker) — Pickers (`pages/pickers.md`)
- [Mouse, Keyboard, and Trackpad](https://developer.apple.com/documentation/AppKit/mouse-keyboard-and-trackpad) — Pointing devices (`pages/pointing-devices.md`)
- [NSPopUpButton](https://developer.apple.com/documentation/AppKit/NSPopUpButton) — Pop-up buttons (`pages/pop-up-buttons.md`)
- [NSPopover](https://developer.apple.com/documentation/AppKit/NSPopover) — Popovers (`pages/popovers.md`)
- [NSDocument](https://developer.apple.com/documentation/AppKit/NSDocument) — Printing (`pages/printing.md`)
- [NSProgressIndicator](https://developer.apple.com/documentation/AppKit/NSProgressIndicator) — Progress indicators (`pages/progress-indicators.md`)
- [pullsDown](https://developer.apple.com/documentation/AppKit/NSPopUpButton/pullsDown) — Pull-down buttons (`pages/pull-down-buttons.md`)
- [NSLevelIndicator.Style.rating](https://developer.apple.com/documentation/AppKit/NSLevelIndicator/Style/rating) — Rating indicators (`pages/rating-indicators.md`)
- [NSScrollView](https://developer.apple.com/documentation/AppKit/NSScrollView) — Scroll views (`pages/scroll-views.md`)
- [NSSearchField](https://developer.apple.com/documentation/AppKit/NSSearchField) — Search fields (`pages/search-fields.md`)
- [NSSegmentedControl](https://developer.apple.com/documentation/AppKit/NSSegmentedControl) — Segmented controls (`pages/segmented-controls.md`)
- [presentAsSheet(_:)](https://developer.apple.com/documentation/AppKit/NSViewController/presentAsSheet(_:)) — Sheets (`pages/sheets.md`)
- [NSSplitViewController](https://developer.apple.com/documentation/AppKit/NSSplitViewController) — Sidebars (`pages/sidebars.md`)
- [NSSlider](https://developer.apple.com/documentation/AppKit/NSSlider) — Sliders (`pages/sliders.md`)
- [NSSplitViewController](https://developer.apple.com/documentation/AppKit/NSSplitViewController) — Split views (`pages/split-views.md`)
- [NSStepper](https://developer.apple.com/documentation/AppKit/NSStepper) — Steppers (`pages/steppers.md`)
- [NSTabView](https://developer.apple.com/documentation/AppKit/NSTabView) — Tab views (`pages/tab-views.md`)
- [NSTextField](https://developer.apple.com/documentation/AppKit/NSTextField) — Text fields (`pages/text-fields.md`)
- [NSTextView](https://developer.apple.com/documentation/AppKit/NSTextView) — Text views (`pages/text-views.md`)
- [NSStatusBar](https://developer.apple.com/documentation/AppKit/NSStatusBar) — The menu bar (`pages/the-menu-bar.md`)
- [NSButton.ButtonType.toggle](https://developer.apple.com/documentation/AppKit/NSButton/ButtonType/toggle) — Toggles (`pages/toggles.md`)
- [NSSwitch](https://developer.apple.com/documentation/AppKit/NSSwitch) — Toggles (`pages/toggles.md`)
- [NSTokenField](https://developer.apple.com/documentation/AppKit/NSTokenField) — Token fields (`pages/token-fields.md`)
- [NSToolbar](https://developer.apple.com/documentation/AppKit/NSToolbar) — Toolbars (`pages/toolbars.md`)
- [Fonts](https://developer.apple.com/documentation/AppKit/fonts) — Typography (`pages/typography.md`)
- [NSWindow](https://developer.apple.com/documentation/AppKit/NSWindow) — Windows (`pages/windows.md`)

### Authentication Services
- [Supporting passkeys](https://developer.apple.com/documentation/AuthenticationServices/supporting-passkeys) — Managing accounts (`pages/managing-accounts.md`)

### ClockKit
- [Sharing an Apple Watch face](https://developer.apple.com/documentation/ClockKit/sharing-an-apple-watch-face) — Watch faces (`pages/watch-faces.md`)

### Core Motion
- [Getting processed device-motion data](https://developer.apple.com/documentation/CoreMotion/getting-processed-device-motion-data) — Gyroscope and accelerometer (`pages/gyro-and-accelerometer.md`)

### Core Spotlight
- [Adding your app’s content to Spotlight indexes](https://developer.apple.com/documentation/CoreSpotlight/adding-your-app-s-content-to-spotlight-indexes) — Searching (`pages/searching.md`)

### CoreLocation
- [Requesting authorization to use location services](https://developer.apple.com/documentation/CoreLocation/requesting-authorization-to-use-location-services) — Privacy (`pages/privacy.md`)

### Foundation
- [App Extension Support](https://developer.apple.com/documentation/Foundation/app-extension-support) — Activity views (`pages/activity-views.md`)
- [UserDefaults](https://developer.apple.com/documentation/Foundation/UserDefaults) — Settings (`pages/settings.md`)
- [UndoManager](https://developer.apple.com/documentation/Foundation/UndoManager) — Undo and redo (`pages/undo-and-redo.md`)

### HealthKit
- [HKActivityRingView](https://developer.apple.com/documentation/HealthKitUI/HKActivityRingView) — Activity rings (`pages/activity-rings.md`)
- [Protecting user privacy](https://developer.apple.com/documentation/HealthKit/protecting-user-privacy) — CareKit (`pages/carekit.md`)
- [Protecting user privacy](https://developer.apple.com/documentation/HealthKit/protecting-user-privacy) — HealthKit (`pages/healthkit.md`)
- [Protecting user privacy](https://developer.apple.com/documentation/HealthKit/protecting-user-privacy) — ResearchKit (`pages/researchkit.md`)
- [Workouts and activity rings](https://developer.apple.com/documentation/HealthKit/workouts-and-activity-rings) — Workouts (`pages/workouts.md`)

### LivePhotosKit JS
- [LivePhotosKit JS](https://developer.apple.com/documentation/LivePhotosKitJS) — Live Photos (`pages/live-photos.md`)

### Messages
- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](https://developer.apple.com/documentation/Messages/adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime) — iMessage apps and stickers (`pages/imessage-apps-and-stickers.md`)

### MusicKit
- [MusicKit](https://developer.apple.com/documentation/MusicKit) — Playing audio (`pages/playing-audio.md`)

### PassKit
- [Apple Pay](https://developer.apple.com/documentation/PassKit/apple-pay) — Apple Pay (`pages/apple-pay.md`)

### PhotoKit
- [PHLivePhoto](https://developer.apple.com/documentation/Photos/PHLivePhoto) — Live Photos (`pages/live-photos.md`)

### ProximityReader
- [Adopting the Verifier API in your iPhone app](https://developer.apple.com/documentation/ProximityReader/adopting-the-verifier-api-in-your-iphone-app) — ID Verifier (`pages/id-verifier.md`)
- [Adding support for Tap to Pay on iPhone to your app](https://developer.apple.com/documentation/ProximityReader/adding-support-for-tap-to-pay-on-iphone-to-your-app) — Tap to Pay on iPhone (`pages/tap-to-pay-on-iphone.md`)

### Sign in with Apple
- [Displaying Sign in with Apple buttons on the web](https://developer.apple.com/documentation/signinwithapple/displaying-sign-in-with-apple-buttons-on-the-web) — Sign in with Apple (`pages/sign-in-with-apple.md`)

### StoreKit
- [In-App Purchase](https://developer.apple.com/documentation/StoreKit/in-app-purchase) — In-app purchase (`pages/in-app-purchase.md`)
- [RequestReviewAction](https://developer.apple.com/documentation/StoreKit/RequestReviewAction) — Ratings and reviews (`pages/ratings-and-reviews.md`)

### Swift, Objective-C
- [Managing your game window for Metal in macOS](https://developer.apple.com/documentation/Metal/managing-your-game-window-for-metal-in-macos) — Going full screen (`pages/going-full-screen.md`)

### SwiftUI
- [confirmationDialog(_:isPresented:titleVisibility:actions:)](https://developer.apple.com/documentation/SwiftUI/View/confirmationDialog(_:isPresented:titleVisibility:actions:)-46zbb) — Action sheets (`pages/action-sheets.md`)
- [alert(_:isPresented:actions:)](https://developer.apple.com/documentation/SwiftUI/View/alert(_:isPresented:actions:)-1bkka) — Alerts (`pages/alerts.md`)
- [GroupBox](https://developer.apple.com/documentation/SwiftUI/GroupBox) — Boxes (`pages/boxes.md`)
- [Button](https://developer.apple.com/documentation/SwiftUI/Button) — Buttons (`pages/buttons.md`)
- [ShareLink](https://developer.apple.com/documentation/SwiftUI/ShareLink) — Collaboration and sharing (`pages/collaboration-and-sharing.md`)
- [Color](https://developer.apple.com/documentation/SwiftUI/Color) — Color (`pages/color.md`)
- [contextMenu(menuItems:)](https://developer.apple.com/documentation/SwiftUI/View/contextMenu(menuItems:)) — Context menus (`pages/context-menus.md`)
- [DisclosureGroup](https://developer.apple.com/documentation/SwiftUI/DisclosureGroup) — Disclosure controls (`pages/disclosure-controls.md`)
- [Input events](https://developer.apple.com/documentation/SwiftUI/Input-events) — Entering data (`pages/entering-data.md`)
- [Documents](https://developer.apple.com/documentation/SwiftUI/Documents) — File management (`pages/file-management.md`)
- [Gauge](https://developer.apple.com/documentation/SwiftUI/Gauge) — Gauges (`pages/gauges.md`)
- [Gestures](https://developer.apple.com/documentation/SwiftUI/Gestures) — Gestures (`pages/gestures.md`)
- [fullScreenCover(item:onDismiss:content:)](https://developer.apple.com/documentation/SwiftUI/View/fullScreenCover(item:onDismiss:content:)) — Going full screen (`pages/going-full-screen.md`)
- [Image](https://developer.apple.com/documentation/SwiftUI/Image) — Image views (`pages/image-views.md`)
- [Images](https://developer.apple.com/documentation/SwiftUI/Images) — Images (`pages/images.md`)
- [Immersive spaces](https://developer.apple.com/documentation/SwiftUI/Immersive-spaces) — Immersive experiences (`pages/immersive-experiences.md`)
- [KeyboardShortcut](https://developer.apple.com/documentation/SwiftUI/KeyboardShortcut) — Keyboards (`pages/keyboards.md`)
- [Input events](https://developer.apple.com/documentation/SwiftUI/Input-events) — Keyboards (`pages/keyboards.md`)
- [Label](https://developer.apple.com/documentation/SwiftUI/Label) — Labels (`pages/labels.md`)
- [Text](https://developer.apple.com/documentation/SwiftUI/Text) — Labels (`pages/labels.md`)
- [Composing custom layouts with SwiftUI](https://developer.apple.com/documentation/SwiftUI/composing-custom-layouts-with-swiftui) — Layout (`pages/layout.md`)
- [List](https://developer.apple.com/documentation/SwiftUI/List) — Lists and tables (`pages/lists-and-tables.md`)
- [Tables](https://developer.apple.com/documentation/SwiftUI/Tables) — Lists and tables (`pages/lists-and-tables.md`)
- [glassEffect(_:in:)](https://developer.apple.com/documentation/SwiftUI/View/glassEffect(_:in:)) — Materials (`pages/materials.md`)
- [Material](https://developer.apple.com/documentation/SwiftUI/Material) — Materials (`pages/materials.md`)
- [Menu](https://developer.apple.com/documentation/SwiftUI/Menu) — Menus (`pages/menus.md`)
- [Presentation modifiers](https://developer.apple.com/documentation/SwiftUI/View-Presentation) — Modality (`pages/modality.md`)
- [Animating views and transitions](https://developer.apple.com/tutorials/SwiftUI/animating-views-and-transitions) — Motion (`pages/motion.md`)
- [ornament(visibility:attachmentAnchor:contentAlignment:ornament:)](https://developer.apple.com/documentation/SwiftUI/View/ornament(visibility:attachmentAnchor:contentAlignment:ornament:)) — Ornaments (`pages/ornaments.md`)
- [OutlineGroup](https://developer.apple.com/documentation/SwiftUI/OutlineGroup) — Outline views (`pages/outline-views.md`)
- [PageTabViewStyle](https://developer.apple.com/documentation/SwiftUI/PageTabViewStyle) — Page controls (`pages/page-controls.md`)
- [Picker](https://developer.apple.com/documentation/SwiftUI/Picker) — Pickers (`pages/pickers.md`)
- [Input events](https://developer.apple.com/documentation/SwiftUI/Input-events) — Pointing devices (`pages/pointing-devices.md`)
- [MenuPickerStyle](https://developer.apple.com/documentation/SwiftUI/MenuPickerStyle) — Pop-up buttons (`pages/pop-up-buttons.md`)
- [popover(isPresented:attachmentAnchor:arrowEdge:content:)](https://developer.apple.com/documentation/SwiftUI/View/popover(isPresented:attachmentAnchor:arrowEdge:content:)) — Popovers (`pages/popovers.md`)
- [ProgressView](https://developer.apple.com/documentation/SwiftUI/ProgressView) — Progress indicators (`pages/progress-indicators.md`)
- [MenuPickerStyle](https://developer.apple.com/documentation/SwiftUI/MenuPickerStyle) — Pull-down buttons (`pages/pull-down-buttons.md`)
- [Preparing views for localization](https://developer.apple.com/documentation/SwiftUI/Preparing-views-for-localization) — Right to left (`pages/right-to-left.md`)
- [ScrollView](https://developer.apple.com/documentation/SwiftUI/ScrollView) — Scroll views (`pages/scroll-views.md`)
- [look](https://developer.apple.com/documentation/SwiftUI/ScrollInputKind/look) — Scroll views (`pages/scroll-views.md`)
- [Adding a search interface to your app](https://developer.apple.com/documentation/SwiftUI/Adding-a-search-interface-to-your-app) — Search fields (`pages/search-fields.md`)
- [searchable(text:placement:prompt:)](https://developer.apple.com/documentation/SwiftUI/View/searchable(text:placement:prompt:)) — Search fields (`pages/search-fields.md`)
- [segmented](https://developer.apple.com/documentation/SwiftUI/PickerStyle/segmented) — Segmented controls (`pages/segmented-controls.md`)
- [Settings](https://developer.apple.com/documentation/SwiftUI/Settings) — Settings (`pages/settings.md`)
- [sheet(item:onDismiss:content:)](https://developer.apple.com/documentation/SwiftUI/View/sheet(item:onDismiss:content:)) — Sheets (`pages/sheets.md`)
- [sidebarAdaptable](https://developer.apple.com/documentation/SwiftUI/TabViewStyle/sidebarAdaptable) — Sidebars (`pages/sidebars.md`)
- [NavigationSplitView](https://developer.apple.com/documentation/SwiftUI/NavigationSplitView) — Sidebars (`pages/sidebars.md`)
- [sidebar](https://developer.apple.com/documentation/SwiftUI/ListStyle/sidebar) — Sidebars (`pages/sidebars.md`)
- [Slider](https://developer.apple.com/documentation/SwiftUI/Slider) — Sliders (`pages/sliders.md`)
- [NavigationSplitView](https://developer.apple.com/documentation/SwiftUI/NavigationSplitView) — Split views (`pages/split-views.md`)
- [TabView](https://developer.apple.com/documentation/SwiftUI/TabView) — Tab bars (`pages/tab-bars.md`)
- [TabViewBottomAccessoryPlacement](https://developer.apple.com/documentation/SwiftUI/TabViewBottomAccessoryPlacement) — Tab bars (`pages/tab-bars.md`)
- [Enhancing your app’s content with tab navigation](https://developer.apple.com/documentation/SwiftUI/Enhancing-your-app-content-with-tab-navigation) — Tab bars (`pages/tab-bars.md`)
- [TabView](https://developer.apple.com/documentation/SwiftUI/TabView) — Tab views (`pages/tab-views.md`)
- [TextField](https://developer.apple.com/documentation/SwiftUI/TextField) — Text fields (`pages/text-fields.md`)
- [SecureField](https://developer.apple.com/documentation/SwiftUI/SecureField) — Text fields (`pages/text-fields.md`)
- [Text](https://developer.apple.com/documentation/SwiftUI/Text) — Text views (`pages/text-views.md`)
- [CommandMenu](https://developer.apple.com/documentation/SwiftUI/CommandMenu) — The menu bar (`pages/the-menu-bar.md`)
- [Toggle](https://developer.apple.com/documentation/SwiftUI/Toggle) — Toggles (`pages/toggles.md`)
- [Toolbars](https://developer.apple.com/documentation/SwiftUI/Toolbars) — Toolbars (`pages/toolbars.md`)
- [Text input and output](https://developer.apple.com/documentation/SwiftUI/Text-input-and-output) — Typography (`pages/typography.md`)
- [keyboardType(_:)](https://developer.apple.com/documentation/SwiftUI/View/keyboardType(_:)) — Virtual keyboards (`pages/virtual-keyboards.md`)
- [textContentType(_:)](https://developer.apple.com/documentation/SwiftUI/View/textContentType(_:)) — Virtual keyboards (`pages/virtual-keyboards.md`)
- [Windows](https://developer.apple.com/documentation/SwiftUI/Windows) — Windows (`pages/windows.md`)
- [WindowGroup](https://developer.apple.com/documentation/SwiftUI/WindowGroup) — Windows (`pages/windows.md`)

### Symbols framework
- [Symbols](https://developer.apple.com/documentation/Symbols) — SF Symbols (`pages/sf-symbols.md`)

### TVML
- [Focus Attributes](https://developer.apple.com/documentation/TVML/focus-attributes) — Focus and selection (`pages/focus-and-selection.md`)

### TVUIKit
- [TVDigitEntryViewController](https://developer.apple.com/documentation/TVUIKit/TVDigitEntryViewController) — Digit entry views (`pages/digit-entry-views.md`)
- [TVLockupView](https://developer.apple.com/documentation/TVUIKit/TVLockupView) — Lockups (`pages/lockups.md`)
- [TVLockupHeaderFooterView](https://developer.apple.com/documentation/TVUIKit/TVLockupHeaderFooterView) — Lockups (`pages/lockups.md`)

### UIKit
- [UIAlertController.Style.actionSheet](https://developer.apple.com/documentation/UIKit/UIAlertController/Style/actionSheet) — Action sheets (`pages/action-sheets.md`)
- [UIActivityViewController](https://developer.apple.com/documentation/UIKit/UIActivityViewController) — Activity views (`pages/activity-views.md`)
- [UIActivity](https://developer.apple.com/documentation/UIKit/UIActivity) — Activity views (`pages/activity-views.md`)
- [UIAlertController](https://developer.apple.com/documentation/UIKit/UIAlertController) — Alerts (`pages/alerts.md`)
- [UIButton](https://developer.apple.com/documentation/UIKit/UIButton) — Buttons (`pages/buttons.md`)
- [UICollectionView](https://developer.apple.com/documentation/UIKit/UICollectionView) — Collections (`pages/collections.md`)
- [UIColorWell](https://developer.apple.com/documentation/UIKit/UIColorWell) — Color wells (`pages/color-wells.md`)
- [UIColorPickerViewController](https://developer.apple.com/documentation/UIKit/UIColorPickerViewController) — Color wells (`pages/color-wells.md`)
- [UIColor](https://developer.apple.com/documentation/UIKit/UIColor) — Color (`pages/color.md`)
- [UIContextMenuInteraction](https://developer.apple.com/documentation/UIKit/UIContextMenuInteraction) — Context menus (`pages/context-menus.md`)
- [Drag and drop](https://developer.apple.com/documentation/UIKit/drag-and-drop) — Drag and drop (`pages/drag-and-drop.md`)
- [UIEditMenuInteraction](https://developer.apple.com/documentation/UIKit/UIEditMenuInteraction) — Edit menus (`pages/edit-menus.md`)
- [Animation and haptics](https://developer.apple.com/documentation/UIKit/animation-and-haptics) — Feedback (`pages/feedback.md`)
- [Focus-based navigation](https://developer.apple.com/documentation/UIKit/focus-based-navigation) — Focus and selection (`pages/focus-and-selection.md`)
- [About focus interactions for Apple TV](https://developer.apple.com/documentation/UIKit/about-focus-interactions-for-apple-tv) — Focus and selection (`pages/focus-and-selection.md`)
- [UITouch](https://developer.apple.com/documentation/UIKit/UITouch) — Gestures (`pages/gestures.md`)
- [Add Home Screen quick actions](https://developer.apple.com/documentation/UIKit/add-home-screen-quick-actions) — Home Screen quick actions (`pages/home-screen-quick-actions.md`)
- [UIImageView](https://developer.apple.com/documentation/UIKit/UIImageView) — Image views (`pages/image-views.md`)
- [UIImageView](https://developer.apple.com/documentation/UIKit/UIImageView) — Images (`pages/images.md`)
- [Handling key presses made on a physical keyboard](https://developer.apple.com/documentation/UIKit/handling-key-presses-made-on-a-physical-keyboard) — Keyboards (`pages/keyboards.md`)
- [UILabel](https://developer.apple.com/documentation/UIKit/UILabel) — Labels (`pages/labels.md`)
- [Responding to the launch of your app](https://developer.apple.com/documentation/UIKit/responding-to-the-launch-of-your-app) — Launching (`pages/launching.md`)
- [UITableView](https://developer.apple.com/documentation/UIKit/UITableView) — Lists and tables (`pages/lists-and-tables.md`)
- [Mac Catalyst](https://developer.apple.com/documentation/UIKit/mac-catalyst) — Mac Catalyst (`pages/mac-catalyst.md`)
- [UIVisualEffectView](https://developer.apple.com/documentation/UIKit/UIVisualEffectView) — Materials (`pages/materials.md`)
- [Menus and shortcuts](https://developer.apple.com/documentation/UIKit/menus-and-shortcuts) — Menus (`pages/menus.md`)
- [UIModalPresentationStyle](https://developer.apple.com/documentation/UIKit/UIModalPresentationStyle) — Modality (`pages/modality.md`)
- [Responding to the launch of your app](https://developer.apple.com/documentation/UIKit/responding-to-the-launch-of-your-app) — Multitasking (`pages/multitasking.md`)
- [Multitasking on iPad, Mac, and Apple Vision Pro](https://developer.apple.com/documentation/UIKit/multitasking-on-ipad-mac-and-apple-vision-pro) — Multitasking (`pages/multitasking.md`)
- [UIPageControl](https://developer.apple.com/documentation/UIKit/UIPageControl) — Page controls (`pages/page-controls.md`)
- [UIDatePicker](https://developer.apple.com/documentation/UIKit/UIDatePicker) — Pickers (`pages/pickers.md`)
- [UIPickerView](https://developer.apple.com/documentation/UIKit/UIPickerView) — Pickers (`pages/pickers.md`)
- [Pointer interactions](https://developer.apple.com/documentation/UIKit/pointer-interactions) — Pointing devices (`pages/pointing-devices.md`)
- [changesSelectionAsPrimaryAction](https://developer.apple.com/documentation/UIKit/UIButton/changesSelectionAsPrimaryAction) — Pop-up buttons (`pages/pop-up-buttons.md`)
- [UIPopoverPresentationController](https://developer.apple.com/documentation/UIKit/UIPopoverPresentationController) — Popovers (`pages/popovers.md`)
- [UIPrintInteractionController](https://developer.apple.com/documentation/UIKit/UIPrintInteractionController) — Printing (`pages/printing.md`)
- [Requesting access to protected resources](https://developer.apple.com/documentation/UIKit/requesting-access-to-protected-resources) — Privacy (`pages/privacy.md`)
- [UIProgressView](https://developer.apple.com/documentation/UIKit/UIProgressView) — Progress indicators (`pages/progress-indicators.md`)
- [UIActivityIndicatorView](https://developer.apple.com/documentation/UIKit/UIActivityIndicatorView) — Progress indicators (`pages/progress-indicators.md`)
- [UIRefreshControl](https://developer.apple.com/documentation/UIKit/UIRefreshControl) — Progress indicators (`pages/progress-indicators.md`)
- [showsMenuAsPrimaryAction](https://developer.apple.com/documentation/UIKit/UIControl/showsMenuAsPrimaryAction) — Pull-down buttons (`pages/pull-down-buttons.md`)
- [UIScrollView](https://developer.apple.com/documentation/UIKit/UIScrollView) — Scroll views (`pages/scroll-views.md`)
- [UISearchBar](https://developer.apple.com/documentation/UIKit/UISearchBar) — Search fields (`pages/search-fields.md`)
- [UISearchTextField](https://developer.apple.com/documentation/UIKit/UISearchTextField) — Search fields (`pages/search-fields.md`)
- [UISegmentedControl](https://developer.apple.com/documentation/UIKit/UISegmentedControl) — Segmented controls (`pages/segmented-controls.md`)
- [Configuring and displaying symbol images in your UI](https://developer.apple.com/documentation/UIKit/configuring-and-displaying-symbol-images-in-your-ui) — SF Symbols (`pages/sf-symbols.md`)
- [Creating custom symbol images for your app](https://developer.apple.com/documentation/UIKit/creating-custom-symbol-images-for-your-app) — SF Symbols (`pages/sf-symbols.md`)
- [UISheetPresentationController](https://developer.apple.com/documentation/UIKit/UISheetPresentationController) — Sheets (`pages/sheets.md`)
- [UICollectionLayoutListConfiguration](https://developer.apple.com/documentation/UIKit/UICollectionLayoutListConfiguration-swift.struct) — Sidebars (`pages/sidebars.md`)
- [UISlider](https://developer.apple.com/documentation/UIKit/UISlider) — Sliders (`pages/sliders.md`)
- [UISplitViewController](https://developer.apple.com/documentation/UIKit/UISplitViewController) — Split views (`pages/split-views.md`)
- [UIStatusBarStyle](https://developer.apple.com/documentation/UIKit/UIStatusBarStyle) — Status bars (`pages/status-bars.md`)
- [preferredStatusBarStyle](https://developer.apple.com/documentation/UIKit/UIViewController/preferredStatusBarStyle) — Status bars (`pages/status-bars.md`)
- [UIStepper](https://developer.apple.com/documentation/UIKit/UIStepper) — Steppers (`pages/steppers.md`)
- [UITabBar](https://developer.apple.com/documentation/UIKit/UITabBar) — Tab bars (`pages/tab-bars.md`)
- [Elevating your iPad app with a tab bar and sidebar](https://developer.apple.com/documentation/UIKit/elevating-your-ipad-app-with-a-tab-bar-and-sidebar) — Tab bars (`pages/tab-bars.md`)
- [UITextField](https://developer.apple.com/documentation/UIKit/UITextField) — Text fields (`pages/text-fields.md`)
- [UITextView](https://developer.apple.com/documentation/UIKit/UITextView) — Text views (`pages/text-views.md`)
- [Adding menus and shortcuts to the menu bar and user interface](https://developer.apple.com/documentation/UIKit/adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface) — The menu bar (`pages/the-menu-bar.md`)
- [UISwitch](https://developer.apple.com/documentation/UIKit/UISwitch) — Toggles (`pages/toggles.md`)
- [UIToolbar](https://developer.apple.com/documentation/UIKit/UIToolbar) — Toolbars (`pages/toolbars.md`)
- [Text display and fonts](https://developer.apple.com/documentation/UIKit/text-display-and-fonts) — Typography (`pages/typography.md`)
- [UIKeyboardType](https://developer.apple.com/documentation/UIKit/UIKeyboardType) — Virtual keyboards (`pages/virtual-keyboards.md`)
- [UIWindow](https://developer.apple.com/documentation/UIKit/UIWindow) — Windows (`pages/windows.md`)

### User Notifications
- [Asking permission to use notifications](https://developer.apple.com/documentation/UserNotifications/asking-permission-to-use-notifications) — Notifications (`pages/notifications.md`)

### WatchKit
- [WKInterfacePaymentButton](https://developer.apple.com/documentation/WatchKit/WKInterfacePaymentButton) — Apple Pay (`pages/apple-pay.md`)
- [WKCrownDelegate](https://developer.apple.com/documentation/WatchKit/WKCrownDelegate) — Digital Crown (`pages/digital-crown.md`)
- [WKPageOrientation](https://developer.apple.com/documentation/WatchKit/WKPageOrientation) — Scroll views (`pages/scroll-views.md`)

### WebKit
- [WKWebView](https://developer.apple.com/documentation/WebKit/WKWebView) — Web views (`pages/web-views.md`)

### WidgetKit
- [Developing a WidgetKit strategy](https://developer.apple.com/documentation/WidgetKit/Developing-a-WidgetKit-strategy) — Live Activities (`pages/live-activities.md`)
- [Developing a WidgetKit strategy](https://developer.apple.com/documentation/WidgetKit/Developing-a-WidgetKit-strategy) — Widgets (`pages/widgets.md`)

### Xcode
- [Localization](https://developer.apple.com/documentation/Xcode/localization) — Inclusion (`pages/inclusion.md`)
- [Specifying your app’s launch screen](https://developer.apple.com/documentation/Xcode/specifying-your-apps-launch-screen) — Launching (`pages/launching.md`)

### visionOS
- [Adopting best practices for privacy and user preferences](https://developer.apple.com/documentation/visionOS/adopting-best-practices-for-privacy) — Eyes (`pages/eyes.md`)
- [Drawing sharp layer-based content in visionOS](https://developer.apple.com/documentation/visionOS/drawing-sharp-layer-based-content) — Images (`pages/images.md`)
- [Creating fully immersive experiences in your app](https://developer.apple.com/documentation/visionOS/creating-fully-immersive-experiences) — Immersive experiences (`pages/immersive-experiences.md`)
- [Incorporating real-world surroundings in an immersive experience](https://developer.apple.com/documentation/visionOS/incorporating-real-world-surroundings-in-an-immersive-experience) — Immersive experiences (`pages/immersive-experiences.md`)
- [ImmersionStyle](https://developer.apple.com/documentation/SwiftUI/ImmersionStyle) — Immersive experiences (`pages/immersive-experiences.md`)
- [Presenting windows and spaces](https://developer.apple.com/documentation/visionOS/presenting-windows-and-spaces) — Spatial layout (`pages/spatial-layout.md`)
- [Positioning and sizing windows](https://developer.apple.com/documentation/visionOS/positioning-and-sizing-windows) — Spatial layout (`pages/spatial-layout.md`)
- [Adding 3D content to your app](https://developer.apple.com/documentation/visionOS/adding-3d-content-to-your-app) — Spatial layout (`pages/spatial-layout.md`)

### watchOS apps
- [Designing your app for the Always On state](https://developer.apple.com/documentation/watchOS-Apps/designing-your-app-for-the-always-on-state) — Always On (`pages/always-on.md`)
