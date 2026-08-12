# iPadOS-specific guidance, collected

Every place the HIG states a rule specific to iPadOS, lifted from the page it lives on. Sections appear alphabetically by page.

A heading like `### iPadOS, iPadOS` upstream means the rule is shared; it's reproduced here in full so you don't have to go looking. Each entry links to the complete page, which also carries the cross-platform guidance this file deliberately omits.

---

## Action sheets

Full page: `references/action-sheets.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/action-sheets

*(upstream heading: iOS, iPadOS)*

**Use an action sheet — not a menu — to provide choices related to an action.** People are accustomed to having an action sheet appear when they perform an action that might require clarifying choices. In contrast, people expect a menu to appear when they choose to reveal it.

**Avoid letting an action sheet scroll.** The more buttons an action sheet has, the more time and effort it takes for people to make a choice. Also, scrolling an action sheet can be hard to do without inadvertently tapping a button.

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

## Focus and selection

Full page: `references/focus-and-selection.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/focus-and-selection

iPadOS 15 and later defines a focus system that supports keyboard interactions for navigating text fields, text views, and sidebars, in addition to various types of collection views and other custom views in your app.

The iPadOS and tvOS focus systems are similar. People perform actions by moving a focus indicator to an item and then selecting it (for guidance, see [tvOS](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection#tvOS)). Although the underlying system is the same, the user experiences are a little different. tvOS uses *directional focus*, which means people can use the same interaction — that is, swiping the Siri Remote or using only the arrow keys on a connected keyboard — to navigate to every onscreen component. In contrast, iPadOS defines *focus groups*, which represent specific areas within an app, like a sidebar, grid, or list. Using focus groups, iPadOS can support two different keyboard interactions.

- Pressing the Tab key moves focus among focus groups, letting people navigate to sidebars, grids, and other app areas.
- Pressing an arrow key supports a directional focus interaction that’s similar to tvOS, but limited to navigation among items in the same focus group. For example, people can use an arrow key to move through the items in a list or a sidebar.

Onscreen components can indicate focus by using the halo effect or the highlighted appearance.

The *halo* focus effect — also known as the *focus ring* — displays a customizable outline around the component. You can apply the halo effect to custom views and to fully opaque content within a collection or list cell, such as an image.

![An illustration of a collection view of photos showing the standard halo effect that outlines the focused photo.](https://docs-assets.developer.apple.com/published/2bfe6fedc5a6a8ecf6d7e74e9492a096/focus-and-selection-halo-focus-effect%402x.png)

**Customize the halo focus effect when necessary.** By default, the system uses an item’s shape to infer the shape of its halo. If the system-provided halo doesn’t give you the appearance you want, you can refine it to match contours like rounded corners or shapes defined by Bézier paths. You can also adjust a halo’s position if another component occludes or clips it. For example, you might need to ensure that a badge appears above the halo or that a parent view doesn’t clip it. For developer guidance, see [UIFocusHaloEffect](https://developer.apple.com/documentation/UIKit/UIFocusHaloEffect).

![An illustration of a collection view of photos showing a rounded-rectangle halo effect that outlines the focused photo.](https://docs-assets.developer.apple.com/published/84681bbfe2ac9200f62a96977bb3a204/focus-and-selection-customized-halo%402x.png)

The *highlighted* appearance — in which the component’s text uses the app’s accent color — also indicates focus, but it’s not a focus effect. The highlight appearance occurs automatically when people select a collection view cell on which you’ve set content configurations (for developer guidance, see [UICollectionViewCell](https://developer.apple.com/documentation/UIKit/UICollectionViewCell)).

![An illustration of a list of menu items with the second item highlighted. The item's title and icon are tinted with a red accent color.](https://docs-assets.developer.apple.com/published/6439b067fb9cc599a6a6840959e2d40d/focus-and-selection-highlighted-appearance%402x.png)

**Ensure that focus moves through your custom views in ways that make sense.** As people continue pressing the Tab key, focus moves through focus groups in reading order: leading to trailing, and top to bottom. Although focus moves through system-provided views in ways that people expect, you might need to adjust the order in which the focus system visits your custom views. For example, if you want focus to move down through a vertical stack of custom views before it moves in the trailing direction to the next view, you need to identify the stack container as a single focus group. For developer guidance, see [focusGroupIdentifier](https://developer.apple.com/documentation/UIKit/UIFocusEnvironment/focusGroupIdentifier).

**Adjust the priority of an item to reflect its importance within a focus group.** When a group receives focus, its *primary item* automatically receives focus too, making it easy for people to select the item they’re most likely to want. You can make an item primary by increasing its priority. For developer guidance, see [UIFocusGroupPriority](https://developer.apple.com/documentation/UIKit/UIFocusGroupPriority).

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

People can freely resize windows down to a minimum width and height, similar to window behavior in macOS. It’s important to account for this resizing behavior and the full range of possible window sizes when designing your layout. For guidance, see [iPadOS](https://developer.apple.com/design/human-interface-guidelines/multitasking#iPadOS) and [iPadOS](https://developer.apple.com/design/human-interface-guidelines/windows#iPadOS).

**As someone resizes a window, defer switching to a compact view for as long as possible.** Design for a full-screen view first, and only switch to a compact view when a version of the full layout no longer fits. This helps the UI feel more stable and familiar in as many situations as possible. For more complex layouts such as [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views), prefer hiding tertiary columns such as inspectors as the view narrows.

**Test your layout at common system-provided sizes, and provide smooth transitions.** Window controls provide the option to arrange windows to fill halves, thirds, and quadrants of the screen, so it’s important to check your layout at each of these sizes on a variety of devices. Be sure to minimize unexpected UI changes as people adjust down to the minimum and up to the maximum window size.

**Consider a convertible tab bar for adaptive navigation.** For many apps, you don’t need to choose between a tab bar or sidebar for navigation; instead, you can adopt a style of tab bar that provides both. The app first launches with your choice of a sidebar or a tab bar, and then people can tap to switch between them. As the view resizes, the presentation style changes to fit the width of the view. For guidance, see [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars). For developer guidance, see [sidebarAdaptable](https://developer.apple.com/documentation/SwiftUI/TabViewStyle/sidebarAdaptable).

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

On iPad, people can view and interact with the [Windows](https://developer.apple.com/design/human-interface-guidelines/windows) of several different apps at the same time. An individual app can also support multiple open windows, which lets people view and interact with more than one window in the same app at one time.

People can use iPad with either full-screen or windowed apps. When full screen, apps occupy the full screen, and people can switch between individual app windows using the app switcher.

![A screenshot of the iPad app switcher in landscape orientation, showing five open apps. Thumbnail representations of the apps are arranged in a grid.](https://docs-assets.developer.apple.com/published/b1c2946808ad75c7036af18706a55b79/multitasking-ipad-app-switcher%402x.png)

When using windowed apps, app windows are resizable, and people can arrange them to suit their needs with behavior similar to macOS. The system provides window controls for common tiling configurations, entering full screen, minimizing, and closing windows. The system identifies the frontmost window by coloring its window controls and casting a drop shadow on windows behind it. For guidance, see [iPadOS](https://developer.apple.com/design/human-interface-guidelines/windows#iPadOS).

![A screenshot of two windowed apps on iPad in landscape orientation. The frontmost app window overlaps and casts a shadow on the one behind it, and has colored window controls to indicate that the window is active. Both windows sit atop the Home Screen background, and the Dock appears at the bottom.](https://docs-assets.developer.apple.com/published/433d49d66e117152f7cca9605ebe9628/multitasking-ipad-windows-maps-landmarks%402x.png)

Additionally, videos and FaceTime calls can also play in a Picture in Picture overlay above other content regardless of whether apps are full screen or windowed.

> **Note:** Apps don’t control multitasking configurations or receive any indication of the ones that people choose.

To help your app respond correctly when people open it while windowed, make sure it adapts gracefully to different screen sizes. For guidance, see [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) and [Windows](https://developer.apple.com/design/human-interface-guidelines/windows); for developer guidance, see [Multitasking on iPad, Mac, and Apple Vision Pro](https://developer.apple.com/documentation/UIKit/multitasking-on-ipad-mac-and-apple-vision-pro). To learn more about how people use iPad multitasking features, see [Use multitasking on your iPad](https://support.apple.com/en-us/HT207582).

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

## Pointing devices

Full page: `references/pointing-devices.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/pointing-devices

iPadOS builds on the traditional pointer experience, automatically adapting the pointer to the current context and providing rich visual feedback at a level of precision that enhances productivity and simplifies common tasks on a touchscreen device. The iPadOS pointing system gives people an additional way to interact with apps and content — it doesn’t replace touch.

**Allow multiple selection in custom views when necessary.** In iPadOS 15 and later, people can click and drag the pointer over multiple items to select them. As people use the pointer in this way, it expands into a visible rectangle that selects the items it encompasses. Standard nonlist collection views support this interaction by default; if you want to support multiple selection in custom views, you need to implement it yourself. For developer guidance, see [UIBandSelectionInteraction](https://developer.apple.com/documentation/UIKit/UIBandSelectionInteraction).

**Distinguish between pointer and finger input only if it provides value.** For example, a scrubber can give people an additional way to target a location in a video when they’re using the pointer. In this scenario, people can drag the playhead using either the pointer or touch, but they can use the pointer to click a precise seek destination.

#### Pointer shape and content effects

iPadOS integrates the appearance and behavior of both the pointer and the element it moves over, bringing focus to the item the pointer is targeting. You can support the system-provided pointer effects or modify them to suit your experience.

By default, the pointer’s shape is a circle, but it can display a system-defined or custom shape when people move it over specific elements or regions. For example, the pointer automatically uses the familiar I-beam shape when people move it over a text-entry area.

With a *content effect*, the UI element or region beneath the pointer can also change its appearance when people hold the pointer over it. Depending on the type of content effect, the pointer can retain its current shape or transform into a shape that integrates with the element’s new appearance.

iPadOS defines three content effects that bring focus to different types of interactive elements in your app: highlight, lift, and hover.

The *highlight* effect transforms the pointer into a translucent, rounded rectangle that acts as a background for a control and includes a gentle parallax. The subtle highlighting and movement bring focus to the control without distracting people from their task. By default, iPadOS applies the highlight effect to bar buttons, tab bars, segmented controls, and edit menus.

The *lift* effect combines a subtle parallax with the appearance of elevation to make an element seem like it’s floating above the screen. As the pointer fades out beneath the element, iPadOS creates the illusion of lift by scaling the element up while adding a shadow below it and a soft specular highlight on top of it. By default, iPadOS applies the lift effect to app icons and to buttons in Control Center.

*Hover* is a generic effect that lets you apply custom scale, tint, or shadow values to an element as the pointer moves over it. The hover effect combines your custom values to bring focus to an item, but it doesn’t transform the default pointer shape.

#### Pointer accessories

Pointer accessories are visual indicators that help people understand how they can use the pointer to interact with the current UI element. For example, a pointer approaching a resizable element might display small arrows to indicate that the element allows resizing along a certain axis.

Unlike pointer shapes and content effects, accessories are secondary items that can combine with any pointer to communicate additional information. For developer guidance, see [UIPointerAccessory](https://developer.apple.com/documentation/UIKit/UIPointerAccessory).

**Use clear, simple images to create custom accessories.** A pointer accessory is small, so it’s essential to create an image that communicates the pointer interaction without using too many details.

**Consider using the accessory transition to signal a change in an element’s state or behavior.** In addition to animating the appearance and disappearance of pointer accessories, the system also animates the transitions among accessory shapes and positions that can accompany content effects. For example, you could communicate that an add action has become unavailable by transitioning the pointer accessory from the `plus` symbol to the `circle.slash` symbol.

#### Pointer magnetism

iPadOS helps people use the pointer to target an element by making the element appear to attract the pointer. People can experience this magnetic effect when they move the pointer close to an element and when they flick the pointer toward an element.

When people move the pointer close to an element, the system starts transforming the pointer’s shape as soon as it reaches the element’s hit region. Because an element’s hit region typically extends beyond its visible boundaries, the pointer begins to transform before it appears to touch the element itself, creating the illusion that the element is pulling the pointer toward it.

When people flick the pointer toward an element, iPadOS examines the pointer’s trajectory to discover the element that’s the most likely target. When there’s an element in the pointer’s path, the system uses magnetism to pull the pointer toward the element’s center.

By default, iPadOS applies magnetism to elements that use the lift effect (like app icons) and the highlight effect (like bar buttons), but not to elements that use hover. Because an element that supports hover doesn’t transform the default pointer shape, adding magnetism could be jarring and might make people feel that they’ve lost control of the pointer.

The system also applies magnetism to text-entry areas, where it can help people avoid skipping to another line if they make unintended vertical movements while they’re selecting text.

#### Standard pointers and effects

**When possible, support the system-provided content effects.** People quickly become accustomed to the content effects they see throughout the system and generally expect their experience to apply to every app they use. To provide a consistent user experience, align your interactions with the design intent of each effect. Specifically:

- Use highlight for a small element that has a transparent background.
- Use lift for a small element that has an opaque background.
- Use hover for large elements and customize the scale, tint, and shadow attributes as needed (for guidance, see [Customizing pointers](https://developer.apple.com/design/human-interface-guidelines/pointing-devices#Customizing-pointers)).

**Prefer the system-provided pointer appearances for standard buttons and text-entry areas.** You can help people feel more comfortable with your app when the pointer behaves in ways they expect.

**Add padding around interactive elements to create comfortable hit regions.** You might need to experiment to determine the right size for an element’s hit region. If the hit region is too small, it can make people feel that they have to be extra precise when interacting with the element. On the other hand, when an element’s hit region is too large, people can feel that it takes a lot of effort to pull the pointer away from the element. In general, it works well to add about 12 points of padding around elements that include a bezel; for elements without a bezel, it works well to add about 24 points of padding around the element’s visible edges.

![An illustration of a button that has a filled, rounded-rectangle bezel. The button is centered on top of a shaded rectangle that extends beyond the button by the same distance on all sides. Centered on each side, a callout indicates that the padding between the button and each edge of the shaded rectangle is 12 points.](https://docs-assets.developer.apple.com/published/3993cfe0b8ec1f79e7c27496d92b240e/padding-for-button-with-bezel%402x.png)

![An illustration of a symbol centered on top of a shaded rectangle that extends beyond the symbol by the same distance on all sides. Centered on each side, a callout indicates that the padding between the symbol and each edge of the shaded rectangle is 24 points.](https://docs-assets.developer.apple.com/published/58bee8289c0508cc5b9e83f030925cb6/padding-for-glyph%402x.png)

![An illustration of a button without a bezel, centered on top of a shaded rectangle that extends beyond the button by the same distance on all sides. Centered on each side, a callout indicates that the padding between the button and each edge of the shaded rectangle is 24 points.](https://docs-assets.developer.apple.com/published/5a79ca3d0a9d4bbd3bf71c23bf8c5da3/padding-for-button-without-bezel%402x.png)

**Create contiguous hit regions for custom bar buttons.** If there’s space between the hit regions of adjacent buttons in a bar, people may experience a distracting motion when the pointer reverts briefly to its default shape as it moves between buttons.

**Specify the corner radius of a nonstandard element that receives the lift effect.** With the system-provided lift effect, the pointer transforms to match the element’s shape as it fades out. By default, the pointer uses the system-defined corner radius to transform into a rounded rectangle. If your element is a different shape — if it’s a circle, for example — you need to provide the radius so the pointer can animate seamlessly into the shape of the element. For developer guidance, see [UIPointerShape.roundedRect(_:radius:)](https://developer.apple.com/documentation/UIKit/UIPointerShape-swift.enum/roundedRect(_:radius:)).

#### Customizing pointers

**Prefer system-provided pointer effects for custom elements that behave like standard elements.** When a custom element behaves like a standard one, people generally expect to interact with it using familiar pointer interactions. For example, if buttons in a custom toolbar don’t use the standard highlight effect, people might think they’re broken.

**Use pointer effects in consistent ways throughout your app.** For example, if your app helps people draw, provide a similar pointer experience for every drawing area in your app so that people can apply the knowledge they gain in one area to the others.

**Avoid creating gratuitous pointer and content effects.** People notice when the appearance of the pointer or the UI element beneath it changes, and they expect the changes to be useful. Creating a purely decorative pointer effect can distract and even irritate people without providing any practical value.

**Keep custom pointer shapes simple.** Ideally, the pointer’s shape signals the action people can take in the current context without drawing too much attention to itself. If people don’t instantly understand your custom pointer shape, they’re likely to waste time trying to discover what the shape means.

**Consider enhancing the pointer experience by displaying custom annotations that provide useful information.** For example, you could display X and Y values when people hold the pointer over a graphing area in your app. Keynote uses annotations to display the current width and height of a resizable image.

![An illustration of a custom pointer hovering over a resize handle on the edge of a shaded rectangle. Above the pointer is a small annotation that displays the image’s width and height values against a dark background.](https://docs-assets.developer.apple.com/published/291aebad59eee8712e94047fcca4e7cf/useful-pointer-annotation%402x.png)

**Avoid displaying instructional text with a pointer.** A pointer that displays instructional text can make an app seem complicated and difficult to use. Instead of providing instructions, prioritize clarity and simplicity in your interface, so that people can quickly grasp how to use your app whether they’re using the pointer or touching the screen.

**Consider the interplay of shadow, scale, and element spacing when defining custom hover effects.** In general, reserve scaling for elements that can increase in size without crowding nearby elements. For example, scaling doesn’t work well for a table row because a row can’t expand without overlapping adjacent rows. For an element that has little space around it, consider using a hover effect that includes tint, but not scale and shadow. Note that it doesn’t work well to use shadow without including scale, because an unscaled element doesn’t appear to get closer to the viewer even when its shadow implies that it’s elevated above the screen.

---

## Pop-up buttons

Full page: `references/pop-up-buttons.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons

**Within a popover or modal view, consider using a pop-up button instead of a disclosure indicator to present multiple options for a list item.** For example, people can quickly choose an option from the pop-up button’s menu without navigating to a detail view. Consider using a pop-up button in this scenario when you have a fairly small, well-defined set of options that work well in a menu.

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

*(upstream heading: iPadOS, macOS)*

The placement and behavior of the search field in iPadOS and macOS is similar. If your app is available on both iPad and Mac, try to keep the search experience as consistent as possible across both platforms.

![An illustration of an iPad screen with a search field on the trailing edge of the top toolbar. The search field has the word Design entered into the field, and three search suggestions appear in a list beneath the field.](https://docs-assets.developer.apple.com/published/01e4b658632c116aba99bfab9116e252/search-fields-toolbar-search-ipad%402x.png)

![An illustration of a Mac screen with a search field on the trailing edge of the toolbar. The search field has the word Design entered into the field, and three search suggestions appear in a list beneath the field.](https://docs-assets.developer.apple.com/published/7a365ba6d24529c8274e67933bc09cd2/search-fields-toolbar-search-mac%402x.png)

**Put a search field at the trailing side of the toolbar for many common uses.** Many apps benefit from the familiar pattern of search in the toolbar, particularly apps with split views that need to search across multiple columns of information, like Mail, Notes, and Voice Memos. This placement makes great use of space because it lets people navigate results while keeping their selection visible in the detail view. Additionally, consider placing search in the toolbar if results appear in the detail view of your app, like in Freeform, where search in the toolbar filters the boards in the detail view below.

**Include search at the top of the sidebar when filtering content or navigation there.** Apps such as Settings take advantage of search to quickly filter the sidebar and expose sections that may be multiple levels deep, providing a simple way for people to search, preview, and navigate to the section or setting they’re looking for. This approach is useful if your app has a rich detail view and you need to create a distinct separation between the sidebar you’re filtering and the adjacent view.

![An illustration of an iPad screen with a search field at the top of the sidebar on the leading edge of the screen.](https://docs-assets.developer.apple.com/published/e4e1484edf725bbfd2b3c2b6914fe1b1/search-fields-ipad-search-in-sidebar%402x.png)

**Include search as an item in the sidebar or tab bar when you want an area dedicated to discovery.** If your search is paired with rich suggestions, categories, or content that needs more space, it can be helpful to have a dedicated area for it. This is particularly useful for apps where browsing and search go hand in hand, like Music and TV, where it provides a unified location to highlight suggested content, categories, and recent searches. A dedicated area also ensures search is always available as people navigate and switch sections of your app.

![An illustration of an iPad screen with a tab bar at the top edge. The trailing side of the tab bar includes a Search tab with a distinct background color to differentiate it from other tab areas.](https://docs-assets.developer.apple.com/published/b1d4ba4043901d200c27a038279109bc/search-fields-ipad-search-in-tab-bar%402x.png)

**In a search field in a dedicated area, consider immediately focusing the field when a person navigates to the area to help them search faster and locate the field more easily.** An exception to this is on iPad when only a virtual keyboard is available, in which case it’s better to leave the field unfocused to prevent the keyboard from unexpectedly covering the view.

**Account for window resizing with the placement of the search field.** On iPad, the search field fluidly resizes with the app window like it does on Mac. However, for compact views on iPad, itʼs important to ensure that search is available where it’s most contextually useful. For example, Notes and Mail place search above the column for the content list when they resize down to a compact view.

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

In iPadOS, a split view can include either two vertical panes, like Mail, or three vertical panes, like Keynote.

**Account for narrow, compact, and intermediate window widths.** Since iPad windows are fluidly resizable, it’s important to consider the design of a split view layout at multiple widths. In particular, ensure that it’s possible to navigate between the various panes in a logical way. For guidance, see [Layout](https://developer.apple.com/design/human-interface-guidelines/layout). For developer guidance, see [NavigationSplitView](https://developer.apple.com/documentation/SwiftUI/NavigationSplitView) and [UISplitViewController](https://developer.apple.com/documentation/UIKit/UISplitViewController).

---

## Tab bars

Full page: `references/tab-bars.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/tab-bars

The system displays a tab bar near the top of the screen. You can choose to have the tab bar appear as a fixed element, or with a button that converts it to a sidebar. For developer guidance, see [tabBarOnly](https://developer.apple.com/documentation/SwiftUI/TabViewStyle/tabBarOnly) and [sidebarAdaptable](https://developer.apple.com/documentation/SwiftUI/TabViewStyle/sidebarAdaptable).

> **Note:** To present a sidebar without the option to convert it to a tab bar, use a [navigation split view](https://developer.apple.com/documentation/swiftui/navigationsplitview) instead of a tab view. For guidance, see [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars).

**Prefer a tab bar for navigation.** A tab bar provides access to the sections of your app that people use most. If your app is more complex, you can provide the option to convert the tab bar to a sidebar so people can access a wider set of navigation options.

**Let people customize the tab bar.** In apps with a lot of sections that people might want to access, it can be useful to let people select items that they use frequently and add them to the tab bar, or remove items that they use less frequently. For example, in the Music app, a person can choose a favorite playlist to display in the tab bar. If you let people select their own tabs, aim for a default list of five or fewer to preserve continuity between compact and regular view sizes. For developer guidance, see [TabViewCustomization](https://developer.apple.com/documentation/SwiftUI/TabViewCustomization) and [UITab.Placement](https://developer.apple.com/documentation/UIKit/UITab/Placement).

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

## The menu bar

Full page: `references/the-menu-bar.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/the-menu-bar

The menu bar displays the top-level menus for your app or game, including both system-provided menus and any custom ones you choose to add. People reveal the menu bar by moving the pointer to the top edge of the screen, or swiping down from it. When visible, the menu bar occupies the same vertical space as the [Status bars](https://developer.apple.com/design/human-interface-guidelines/status-bars) at the top edge of the screen.

As with the macOS menu bar, the iPadOS menu bar provides a familiar way for people to learn what an app does, find the commands they need, and discover keyboard shortcuts.  While they are similar in most respects, there are a few key differences between the menu bars on each platform.

|  | iPadOS | macOS |
| --- | --- | --- |
| Menu bar visibility | Hidden until revealed | Visible by default |
| Horizontal alignment | Centered | Leading side |
| Menu bar extras | Not available | System default and custom |
| Window controls | In the menu bar when the app is full screen | Never in the menu bar |
| Apple menu | Not available | Always available |
| App menu | About, Services, and app visibility-related items not available | Always available |

**Because the menu bar is often hidden when running an app full screen, ensure that people can access all of your app’s functions through its UI.**  In particular, always offer other ways to accomplish tasks assigned to dynamic menu items, since these are only available when a hardware keyboard is connected. Avoid using the menu bar as a catch-all location for functionality that doesn’t fit in elsewhere.

**Reserve the YourAppName > Settings menu item for opening your app’s page in iPadOS Settings.** If your app includes its own internal preferences area, link to it with a separate menu item beneath Settings in the same group. Place any other custom app-wide configuration options in this section as well.

**For apps with tab-style navigation, consider adding each tab as a menu item in the View menu.** Since each tab is a different view of the app, the View menu is a natural place to offer an additional way to navigate between tabs. If you do this, consider assigning key bindings to each tab to make navigation even more convenient.

**Consider grouping menu items into submenus to conserve vertical space.** Menu item rows on iPad use more space than on Mac to make them easier to tap. Because of this, and the smaller screen sizes of some iPads, it can be helpful to group related items into submenus more frequently than in the menu bar on Mac.

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

**Consider combining a toolbar with a tab bar.** In iPadOS, a toolbar and a [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) can coexist in the same horizontal space at the top of the view. This is particularly useful for layouts where you want to navigate between a few main app areas while keeping the full width of the window available for content. For guidance, see [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) and [Windows](https://developer.apple.com/design/human-interface-guidelines/windows).

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

## Windows

Full page: `references/windows.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/windows

Windows present in one of two ways depending on a person’s choice in Multitasking & Gestures settings.

- **Full screen.** App windows fill the entire screen, and people switch between them — or between multiple windows of the same app — using the app switcher.
- **Windowed.** People can freely resize app windows. Multiple windows can be onscreen at once, and people can reposition them and bring them to the front. The system remembers window size and placement even when an app is closed.

**Make sure window controls don’t overlap toolbar items.** When windowed, app windows include window controls at the leading edge of the toolbar. If your app has toolbar buttons at the leading edge, they might be hidden by window controls when they appear. To prevent this, instead of placing buttons directly on the leading edge, move them inward when the window controls appear.

**Consider letting people use a gesture to open content in a new window.** For example, people can use the pinch gesture to expand a Notes item into a new window. For developer guidance, see [collectionView(_:sceneActivationConfigurationForItemAt:point:)](https://developer.apple.com/documentation/UIKit/UICollectionViewDelegate/collectionView(_:sceneActivationConfigurationForItemAt:point:)) (to transition from a collection view item), or [UIWindowScene.ActivationInteraction](https://developer.apple.com/documentation/UIKit/UIWindowScene/ActivationInteraction) (to transition from an item in any other view).

> **Tip:** If you only need to let people view one file, you can present it without creating your own window, but you must support multiple windows in your app. For developer guidance, see [QLPreviewSceneActivationConfiguration](https://developer.apple.com/documentation/QuickLook/QLPreviewSceneActivationConfiguration).

---
