# iOS-specific guidance, collected

Every place the HIG states a rule specific to iOS, lifted from the page it lives on. Sections appear alphabetically by page.

A heading like `### iOS, iPadOS` upstream means the rule is shared; it's reproduced here in full so you don't have to go looking. Each entry links to the complete page, which also carries the cross-platform guidance this file deliberately omits.

---

## Action button

Full page: `references/action-button.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/action-button

**Let people use your actions without leaving their current context.** When possible, make use of lightweight multitasking capabilities like [Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities) and custom snippets to provide functionality without opening your app. For example, the “Set Timer” action doesn’t launch the Clock app; it prompts people to set a duration for the timer, and then launches a Live Activity with the countdown.

---

## Action sheets

Full page: `references/action-sheets.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/action-sheets

*(upstream heading: iOS, iPadOS)*

**Use an action sheet — not a menu — to provide choices related to an action.** People are accustomed to having an action sheet appear when they perform an action that might require clarifying choices. In contrast, people expect a menu to appear when they choose to reveal it.

**Avoid letting an action sheet scroll.** The more buttons an action sheet has, the more time and effort it takes for people to make a choice. Also, scrolling an action sheet can be hard to do without inadvertently tapping a button.

---

## Activity rings

Full page: `references/activity-rings.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/activity-rings

Activity rings are available in iOS with [HKActivityRingView](https://developer.apple.com/documentation/HealthKitUI/HKActivityRingView). The appearance of the Activity ring element changes automatically depending on whether an Apple Watch is paired:

- With an Apple Watch paired, iOS shows all three Activity rings.
- Without an Apple Watch paired, iOS shows the Move ring only, which represents an approximation of a person’s activity based on their steps and workout information from other apps.

![A screenshot of the Activity summary in the iOS Fitness app with Apple Watch paired. All three Activity rings are displayed.](https://docs-assets.developer.apple.com/published/47867ef56f48e103ecb03751a2e2faae/activity-rings-watch-paired%402x.png)

![A screenshot of the Activity summary in the iOS Fitness app with no Apple Watch paired. Only the Move ring is displayed.](https://docs-assets.developer.apple.com/published/25295e1487dbbb86501d5afbe8c94274/activity-rings-no-watch-paired%402x.png)

Because iOS shows Activity rings whether or not an Apple Watch is paired, activity history can include a combination of both styles. For example, Activity rings in Fitness have three rings when a person exercises with their Apple Watch paired, and only the Move ring when they exercise without their Apple Watch.

---

## Alerts

Full page: `references/alerts.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/alerts

*(upstream heading: iOS, iPadOS)*

**Use an action sheet — not an alert — to offer choices related to an intentional action.** For example, when people cancel the Mail message they’re editing, an action sheet provides three choices: delete the edits (or the entire draft), save the draft, or return to editing. Although an alert can also help people confirm or cancel an action that has destructive consequences, it doesn’t provide additional choices related to the action. For guidance, see [Action sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets).

**When possible, avoid displaying an alert that scrolls.** Although an alert might scroll if the text size is large enough, be sure to minimize the potential for scrolling by keeping alert titles short and including a brief message only when necessary.

---

## App Shortcuts

Full page: `references/app-shortcuts.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/app-shortcuts

*(upstream heading: iOS, iPadOS)*

App Shortcuts can appear in the Top Hit area of Spotlight when people search for your app, or in the Shortcuts area below. Each App Shortcut includes a symbol from [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) that you choose to represent its functionality, or a preview image of an item that the shortcut links to directly.

**Order shortcuts based on importance.** The order you choose determines how App Shortcuts initially appear in both Spotlight and the Shortcuts app, so it’s helpful to include the most generally useful ones first. Once people start using your App Shortcuts, the system updates to prioritize the ones they use most frequently.

---

## Boxes

Full page: `references/boxes.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/boxes

*(upstream heading: iOS, iPadOS)*

By default, iOS and iPadOS use the secondary and tertiary background [colors](https://developer.apple.com/design/human-interface-guidelines/color) in boxes.

---

## Buttons

Full page: `references/buttons.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/buttons

*(upstream heading: iOS, iPadOS)*

**Configure a button to display an activity indicator when you need to provide feedback about an action that doesn’t instantly complete.** Displaying an activity indicator within a button can save space in your user interface while clearly communicating the reason for the delay. To help clarify what’s happening, you can also configure the button to display a different label alongside the activity indicator. For example, the label “Checkout” could change to “Checking out…” while the activity indicator is visible. When a delay occurs after people click or tap your configured button, the system displays the activity indicator next to the original or alternative label, hiding the button image, if there is one.

![An illustration of a button labeled Checkout.](https://docs-assets.developer.apple.com/published/d03da7e4b2e307f2f115e04163b278f4/button-activity-indicator-hidden%402x.png)

![An illustration of a button labeled Checking out, with an activity indicator on the leading side of the label.](https://docs-assets.developer.apple.com/published/3b10cafeebf83689d3749708bdaeeea7/button-activity-indicator-visible%402x.png)

---

## Collections

Full page: `references/collections.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/collections

*(upstream heading: iOS, iPadOS)*

**Use caution when making dynamic layout changes.** The layout of a collection can change dynamically. Be sure any changes make sense and are easy to track. If possible, try to avoid changing the layout while people are viewing and interacting with it, unless it’s in response to an explicit action.

---

## Color

Full page: `references/color.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/color

*(upstream heading: iOS, iPadOS)*

iOS defines two sets of dynamic background colors — *system* and *grouped* — each of which contains primary, secondary, and tertiary variants that help you convey a hierarchy of information. In general, use the grouped background colors ([systemGroupedBackground](https://developer.apple.com/documentation/UIKit/UIColor/systemGroupedBackground), [secondarySystemGroupedBackground](https://developer.apple.com/documentation/UIKit/UIColor/secondarySystemGroupedBackground), and [tertiarySystemGroupedBackground](https://developer.apple.com/documentation/UIKit/UIColor/tertiarySystemGroupedBackground)) when you have a grouped table view; otherwise, use the system set of background colors ([systemBackground](https://developer.apple.com/documentation/UIKit/UIColor/systemBackground), [secondarySystemBackground](https://developer.apple.com/documentation/UIKit/UIColor/secondarySystemBackground), and [tertiarySystemBackground](https://developer.apple.com/documentation/UIKit/UIColor/tertiarySystemBackground)).

With both sets of background colors, you generally use the variants to indicate hierarchy in the following ways:

- Primary for the overall view
- Secondary for grouping content or elements within the overall view
- Tertiary for grouping content or elements within secondary elements

For foreground content, iOS defines the following dynamic colors:

| Color | Use for… | UIKit API |
| --- | --- | --- |
| Label | A text label that contains primary content. | [label](https://developer.apple.com/documentation/UIKit/UIColor/label) |
| Secondary label | A text label that contains secondary content. | [secondaryLabel](https://developer.apple.com/documentation/UIKit/UIColor/secondaryLabel) |
| Tertiary label | A text label that contains tertiary content. | [tertiaryLabel](https://developer.apple.com/documentation/UIKit/UIColor/tertiaryLabel) |
| Quaternary label | A text label that contains quaternary content. | [quaternaryLabel](https://developer.apple.com/documentation/UIKit/UIColor/quaternaryLabel) |
| Placeholder text | Placeholder text in controls or text views. | [placeholderText](https://developer.apple.com/documentation/UIKit/UIColor/placeholderText) |
| Separator | A separator that allows some underlying content to be visible. | [separator](https://developer.apple.com/documentation/UIKit/UIColor/separator) |
| Opaque separator | A separator that doesn’t allow any underlying content to be visible. | [opaqueSeparator](https://developer.apple.com/documentation/UIKit/UIColor/opaqueSeparator) |
| Link | Text that functions as a link. | [link](https://developer.apple.com/documentation/UIKit/UIColor/link) |

---

## Context menus

Full page: `references/context-menus.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/context-menus

*(upstream heading: iOS, iPadOS)*

**Provide either a context menu or an edit menu for an item, but not both.** If you provide both features for the same item, it can be confusing to people — and difficult for the system to detect their intent. See [Edit menus](https://developer.apple.com/design/human-interface-guidelines/edit-menus).

**In iPadOS, consider using a context menu to let people create a new object in your app.** iPadOS lets you reveal a context menu when people perform a long press on the touchscreen or use a secondary click with an attached trackpad or keyboard. For example, Files lets people create a new folder by revealing a context menu in an area between existing files and folders.

In iOS and iPadOS, a context menu can display a preview of the current content near the list of commands. People can choose a command in the menu or — in some cases — they can tap the preview to open it or drag it to another area.

**Prefer a graphical preview that clarifies the target of a context menu’s commands.** For example, when people reveal a context menu on a list item in Notes or Mail, the preview shows a condensed version of the actual content to help people confirm that they’re working with the item they intend.

**Ensure that your preview looks good as it animates.** As people reveal a context menu on an onscreen object, the system animates the preview image as it emerges from the content, dimming the screen behind the preview and the menu. It’s important to adjust the preview’s clipping path to match the shape of the preview image so that its contours, such as the rounded corners, don’t appear to change during animation. For developer guidance, see [UIContextMenuInteractionDelegate](https://developer.apple.com/documentation/UIKit/UIContextMenuInteractionDelegate).

---

## Dark Mode

Full page: `references/dark-mode.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/dark-mode

*(upstream heading: iOS, iPadOS)*

In Dark Mode, the system uses two sets of background colors — called *base* and *elevated* — to enhance the perception of depth when one dark interface is layered above another. The base colors are dimmer, making background interfaces appear to recede, and the elevated colors are brighter, making foreground interfaces appear to advance.

![A diagram that shows a stack of 4 terms on top of a black background. The term at the top shows the most contrast with the background and the term at the bottom shows the least.](https://docs-assets.developer.apple.com/published/0d71ac9f5186541dce35b5f702311bd0/base-with-four-semantic-colors%402x.png)

![A diagram that shows a stack of 4 terms on top of a nearly black background. The term at the top shows the most contrast with the background and the term at the bottom shows the least.](https://docs-assets.developer.apple.com/published/0dacc182adc819b08eb8cdcc897b08a4/elevated-with-four-semantic-colors%402x.png)

![A diagram that shows a stack of 4 terms on top of a white background. The term at the top shows the most contrast with the background and the term at the bottom shows the least.](https://docs-assets.developer.apple.com/published/cbbe9a39049fd3d3d2122876de64d207/light-with-four-semantic-colors%402x.png)

**Prefer the system background colors.** Dark Mode is dynamic, which means that the background color automatically changes from base to elevated when an interface is in the foreground, such as a popover or modal sheet. The system also uses the elevated background color to provide visual separation between apps in a multitasking environment and between windows in a multiple-window context. Using a custom background color can make it harder for people to perceive these system-provided visual distinctions.

---

## Disclosure controls

Full page: `references/disclosure-controls.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/disclosure-controls

*(upstream heading: iOS, iPadOS, visionOS)*

Disclosure controls are available in iOS, iPadOS, and visionOS with the SwiftUI [DisclosureGroup](https://developer.apple.com/documentation/SwiftUI/DisclosureGroup) view.

---

## Drag and drop

Full page: `references/drag-and-drop.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/drag-and-drop

*(upstream heading: iOS, iPadOS)*

**Let people perform multiple simultaneous drag activities.** In iPadOS, people can sequentially add items to an in-progress drag session, gathering as many items as their fingers can handle. For example, people can select an app icon on the Home Screen, start dragging it, and select additional app icons before dropping all of them in a different Home Screen or in a folder. To support this interaction, you need to let people add items during a drag — providing visual feedback through flocking — and accept multiple, simultaneous drops.

---

## Edit menus

Full page: `references/edit-menus.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/edit-menus

*(upstream heading: iOS, iPadOS)*

**Ensure your edit menu works well in both styles.** The system displays the compact, horizontal style when people use Multi-Touch gestures to reveal the edit menu, and the vertical style when people use a keyboard or pointing device to reveal it. For guidance using the vertical menu layout, see [iOS, iPadOS](https://developer.apple.com/design/human-interface-guidelines/menus#iOS-iPadOS).

**Adjust an edit menu’s placement, if necessary.** Depending on available space, the default menu position is above or below the insertion point or selection. The system also displays a visual indicator that points to the targeted content. Although you can’t change the shape of the menu or its pointer, you can change the menu’s position. For example, you might need to move the menu to prevent it from covering important content or parts of your interface.

---

## File management

Full page: `references/file-management.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/file-management

*(upstream heading: iOS, iPadOS)*

#### Document launcher

Starting in iOS 18 and iPadOS 18, document-based apps can use the system’s document launcher to give people a consistent, highly graphical way to browse, open, and create files. The document launcher presents a full-screen experience that highlights key elements of your app’s theme, while making it easy for people to create new documents. For developer guidance, see [DocumentGroupLaunchScene](https://developer.apple.com/documentation/SwiftUI/DocumentGroupLaunchScene).

The document launcher consists of three main parts:

- A *title card* that displays the app title and two app-specific buttons
- A background image that appears behind the title card and additional images — called *accessories* — that can appear around it
- A sheet that contains a file browser and optional app-specific controls

You can customize all three parts of the document launcher. Although the system automatically displays your app name in the title card, you specify the text and functions of the card’s primary and secondary buttons. You can also create a custom background image, one or more accessory images to surround the title card, and provide some custom controls that can appear in the file browser’s toolbar.

![A screenshot of a writing app's document launcher on iPad in landscape orientation. The document launcher displays a custom background and two accessory images. At the bottom, the file browser sheet provides 3 tabs: Recents, Shared, and Browse.](https://docs-assets.developer.apple.com/published/b0639d19130aedee8ab233cc0d0d111a/file-management-document-launcher%402x.png)

**Assign the title card’s buttons to your app’s most important functions.** The primary button typically creates a new document, and the secondary button can provide additional options. For example, the primary button in Numbers is Start Writing and the secondary button is Choose a Template.

**Provide a background that’s clearly distinct from the accessories and title card.** You can use a solid color, a gradient, or a pattern. Avoid including complex images or patterns that might distract from foreground elements.

**Be mindful of accessory placement.** For example, you can place accessories both in front of and behind the title card to create the appearance of depth, but you need to make sure that your app name and both buttons remain clearly visible. Avoid cluttering the title card with too many accessories, and be sure to test its overall appearance across the range of screen sizes and device orientations that you support.

**Use animation sparingly.** Too much motion on the display can confuse or disorient people. If you want to animate your accessories, consider creating gentle, repeating animations that subtly highlight and enhance your app’s content. For example, you might create an animation that makes an accessory appear to breathe or sway softly. For guidance, see [Motion](https://developer.apple.com/design/human-interface-guidelines/motion).

#### File provider app extension

If your app can share its files with other apps, you can create a file provider app extension that displays a custom interface for importing, exporting, opening, and moving your app’s documents. For developer guidance, see [File Provider](https://developer.apple.com/documentation/FileProvider). An *app extension* is code you provide that people can install and use to extend the functionality of a specific area of the system; to learn more, see [App extensions](https://developer.apple.com/app-extensions/).

**When someone uses your file provider extension to open or import documents, display only documents that are appropriate in the current context.** For example, if a PDF-editing app loads your extension, only list PDF files for opening or import. You might also want to display additional information, such as modification dates, sizes, and whether documents are local or remote.

**Let people select a destination when exporting and moving documents.** Unless your app stores documents in a single directory, let people navigate to a specific destination in your directory hierarchy. You could also provide a way to add new subdirectories.

**Avoid including a custom top toolbar.** Your extension loads within a modal view that already includes a toolbar. Providing a second toolbar is confusing and takes space away from your content.

Your app can also let people browse and open files from other apps. For developer guidance, see [Adding a document browser to your app](https://developer.apple.com/documentation/UIKit/adding-a-document-browser-to-your-app).

---

## Gestures

Full page: `references/gestures.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/gestures

*(upstream heading: iOS, iPadOS)*

In addition to the [Standard gestures](https://developer.apple.com/design/human-interface-guidelines/gestures#Standard-gestures) supported in all platforms, iOS and iPadOS support a few other gestures that people expect.

| Gesture | Common action |
| --- | --- |
| Three-finger swipe | Initiate undo (left swipe); initiate redo (right swipe). |
| Three-finger pinch | Copy selected text (pinch in); paste copied text (pinch out). |
| Four-finger swipe (iPadOS only) | Switch between apps. |
| Shake | Initiate undo; initiate redo. |

**Consider allowing simultaneous recognition of multiple gestures if it enhances the experience.** Although simultaneous gestures are unlikely to be useful in nongame apps, a game might include multiple onscreen controls — such as a joystick and firing buttons — that people can operate at the same time. For guidance on integrating touchscreen input with Apple Pencil input in your iPadOS app, see [Apple Pencil and Scribble](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble).

---

## Going full screen

Full page: `references/going-full-screen.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/going-full-screen

*(upstream heading: iOS, iPadOS)*

**Consider deferring system gestures to prevent accidental exits in a full-screen app or game.** By default, the Home Screen indicator automatically hides shortly after someone switches to your app or game. It reappears when someone interacts with the bottom portion of the screen, allowing them to swipe once to exit. Whenever possible, retain this behavior because it’s familiar and what people expect. If supporting this results in unexpected exits, you can enable two swipes rather than one to exit. For developer guidance, see [preferredScreenEdgesDeferringSystemGestures](https://developer.apple.com/documentation/SwiftUI/UIHostingController/preferredScreenEdgesDeferringSystemGestures).

---

## Launching

Full page: `references/launching.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/launching

*(upstream heading: iOS, iPadOS)*

**Launch in the appropriate orientation.** If your app or game supports both portrait and landscape modes, launch using the device’s current orientation. If your interface only runs in one orientation, launch in that orientation and let people rotate the device if necessary. Ensure a landscape-only interface responds correctly, regardless of whether people enter landscape orientation by rotating the device left or right. For guidance, see [Layout](https://developer.apple.com/design/human-interface-guidelines/layout).

---

## Layout

Full page: `references/layout.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/layout

**Aim to support both portrait and landscape orientations.** People appreciate apps and games that work well in different device orientations, but sometimes your experience needs to run in only portrait or only landscape. When this is the case, you can rely on people trying both orientations before settling on the one you support — there’s no need to tell people to rotate their device. If your app or game is landscape-only, make sure it runs equally well whether people rotate their device to the left or the right.

**Prefer a full-bleed interface for your game.** Give players a beautiful interface that fills the screen while accommodating the corner radius, sensor housing, and features like Dynamic Island. If necessary, consider giving players the option to view your game using a letterboxed or pillarboxed appearance.

**Avoid full-width buttons.** Buttons feel at home in iOS when they respect system-defined margins and are inset from the edges of the screen. If you need to include a full-width button, make sure it harmonizes with the curvature of the hardware and aligns with adjacent safe areas.

**Hide the status bar only when it adds value or enhances your experience.** The status bar displays information people find useful and it occupies an area of the screen most apps don’t fully use, so it’s generally a good idea to keep it visible. The exception is if you offer an in-depth experience like playing a game or viewing media, where it might make sense to hide the status bar.

---

## Lists and tables

Full page: `references/lists-and-tables.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/lists-and-tables

*(upstream heading: iOS, iPadOS, visionOS)*

**Use an info button only to reveal more information about a row’s content.** An info button — called a *detail disclosure button* when it appears in a list row — doesn’t support navigation through a hierarchical table or list. If you need to let people drill into a list or table row’s subviews, use a disclosure indicator accessory control. For developer guidance, see [UITableViewCell.AccessoryType.disclosureIndicator](https://developer.apple.com/documentation/UIKit/UITableViewCell/AccessoryType-swift.enum/disclosureIndicator).

![An illustration of a grouped list of rows. Each list item includes an info button at the trailing end of the row.](https://docs-assets.developer.apple.com/published/fd301d26835e0341b95eaa2027f200f2/info-button-in-list%402x.png)

![An illustration of a grouped list of rows. Each list item includes a right-pointing chevron at the trailing end of the row.](https://docs-assets.developer.apple.com/published/dcb3678fe458846713b03756ab5e1a28/disclosure-indicator-in-list%402x.png)

**Avoid adding an index to a table that displays controls — like disclosure indicators — in the trailing ends of its rows.** An *index* typically consists of the letters in an alphabet, displayed vertically at the trailing side of a list. People can jump to a specific section in the list by choosing the index letter that maps to it. Because both the index and elements like disclosure indicators appear on the trailing side of a list, it can be difficult for people to use one element without activating the other.

---

## Materials

Full page: `references/materials.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/materials

*(upstream heading: iOS, iPadOS)*

In addition to Liquid Glass, iOS and iPadOS continue to provide four standard materials — ultra-thin, thin, regular (default), and thick — which you can use in the content layer to help create visual distinction.

![An illustration of the iOS and iPadOS ultraThin material above a colorful background. Where the material overlaps the background, it provides a diffuse gradient of the background colors.](https://docs-assets.developer.apple.com/published/f93e23fa71e0cb11edfee69686baeef1/materials-ios-material-background-ultrathin%402x.png)

![An illustration of the iOS and iPadOS thin material above a colorful background. Where the material overlaps the background, it provides a diffuse and slightly darkened gradient of the background colors.](https://docs-assets.developer.apple.com/published/9eba354f5c5be4fc6ec90989195d75da/materials-ios-material-background-thin%402x.png)

![An illustration of the iOS and iPadOS regular material above a colorful background. Where the material overlaps the background, it provides a diffuse and darkened gradient of the background colors.](https://docs-assets.developer.apple.com/published/baca5883e2cae399a546a10f83f25a3e/materials-ios-material-background-regular%402x.png)

![An illustration of the iOS and iPadOS thick material above a colorful background. Where the material overlaps the background, it provides a dark, muted gradient of the background colors.](https://docs-assets.developer.apple.com/published/efcc1bd2c20aea7eca1915d7cbeabc40/materials-ios-material-background-thick%402x.png)

iOS and iPadOS also define vibrant colors for labels, fills, and separators that are specifically designed to work with each material. Labels and fills both have several levels of vibrancy; separators have one level. The name of a level indicates the relative amount of contrast between an element and the background: The default level has the highest contrast, whereas quaternary (when it exists) has the lowest contrast.

Except for quaternary, you can use the following vibrancy values for labels on any material. In general, avoid using quaternary on top of the [thin](https://developer.apple.com/documentation/SwiftUI/Material/thin) and [ultraThin](https://developer.apple.com/documentation/SwiftUI/Material/ultraThin) materials, because the contrast is too low.

- [UIVibrancyEffectStyle.label](https://developer.apple.com/documentation/UIKit/UIVibrancyEffectStyle/label) (default)
- [UIVibrancyEffectStyle.secondaryLabel](https://developer.apple.com/documentation/UIKit/UIVibrancyEffectStyle/secondaryLabel)
- [UIVibrancyEffectStyle.tertiaryLabel](https://developer.apple.com/documentation/UIKit/UIVibrancyEffectStyle/tertiaryLabel)
- [UIVibrancyEffectStyle.quaternaryLabel](https://developer.apple.com/documentation/UIKit/UIVibrancyEffectStyle/quaternaryLabel)

You can use the following vibrancy values for fills on all materials.

- [UIVibrancyEffectStyle.fill](https://developer.apple.com/documentation/UIKit/UIVibrancyEffectStyle/fill) (default)
- [UIVibrancyEffectStyle.secondaryFill](https://developer.apple.com/documentation/UIKit/UIVibrancyEffectStyle/secondaryFill)
- [UIVibrancyEffectStyle.tertiaryFill](https://developer.apple.com/documentation/UIKit/UIVibrancyEffectStyle/tertiaryFill)

The system provides a single, default vibrancy value for a [UIVibrancyEffectStyle.separator](https://developer.apple.com/documentation/UIKit/UIVibrancyEffectStyle/separator), which works well on all materials.

---

## Menus

Full page: `references/menus.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/menus

*(upstream heading: iOS, iPadOS)*

In iOS and iPadOS, a menu can display items in one of the following three layouts.

![A diagram showing small, medium, and large menu layouts, each containing the same set of menu items.](https://docs-assets.developer.apple.com/published/db1b155d1bc5967b4bbe6a7f20a94879/small-medium-large-menu-layouts%402x.png)

- **Small.** A row of four items appears at the top of the menu, above a list that contains the remaining items. For each item in the top row, the menu displays a symbol or icon, but no label.
- **Medium.** A row of three items appears at the top of the menu, above a list that contains the remaining items. For each item in the top row, the menu displays a symbol or icon above a short label.
- **Large (the default).** The menu displays all items in a list.

For developer guidance, see [preferredElementSize](https://developer.apple.com/documentation/UIKit/UIMenu/preferredElementSize).

**Choose a small or medium menu layout when it can help streamline people’s choices.** Consider using the medium layout if your app has three important actions that people often want to perform. For example, Notes uses the medium layout to give people a quick way to perform the Scan, Lock, and Pin actions. Use the small layout only for closely related actions that typically appear as a group, such as Bold, Italic, Underline, and Strikethrough. For each action, use a recognizable symbol that helps people identify the action without a label.

---

## Multitasking

Full page: `references/multitasking.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/multitasking

On iPhone, multitasking lets people use FaceTime or watch a video in Picture in Picture while they also use a different app.

![A screenshot of the app switcher on iPhone, showing four open apps.](https://docs-assets.developer.apple.com/published/519ce5b2d1298e573aab62d4ea3427c9/multitasking-app-switcher-iphone%402x.png)

![A screenshot of Mail on iPhone, showing an individual email. On top of the email body content, a small image in the bottom-left corner shows the person currently in a FaceTime call.](https://docs-assets.developer.apple.com/published/f68005bf620706a5d6c6c03d09af37f4/multitasking-pip-iphone%402x.png)

---

## Nearby interactions

Full page: `references/nearby-interactions.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/nearby-interactions

On iPhone, Nearby Interaction APIs provide a peer device’s distance and direction.

---

## Page controls

Full page: `references/page-controls.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/page-controls

*(upstream heading: iOS, iPadOS)*

A page control can adjust the appearance of indicators to provide more information about the list. For example, the control highlights the indicator of the current page so people can estimate the page’s relative position in the list. When there are more indicators than fit in the space, the control can shrink indicators at both sides to suggest that more pages are available.

![An illustration of a page control. The page control displays a total of 9 dots. The center 5 dots use the default size; the second and eighth dots are about half the default size and the first and ninth dots are about one quarter the default size. The center dot is filled, indicating the location of the current page in the list.](https://docs-assets.developer.apple.com/published/35dd1a1f9dfe863502d77151eaf5d1f2/page-controls-many-indicators%402x.png)

People interact with page controls by tapping or scrubbing (to *scrub*, people touch the control and drag left or right). Tapping on the leading or trailing side of the current-page indicator reveals the next or previous page; in iPadOS, people can also use the pointer to target a specific indicator. Scrubbing opens pages in sequence, and scrubbing past the leading or trailing edge of the control helps people quickly reach the first or last page.

> **Note:** In the API, *tapping* is a *discrete interaction*, whereas *scrubbing* is a *continuous interaction*; for developer guidance, see [UIPageControl.InteractionState](https://developer.apple.com/documentation/UIKit/UIPageControl/InteractionState-swift.enum).

**Avoid animating page transitions during scrubbing.** People can scrub very quickly, and using the scrolling animation for every transition can make your app lag and cause distracting visual flashes. Use the animated scrolling transition only for tapping.

A page control can include a translucent, rounded-rectangle background appearance that provides visual contrast for the indicators. You can choose one of the following background styles:

- Automatic — Displays the background only when people interact with the control. Use this style when the page control isn’t the primary navigational element in the UI.
- Prominent — Always displays the background. Use this style only when the control is the primary navigational control in the screen.
- Minimal — Never displays the background. Use this style when you just want to show the position of the current page in the list and you don’t need to provide visual feedback during scrubbing.

For developer guidance, see [backgroundStyle](https://developer.apple.com/documentation/UIKit/UIPageControl/backgroundStyle-swift.property).

**Avoid supporting the scrubber when you use the minimal background style.** The minimal style doesn’t provide visual feedback during scrubbing. If you want to let people scrub a list of pages in your app, use the automatic or prominent background styles.

---

## Pickers

Full page: `references/pickers.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/pickers

*(upstream heading: iOS, iPadOS)*

A date picker is an efficient interface for selecting a specific date, time, or both, using touch, a keyboard, or a pointing device. You can display a date picker in one of the following styles:

- Compact — A button that displays editable date and time content in a modal view.
- Inline — For time only, a button that displays wheels of values; for dates and times, an inline calendar view.
- Wheels — A set of scrolling wheels that also supports data entry through built-in or external keyboards.
- Automatic — A system-determined style based on the current platform and date picker mode.

A date picker has four modes, each of which presents a different set of selectable values.

- Date — Displays months, days of the month, and years.
- Time — Displays hours, minutes, and (optionally) an AM/PM designation.
- Date and time — Displays dates, hours, minutes, and (optionally) an AM/PM designation.
- Countdown timer — Displays hours and minutes, up to a maximum of 23 hours and 59 minutes. This mode isn’t available in the inline or compact styles.

The exact values shown in a date picker, and their order, depend on the device location.

Here are several examples of date pickers showing different combinations of style and mode.

**Use a compact date picker when space is constrained.** The compact style displays a button that shows the current value in your app’s accent color. When people tap the button, the date picker opens a modal view, providing access to a familiar calendar-style editor and time picker. Within the modal view, people can make multiple edits to dates and times before tapping outside the view to confirm their choices.

---

## Playing audio

Full page: `references/playing-audio.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/playing-audio

*(upstream heading: iOS, iPadOS)*

**Use the system’s sound services to play short sounds and vibrations.** For developer guidance, see [Audio Services](https://developer.apple.com/documentation/AudioToolbox/audio-services).

---

## Playing haptics

Full page: `references/playing-haptics.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/playing-haptics

On supported iPhone models, you can add haptics to your experience in the following ways:

- Use standard UI components — like [toggles](https://developer.apple.com/design/human-interface-guidelines/toggles), [sliders](https://developer.apple.com/design/human-interface-guidelines/sliders), and [pickers](https://developer.apple.com/design/human-interface-guidelines/pickers) — that play Apple-designed system haptics by default.
- When it makes sense, use a feedback generator to play one of several predefined haptic patterns in the categories of [notification](https://developer.apple.com/design/human-interface-guidelines/playing-haptics#Notification), [impact](https://developer.apple.com/design/human-interface-guidelines/playing-haptics#Impact), and [selection](https://developer.apple.com/design/human-interface-guidelines/playing-haptics#Selection) (for developer guidance, see [UIFeedbackGenerator](https://developer.apple.com/documentation/UIKit/UIFeedbackGenerator)).

#### Notification

Notification haptics provide feedback about the outcome of a task or action, such as depositing a check or unlocking a vehicle.

#### Impact

Impact haptics provide a physical metaphor you can use to complement a visual experience. For example, people might feel a tap when a view snaps into place or a thud when two heavy objects collide.

#### Selection

Selection haptics provide feedback while the values of a UI element are changing.

---

## Popovers

Full page: `references/popovers.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/popovers

*(upstream heading: iOS, iPadOS)*

**Avoid displaying popovers in compact views.** Make your app or game dynamically adjust its layout based on the size class of the content area. Reserve popovers for wide views; for compact views, use all available screen space by presenting information in a full-screen modal view like a sheet instead. For related guidance, see [Modality](https://developer.apple.com/design/human-interface-guidelines/modality).

---

## Progress indicators

Full page: `references/progress-indicators.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/progress-indicators

*(upstream heading: iOS, iPadOS)*

#### Refresh content controls

A refresh control lets people immediately reload content, typically in a table view, without waiting for the next automatic content update to occur. A refresh control is a specialized type of activity indicator that’s hidden by default, becoming visible when people drag down the view they want to reload. In Mail, for example, people can drag down the list of Inbox messages to check for new messages.

![A screenshot of a refresh content control spinning while Mail checks for new messages.](https://docs-assets.developer.apple.com/published/50a9348d9e19b5ca206d8567d1d1fc20/refresh-controls%402x.png)

**Perform automatic content updates.** Although people appreciate being able to do an immediate content refresh, they also expect automatic refreshes to occur periodically. Don’t make people responsible for initiating every update. Keep data fresh by updating it regularly.

**Supply a short title only if it adds value.** Optionally, a refresh control can include a title. In most cases, this is unnecessary, as the animation of the control indicates that content is loading. If you do include a title, don’t use it to explain how to perform a refresh. Instead, provide information of value about the content being refreshed. A refresh control in Podcasts, for example, uses a title to tell people when the last podcast update occurred.

For developer guidance, see [UIRefreshControl](https://developer.apple.com/documentation/UIKit/UIRefreshControl).

---

## Pull-down buttons

Full page: `references/pull-down-buttons.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons

*(upstream heading: iOS, iPadOS)*

> **Note:** You can also let people reveal a pull-down menu by performing a specific gesture on a button. For example, in iOS 14 and later, Safari responds to a touch and hold gesture on the Tabs button by displaying a menu of tab-related actions, like New Tab and Close All Tabs.

**Consider using a More pull-down button to present items that don’t need prominent positions in the main interface.** A More button can help you offer a range of items where space is constrained, but it can also hinder discoverability. Although people generally understand that a More button offers additional functionality related to the current context, the ellipsis icon doesn’t necessarily help them predict its contents. To design an effective More button, weigh the convenience of its size against its impact on discoverability to find a balance that works in your app.

![A screenshot of the Notes app on iPhone, open to a Notes document titled Nature Walks. The top toolbar includes a More button on the trailing edge.](https://docs-assets.developer.apple.com/published/c8c27b1f9b28c5e1ec749260d87cb7dd/menu-secondary-actions-collapsed%402x.png)

![A screenshot of the Notes app on iPhone, open to a Notes document titled Nature Walks. The More button in the top toolbar is expanded, revealing the More menu with additional funtionality.](https://docs-assets.developer.apple.com/published/de6253180f10a2e0e0c317faaa8be6cb/menu-secondary-actions-expanded%402x.png)

---

## Scroll views

Full page: `references/scroll-views.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/scroll-views

*(upstream heading: iOS, iPadOS)*

**Consider showing a page control when a scroll view is in page-by-page mode.** [Page controls](https://developer.apple.com/design/human-interface-guidelines/page-controls) show how many pages, screens, or other chunks of content are available and indicates which one is currently visible. For example, Weather uses a page control to indicate movement between people’s saved locations. If you show a page control with a scroll view, don’t show the scrolling indicator on the same axis to avoid confusing people with redundant controls.

---

## Search fields

Full page: `references/search-fields.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/search-fields

There are three main places you can position the entry point for search:

- As a tab in a tab bar
- In a toolbar at the bottom or top of the screen
- Directly inline with content

Where search makes the most sense depends on the layout, content, and navigation of your app.

#### Search as a tab

You can place search as a tab in a tab bar, which keeps search visible and always available as people switch between the sections of your app. There are two styles of search tabs:

- **Standard tab.** This style displays the search tab uniformly with the rest of the tab bar. Tapping the search tab navigates people to a search landing page with a search field at the top.
- **Button appearance.** This style displays the search tab as a separate button and allows people to start searching immediately. Tapping the search tab brings focus to the search field and displays the keyboard.

![An illustration of a tab bar at the bottom of an iPhone screen. A tab for search appears as part of the tab bar.](https://docs-assets.developer.apple.com/published/ceedd10e5714cf0b7354d5aac41540fc/search-fields-search-as-tab-standard%402x.png)

![An illustration of a tab bar at the bottom of an iPhone screen. A tab for search appears on the trailing edge as a separate button.](https://docs-assets.developer.apple.com/published/69e306ce727b65d8880c0ead03251499/search-fields-search-as-tab-prominent%402x.png)

**Choose the standard tab style to provide suggestions, promote discovery, and encourage exploration.** This style of search tab creates a dedicated landing page for search, providing an opportunity to reveal any content or suggestions that might be helpful before someone taps the field to begin the search. This approach is great for an app with a variety of rich content that people might want to explore. For example, Apple TV uses this search tab style to present its various genres and categories, helping ground people in what’s available before they search.

**Choose the button appearance to help people quickly find what they need.** When someone interacts with this style of search tab, the keyboard immediately appears with the search field above it, ready to begin the search. This approach provides a more transient experience that brings people directly back to their previous tab after they exit search, and is ideal when you want search to resolve quickly and seamlessly.

#### Search in a toolbar

As an alternative to search in a tab bar, you can also place search in a toolbar either at the bottom or top of the screen.

- You can include search in a bottom toolbar either as an expanded field or as a toolbar button, depending on how much space is available. When someone taps it, it animates into a search field above the keyboard so they can begin typing.
- You can include search in a top toolbar, also called a navigation bar, where it appears as a toolbar button. When someone taps it, it animates into a search field that appears either above the keyboard or at the top if there isn’t space at the bottom.

![An illustration of an iPhone screen with search in a bottom toolbar. The search field is positioned in an isolated group between a Filter button on the leading edge and a Compose button on the trailing edge.](https://docs-assets.developer.apple.com/published/508889e5f10444e6afc709d03a78099d/search-fields-ios-toolbar-with-items%402x.png)

![An illustration of an iPhone screen with search in a top toolbar. A Back button appears on the leading edge, and an Add button appears on the trailing edge. A button group with Search and More appears next to the Add button.](https://docs-assets.developer.apple.com/published/dcc92f43473bbfbb718290667f6667cf/search-fields-ios-navigation-bar-item%402x.png)

**Place search at the bottom if there’s room.** You can either add a search field to an existing toolbar, or as a new toolbar where search is the only item. Search at the bottom is useful in any situation where search is a priority, since it keeps the search experience easy to reach. Examples of apps with search at the bottom in various toolbar layouts include Settings, where it’s the only item, and Mail and Notes, where it fits alongside other important controls.

**Place search at the top when itʼs important to defer to content at the bottom of the screen, or thereʼs no bottom toolbar.** Use search at the top in cases where covering the content might interfere with a primary function of the app. The Wallet app, for example, includes event passes in a stack at the bottom of the screen for easy access and viewing at a glance.

#### Search as an inline field

In some cases you might want your app to include a search field inline with content.

**Place search as an inline field when its position alongside the content it searches strengthens that relationship.** When you need to filter or search within a single view, it can be helpful to have search appear directly next to content to illustrate that the search applies to it, rather than globally. This pattern is useful if your app has more than one search field and if location plays a critical role in the scope of your search. For example, although the main search in the Music app is a tab, people can navigate to their library and use an inline search field to filter their songs and albums.

**When at the top, position an inline search field above the list it searches, and consider pinning it to the top toolbar when scrolling.** This helps keep it distinct from search that appears in other locations.

---

## Segmented controls

Full page: `references/segmented-controls.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/segmented-controls

*(upstream heading: iOS, iPadOS)*

**Consider a segmented control to switch between closely related subviews.** A segmented control can be useful as a way to quickly switch between related subviews. For example, the segmented control in Calendar’s New Event sheet switches between the subviews for creating a new event and a new reminder. For switching between completely separate sections of an app, use a [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) instead.

![A screenshot of the top half of the iOS Calendar app, showing the New Event sheet. A segmented control provides the ability to switch between adding a new event and a new reminder.](https://docs-assets.developer.apple.com/published/e332c65fedbefd2b5d084f7d70c67183/segmented-controls-calendar-new-event%402x.png)

---

## Sheets

Full page: `references/sheets.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/sheets

*(upstream heading: iOS, iPadOS)*

In iOS and iPadOS, for sheets with a single view, the Cancel button belongs on the leading edge of the top toolbar. When present, the Done button belongs on the trailing edge.

![An illustration of the top half of a sheet on iPhone. A Cancel button appears in the top-left corner of the view, and a Done button appears in the top-right corner.](https://docs-assets.developer.apple.com/published/0338c64cf7840bf59cdd15c6c3bfa5f3/sheets-buttons-placement-cancel-done%402x.png)

For sheets with a multi-step flow, the placement of buttons can vary across steps.

A resizable sheet expands when people scroll its contents or drag the *grabber*, which is a small horizontal indicator that can appear at the top edge of a sheet. Sheets resize according to their *detents*, which are particular heights at which a sheet naturally rests. Designed for iPhone, detents specify particular heights at which a sheet naturally rests. The system defines two detents: *large* is the height of a fully expanded sheet and *medium* is about half of the fully expanded height. Sheets can have one or more custom detent values.

![An illustration showing an iPhone screen in portrait orientation containing a solid rounded rectangle that occupies almost all of the screen, representing a full-screen sheet. A rounded close button appears in the upper-left corner of the sheet.](https://docs-assets.developer.apple.com/published/54e49fb3f1a0256283e402a167d93640/sheets-large-detent%402x.png)

![An illustration showing an iPhone screen in portrait orientation containing a solid rounded rectangle that occupies half of the screen, representing a half-screen sheet. A rounded close button appears in the upper-left corner of the sheet.](https://docs-assets.developer.apple.com/published/74600908c64d57d1d0cc73d353640799/sheets-medium-detent%402x.png)

Sheets automatically support the large detent. Adding the medium detent allows the sheet to rest at both heights, whereas specifying only medium prevents the sheet from expanding to full height. For developer guidance, see [detents](https://developer.apple.com/documentation/UIKit/UISheetPresentationController/detents).

**In an iPhone app, consider supporting the medium detent to allow progressive disclosure of the sheet’s content.** For example, a share sheet displays the most relevant items within the medium detent, where they’re visible without resizing. To view more items, people can scroll or expand the sheet. In contrast, you might not want to support the medium detent if a sheet’s content is more useful when it displays at full height. For example, the compose sheets in Messages and Mail display only at full height to give people enough room to create content.

**Include a grabber in a resizable sheet.** A grabber shows people that they can drag the sheet to resize it; they can also tap it to cycle through the detents. In addition to providing a visual indicator of resizability, a grabber also works with VoiceOver so people can resize the sheet without seeing the screen. For developer guidance, see [prefersGrabberVisible](https://developer.apple.com/documentation/UIKit/UISheetPresentationController/prefersGrabberVisible).

**Support swiping to dismiss a sheet.** People expect to swipe vertically to dismiss a sheet instead of tapping a dismiss button. If people have unsaved changes in the sheet when they begin swiping to dismiss it, use an action sheet to let them confirm their action.

**Prefer using the page or form sheet presentation styles in an iPadOS app.** Each style uses a default size for the sheet, centering its content on top of a dimmed background view and providing a consistent experience. For developer guidance, see [UIModalPresentationStyle](https://developer.apple.com/documentation/UIKit/UIModalPresentationStyle).

---

## Sidebars

Full page: `references/sidebars.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/sidebars

*(upstream heading: iOS, iPadOS)*

When you use the [sidebarAdaptable](https://developer.apple.com/documentation/SwiftUI/TabViewStyle/sidebarAdaptable) style of tab view to present a sidebar, you choose whether to display a sidebar or a tab bar when your app opens. Both variations include a button that people can use to switch between them. This style also adapts its appearance depending on the platform, and responds automatically to rotation and window resizing, providing a version of the control that’s appropriate to the width of the view.

> **Note:** To display a sidebar only, use [NavigationSplitView](https://developer.apple.com/documentation/SwiftUI/NavigationSplitView) to present a sidebar in the primary pane of a split view, or use [UISplitViewController](https://developer.apple.com/documentation/UIKit/UISplitViewController).

**Consider using a tab bar first.** A tab bar provides more space to feature content, and offers enough flexibility to navigate between many apps’ main areas. If you need to expose more areas than fit in a tab bar, the tab bar’s convertible sidebar-style appearance can provide access to content that people use less frequently. For guidance, see [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars).

**If necessary, apply the correct appearance to a sidebar.** If you’re not using SwiftUI to create a sidebar, you can use the [UICollectionLayoutListConfiguration.Appearance.sidebar](https://developer.apple.com/documentation/UIKit/UICollectionLayoutListConfiguration-swift.struct/Appearance-swift.enum/sidebar) appearance of a collection view list layout. For developer guidance, see [UICollectionLayoutListConfiguration.Appearance](https://developer.apple.com/documentation/UIKit/UICollectionLayoutListConfiguration-swift.struct/Appearance-swift.enum).

---

## Sliders

Full page: `references/sliders.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/sliders

*(upstream heading: iOS, iPadOS)*

**Don’t use a slider to adjust audio volume.** If you need to provide volume control in your app, use a volume view, which is customizable and includes a volume-level slider and a control for changing the active audio output device. For guidance, see [Playing audio](https://developer.apple.com/design/human-interface-guidelines/playing-audio).

---

## Split views

Full page: `references/split-views.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/split-views

**Prefer using a split view in a regular — not a compact — environment.** A split view needs horizontal space in which to display multiple panes. In a compact environment, such as iPhone in portrait orientation, it’s difficult to display multiple panes without wrapping or truncating the content, making it less legible and harder to interact with.

---

## Tab bars

Full page: `references/tab-bars.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/tab-bars

A tab bar floats above content at the bottom of the screen. Its items rest on a [Liquid Glass](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass) background that allows content beneath to peek through.

For tab bars with an attached accessory, like the MiniPlayer in Music, you can choose to minimize the tab bar and move the accessory inline with it when a person scrolls down. A person can exit the minimized state by tapping a tab or scrolling to the top of the view. For developer guidance, see [TabBarMinimizeBehavior](https://developer.apple.com/documentation/SwiftUI/TabBarMinimizeBehavior) and [UITabBarController.MinimizeBehavior](https://developer.apple.com/documentation/UIKit/UITabBarController/MinimizeBehavior).

![An illustration of the bottom half of an iPhone in portrait orientation, with the Music app open. The MiniPlayer is open above the tab bar at the bottom of the screen.](https://docs-assets.developer.apple.com/published/fa928910fce5a5a6714124eb177171c1/tab-bar-with-accessory-expanded%402x.png)

![An illustration of the bottom half of an iPhone in portrait orientation, with the Music app open. The tab bar is minimized into the currently open tab at the leading bottom corner of the screen, with the MiniPlayer at the bottom center, and the search tab in the trailing corner.](https://docs-assets.developer.apple.com/published/b4d31e52ed5203c363b2a83aee77bcbd/tab-bar-with-accessory-collapsed%402x.png)

A tab bar can include a dedicated search tab at the trailing end. For guidance, see [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields).

---

## Tab views

Full page: `references/tab-views.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/tab-views

*(upstream heading: iOS, iPadOS)*

For similar functionality, consider using a [segmented control](https://developer.apple.com/design/human-interface-guidelines/segmented-controls) instead.

---

## Text fields

Full page: `references/text-fields.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/text-fields

*(upstream heading: iOS, iPadOS)*

**Display a Clear button in the trailing end of a text field to help people erase their input.** When this element is present, people can tap it to clear the text field’s contents, without having to keep tapping the Delete key.

**Use images and buttons to provide clarity and functionality in text fields.** You can display custom images in both ends of a text field, or you can add a system-provided button, such as the Bookmarks button. In general, use the leading end of a text field to indicate a field’s purpose and the trailing end to offer additional features, such as bookmarking.

---

## Text views

Full page: `references/text-views.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/text-views

*(upstream heading: iOS, iPadOS)*

**Show the appropriate keyboard type.** Several different keyboard types are available, each designed to facilitate a different type of input. To streamline data entry, the keyboard you display when editing a text view needs to be appropriate for the type of content. For guidance, see [Virtual keyboards](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards).

---

## Toggles

Full page: `references/toggles.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/toggles

*(upstream heading: iOS, iPadOS)*

**Use the switch toggle style only in a list row.** You don’t need to supply a label in this situation because the content in the row provides the context for the state the switch controls.

**Change the default color of a switch only if necessary.** The default green color tends to work well in most cases, but you might want to use your app’s accent color instead. Be sure to use a color that provides enough contrast with the uncolored appearance to be perceptible.

![An illustration of two list rows, one with an active switch toggle and one with an inactive switch toggle. The active toggle is tinted green with the standard switch color.](https://docs-assets.developer.apple.com/published/3399459ec1e00637f7b8dbb7ca2ad353/toggles-ios-default-color%402x.png)

![An illustration of two list rows, one with an active switch toggle and one with an inactive switch toggle. The active toggle is tinted purple with a custom switch color.](https://docs-assets.developer.apple.com/published/a9ab222932bbc5c83b080140f15d2ebd/toggles-ios-custom-color%402x.png)

**Outside of a list, use a button that behaves like a toggle, not a switch.** For example, the Phone app uses a toggle on the filter button to let users filter their recent calls.  The app adds a blue highlight to indicate when the toggle is active, and removes it when the toggle is inactive.

![A screenshot of the top half of the Phone app on iPhone, showing the filtered list of recent missed calls. The filter button in the top trailing corner has a blue highlight, indicating that the toggle is active.](https://docs-assets.developer.apple.com/published/de5b69927ab5e98eb233b32520b9a419/toggles-ios-phone-filter-on%402x.png)

![A screenshot of the top half of the Phone app on iPhone, showing all recent calls. The filter button in the top trailing corner has no highlight, indicating that the toggle is inactive.](https://docs-assets.developer.apple.com/published/812fdeb4c428b1b163a3070304b7ff4e/toggles-ios-phone-filter-off%402x.png)

**Avoid supplying a label that explains the button’s purpose.** The interface icon you create — combined with the alternative background appearances you supply — help people understand what the button does. For developer guidance, see [changesSelectionAsPrimaryAction](https://developer.apple.com/documentation/UIKit/UIButton/changesSelectionAsPrimaryAction).

---

## Toolbars

Full page: `references/toolbars.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/toolbars

**Prioritize only the most important items for inclusion in the main toolbar area.** Because space is so limited, carefully consider which actions are essential to your app and include those first. Create a More menu to include additional items.

**Use a large title to help people stay oriented as they navigate and scroll.** By default, a large title transitions to a standard title as people begin scrolling the content, and transitions back to large when people scroll to the top, reminding them of their current location. For developer guidance, see [prefersLargeTitles](https://developer.apple.com/documentation/UIKit/UINavigationBar/prefersLargeTitles).

---

## Typography

Full page: `references/typography.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/typography

*(upstream heading: iOS, iPadOS)*

SF Pro is the system font in iOS and iPadOS. iOS and iPadOS apps can also use NY.

---

## Undo and redo

Full page: `references/undo-and-redo.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/undo-and-redo

*(upstream heading: iOS, iPadOS)*

**Avoid redefining standard gestures for undo and redo.** For example, people can use a three-finger swipe to initiate an undo or redo, or shake their iPhone. As with all standard gestures, redefining them in your interface runs the risk of confusing people and making your experience unpredictable.

**Briefly and precisely describe the operation to be undone or redone.** The undo and redo alert title automatically includes a prefix of “Undo ” or “Redo ” (including the trailing space). You need to provide an additional word or two that describes what’s being undone or redone, to appear after this prefix. For example, you might create alert titles such as “Undo Name” or “Redo Address Change.”

---

## Virtual keyboards

Full page: `references/virtual-keyboards.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards

*(upstream heading: iOS, iPadOS)*

**Use the keyboard layout guide to make the keyboard feel like an integrated part of your interface.** Using the layout guide also helps you keep important parts of your interface visible while the virtual keyboard is onscreen. For developer guidance, see [Adjusting your layout with keyboard layout guide](https://developer.apple.com/documentation/UIKit/adjusting-your-layout-with-keyboard-layout-guide).

![An illustration of an app layout on iPhone, showing two stacked text fields and a button above the keyboard.](https://docs-assets.developer.apple.com/published/72f8e84e391d9edfd375fe7c955e0b65/ui-fully-visible%402x.png)

![A checkmark in a circle to indicate a correct example.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![An illustration of an app layout on iPhone, showing two stacked text fields. The keyboard covers part of the bottom text field.](https://docs-assets.developer.apple.com/published/f27dfe0a95c0f730c07efd686ba84293/text-field-hidden%402x.png)

![An X in a circle to indicate an incorrect example.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![An illustration of an app layout on iPhone, showing two stacked text fields and a button above the keyboard. The keyboard covers part of the button.](https://docs-assets.developer.apple.com/published/a698e78c6c87b5475fe1c08db764acb5/button-hidden%402x.png)

![An X in a circle to indicate an incorrect example.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

**Place custom controls above the keyboard thoughtfully.** Some apps position an input accessory view containing custom controls above the keyboard to offer app-specific functionality related to the data people are working with. For example, Numbers displays controls that help people apply standard or custom calculations to spreadsheet data. If your app offers custom controls that augment the keyboard, make sure they’re relevant to the current task. If other views in your app use Liquid Glass, or if your view looks out of place above the keyboard, apply Liquid Glass to the view that contains your controls to maintain consistency. If you use a standard toolbar to contain your controls, it automatically adopts Liquid Glass. Use the keyboard layout guide and standard padding to ensure the system positions your controls as expected within the view. For developer guidance, see [ToolbarItemPlacement](https://developer.apple.com/documentation/SwiftUI/ToolbarItemPlacement) (SwiftUI), [inputAccessoryView](https://developer.apple.com/documentation/UIKit/UIResponder/inputAccessoryView) (UIKit), and [UIKeyboardLayoutGuide](https://developer.apple.com/documentation/UIKit/UIKeyboardLayoutGuide) (UIKit).

---

## Widgets

Full page: `references/widgets.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/widgets

*(upstream heading: iOS, iPadOS)*

Widgets on the Lock Screen are functionally similar to watch complications and follow design principles for [Complications](https://developer.apple.com/design/human-interface-guidelines/complications) in addition to design principles for widgets. Provide useful information in your Lock Screen widget, and don’t treat it only as an additional way for people to launch into your app. In many cases, a design for complications also works well for widgets on the Lock Screen (and vice versa), so consider creating them in tandem.

Your app can offer widgets on the Lock Screen in three different shapes: as inline text that appears above the clock, and as circular and rectangular shapes that appear below the clock.

![A partial screenshot of the Lock Screen on iPhone that shows a Calendar widget and two Weather widgets below the time. From the left, the widgets are an inline text widget and two circular widgets.](https://docs-assets.developer.apple.com/published/6e55a3d32170489baeb1835febdfbfb5/widget-lock-screen-display-appearances%402x.png)

**Support the Always-On display on iPhone.** Devices with the Always-On display render widgets on the Lock Screen with reduced luminance. Use levels of gray that provide enough contrast in the Always-On display, and make sure your content remains legible.

For developer guidance, see [Creating accessory widgets and watch complications](https://developer.apple.com/documentation/WidgetKit/Creating-accessory-widgets-and-watch-complications).

**Offer Live Activities to show real-time updates.** Widgets don’t show real-time information. If your app allows people to track the progress of a task or event for a limited amount of time with frequent updates, consider offering Live Activities. Widgets and Live Activities use the same underlying frameworks and share design similarities. As a result, it can be a good idea to develop widgets and Live Activities in tandem and reuse code and design components for both features. For design guidance on Live Activities, see [Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities); for developer guidance, see [ActivityKit](https://developer.apple.com/documentation/ActivityKit).

#### StandBy and CarPlay

On iPhone in StandBy, the system displays two small system family widgets side-by-side, scaled up so they fill the Lock Screen. By supporting StandBy, you also ensure your widgets work well in CarPlay. CarPlay and StandBy widgets both use the small system family widget with the background removed and scaled up to best fit the grid on the Widgets screen. Glanceable information and large text are especially important in CarPlay to make your widget easy to read on a car’s display.

**Limit usage of rich images or color to convey meaning in StandBy.** Instead, make use of the additional space by scaling up and rearranging text so people can glance at the widget content from a greater distance. To seamlessly blend with the black background, don’t use background colors for your widget when it appears in StandBy.

For developer guidance, see [Displaying the right widget background](https://developer.apple.com/documentation/WidgetKit/Displaying-the-right-widget-background).

On iPhone in StandBy in low-light conditions, the system renders widgets in a monochromatic look with a red tint.

![An image of iPhone in low-light conditions. It shows a Clock widget on the left that displays the time as 9:41 a.m. and a Weather widget set to Cupertino with the temperature at 70 degrees Fahrenheit on the right.](https://docs-assets.developer.apple.com/published/2177fb5bad3e77776eaec5cba873b61e/widgets-standby-low-light%402x.png)

---
