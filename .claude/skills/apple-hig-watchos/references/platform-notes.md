# watchOS-specific guidance, collected

Every place the HIG states a rule specific to watchOS, lifted from the page it lives on. Sections appear alphabetically by page.

A heading like `### watchOS, iPadOS` upstream means the rule is shared; it's reproduced here in full so you don't have to go looking. Each entry links to the complete page, which also carries the cross-platform guidance this file deliberately omits.

---

## Action button

Full page: `references/action-button.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/action-button

In watchOS, a person can assign the Action button’s first press to drop a waypoint, start a dive, or begin a specific workout. Beyond a single button press, the Action button also supports secondary actions like marking a segment or transitioning to the next modality during a multi-part workout.

**Consider offering a secondary function that supports or advances the primary action people choose.** People often use the Action button without looking at the screen, so a subsequent button press needs to flow logically from the first press, while also making sense in the current context. If your app supports workout or dive actions, consider designing a simple, intuitive secondary function that people can easily learn and remember. Consider carefully before you offer more than one secondary function, because doing so can increase people’s cognitive load and make your app seem harder to use.

**Prefer using subsequent button presses to support additional functionality rather than to stop or conclude a function.** If you need to let people stop their main task — as opposed to pausing the current function — offer this option within your interface instead.

**Pause the current function when people press the Action button and side button together.** The exception is in a diving app where pausing a dive may be dangerous to the diver, causing them to lose track of their depth or not understand how long they’ve been underwater. Unless pausing the current function results in a negative experience, be sure to meet people’s expectations by letting them pause their current activity when they press both buttons at the same time.

---

## Action sheets

Full page: `references/action-sheets.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/action-sheets

The system-defined style for action sheets includes a title, an optional message, a Cancel button, and one or more additional buttons. The appearance of this interface is different depending on the device.

![An illustration of an action sheet on Apple Watch, showing content that represents text in the top half of the watch screen and two stacked buttons in the bottom half.](https://docs-assets.developer.apple.com/published/2e16789659cacc205c110daa36988c6e/action-sheet-watch-system-defined%402x.png)

Each button has an associated style that conveys information about the button’s effect. There are three system-defined button styles:

| Style | Meaning |
| --- | --- |
| Default | The button has no special meaning. |
| Destructive | The button destroys user data or performs a destructive action in the app. |
| Cancel | The button dismisses the view without taking any action. |

**Avoid displaying more than four buttons in an action sheet, including the Cancel button.** When there are fewer buttons onscreen, it’s easier for people to view all their options at once. Because the Cancel button is required, aim to provide no more than three additional choices.

---

## App icons

Full page: `references/app-icons.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/app-icons

**Avoid using black for your icon’s background.** Lighten a black background so the icon doesn’t blend into the display background.

---

## Buttons

Full page: `references/buttons.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/buttons

watchOS displays all inline buttons using the [capsule](https://developer.apple.com/documentation/SwiftUI/ButtonBorderShape/capsule) button shape. When you place a button inline with content, it gains a material effect that contrasts with the background to ensure legibility.

![An illustration that represents a screen on Apple Watch, which includes capsule-shaped Primary and Secondary buttons.](https://docs-assets.developer.apple.com/published/8af88bae79829cee4456dd3044a00a8c/buttons-watch-full-width%402x.png)

**Use a toolbar to place buttons in the corners.** The system automatically moves the time and title to accommodate toolbar buttons. The system also applies the [Liquid Glass](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass) appearance to toolbar buttons, providing a clear visual distinction from the content beneath them.

![An illustration showing toolbar buttons in the top leading and trailing corners, as well as three toolbar buttons across the bottom of the screen.](https://docs-assets.developer.apple.com/published/aa71da29ca2f0bfb3df010a0030a3844/buttons-watch-toolbar-corners%402x.png)

**Prefer buttons that span the width of the screen for primary actions in your app.** Full-width buttons look better and are easier for people to tap. If two buttons must share the same horizontal space, use the same height for both, and use images or short text titles for each button’s content.

**Use toolbar buttons to provide either navigation to related areas or contextual actions for the view’s content.** These buttons provide access to additional information or secondary actions for the view’s content.

**Use the same height for vertical stacks of one- and two-line text buttons.** As much as possible, use identical button heights for visual consistency.

---

## Charts

Full page: `references/charts.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/charts

**In general, avoid requiring complex chart interactions in your watchOS app.** As much as possible, prefer displaying useful information people can get at a glance and supporting simple interactions when they add value. If you also offer a version of your app in another platform, consider using it to display more details and to support additional interactions with your chart. For example, Heart Rate in watchOS displays a chart of the wearer’s heart-rate data for the current day, whereas the Health app on iPhone displays heart-rate data for several different periods of time and lets people examine individual marks.

---

## Collaboration and sharing

Full page: `references/collaboration-and-sharing.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing

In your SwiftUI app running in watchOS, use [ShareLink](https://developer.apple.com/documentation/SwiftUI/ShareLink) to present the system-provided share sheet.

---

## Color

Full page: `references/color.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/color

**Use background color to support existing content or supply additional information.** Background color can establish a sense of place and help people recognize key content. For example, in Activity, each infographic view for the Move, Exercise, and Stand Activity rings has a background that matches the color of the ring. Use background color when you have something to communicate, rather than as a solely visual flourish. Avoid using full-screen background color in views that are likely to remain onscreen for long periods of time, such as in a workout or audio-playing app.

**Recognize that people might prefer graphic complications to use tinted mode instead of full color.** The system can use a single color that’s based on the wearer’s selected color in a graphic complication’s images, gauges, and text. For guidance, see [Complications](https://developer.apple.com/design/human-interface-guidelines/complications).

---

## Feedback

Full page: `references/feedback.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/feedback

**Avoid displaying an indeterminate progress indicator — such as a loading indicator — in a watchOS app.** An animated indicator can make people think they need to continue paying attention to the display, which isn’t a good user experience. To provide a better experience, reassure people that they’ll receive a notification when the process completes.

---

## Game Center

Full page: `references/game-center.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/game-center

**Be aware of Game Center support on watchOS.** While GameKit features and API are available for watchOS games, keep in mind that there’s no system-supported Game Center UI that you can invoke on watchOS. Instead, Game Center content for watchOS games appears on a connected iPhone.

---

## Gestures

Full page: `references/gestures.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/gestures

#### Double tap

In watchOS 11 and later, people can use the double-tap gesture to scroll through lists and scroll views, and to advance between vertical tab views. Additionally, you can specify a toggle or button as the primary action in your app, or in your widget or Live Activity when the system displays it in the Smart Stack. Double-tapping in a view with a primary action highlights the control and then performs the action. The system also supports double tap for custom actions that you offer in [Notifications](https://developer.apple.com/design/human-interface-guidelines/notifications), where it acts on the first nondestructive action in the notification.

**Avoid setting a primary action in views with lists, scroll views, or vertical tabs.** This conflicts with the default navigation behaviors that people expect when they double-tap.

**Choose the button that people use most commonly as the primary action in a view.** Double tap is helpful in a nonscrolling view when it performs the action that people use the most. For example, in a media controls view, you could assign the primary action to the play/pause button. For developer guidance, see [handGestureShortcut(_:isEnabled:)](https://developer.apple.com/documentation/SwiftUI/View/handGestureShortcut(_:isEnabled:)) and [primaryAction](https://developer.apple.com/documentation/SwiftUI/HandGestureShortcut/primaryAction).

---

## Image views

Full page: `references/image-views.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/image-views

**Use SwiftUI to create animations when possible.** Alternatively, you can use WatchKit to animate a sequence of images within an image element if necessary. For developer guidance, see [WKImageAnimatable](https://developer.apple.com/documentation/WatchKit/WKImageAnimatable).

---

## Images

Full page: `references/images.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/images

**In general, avoid transparency to keep image files small.** If you always composite an image on the same solid background color, it’s more efficient to include the background in the image. However, transparency is necessary in complication images, menu icons, and other interface icons that serve as template images, because the system uses it to determine where to apply color.

**Use autoscaling PDFs to let you provide a single asset for all screen sizes.** Design your image for the 40mm and 42mm screens at 2x. When you load the PDF, WatchKit automatically scales the image based on the device’s screen size, using the values shown below:

| Screen size | Image scale |
| --- | --- |
| 38mm | 90% |
| 40mm | 100% |
| 41mm | 106% |
| 42mm | 100% |
| 44mm | 110% |
| 45mm | 119% |
| 49mm | 119% |

---

## In-app purchase

Full page: `references/in-app-purchase.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/in-app-purchase

The sign-up screen in your watchOS app needs to display the same set of information about your subscription options that you display in other versions of your app. For the complete list of required items, see [Making signup effortless](https://developer.apple.com/design/human-interface-guidelines/in-app-purchase#Making-signup-effortless). The following guidelines can help you design a sign-up screen that feels at home on Apple Watch.

**Clearly describe the differences between versions of your app that run on different devices.** If your watchOS app supports different functionality or provides a subset of the content that’s available on other devices, be sure to clarify these differences in your description. Be straightforward about the advantages of accessing subscription content through your watchOS app without implying that the experience is identical to the ones in other versions of your app.

![A screenshot of an app running on Apple Watch. The screen includes text that reads: Intrepid Pro. Unlock 90,000 topographic maps, advanced GPS features, and offline access for trail guidance anywhere. A Close button appears in the top-left corner of the screen.](https://docs-assets.developer.apple.com/published/00bc22f23ed8cc2eb6be337decc3af7b/clarify-description-before%402x.png)

![A screenshot of an app running on Apple Watch. The screen includes text that reads: Intrepid Pro. Use advanced GPS features for trail guidance on Apple Watch. Unlock 90,000 topographic maps for use on iPhone and other devices. A Close button appears in the top-left corner of the screen.](https://docs-assets.developer.apple.com/published/ee0a650637153e7fd6506555082cca8c/clarify-description-after%402x.png)

**Consider using a modal sheet to display the required information.** After people respond to your call to action to learn more about your subscription offers, you can use a modal sheet to present all required items in a single view. Even though people must scroll the view to access all the information, displaying it in a modal sheet helps your app UI remain streamlined and concise. Also, a modal sheet’s default Close button makes it easy for people to return to your free content with one tap. If you create a custom sign-up view instead of using a modal sheet, design a complete, efficient flow and include a Close or Cancel button that lets people return to your free content.

**Make subscription options easy to compare on a small screen.** People need to understand the terms of each subscription option before they can choose one. Aim to display the duration and discount information for each option in a compact way that’s easy to scan and compare. Here are two ways you might present subscription options in your watchOS app:

- Display each option in a separate button. Using one button per payment option lets people start the signup process with one tap. In this design, it’s important to lock up each button with its description so that people can see how these elements are related, especially while scrolling.
- Display a list of options, followed by a button people tap to start the signup process. Using a list to display one option per row gives you a compact design that minimizes scrolling while making subscription choices easy to scan and understand. In this design, the button’s title can update to reflect the chosen option.

![A screenshot of an app running on Apple Watch. The screen includes two subscription buttons: $4.99 per month and $29.99 per year. A Close button appears in the top-left corner of the screen.](https://docs-assets.developer.apple.com/published/d1beed8e9dddac07a14bd09ed184a984/lock-up-option-information%402x.png)

![A screenshot of an app running on Apple Watch. The screen includes a list of subscription options: $4.99 billed monthly and $29.99 billed yearly. The $29.99 option is selected. A $29.99 per year button appears at the bottom of the screen, and a Close button appears in the top-left corner of the screen.](https://docs-assets.developer.apple.com/published/2c6e9ab3b201604f462d49cbd3473813/list-option-information%402x.png)

---

## Labels

Full page: `references/labels.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/labels

Date and time text components (shown below on the left) display the current date, the current time, or a combination of both. You can configure a date text component to use a variety of formats, calendars, and time zones. A countdown timer text component (shown below on the right) displays a precise countdown or count-up timer. You can configure a timer text component to display its count value in a variety of formats.

![An illustration of date and time text components on Apple Watch, with the date aligned to the leading edge and the time aligned to the trailing edge.](https://docs-assets.developer.apple.com/published/3cedf27f398b6683c78d37a325f26c33/labels-date-time-text-component%402x.png)

![An illustration of a countdown timer text component on Apple Watch, with the time value at the center.](https://docs-assets.developer.apple.com/published/bc3014364c7bc508ff68d21d79c15441/labels-countdown-timer-text-component%402x.png)

When you use the system-provided date and timer text components, watchOS automatically adjusts the label’s presentation to fit the available space. The system also updates the content without further input from your app.

Consider using date and timer components in complications. For design guidance, see [Complications](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications); for developer guidance, see [Text](https://developer.apple.com/documentation/SwiftUI/Text).

---

## Layout

Full page: `references/layout.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/layout

**Design your content to extend from one edge of the screen to the other.** The Apple Watch bezel provides a natural visual padding around your content. To avoid wasting valuable space, consider minimizing the padding between elements.

![An illustration of the Workout app’s main list of workouts on Apple Watch. A callout indicates that the currently focused workout item spans the full width of the available screen area.](https://docs-assets.developer.apple.com/published/9b9b27a4e9e752fc4ed6be98f5eb5b0d/layout-full-width%402x.png)

**Avoid placing more than two or three controls side by side in your interface.** As a general rule, display no more than three buttons that contain glyphs — or two buttons that contain text — in a row. Although it’s usually better to let text buttons span the full width of the screen, two side-by-side buttons with short text labels can also work well, as long as the screen doesn’t scroll.

![A diagram of an Apple Watch screen showing two side-by-side buttons beneath three lines of text.](https://docs-assets.developer.apple.com/published/25c5882538789bded5a9953eb5e2001f/layout-controls%402x.png)

**Support autorotation in views people might want to show others.** When people flip their wrist away, apps typically respond to the motion by sleeping the display, but in some cases it makes sense to autorotate the content. For example, a wearer might want to show an image to a friend or display a QR code to a reader. For developer guidance, see [isAutorotating](https://developer.apple.com/documentation/WatchKit/WKExtension/isAutorotating).

---

## Lists and tables

Full page: `references/lists-and-tables.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/lists-and-tables

**When possible, limit the number of rows.** Short lists are easier for people to scan, but sometimes people expect a long list of items. For example, if people subscribe to a large number of podcasts, they might think something’s wrong if they can’t view all their items. You can help make a long list more manageable by listing the most relevant items and providing a way for people to view more.

**Constrain the length of detail views if you want to support vertical page-based navigation.** People use vertical page-based navigation to swipe vertically among the detail items of different list rows. Navigating in this way saves time because people don’t need to return to the list to tap a new detail item, but it works only when detail views are short. If your detail views scroll, people won’t be able to use vertical page-based navigation to swipe among them.

---

## Live Activities

Full page: `references/live-activities.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/live-activities

When a Live Activity begins on iPhone, it appears on a paired Apple Watch at the top of the Smart Stack. By default, the view displayed in the Smart Stack combines the leading and trailing elements from the Live Activity’s compact presentation on iPhone.

If you offer a watchOS app and someone taps the Live Activity in the Smart Stack, it opens your watchOS app. Without a watchOS app, tapping opens a full-screen view with a button to open your app on the paired iPhone.

**Consider creating a custom watchOS layout.** While the system provides a default view automatically, a custom layout designed for Apple Watch can show more information and add interactive functionality like a button or toggle.

**Carefully consider including buttons or toggles in your custom layout.** The custom watchOS layout also applies to your Live Activity in CarPlay where the system deactivates interactive elements. If people are likely to start or observe your Live Activity while driving, don’t include buttons or toggles in your custom watchOS layout. For developer guidance, see [Creating custom views for Live Activities](https://developer.apple.com/documentation/ActivityKit/creating-custom-views-for-live-activities).

![An illustration that shows the compact presentation of a Live Activity in the Dynamic Island on iPhone.](https://docs-assets.developer.apple.com/published/31abf69a42e7760de80d1c165f9c52c0/live-activities-ios-dynamic-island-default%402x.png)

![An illustration that shows the automatically generated default presentation of a Live Activity in a Smart Stack view, with the leading and trailing elements from the iPhone compact view spaced apart in the lower corners.](https://docs-assets.developer.apple.com/published/1da35f7f7a09e0cf450303920f79a119/live-activity-watch-default-implementation%402x.png)

![An illustration that shows a custom presentation of a Live Activity in a Smart Stack view, with a balanced design that shows a graphical countdown timer balanced with explanatory text.](https://docs-assets.developer.apple.com/published/ed2be6ed02a8b095a9737a9c40eb3c9f/live-activity-watch-custom-implementation%402x.png)

**Focus on essential information and significant updates.** Use space in the Smart Stack as efficiently as possible and think of the most useful information that a Live Activity can convey:

- Progress, like the estimated arrival time of a delivery
- Interactive elements, like stopwatch or timer controls
- Significant updates, like sports score changes

---

## Loading

Full page: `references/loading.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/loading

**As much as possible, avoid showing a loading indicator in your watchOS experience.** People expect quick interactions with their Apple Watch, so aim to display content immediately. In situations where content needs a second or two to load, it’s better to display a loading indicator than a blank screen.

---

## Managing accounts

Full page: `references/managing-accounts.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/managing-accounts

Use iCloud synchronization to provide access to the Keychain, letting people autofill user names and passwords and preserve app settings.

---

## Managing notifications

Full page: `references/managing-notifications.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/managing-notifications

By default, the notification settings people use for apps on their iPhone apply to the same apps on their Apple Watch. People can manage these settings in the Apple Watch app on iPhone, or they can access per-notification options — such as Mute 1 Hour or Turn off Time Sensitive — by swiping left when a notification arrives on their Apple Watch.

---

## Maps

Full page: `references/maps.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/maps

On Apple Watch, maps are static snapshots of geographic locations. Place a map in your interface at design time and show the appropriate region at runtime. The displayed region isn’t interactive; tapping it opens the Maps app on Apple Watch. You can add up to five annotations to a map to highlight points of interest or other relevant information. For developer guidance, see [WKInterfaceMap](https://developer.apple.com/documentation/WatchKit/WKInterfaceMap).

![A screenshot of a map on Apple Watch, displaying Apple Park and some of the surrounding area.](https://docs-assets.developer.apple.com/published/befea7e8b96bc123bfef582ba3857d64/maps-watch1%402x.png)

**Fit the map interface element to the screen.** The entire element needs to be visible on the Apple Watch display without requiring scrolling.

**Show the smallest region that encompasses the points of interest.** The content within a map interface element doesn’t scroll, so all key content must be visible within the displayed region.

For developer guidance, see [WKInterfaceMap](https://developer.apple.com/documentation/WatchKit/WKInterfaceMap).

---

## Materials

Full page: `references/materials.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/materials

**Use materials to provide context in a full-screen modal view.** Because full-screen modal views are common in watchOS, the contrast provided by material layers can help orient people in your app and distinguish controls and system elements from other content. Avoid removing or replacing material backgrounds for modal sheets when they’re provided by default.

![An illustration of a modal view in watchOS with an example title, descriptive text, and a single action button. The modal completely covers the screen with a transparent material, and uses a thinner material for the button along with vibrant label text.](https://docs-assets.developer.apple.com/published/07e5fe8350a946dbc2ed1610f722ce61/watchos-modal-view-material-background%402x.png)

---

## Motion

Full page: `references/motion.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/motion

SwiftUI provides a powerful and streamlined way to add motion to your app. If you need to use WatchKit to animate layout and appearance changes — or create animated image sequences — see [WKInterfaceImage](https://developer.apple.com/documentation/WatchKit/WKInterfaceImage#1652345).

> **Note:** All layout- and appearance-based animations automatically include built-in easing that plays at the start and end of the animation. You can’t turn off or customize easing.

---

## Nearby interactions

Full page: `references/nearby-interactions.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/nearby-interactions

On Apple Watch, Nearby Interaction APIs provide a peer device’s distance. Also, all watchOS apps participating in a nearby interaction experience must be in the foreground.

---

## Notifications

Full page: `references/notifications.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/notifications

On Apple Watch, notifications occur in two stages: *short look* and *long look*. People can also view notifications in Notification Center. On supported devices, people can double-tap to respond to notifications.

You can help people have a great notification experience by designing app-specific assets and actions that are relevant on Apple Watch. If your watchOS app has an iPhone companion that supports notifications, watchOS can automatically provide default short-look and long-look interfaces if necessary.

#### Short looks

A short look appears when the wearer’s wrist is raised and disappears when it’s lowered.

![An illustration that represents a short look notification from a generic app. It includes a large primary image in the center, a title, and a short preview of the notification content.](https://docs-assets.developer.apple.com/published/609f4ae816d78b5c87a340416f4874a9/notifications-short-looks%402x.png)

**Avoid using a short look as the only way to communicate important information.** A short look appears only briefly, giving people just enough time to see what the notification is about and which app sent it. If your notification information is critical, make sure you deliver it in other ways, too.

**Keep privacy in mind.** Short looks are intended to be discreet, so it’s important to provide only basic information. Avoid including potentially sensitive information in the notification’s title.

#### Long looks

Long looks provide more detail about a notification. If necessary, people can swipe vertically or use the Digital Crown to scroll a long look. After viewing a long look, people can dismiss it by tapping it or simply by lowering their wrist.

![An illustration that represents a long look notification from a generic app. It includes a small primary image in the upper left corner, badging a platter with the notification title and content. Beneath the notification are two full width action buttons, the second of which extends off the screen to indicate that the view is scrollable.](https://docs-assets.developer.apple.com/published/a48f434c960e0f14429018803ee4b180/notifications-long-looks%402x.png)

A custom long-look interface can be static or dynamic. The *static* interface lets you display a notification’s message along with additional static text and images. The *dynamic* interface gives you access to the notification’s full content and offers more options for configuring the appearance of the interface.

You can customize the content area for both static and dynamic long looks, but you can’t change the overall structure of the interface. The system-defined structure includes a *sash* at the top of the interface and a Dismiss button at the bottom, below all custom buttons.

**Consider using a rich, custom long-look notification to let people get the information they need without launching your app.** You can use SwiftUI [Animations](https://developer.apple.com/documentation/SwiftUI/Animations) to create engaging, interruptible animations; alternatively, you can use [SpriteKit](https://developer.apple.com/documentation/SpriteKit) or [SceneKit](https://developer.apple.com/documentation/SceneKit).

**At the minimum, provide a static interface; prefer providing a dynamic interface too.** The system defaults to the static interface when the dynamic interface is unavailable, such as when there is no network or the iPhone companion app is unreachable. Be sure to create the resources for your static interface in advance and package them with your app.

**Choose a background appearance for the sash.** The system-provided sash, at the top of the long-look interface, displays your app icon and name. You can customize the sash’s color or give it a blurred appearance. If you display a photo at the top of the content area, you’ll probably want to use the blurred sash, which has a light, translucent appearance that gives the illusion of overlapping the image.

**Choose a background color for the content area.** By default, the long look’s background is transparent. If you want to match the background color of other system notifications, use white with 18% opacity; otherwise, you can use a custom color, such as a color within your brand’s palette.

**Provide up to four custom actions below the content area.** For each long look, the system uses the notification’s type to determine which of your custom actions to display as buttons in the notification UI. In addition, the system always displays a Dismiss button at the bottom of the long-look interface, below all custom buttons. If your watchOS app has an iPhone companion that supports notifications, the system shares the actionable notification types already registered by your iPhone app and uses them to configure your custom action buttons.

#### Double tap

People can double-tap to respond to notifications on supported devices. When a person responds to a notification with a double tap, the system selects the first nondestructive action as the response.

**Keep double tap in mind when choosing the order of custom actions you present as responses to a notification.** Because a double tap runs the first nondestructive action, consider placing the action that people use most frequently at the top of the list. For example, a parking app that provides custom actions for extending the time on a paid parking spot could offer options to extend the time by 5 minutes, 15 minutes, or an hour, with the most common choice listed first.

---

## Page controls

Full page: `references/page-controls.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/page-controls

In watchOS, page controls can be displayed at the bottom of the screen for horizontal pagination, or next to the Digital Crown when presenting a vertical [tab view](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views). When using vertical tab views, the page indicator shows people where they are in the navigation, both within the current page and within the set of pages. The page control transitions between scrolling through a page’s content and scrolling to other pages.

![An illustration representing a screen that includes a vertical tab view on Apple Watch. A page control next to the Digital Crown shows that the fourth tab is currently selected.](https://docs-assets.developer.apple.com/published/13d0909bd0df2e26693f76b6bfbcd428/page-controls-watch-vertical%402x.png)

![An illustration representing a screen that includes a horizontal tab view on Apple Watch. A page control at the bottom shows that the second tab is currently selected.](https://docs-assets.developer.apple.com/published/0f915ec7b0e8755a2d60845617746f71/page-controls-watch-horizontal%402x.png)

**Use vertical pagination to separate multiple views into distinct, purposeful pages.** Give each page a clear purpose, and let people scroll through the pages using the Digital Crown. In watchOS, this design is more effective than horizontal pagination or many levels of hierarchical navigation.

**Consider limiting the content of an individual page to a single screen height.** Embracing this constraint encourages each page to serve a clear and distinct purpose and results in a more glanceable design. Use variable-height pages judiciously and, if possible, only place them after fixed-height pages in your app design.

---

## Pickers

Full page: `references/pickers.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/pickers

Pickers display lists of items that people navigate using the Digital Crown, which helps people manage selections in a precise and engaging way.

A picker can display a list of items using the wheels style. watchOS can also display date and time pickers using the wheels style. For developer guidance, see [Picker](https://developer.apple.com/documentation/SwiftUI/Picker) and [DatePicker](https://developer.apple.com/documentation/SwiftUI/DatePicker).

![An illustration representing a screen containing a picker view on Apple Watch, showing three items in a list. The center item is highlighted.](https://docs-assets.developer.apple.com/published/3324da7e747432a1e22d847d45b4430d/pickers-wheel-watch%402x.png)

![An illustration representing a screen containing a date picker on Apple Watch, with the day highlighted.](https://docs-assets.developer.apple.com/published/e2c5c57649b0b94a5a0319688f300cd0/pickers-date-watch%402x.png)

![An illustration representing a screen containing a time picker on Apple Watch, with the minutes highlighted.](https://docs-assets.developer.apple.com/published/1b10bb28a6101999c45dc2aca39bba32/pickers-time-watch%402x.png)

You can configure a picker to display an outline, caption, and scrolling indicator.

For longer lists, the navigation link displays the picker as a button. When someone taps the button, the system shows the list of options. The person can also scrub through the options using the Digital Crown without tapping the button. For developer guidance, see [navigationLink](https://developer.apple.com/documentation/SwiftUI/PickerStyle/navigationLink).

![An illustration representing a screen that contains a picker button on Apple Watch. The button’s text denotes that the second item is selected.](https://docs-assets.developer.apple.com/published/21fcdd5021089b020137dd099821dc85/pickers-navigation-button-watch%402x.png)

![An illustration representing a screen showing a list of items on Apple Watch. The second item in the list is selected.](https://docs-assets.developer.apple.com/published/f56f12978536df47dc0a7f67e3f0a686/pickers-navigation-list-watch%402x.png)

---

## Playing audio

Full page: `references/playing-audio.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/playing-audio

In watchOS, the system manages audio playback. An app can play short audio clips while it’s active and running in the foreground, or it can play longer audio that continues even when people lower their wrist or switch to another app. For developer guidance, see [Playing Background Audio](https://developer.apple.com/documentation/WatchKit/playing-background-audio).

**Use the recommended encoding values for media assets.** Specifically, use the 64 kbps HE-AAC (High-Efficiency Advanced Audio Coding) format to produce good-quality audio with lower data requirements.

**Consider** **presenting a Now Playing view so people can control current or recently played audio without leaving your app.** The system-provided Now Playing view also displays information about the current audio source — which might be another app on a person’s Apple Watch or iPhone — and automatically selects the current or most recently used source. For developer guidance, see [Adding a Now Playing View](https://developer.apple.com/documentation/WatchKit/adding-a-now-playing-view).

---

## Playing haptics

Full page: `references/playing-haptics.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/playing-haptics

Apple Watch Series 4 and later provides haptic feedback for the Digital Crown, which gives people a more tactile experience as they scroll through content. By default, the system provides linear haptic detents that people can feel as they rotate the Digital Crown. Some system controls, like table views, provide detents as new items scroll onto the screen. For developer guidance, see [WKHapticType](https://developer.apple.com/documentation/WatchKit/WKHapticType).

watchOS defines the following set of haptics, each of which conveys a specific meaning to people.

---

## Playing video

Full page: `references/playing-video.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/playing-video

In watchOS, the system manages video playback. Apps can play short video clips while the app is active and running in the foreground. You can use a movie element to embed clips in your interface and play video inline, or you can play a clip in a separate interface. For developer guidance, see [VideoPlayer](https://developer.apple.com/documentation/AVKit/VideoPlayer).

**Keep video clips short.** Prefer shorter clips of no longer than 30 seconds. Long clips consume more disk space and require people to keep their wrists raised for longer periods of time, which can cause fatigue.

**Use the recommended sizes and encoding values for media assets.** In particular, avoid scaling video clips, which affects performance and results in a suboptimal appearance. The following table lists the recommended encoding and resolution values for video assets. The audio encoding values apply to both movies and audio-only assets.

| Attribute | Value |
| --- | --- |
| Video codec | H.264 High Profile |
| Video bit rate | 160 kbps at up to 30 fps |
| Resolution (full screen) | 208x260 px (portrait orientation) |
| Resolution (16:9) | 320x180 px (landscape orientation) |
| Audio | 64 kbps HE-AAC |

**Avoid creating a poster image that looks like a system control.** You want people to understand that they can tap a movie element for playback; you don’t want to confuse people by making movie elements look like something else.

**Consider creating a poster image that represents a video clip’s contents.** When people tap a poster image, the system replaces the image with the video and begins inline playback. A relevant poster image can help people make an informed decision about whether to view the video. In general, avoid creating a poster image that has nothing to do with the content or that people might mistake for a control.

---

## Progress indicators

Full page: `references/progress-indicators.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/progress-indicators

By default the system displays the progress indicators in white over the scene’s background color. You can change the color of the progress indicator by setting its tint color.

![An image of a progress bar filling from left to right in watchOS.](https://docs-assets.developer.apple.com/published/33bbf8ea9d047a5933e60cb120d3556e/progress-bar-watch%402x.png)

![An image of a circular progress indicator filling clockwise in watchOS.](https://docs-assets.developer.apple.com/published/95240440cd8d1384c68b146aad1912b0/progress-ring-watch%402x.png)

![An image of a spinning activity indicator in watchOS.](https://docs-assets.developer.apple.com/published/02a8427a04f946d9b80d2907f84ab365/activity-indicators-watch%402x.png)

---

## Scroll views

Full page: `references/scroll-views.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/scroll-views

**Prefer vertically scrolling content.** People are accustomed to using the Digital Crown to navigate to and within apps on Apple Watch. If your app contains a single list or content view, rotating the Digital Crown scrolls vertically when your app’s content is taller than the height of the display.

**Use tab views to provide page-by-page scrolling.** watchOS displays tab views as pages. If you place tab views in a vertical stack, people can rotate the Digital Crown to move vertically through full-screen pages of content. In this scenario, the system displays a page indicator next to the Digital Crown that shows people where they are in the content, both within the current page and within a set of pages. For guidance, see [Tab views](https://developer.apple.com/design/human-interface-guidelines/tab-views).

**When displaying paged content, consider limiting the content of an individual page to a single screen height.** Embracing this constraint clarifies the purpose of each page, helping you create a more glanceable design. However, if your app has long pages, people can still use the Digital Crown both to navigate between shorter pages and to scroll content in a longer page because the page indicator expands into a scroll indicator when necessary. Use variable-height pages judiciously and place them after fixed-height pages when possible.

---

## Search fields

Full page: `references/search-fields.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/search-fields

When someone taps the search field, the system displays a text-input control that covers the entire screen. The app only returns to the search field after they tap the Cancel or Search button.

---

## Settings

Full page: `references/settings.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/settings

In watchOS, apps and games don’t add custom settings to the system-provided Settings app. As an alternative, consider making a small number of essential options available at the bottom of the main view or letting people use a More menu to reconfigure objects.

---

## Sheets

Full page: `references/sheets.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/sheets

In watchOS, a sheet is a full-screen view that slides over your app’s current content. The sheet is semitransparent to help maintain the current context, but the system applies a material to the background that blurs and desaturates the covered content.

![A screenshot of a sheet with a primary Action button and a default cancel button on Apple Watch.](https://docs-assets.developer.apple.com/published/15674b58cf1c9bb5e1e4e8fac1a618a7/sheets-watch-overlay%402x.png)

**Use a sheet only when your modal task requires a custom title or custom content presentation.** If you need to give people important information or present a set of choices, consider using an [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) or [Action sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets).

**Keep sheet interactions brief and occasional.** Use a sheet only as a temporary interruption to the current workflow, and only to facilitate an important task. Avoid using a sheet to help people navigate your app’s content.

**If you change the default label, prefer using SF Symbols to represent the action.** Avoid using a label that might mislead people into thinking that the sheet is part of a hierarchical navigation interface. Also, if the text in the top-leading corner looks like a page or app title, people won’t know how to dismiss the sheet. For guidance, see [Standard icons](https://developer.apple.com/design/human-interface-guidelines/icons#Standard-icons).

![A screenshot that shows a top toolbar with a custom Back button at the top of the screen on Apple Watch.](https://docs-assets.developer.apple.com/published/e8e05be419a7f0eaf6c07b3422bd7633/modal-sheet-watchos-do-not-1%402x.png)

![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![A screenshot that shows a top toolbar with a button with the words Page title at the top of the screen on Apple Watch.](https://docs-assets.developer.apple.com/published/df489a7dc08d52f019cefc9947a77a3d/modal-sheet-watchos-do-not-2%402x.png)

![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![A screenshot that shows a top toolbar with the default Cancel button at the top of the screen on Apple Watch.](https://docs-assets.developer.apple.com/published/6ec716274495aca4317edebfded64504/modal-sheet-watchos-do%402x.png)

![A checkmark in a circle to indicate correct usage.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

---

## Sliders

Full page: `references/sliders.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/sliders

A slider is a horizontal track — appearing as a set of discrete steps or as a continuous bar — that represents a finite range of values. People can tap buttons on the sides of the slider to increase or decrease its value by a predefined amount.

![An illustration of a watchOS volume slider with discrete steps. The first two of three steps are filled with a green highlight color, indicating the volume level.](https://docs-assets.developer.apple.com/published/3acc4339289d9cf65ec982e73f950f97/sliders-watchos-discrete%402x.png)

![An illustration of a watchOS volume slider with a continuous bar. Two-thirds of the bar is filled with a green highlight color, indicating the volume level.](https://docs-assets.developer.apple.com/published/b356f0616bad32afce9ac9e62763414b/sliders-watchos-continuous%402x.png)

**If necessary, create custom glyphs to communicate what the slider does.** The system displays plus and minus signs by default.

---

## Split views

Full page: `references/split-views.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/split-views

In watchOS, the split view displays either the list view or a detail view as a full-screen view.

**Automatically display the most relevant detail view.** When your app launches, show people the most pertinent information. For example, display information relevant to their location, the time, or their recent actions.

**If your app displays multiple detail pages, place the detail views in a vertical [Tab views](https://developer.apple.com/design/human-interface-guidelines/tab-views).** People can then use the Digital Crown to scroll between the detail view’s tabs. watchOS also displays a page indicator next to the Digital Crown, indicating the number of tabs and the currently selected tab.

![A screenshot showing a detail view with a vertical tab on Apple Watch. The page indicator next to the Digital Crown shows that the fifth tab is currently selected.](https://docs-assets.developer.apple.com/published/3f36258648d54880e800568e88b5076b/split-view-watch-vertical-tab%402x.png)

---

## Tab views

Full page: `references/tab-views.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/tab-views

watchOS displays tab views using [page controls](https://developer.apple.com/design/human-interface-guidelines/components/presentation/page-controls). For developer guidance, see [TabView](https://developer.apple.com/documentation/SwiftUI/TabView).

![An illustration showing the page control next to the Digital Crown on Apple Watch. The current dot is enlarged, indicating that people can scroll through the current content, as well as scroll between pages.](https://docs-assets.developer.apple.com/published/c65574d8caec7a02132f9beeee66b84f/tab-view-watch-vertical%402x.png)

---

## Text fields

Full page: `references/text-fields.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/text-fields

**Present a text field only when necessary.** Whenever possible, prefer displaying a list of options rather than requiring text entry.

---

## Toolbars

Full page: `references/toolbars.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/toolbars

A toolbar button lets you offer important app functionality in a view that displays related content. You can place toolbar buttons in the top corners or along the bottom. If you place these buttons above scrolling content, the buttons always remain visible, as the content scrolls under them.

![A screenshot showing toolbar buttons in the top leading and trailing corners.](https://docs-assets.developer.apple.com/published/25237597303b13745dae4aefbb637a69/toolbars-watch-top-buttons%402x.png)

![A screenshot showing two toolbar buttons in the bottom leading and trailing corners.](https://docs-assets.developer.apple.com/published/244872b6e6e536c6607ea2383c7b73d2/toolbars-watch-bottom-buttons%402x.png)

For developer guidance, see [topBarLeading](https://developer.apple.com/documentation/SwiftUI/ToolbarItemPlacement/topBarLeading), [topBarTrailing](https://developer.apple.com/documentation/SwiftUI/ToolbarItemPlacement/topBarTrailing), or [bottomBar](https://developer.apple.com/documentation/SwiftUI/ToolbarItemPlacement/bottomBar).

You can also place a button in the scrolling view. By default, a scrolling toolbar button remains hidden until people reveal it by scrolling up. People frequently scroll to the top of a scrolling view, so discovering a toolbar button is automatic.

![A screenshot showing two toolbar buttons in the top leading and trailing corners. The toolbar also has a primary action button in the scroll view, but it's hidden.](https://docs-assets.developer.apple.com/published/7fcd92c8f2a6ff666062c610c595bd48/toolbars-watch-primary-button-hidden%402x.png)

![A screenshot showing two toolbar buttons in the top leading and trailing corners. The toolbar also displays a primary action button in the scroll view.](https://docs-assets.developer.apple.com/published/6188e8ce88dd4fff8384b99a2641f0df/toolbars-watch-primary-button-visible%402x.png)

For developer guidance, see [primaryAction](https://developer.apple.com/documentation/SwiftUI/ToolbarItemPlacement/primaryAction).

**Use a scrolling toolbar button for an important action that isn’t a primary app function.** A toolbar button gives you the flexibility to offer important functionality in a view whose primary purpose is related to that functionality, but may not be the same. For example, Mail provides the essential New Message action in a toolbar button at the top of the Inbox view. The primary purpose of the Inbox is to display a scrollable list of email messages, so it makes sense to offer the closely related compose action in a toolbar button at the top of the view.

---

## Typography

Full page: `references/typography.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/typography

SF Compact is the system font in watchOS, and apps can also use NY. In complications, watchOS uses SF Compact Rounded.

---

## Virtual keyboards

Full page: `references/virtual-keyboards.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards

On Apple Watch, a text field can show a keyboard if the device screen is large enough. Otherwise, the system lets people use dictation or Scribble to enter information. You can’t change the keyboard type in watchOS, but you can set the content type of the text field. The system uses this information to make text entry easier, such as by offering suggestions. For developer guidance, see [textContentType(_:)](https://developer.apple.com/documentation/SwiftUI/View/textContentType(_:)) (SwiftUI).

People can also use a nearby paired iPhone to enter text on Apple Watch.

---

## Wallet

Full page: `references/wallet.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/wallet

On Apple Watch, Wallet displays passes in a scrolling carousel of cards. People can add your pass to their Apple Watch even if you don’t create a watch-specific app, so it’s important to understand how your pass can look on the device.

![A screenshot of a selected flight pass in a list of passes on Apple Watch. The pass includes information about a flight from SFO to LGA. The next pass in the list is a gym membership card with a barcode.](https://docs-assets.developer.apple.com/published/9b54ebf2a350a1e748a38c0b2cc3b74a/watch-card-and-details%402x.png)

People can tap a pass on their Apple Watch to reveal a details screen that displays additional information in a scroll view. In some cases, people can also tap a specific transaction to get more information.

![A screenshot of a flight pass on Apple Watch. The pass includes information about a flight from SFO to LGA, and appears above a QR code.](https://docs-assets.developer.apple.com/published/0f74b7b757684a79981367adf14d6adb/watch-pass-design-intro%402x.png)

Each pass style specifies the fields and images that can appear in the basic layout areas shown below:

![A diagram that shows the basic layout of a pass on Apple Watch. A top row contains a logo image and an essential field area. A second row contains a primary field area. A third row contains a secondary and auxiliary fields area.](https://docs-assets.developer.apple.com/published/063f7297022ac58ae52b2b9fa2f0121d/watch-layout-diagram%402x.png)

If some information doesn’t fit within the layout areas, the system displays it in the scrolling details screen.

> **Important:** In every style, watchOS crops the strip image to fit the aspect ratio of the card interface and may crop white space from other images.

---

## Widgets

Full page: `references/widgets.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/widgets

**Provide a colorful background that conveys meaning.** By default, widgets in the Smart Stack use a black background. Consider using a custom background color that provides additional meaning. For example, the Stocks app uses a red background for falling stock values and a green background if a stock’s value rises.

**Encourage the system to display or elevate the position of your watchOS widget in the Smart Stack.** Relevancy information helps the system show your widget when people need it most. Relevance can be location-based or specific to ongoing system actions, like a workout. For developer guidance, see [RelevanceKit](https://developer.apple.com/documentation/RelevanceKit).

---
