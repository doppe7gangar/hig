# What changes per platform

The HIG documents a component once and lists its platform exceptions in a 'Platform considerations' section. Those exceptions are collected here, by platform, so adapting a design to another Apple platform is one lookup rather than 178.

A topic absent from a platform's section means the HIG states no exception for it — the general rule applies. That's a real answer, not a gap.

---

## iOS

### Action button
<sub>`pages/action-button.md`</sub>

**Let people use your actions without leaving their current context.** When possible, make use of lightweight multitasking capabilities like [Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities) and custom snippets to provide functionality without opening your app. For example, the “Set Timer” action doesn’t launch the Clock app; it prompts people to set a duration for the timer, and then launches a Live Activity with the countdown.

### Action sheets
<sub>`pages/action-sheets.md` — upstream heading: iOS, iPadOS</sub>

**Use an action sheet — not a menu — to provide choices related to an action.** People are accustomed to having an action sheet appear when they perform an action that might require clarifying choices. In contrast, people expect a menu to appear when they choose to reveal it.

**Avoid letting an action sheet scroll.** The more buttons an action sheet has, the more time and effort it takes for people to make a choice. Also, scrolling an action sheet can be hard to do without inadvertently tapping a button.

### Activity rings
<sub>`pages/activity-rings.md`</sub>

Activity rings are available in iOS with [HKActivityRingView](https://developer.apple.com/documentation/healthkitui/hkactivityringview). The appearance of the Activity ring element changes automatically depending on whether an Apple Watch is paired:

- With an Apple Watch paired, iOS shows all three Activity rings.
- Without an Apple Watch paired, iOS shows the Move ring only, which represents an approximation of a person’s activity based on their steps and workout information from other apps.

![A screenshot of the Activity summary in the iOS Fitness app with Apple Watch paired. All three Activity rings are displayed.](/images/com.apple.HIG/activity-rings-watch-paired@2x.png)

![A screenshot of the Activity summary in the iOS Fitness app with no Apple Watch paired. Only the Move ring is displayed.](/images/com.apple.HIG/activity-rings-no-watch-paired@2x.png)

Because iOS shows Activity rings whether or not an Apple Watch is paired, activity history can include a combination of both styles. For example, Activity rings in Fitness have three rings when a person exercises with their Apple Watch paired, and only the Move ring when they exercise without their Apple Watch.

### Alerts
<sub>`pages/alerts.md` — upstream heading: iOS, iPadOS</sub>

**Use an action sheet — not an alert — to offer choices related to an intentional action.** For example, when people cancel the Mail message they’re editing, an action sheet provides three choices: delete the edits (or the entire draft), save the draft, or return to editing. Although an alert can also help people confirm or cancel an action that has destructive consequences, it doesn’t provide additional choices related to the action. For guidance, see [Action sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets).

**When possible, avoid displaying an alert that scrolls.** Although an alert might scroll if the text size is large enough, be sure to minimize the potential for scrolling by keeping alert titles short and including a brief message only when necessary.

### App Shortcuts
<sub>`pages/app-shortcuts.md` — upstream heading: iOS, iPadOS</sub>

App Shortcuts can appear in the Top Hit area of Spotlight when people search for your app, or in the Shortcuts area below. Each App Shortcut includes a symbol from [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) that you choose to represent its functionality, or a preview image of an item that the shortcut links to directly.

**Order shortcuts based on importance.** The order you choose determines how App Shortcuts initially appear in both Spotlight and the Shortcuts app, so it’s helpful to include the most generally useful ones first. Once people start using your App Shortcuts, the system updates to prioritize the ones they use most frequently.

### Boxes
<sub>`pages/boxes.md` — upstream heading: iOS, iPadOS</sub>

By default, iOS and iPadOS use the secondary and tertiary background [colors](https://developer.apple.com/design/human-interface-guidelines/color) in boxes.

### Buttons
<sub>`pages/buttons.md` — upstream heading: iOS, iPadOS</sub>

**Configure a button to display an activity indicator when you need to provide feedback about an action that doesn’t instantly complete.** Displaying an activity indicator within a button can save space in your user interface while clearly communicating the reason for the delay. To help clarify what’s happening, you can also configure the button to display a different label alongside the activity indicator. For example, the label “Checkout” could change to “Checking out…” while the activity indicator is visible. When a delay occurs after people click or tap your configured button, the system displays the activity indicator next to the original or alternative label, hiding the button image, if there is one.

![An illustration of a button labeled Checkout.](/images/com.apple.HIG/button-activity-indicator-hidden@2x.png)

![An illustration of a button labeled Checking out, with an activity indicator on the leading side of the label.](/images/com.apple.HIG/button-activity-indicator-visible@2x.png)

### Collections
<sub>`pages/collections.md` — upstream heading: iOS, iPadOS</sub>

**Use caution when making dynamic layout changes.** The layout of a collection can change dynamically. Be sure any changes make sense and are easy to track. If possible, try to avoid changing the layout while people are viewing and interacting with it, unless it’s in response to an explicit action.

### Color
<sub>`pages/color.md` — upstream heading: iOS, iPadOS</sub>

iOS defines two sets of dynamic background colors — *system* and *grouped* — each of which contains primary, secondary, and tertiary variants that help you convey a hierarchy of information. In general, use the grouped background colors ([systemGroupedBackground](https://developer.apple.com/documentation/uikit/uicolor/systemgroupedbackground), [secondarySystemGroupedBackground](https://developer.apple.com/documentation/uikit/uicolor/secondarysystemgroupedbackground), and [tertiarySystemGroupedBackground](https://developer.apple.com/documentation/uikit/uicolor/tertiarysystemgroupedbackground)) when you have a grouped table view; otherwise, use the system set of background colors ([systemBackground](https://developer.apple.com/documentation/uikit/uicolor/systembackground), [secondarySystemBackground](https://developer.apple.com/documentation/uikit/uicolor/secondarysystembackground), and [tertiarySystemBackground](https://developer.apple.com/documentation/uikit/uicolor/tertiarysystembackground)).

With both sets of background colors, you generally use the variants to indicate hierarchy in the following ways:

- Primary for the overall view
- Secondary for grouping content or elements within the overall view
- Tertiary for grouping content or elements within secondary elements

For foreground content, iOS defines the following dynamic colors:

| Color | Use for… | UIKit API |
| --- | --- | --- |
| Label | A text label that contains primary content. | [label](https://developer.apple.com/documentation/uikit/uicolor/label) |
| Secondary label | A text label that contains secondary content. | [secondaryLabel](https://developer.apple.com/documentation/uikit/uicolor/secondarylabel) |
| Tertiary label | A text label that contains tertiary content. | [tertiaryLabel](https://developer.apple.com/documentation/uikit/uicolor/tertiarylabel) |
| Quaternary label | A text label that contains quaternary content. | [quaternaryLabel](https://developer.apple.com/documentation/uikit/uicolor/quaternarylabel) |
| Placeholder text | Placeholder text in controls or text views. | [placeholderText](https://developer.apple.com/documentation/uikit/uicolor/placeholdertext) |
| Separator | A separator that allows some underlying content to be visible. | [separator](https://developer.apple.com/documentation/uikit/uicolor/separator) |
| Opaque separator | A separator that doesn’t allow any underlying content to be visible. | [opaqueSeparator](https://developer.apple.com/documentation/uikit/uicolor/opaqueseparator) |
| Link | Text that functions as a link. | [link](https://developer.apple.com/documentation/uikit/uicolor/link) |

### Context menus
<sub>`pages/context-menus.md` — upstream heading: iOS, iPadOS</sub>

**Provide either a context menu or an edit menu for an item, but not both.** If you provide both features for the same item, it can be confusing to people — and difficult for the system to detect their intent. See [Edit menus](https://developer.apple.com/design/human-interface-guidelines/edit-menus).

**In iPadOS, consider using a context menu to let people create a new object in your app.** iPadOS lets you reveal a context menu when people perform a long press on the touchscreen or use a secondary click with an attached trackpad or keyboard. For example, Files lets people create a new folder by revealing a context menu in an area between existing files and folders.

In iOS and iPadOS, a context menu can display a preview of the current content near the list of commands. People can choose a command in the menu or — in some cases — they can tap the preview to open it or drag it to another area.

**Prefer a graphical preview that clarifies the target of a context menu’s commands.** For example, when people reveal a context menu on a list item in Notes or Mail, the preview shows a condensed version of the actual content to help people confirm that they’re working with the item they intend.

**Ensure that your preview looks good as it animates.** As people reveal a context menu on an onscreen object, the system animates the preview image as it emerges from the content, dimming the screen behind the preview and the menu. It’s important to adjust the preview’s clipping path to match the shape of the preview image so that its contours, such as the rounded corners, don’t appear to change during animation. For developer guidance, see [UIContextMenuInteractionDelegate](https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate).

### Dark Mode
<sub>`pages/dark-mode.md` — upstream heading: iOS, iPadOS</sub>

In Dark Mode, the system uses two sets of background colors — called *base* and *elevated* — to enhance the perception of depth when one dark interface is layered above another. The base colors are dimmer, making background interfaces appear to recede, and the elevated colors are brighter, making foreground interfaces appear to advance.

![A diagram that shows a stack of 4 terms on top of a black background. The term at the top shows the most contrast with the background and the term at the bottom shows the least.](/images/com.apple.HIG/base-with-four-semantic-colors@2x.png)

![A diagram that shows a stack of 4 terms on top of a nearly black background. The term at the top shows the most contrast with the background and the term at the bottom shows the least.](/images/com.apple.HIG/elevated-with-four-semantic-colors@2x.png)

![A diagram that shows a stack of 4 terms on top of a white background. The term at the top shows the most contrast with the background and the term at the bottom shows the least.](/images/com.apple.HIG/light-with-four-semantic-colors@2x.png)

**Prefer the system background colors.** Dark Mode is dynamic, which means that the background color automatically changes from base to elevated when an interface is in the foreground, such as a popover or modal sheet. The system also uses the elevated background color to provide visual separation between apps in a multitasking environment and between windows in a multiple-window context. Using a custom background color can make it harder for people to perceive these system-provided visual distinctions.

### Disclosure controls
<sub>`pages/disclosure-controls.md` — upstream heading: iOS, iPadOS, visionOS</sub>

Disclosure controls are available in iOS, iPadOS, and visionOS with the SwiftUI [DisclosureGroup](https://developer.apple.com/documentation/swiftui/disclosuregroup) view.

### Drag and drop
<sub>`pages/drag-and-drop.md` — upstream heading: iOS, iPadOS</sub>

**Let people perform multiple simultaneous drag activities.** In iPadOS, people can sequentially add items to an in-progress drag session, gathering as many items as their fingers can handle. For example, people can select an app icon on the Home Screen, start dragging it, and select additional app icons before dropping all of them in a different Home Screen or in a folder. To support this interaction, you need to let people add items during a drag — providing visual feedback through flocking — and accept multiple, simultaneous drops.

### Edit menus
<sub>`pages/edit-menus.md` — upstream heading: iOS, iPadOS</sub>

**Ensure your edit menu works well in both styles.** The system displays the compact, horizontal style when people use Multi-Touch gestures to reveal the edit menu, and the vertical style when people use a keyboard or pointing device to reveal it. For guidance using the vertical menu layout, see [iOS, iPadOS](https://developer.apple.com/design/human-interface-guidelines/menus#iOS-iPadOS).

**Adjust an edit menu’s placement, if necessary.** Depending on available space, the default menu position is above or below the insertion point or selection. The system also displays a visual indicator that points to the targeted content. Although you can’t change the shape of the menu or its pointer, you can change the menu’s position. For example, you might need to move the menu to prevent it from covering important content or parts of your interface.

### File management
<sub>`pages/file-management.md` — upstream heading: iOS, iPadOS</sub>

If your app can share its files with other apps, you can create a file provider app extension that displays a custom interface for importing, exporting, opening, and moving your app’s documents. For developer guidance, see [File Provider](https://developer.apple.com/documentation/fileprovider). An *app extension* is code you provide that people can install and use to extend the functionality of a specific area of the system; to learn more, see [App extensions](https://developer.apple.com/app-extensions/).

**When someone uses your file provider extension to open or import documents, display only documents that are appropriate in the current context.** For example, if a PDF-editing app loads your extension, only list PDF files for opening or import. You might also want to display additional information, such as modification dates, sizes, and whether documents are local or remote.

**Let people select a destination when exporting and moving documents.** Unless your app stores documents in a single directory, let people navigate to a specific destination in your directory hierarchy. You could also provide a way to add new subdirectories.

**Avoid including a custom top toolbar.** Your extension loads within a modal view that already includes a toolbar. Providing a second toolbar is confusing and takes space away from your content.

Your app can also let people browse and open files from other apps. For developer guidance, see [Adding a document browser to your app](https://developer.apple.com/documentation/uikit/adding-a-document-browser-to-your-app).

### File management
<sub>`pages/file-management.md` — upstream heading: iOS, iPadOS</sub>

Starting in iOS 18 and iPadOS 18, document-based apps can use the system’s document launcher to give people a consistent, highly graphical way to browse, open, and create files. The document launcher presents a full-screen experience that highlights key elements of your app’s theme, while making it easy for people to create new documents. For developer guidance, see [DocumentGroupLaunchScene](https://developer.apple.com/documentation/swiftui/documentgrouplaunchscene).

The document launcher consists of three main parts:

- A *title card* that displays the app title and two app-specific buttons
- A background image that appears behind the title card and additional images — called *accessories* — that can appear around it
- A sheet that contains a file browser and optional app-specific controls

You can customize all three parts of the document launcher. Although the system automatically displays your app name in the title card, you specify the text and functions of the card’s primary and secondary buttons. You can also create a custom background image, one or more accessory images to surround the title card, and provide some custom controls that can appear in the file browser’s toolbar.

![A screenshot of a writing app's document launcher on iPad in landscape orientation. The document launcher displays a custom background and two accessory images. At the bottom, the file browser sheet provides 3 tabs: Recents, Shared, and Browse.](/images/com.apple.HIG/file-management-document-launcher@2x.png)

**Assign the title card’s buttons to your app’s most important functions.** The primary button typically creates a new document, and the secondary button can provide additional options. For example, the primary button in Numbers is Start Writing and the secondary button is Choose a Template.

**Provide a background that’s clearly distinct from the accessories and title card.** You can use a solid color, a gradient, or a pattern. Avoid including complex images or patterns that might distract from foreground elements.

**Be mindful of accessory placement.** For example, you can place accessories both in front of and behind the title card to create the appearance of depth, but you need to make sure that your app name and both buttons remain clearly visible. Avoid cluttering the title card with too many accessories, and be sure to test its overall appearance across the range of screen sizes and device orientations that you support.

**Use animation sparingly.** Too much motion on the display can confuse or disorient people. If you want to animate your accessories, consider creating gentle, repeating animations that subtly highlight and enhance your app’s content. For example, you might create an animation that makes an accessory appear to breathe or sway softly. For guidance, see [Motion](https://developer.apple.com/design/human-interface-guidelines/motion).

### Gestures
<sub>`pages/gestures.md` — upstream heading: iOS, iPadOS</sub>

In addition to the [Standard gestures](https://developer.apple.com/design/human-interface-guidelines/gestures#Standard-gestures) supported in all platforms, iOS and iPadOS support a few other gestures that people expect.

| Gesture | Common action |
| --- | --- |
| Three-finger swipe | Initiate undo (left swipe); initiate redo (right swipe). |
| Three-finger pinch | Copy selected text (pinch in); paste copied text (pinch out). |
| Four-finger swipe (iPadOS only) | Switch between apps. |
| Shake | Initiate undo; initiate redo. |

**Consider allowing simultaneous recognition of multiple gestures if it enhances the experience.** Although simultaneous gestures are unlikely to be useful in nongame apps, a game might include multiple onscreen controls — such as a joystick and firing buttons — that people can operate at the same time. For guidance on integrating touchscreen input with Apple Pencil input in your iPadOS app, see [Apple Pencil and Scribble](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble).

### Going full screen
<sub>`pages/going-full-screen.md` — upstream heading: iOS, iPadOS</sub>

**Consider deferring system gestures to prevent accidental exits in a full-screen app or game.** By default, the Home Screen indicator automatically hides shortly after someone switches to your app or game. It reappears when someone interacts with the bottom portion of the screen, allowing them to swipe once to exit. Whenever possible, retain this behavior because it’s familiar and what people expect. If supporting this results in unexpected exits, you can enable two swipes rather than one to exit. For developer guidance, see [preferredScreenEdgesDeferringSystemGestures](https://developer.apple.com/documentation/swiftui/uihostingcontroller/preferredscreenedgesdeferringsystemgestures).

### Launching
<sub>`pages/launching.md` — upstream heading: iOS, iPadOS</sub>

**Launch in the appropriate orientation.** If your app or game supports both portrait and landscape modes, launch using the device’s current orientation. If your interface only runs in one orientation, launch in that orientation and let people rotate the device if necessary. Ensure a landscape-only interface responds correctly, regardless of whether people enter landscape orientation by rotating the device left or right. For guidance, see [Layout](https://developer.apple.com/design/human-interface-guidelines/layout).

### Layout
<sub>`pages/layout.md`</sub>

**Aim to support both portrait and landscape orientations.** People appreciate apps and games that work well in different device orientations, but sometimes your experience needs to run in only portrait or only landscape. When this is the case, you can rely on people trying both orientations before settling on the one you support — there’s no need to tell people to rotate their device. If your app or game is landscape-only, make sure it runs equally well whether people rotate their device to the left or the right.

**Prefer a full-bleed interface for your game.** Give players a beautiful interface that fills the screen while accommodating the corner radius, sensor housing, and features like Dynamic Island. If necessary, consider giving players the option to view your game using a letterboxed or pillarboxed appearance.

**Avoid full-width buttons.** Buttons feel at home in iOS when they respect system-defined margins and are inset from the edges of the screen. If you need to include a full-width button, make sure it harmonizes with the curvature of the hardware and aligns with adjacent safe areas.

**Hide the status bar only when it adds value or enhances your experience.** The status bar displays information people find useful and it occupies an area of the screen most apps don’t fully use, so it’s generally a good idea to keep it visible. The exception is if you offer an in-depth experience like playing a game or viewing media, where it might make sense to hide the status bar.

### Lists and tables
<sub>`pages/lists-and-tables.md` — upstream heading: iOS, iPadOS, visionOS</sub>

**Use an info button only to reveal more information about a row’s content.** An info button — called a *detail disclosure button* when it appears in a list row — doesn’t support navigation through a hierarchical table or list. If you need to let people drill into a list or table row’s subviews, use a disclosure indicator accessory control. For developer guidance, see [UITableViewCell.AccessoryType.disclosureIndicator](https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype-swift.enum/disclosureindicator).

![An illustration of a grouped list of rows. Each list item includes an info button at the trailing end of the row.](/images/com.apple.HIG/info-button-in-list@2x.png)

![An illustration of a grouped list of rows. Each list item includes a right-pointing chevron at the trailing end of the row.](/images/com.apple.HIG/disclosure-indicator-in-list@2x.png)

**Avoid adding an index to a table that displays controls — like disclosure indicators — in the trailing ends of its rows.** An *index* typically consists of the letters in an alphabet, displayed vertically at the trailing side of a list. People can jump to a specific section in the list by choosing the index letter that maps to it. Because both the index and elements like disclosure indicators appear on the trailing side of a list, it can be difficult for people to use one element without activating the other.

### Materials
<sub>`pages/materials.md` — upstream heading: iOS, iPadOS</sub>

In addition to Liquid Glass, iOS and iPadOS continue to provide four standard materials — ultra-thin, thin, regular (default), and thick — which you can use in the content layer to help create visual distinction.

![An illustration of the iOS and iPadOS ultraThin material above a colorful background. Where the material overlaps the background, it provides a diffuse gradient of the background colors.](/images/com.apple.HIG/materials-ios-material-background-ultrathin@2x.png)

![An illustration of the iOS and iPadOS thin material above a colorful background. Where the material overlaps the background, it provides a diffuse and slightly darkened gradient of the background colors.](/images/com.apple.HIG/materials-ios-material-background-thin@2x.png)

![An illustration of the iOS and iPadOS regular material above a colorful background. Where the material overlaps the background, it provides a diffuse and darkened gradient of the background colors.](/images/com.apple.HIG/materials-ios-material-background-regular@2x.png)

![An illustration of the iOS and iPadOS thick material above a colorful background. Where the material overlaps the background, it provides a dark, muted gradient of the background colors.](/images/com.apple.HIG/materials-ios-material-background-thick@2x.png)

iOS and iPadOS also define vibrant colors for labels, fills, and separators that are specifically designed to work with each material. Labels and fills both have several levels of vibrancy; separators have one level. The name of a level indicates the relative amount of contrast between an element and the background: The default level has the highest contrast, whereas quaternary (when it exists) has the lowest contrast.

Except for quaternary, you can use the following vibrancy values for labels on any material. In general, avoid using quaternary on top of the [thin](https://developer.apple.com/documentation/swiftui/material/thin) and [ultraThin](https://developer.apple.com/documentation/swiftui/material/ultrathin) materials, because the contrast is too low.

- [UIVibrancyEffectStyle.label](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/label) (default)
- [UIVibrancyEffectStyle.secondaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/secondarylabel)
- [UIVibrancyEffectStyle.tertiaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/tertiarylabel)
- [UIVibrancyEffectStyle.quaternaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/quaternarylabel)

You can use the following vibrancy values for fills on all materials.

- [UIVibrancyEffectStyle.fill](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/fill) (default)
- [UIVibrancyEffectStyle.secondaryFill](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/secondaryfill)
- [UIVibrancyEffectStyle.tertiaryFill](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/tertiaryfill)

The system provides a single, default vibrancy value for a [UIVibrancyEffectStyle.separator](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/separator), which works well on all materials.

### Menus
<sub>`pages/menus.md` — upstream heading: iOS, iPadOS</sub>

In iOS and iPadOS, a menu can display items in one of the following three layouts.

![A diagram showing small, medium, and large menu layouts, each containing the same set of menu items.](/images/com.apple.HIG/small-medium-large-menu-layouts@2x.png)

- **Small.** A row of four items appears at the top of the menu, above a list that contains the remaining items. For each item in the top row, the menu displays a symbol or icon, but no label.
- **Medium.** A row of three items appears at the top of the menu, above a list that contains the remaining items. For each item in the top row, the menu displays a symbol or icon above a short label.
- **Large (the default).** The menu displays all items in a list.

For developer guidance, see [preferredElementSize](https://developer.apple.com/documentation/uikit/uimenu/preferredelementsize).

**Choose a small or medium menu layout when it can help streamline people’s choices.** Consider using the medium layout if your app has three important actions that people often want to perform. For example, Notes uses the medium layout to give people a quick way to perform the Scan, Lock, and Pin actions. Use the small layout only for closely related actions that typically appear as a group, such as Bold, Italic, Underline, and Strikethrough. For each action, use a recognizable symbol that helps people identify the action without a label.

### Multitasking
<sub>`pages/multitasking.md`</sub>

On iPhone, multitasking lets people use FaceTime or watch a video in Picture in Picture while they also use a different app.

![A screenshot of the app switcher on iPhone, showing four open apps.](/images/com.apple.HIG/multitasking-app-switcher-iphone@2x.png)

![A screenshot of Mail on iPhone, showing an individual email. On top of the email body content, a small image in the bottom-left corner shows the person currently in a FaceTime call.](/images/com.apple.HIG/multitasking-pip-iphone@2x.png)

### Nearby interactions
<sub>`pages/nearby-interactions.md`</sub>

On iPhone, Nearby Interaction APIs provide a peer device’s distance and direction.

### Page controls
<sub>`pages/page-controls.md` — upstream heading: iOS, iPadOS</sub>

A page control can adjust the appearance of indicators to provide more information about the list. For example, the control highlights the indicator of the current page so people can estimate the page’s relative position in the list. When there are more indicators than fit in the space, the control can shrink indicators at both sides to suggest that more pages are available.

![An illustration of a page control. The page control displays a total of 9 dots. The center 5 dots use the default size; the second and eighth dots are about half the default size and the first and ninth dots are about one quarter the default size. The center dot is filled, indicating the location of the current page in the list.](/images/com.apple.HIG/page-controls-many-indicators@2x.png)

People interact with page controls by tapping or scrubbing (to *scrub*, people touch the control and drag left or right). Tapping on the leading or trailing side of the current-page indicator reveals the next or previous page; in iPadOS, people can also use the pointer to target a specific indicator. Scrubbing opens pages in sequence, and scrubbing past the leading or trailing edge of the control helps people quickly reach the first or last page.

> **Note:** In the API, *tapping* is a *discrete interaction*, whereas *scrubbing* is a *continuous interaction*; for developer guidance, see [UIPageControl.InteractionState](https://developer.apple.com/documentation/uikit/uipagecontrol/interactionstate-swift.enum).

**Avoid animating page transitions during scrubbing.** People can scrub very quickly, and using the scrolling animation for every transition can make your app lag and cause distracting visual flashes. Use the animated scrolling transition only for tapping.

A page control can include a translucent, rounded-rectangle background appearance that provides visual contrast for the indicators. You can choose one of the following background styles:

- Automatic — Displays the background only when people interact with the control. Use this style when the page control isn’t the primary navigational element in the UI.
- Prominent — Always displays the background. Use this style only when the control is the primary navigational control in the screen.
- Minimal — Never displays the background. Use this style when you just want to show the position of the current page in the list and you don’t need to provide visual feedback during scrubbing.

For developer guidance, see [backgroundStyle](https://developer.apple.com/documentation/uikit/uipagecontrol/backgroundstyle-swift.property).

**Avoid supporting the scrubber when you use the minimal background style.** The minimal style doesn’t provide visual feedback during scrubbing. If you want to let people scrub a list of pages in your app, use the automatic or prominent background styles.

### Pickers
<sub>`pages/pickers.md` — upstream heading: iOS, iPadOS</sub>

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

**Compact**

![An illustration of a compact date picker, with a single inline row showing the currently selected date. The picker opens as a popover extending down from the row, and includes a full calendar month for choosing the date.](/images/com.apple.HIG/pickers-date-picker-compact-expanded@2x.png)

**Inline**

![An illustration of an inline date picker, titled 'Date'. A toggle at the top is switched on, and a calendar month for choosing the date appears below the title and toggle.](/images/com.apple.HIG/pickers-date-picker-inline-expanded@2x.png)

**Wheels**

![An illustration of an inline time picker, titled 'Time'. The currently selected time appears in the title row, and three vertical wheels appear below the title row for choosing the hour, minute, and AM or PM value.](/images/com.apple.HIG/pickers-time-picker-inline-wheel@2x.png)


**Use a compact date picker when space is constrained.** The compact style displays a button that shows the current value in your app’s accent color. When people tap the button, the date picker opens a modal view, providing access to a familiar calendar-style editor and time picker. Within the modal view, people can make multiple edits to dates and times before tapping outside the view to confirm their choices.

### Playing audio
<sub>`pages/playing-audio.md` — upstream heading: iOS, iPadOS</sub>

**Use the system’s sound services to play short sounds and vibrations.** For developer guidance, see [Audio Services](https://developer.apple.com/documentation/audiotoolbox/audio-services).

### Playing haptics
<sub>`pages/playing-haptics.md`</sub>

Impact haptics provide a physical metaphor you can use to complement a visual experience. For example, people might feel a tap when a view snaps into place or a thud when two heavy objects collide.

*(video: An animation that represents a single haptic pulse of a specific duration and strength by showing a bar of a specific size and playing an audio tone of a specific pitch. This particular pattern represents a light impact.)*

*(video: An animation that represents a single haptic pulse of a specific duration and strength by showing a bar of a specific size and playing an audio tone of a specific pitch. This particular pattern represents a medium impact.)*

*(video: An animation that represents a single haptic pulse of a specific duration and strength by showing a bar of a specific size and playing an audio tone of a specific pitch. This particular pattern represents a heavy impact.)*

*(video: An animation that represents a single haptic pulse of a specific duration and strength by showing a bar of a specific size and playing an audio tone of a specific pitch. This particular pattern represents a rigid impact.)*

*(video: An animation that represents a single haptic pulse of a specific duration and strength by showing a bar of a specific size and playing an audio tone of a specific pitch. This particular pattern represents a soft impact.)*

### Playing haptics
<sub>`pages/playing-haptics.md`</sub>

Notification haptics provide feedback about the outcome of a task or action, such as depositing a check or unlocking a vehicle.

*(video: An animation that represents a series of two haptic pulses of various durations and strengths by showing bars of different sizes and playing audio tones of different pitches. This particular pattern represents a success.)*

*(video: An animation that represents a series of two haptic pulses of various durations and strengths by showing bars of different sizes and playing audio tones of different pitches. This particular pattern represents a warning.)*

*(video: An animation that represents a series of four haptic pulses of various durations and strengths by showing bars of different sizes and playing audio tones of different pitches. This particular pattern represents an error.)*

### Playing haptics
<sub>`pages/playing-haptics.md`</sub>

On supported iPhone models, you can add haptics to your experience in the following ways:

- Use standard UI components — like [toggles](https://developer.apple.com/design/human-interface-guidelines/toggles), [sliders](https://developer.apple.com/design/human-interface-guidelines/sliders), and [pickers](https://developer.apple.com/design/human-interface-guidelines/pickers) — that play Apple-designed system haptics by default.
- When it makes sense, use a feedback generator to play one of several predefined haptic patterns in the categories of [notification](https://developer.apple.com/design/human-interface-guidelines/playing-haptics#Notification), [impact](https://developer.apple.com/design/human-interface-guidelines/playing-haptics#Impact), and [selection](https://developer.apple.com/design/human-interface-guidelines/playing-haptics#Selection) (for developer guidance, see [UIFeedbackGenerator](https://developer.apple.com/documentation/uikit/uifeedbackgenerator)).

### Playing haptics
<sub>`pages/playing-haptics.md`</sub>

Selection haptics provide feedback while the values of a UI element are changing.

*(video: An animation that represents a single haptic pulse of a specific duration and strength by showing a bar of a specific size and playing an audio tone of a specific pitch. This particular pattern represents a selection.)*

### Popovers
<sub>`pages/popovers.md` — upstream heading: iOS, iPadOS</sub>

**Avoid displaying popovers in compact views.** Make your app or game dynamically adjust its layout based on the size class of the content area. Reserve popovers for wide views; for compact views, use all available screen space by presenting information in a full-screen modal view like a sheet instead. For related guidance, see [Modality](https://developer.apple.com/design/human-interface-guidelines/modality).

### Progress indicators
<sub>`pages/progress-indicators.md` — upstream heading: iOS, iPadOS</sub>

A refresh control lets people immediately reload content, typically in a table view, without waiting for the next automatic content update to occur. A refresh control is a specialized type of activity indicator that’s hidden by default, becoming visible when people drag down the view they want to reload. In Mail, for example, people can drag down the list of Inbox messages to check for new messages.

![A screenshot of a refresh content control spinning while Mail checks for new messages.](/images/com.apple.HIG/refresh-controls@2x.png)

**Perform automatic content updates.** Although people appreciate being able to do an immediate content refresh, they also expect automatic refreshes to occur periodically. Don’t make people responsible for initiating every update. Keep data fresh by updating it regularly.

**Supply a short title only if it adds value.** Optionally, a refresh control can include a title. In most cases, this is unnecessary, as the animation of the control indicates that content is loading. If you do include a title, don’t use it to explain how to perform a refresh. Instead, provide information of value about the content being refreshed. A refresh control in Podcasts, for example, uses a title to tell people when the last podcast update occurred.

For developer guidance, see [UIRefreshControl](https://developer.apple.com/documentation/uikit/uirefreshcontrol).

### Pull-down buttons
<sub>`pages/pull-down-buttons.md` — upstream heading: iOS, iPadOS</sub>

> **Note:** You can also let people reveal a pull-down menu by performing a specific gesture on a button. For example, in iOS 14 and later, Safari responds to a touch and hold gesture on the Tabs button by displaying a menu of tab-related actions, like New Tab and Close All Tabs.

**Consider using a More pull-down button to present items that don’t need prominent positions in the main interface.** A More button can help you offer a range of items where space is constrained, but it can also hinder discoverability. Although people generally understand that a More button offers additional functionality related to the current context, the ellipsis icon doesn’t necessarily help them predict its contents. To design an effective More button, weigh the convenience of its size against its impact on discoverability to find a balance that works in your app.

![A screenshot of the Notes app on iPhone, open to a Notes document titled Nature Walks. The top toolbar includes a More button on the trailing edge.](/images/com.apple.HIG/menu-secondary-actions-collapsed@2x.png)

![A screenshot of the Notes app on iPhone, open to a Notes document titled Nature Walks. The More button in the top toolbar is expanded, revealing the More menu with additional funtionality.](/images/com.apple.HIG/menu-secondary-actions-expanded@2x.png)

### Scroll views
<sub>`pages/scroll-views.md` — upstream heading: iOS, iPadOS</sub>

**Consider showing a page control when a scroll view is in page-by-page mode.** [Page controls](https://developer.apple.com/design/human-interface-guidelines/page-controls) show how many pages, screens, or other chunks of content are available and indicates which one is currently visible. For example, Weather uses a page control to indicate movement between people’s saved locations. If you show a page control with a scroll view, don’t show the scrolling indicator on the same axis to avoid confusing people with redundant controls.

### Search fields
<sub>`pages/search-fields.md`</sub>

As an alternative to search in a tab bar, you can also place search in a toolbar either at the bottom or top of the screen.

- You can include search in a bottom toolbar either as an expanded field or as a toolbar button, depending on how much space is available. When someone taps it, it animates into a search field above the keyboard so they can begin typing.
- You can include search in a top toolbar, also called a navigation bar, where it appears as a toolbar button. When someone taps it, it animates into a search field that appears either above the keyboard or at the top if there isn’t space at the bottom.

![An illustration of an iPhone screen with search in a bottom toolbar. The search field is positioned in an isolated group between a Filter button on the leading edge and a Compose button on the trailing edge.](/images/com.apple.HIG/search-fields-ios-toolbar-with-items@2x.png)

![An illustration of an iPhone screen with search in a top toolbar. A Back button appears on the leading edge, and an Add button appears on the trailing edge. A button group with Search and More appears next to the Add button.](/images/com.apple.HIG/search-fields-ios-navigation-bar-item@2x.png)

**Place search at the bottom if there’s room.** You can either add a search field to an existing toolbar, or as a new toolbar where search is the only item. Search at the bottom is useful in any situation where search is a priority, since it keeps the search experience easy to reach. Examples of apps with search at the bottom in various toolbar layouts include Settings, where it’s the only item, and Mail and Notes, where it fits alongside other important controls.

**Place search at the top when itʼs important to defer to content at the bottom of the screen, or thereʼs no bottom toolbar.** Use search at the top in cases where covering the content might interfere with a primary function of the app. The Wallet app, for example, includes event passes in a stack at the bottom of the screen for easy access and viewing at a glance.

### Search fields
<sub>`pages/search-fields.md`</sub>

In some cases you might want your app to include a search field inline with content.

**Place search as an inline field when its position alongside the content it searches strengthens that relationship.** When you need to filter or search within a single view, it can be helpful to have search appear directly next to content to illustrate that the search applies to it, rather than globally. This pattern is useful if your app has more than one search field and if location plays a critical role in the scope of your search. For example, although the main search in the Music app is a tab, people can navigate to their library and use an inline search field to filter their songs and albums.

**When at the top, position an inline search field above the list it searches, and consider pinning it to the top toolbar when scrolling.** This helps keep it distinct from search that appears in other locations.

### Search fields
<sub>`pages/search-fields.md`</sub>

There are three main places you can position the entry point for search:

- As a tab in a tab bar
- In a toolbar at the bottom or top of the screen
- Directly inline with content

Where search makes the most sense depends on the layout, content, and navigation of your app.

### Search fields
<sub>`pages/search-fields.md`</sub>

You can place search as a tab in a tab bar, which keeps search visible and always available as people switch between the sections of your app. There are two styles of search tabs:

- **Standard tab.** This style displays the search tab uniformly with the rest of the tab bar. Tapping the search tab navigates people to a search landing page with a search field at the top.
- **Button appearance.** This style displays the search tab as a separate button and allows people to start searching immediately. Tapping the search tab brings focus to the search field and displays the keyboard.

![An illustration of a tab bar at the bottom of an iPhone screen. A tab for search appears as part of the tab bar.](/images/com.apple.HIG/search-fields-search-as-tab-standard@2x.png)

![An illustration of a tab bar at the bottom of an iPhone screen. A tab for search appears on the trailing edge as a separate button.](/images/com.apple.HIG/search-fields-search-as-tab-prominent@2x.png)

**Choose the standard tab style to provide suggestions, promote discovery, and encourage exploration.** This style of search tab creates a dedicated landing page for search, providing an opportunity to reveal any content or suggestions that might be helpful before someone taps the field to begin the search. This approach is great for an app with a variety of rich content that people might want to explore. For example, Apple TV uses this search tab style to present its various genres and categories, helping ground people in what’s available before they search.

**Choose the button appearance to help people quickly find what they need.** When someone interacts with this style of search tab, the keyboard immediately appears with the search field above it, ready to begin the search. This approach provides a more transient experience that brings people directly back to their previous tab after they exit search, and is ideal when you want search to resolve quickly and seamlessly.

### Segmented controls
<sub>`pages/segmented-controls.md` — upstream heading: iOS, iPadOS</sub>

**Consider a segmented control to switch between closely related subviews.** A segmented control can be useful as a way to quickly switch between related subviews. For example, the segmented control in Calendar’s New Event sheet switches between the subviews for creating a new event and a new reminder. For switching between completely separate sections of an app, use a [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) instead.

![A screenshot of the top half of the iOS Calendar app, showing the New Event sheet. A segmented control provides the ability to switch between adding a new event and a new reminder.](/images/com.apple.HIG/segmented-controls-calendar-new-event@2x.png)

### Sheets
<sub>`pages/sheets.md` — upstream heading: iOS, iPadOS</sub>

In iOS and iPadOS, for sheets with a single view, the Cancel button belongs on the leading edge of the top toolbar. When present, the Done button belongs on the trailing edge.

![An illustration of the top half of a sheet on iPhone. A Cancel button appears in the top-left corner of the view, and a Done button appears in the top-right corner.](/images/com.apple.HIG/sheets-buttons-placement-cancel-done@2x.png)

For sheets with a multi-step flow, the placement of buttons can vary across steps.

**First step**

![An illustration of the top half of a sheet on iPhone. A Cancel button appears in the top-left corner of the view, and an inactive Done button appears in the top-right corner.](/images/com.apple.HIG/sheets-buttons-placement-navigation-first-page@2x.png)

**Subsequent step**

![An illustration of the top half of a sheet on iPhone. A Back button appears in the top-left corner of the view, and an inactive Done button appears in the top-right corner.](/images/com.apple.HIG/sheets-buttons-placement-navigation-subsequent-page@2x.png)

**Final step**

![An illustration of the top half of a sheet on iPhone. A Back button appears in the top-left corner of the view, and a Done button appears in the top-right corner.](/images/com.apple.HIG/sheets-buttons-placement-navigation-final-page@2x.png)


A resizable sheet expands when people scroll its contents or drag the *grabber*, which is a small horizontal indicator that can appear at the top edge of a sheet. Sheets resize according to their *detents*, which are particular heights at which a sheet naturally rests. Designed for iPhone, detents specify particular heights at which a sheet naturally rests. The system defines two detents: *large* is the height of a fully expanded sheet and *medium* is about half of the fully expanded height. Sheets can have one or more custom detent values.

![An illustration showing an iPhone screen in portrait orientation containing a solid rounded rectangle that occupies almost all of the screen, representing a full-screen sheet. A rounded close button appears in the upper-left corner of the sheet.](/images/com.apple.HIG/sheets-large-detent@2x.png)

![An illustration showing an iPhone screen in portrait orientation containing a solid rounded rectangle that occupies half of the screen, representing a half-screen sheet. A rounded close button appears in the upper-left corner of the sheet.](/images/com.apple.HIG/sheets-medium-detent@2x.png)

Sheets automatically support the large detent. Adding the medium detent allows the sheet to rest at both heights, whereas specifying only medium prevents the sheet from expanding to full height. For developer guidance, see [detents](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/detents).

**In an iPhone app, consider supporting the medium detent to allow progressive disclosure of the sheet’s content.** For example, a share sheet displays the most relevant items within the medium detent, where they’re visible without resizing. To view more items, people can scroll or expand the sheet. In contrast, you might not want to support the medium detent if a sheet’s content is more useful when it displays at full height. For example, the compose sheets in Messages and Mail display only at full height to give people enough room to create content.

**Include a grabber in a resizable sheet.** A grabber shows people that they can drag the sheet to resize it; they can also tap it to cycle through the detents. In addition to providing a visual indicator of resizability, a grabber also works with VoiceOver so people can resize the sheet without seeing the screen. For developer guidance, see [prefersGrabberVisible](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/prefersgrabbervisible).

**Support swiping to dismiss a sheet.** People expect to swipe vertically to dismiss a sheet instead of tapping a dismiss button. If people have unsaved changes in the sheet when they begin swiping to dismiss it, use an action sheet to let them confirm their action.

**Prefer using the page or form sheet presentation styles in an iPadOS app.** Each style uses a default size for the sheet, centering its content on top of a dimmed background view and providing a consistent experience. For developer guidance, see [UIModalPresentationStyle](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle).

### Sidebars
<sub>`pages/sidebars.md` — upstream heading: iOS, iPadOS</sub>

When you use the [sidebarAdaptable](https://developer.apple.com/documentation/swiftui/tabviewstyle/sidebaradaptable) style of tab view to present a sidebar, you choose whether to display a sidebar or a tab bar when your app opens. Both variations include a button that people can use to switch between them. This style also adapts its appearance depending on the platform, and responds automatically to rotation and window resizing, providing a version of the control that’s appropriate to the width of the view.

> **Note:** To display a sidebar only, use [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview) to present a sidebar in the primary pane of a split view, or use [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller).

**Consider using a tab bar first.** A tab bar provides more space to feature content, and offers enough flexibility to navigate between many apps’ main areas. If you need to expose more areas than fit in a tab bar, the tab bar’s convertible sidebar-style appearance can provide access to content that people use less frequently. For guidance, see [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars).

**If necessary, apply the correct appearance to a sidebar.** If you’re not using SwiftUI to create a sidebar, you can use the [UICollectionLayoutListConfiguration.Appearance.sidebar](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebar) appearance of a collection view list layout. For developer guidance, see [UICollectionLayoutListConfiguration.Appearance](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum).

### Sliders
<sub>`pages/sliders.md` — upstream heading: iOS, iPadOS</sub>

**Don’t use a slider to adjust audio volume.** If you need to provide volume control in your app, use a volume view, which is customizable and includes a volume-level slider and a control for changing the active audio output device. For guidance, see [Playing audio](https://developer.apple.com/design/human-interface-guidelines/playing-audio).

### Split views
<sub>`pages/split-views.md`</sub>

**Prefer using a split view in a regular — not a compact — environment.** A split view needs horizontal space in which to display multiple panes. In a compact environment, such as iPhone in portrait orientation, it’s difficult to display multiple panes without wrapping or truncating the content, making it less legible and harder to interact with.

### Tab bars
<sub>`pages/tab-bars.md`</sub>

A tab bar floats above content at the bottom of the screen. Its items rest on a [Liquid Glass](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass) background that allows content beneath to peek through.

For tab bars with an attached accessory, like the MiniPlayer in Music, you can choose to minimize the tab bar and move the accessory inline with it when a person scrolls down. A person can exit the minimized state by tapping a tab or scrolling to the top of the view. For developer guidance, see [TabBarMinimizeBehavior](https://developer.apple.com/documentation/swiftui/tabbarminimizebehavior) and [UITabBarController.MinimizeBehavior](https://developer.apple.com/documentation/uikit/uitabbarcontroller/minimizebehavior).

![An illustration of the bottom half of an iPhone in portrait orientation, with the Music app open. The MiniPlayer is open above the tab bar at the bottom of the screen.](/images/com.apple.HIG/tab-bar-with-accessory-expanded@2x.png)

![An illustration of the bottom half of an iPhone in portrait orientation, with the Music app open. The tab bar is minimized into the currently open tab at the leading bottom corner of the screen, with the MiniPlayer at the bottom center, and the search tab in the trailing corner.](/images/com.apple.HIG/tab-bar-with-accessory-collapsed@2x.png)

A tab bar can include a dedicated search tab at the trailing end. For guidance, see [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields).

### Tab views
<sub>`pages/tab-views.md` — upstream heading: iOS, iPadOS</sub>

For similar functionality, consider using a [segmented control](https://developer.apple.com/design/human-interface-guidelines/segmented-controls) instead.

### Text fields
<sub>`pages/text-fields.md` — upstream heading: iOS, iPadOS</sub>

**Display a Clear button in the trailing end of a text field to help people erase their input.** When this element is present, people can tap it to clear the text field’s contents, without having to keep tapping the Delete key.

**Use images and buttons to provide clarity and functionality in text fields.** You can display custom images in both ends of a text field, or you can add a system-provided button, such as the Bookmarks button. In general, use the leading end of a text field to indicate a field’s purpose and the trailing end to offer additional features, such as bookmarking.

### Text views
<sub>`pages/text-views.md` — upstream heading: iOS, iPadOS</sub>

**Show the appropriate keyboard type.** Several different keyboard types are available, each designed to facilitate a different type of input. To streamline data entry, the keyboard you display when editing a text view needs to be appropriate for the type of content. For guidance, see [Virtual keyboards](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards).

### Toggles
<sub>`pages/toggles.md` — upstream heading: iOS, iPadOS</sub>

**Use the switch toggle style only in a list row.** You don’t need to supply a label in this situation because the content in the row provides the context for the state the switch controls.

**Change the default color of a switch only if necessary.** The default green color tends to work well in most cases, but you might want to use your app’s accent color instead. Be sure to use a color that provides enough contrast with the uncolored appearance to be perceptible.

![An illustration of two list rows, one with an active switch toggle and one with an inactive switch toggle. The active toggle is tinted green with the standard switch color.](/images/com.apple.HIG/toggles-ios-default-color@2x.png)

![An illustration of two list rows, one with an active switch toggle and one with an inactive switch toggle. The active toggle is tinted purple with a custom switch color.](/images/com.apple.HIG/toggles-ios-custom-color@2x.png)

**Outside of a list, use a button that behaves like a toggle, not a switch.** For example, the Phone app uses a toggle on the filter button to let users filter their recent calls.  The app adds a blue highlight to indicate when the toggle is active, and removes it when the toggle is inactive.

![A screenshot of the top half of the Phone app on iPhone, showing the filtered list of recent missed calls. The filter button in the top trailing corner has a blue highlight, indicating that the toggle is active.](/images/com.apple.HIG/toggles-ios-phone-filter-on@2x.png)

![A screenshot of the top half of the Phone app on iPhone, showing all recent calls. The filter button in the top trailing corner has no highlight, indicating that the toggle is inactive.](/images/com.apple.HIG/toggles-ios-phone-filter-off@2x.png)

**Avoid supplying a label that explains the button’s purpose.** The interface icon you create — combined with the alternative background appearances you supply — help people understand what the button does. For developer guidance, see [changesSelectionAsPrimaryAction](https://developer.apple.com/documentation/uikit/uibutton/changesselectionasprimaryaction).

### Toolbars
<sub>`pages/toolbars.md`</sub>

**Prioritize only the most important items for inclusion in the main toolbar area.** Because space is so limited, carefully consider which actions are essential to your app and include those first. Create a More menu to include additional items.

**Use a large title to help people stay oriented as they navigate and scroll.** By default, a large title transitions to a standard title as people begin scrolling the content, and transitions back to large when people scroll to the top, reminding them of their current location. For developer guidance, see [prefersLargeTitles](https://developer.apple.com/documentation/uikit/uinavigationbar/preferslargetitles).

### Typography
<sub>`pages/typography.md` — upstream heading: iOS, iPadOS</sub>

SF Pro is the system font in iOS and iPadOS. iOS and iPadOS apps can also use NY.

### Undo and redo
<sub>`pages/undo-and-redo.md` — upstream heading: iOS, iPadOS</sub>

**Avoid redefining standard gestures for undo and redo.** For example, people can use a three-finger swipe to initiate an undo or redo, or shake their iPhone. As with all standard gestures, redefining them in your interface runs the risk of confusing people and making your experience unpredictable.

**Briefly and precisely describe the operation to be undone or redone.** The undo and redo alert title automatically includes a prefix of “Undo ” or “Redo ” (including the trailing space). You need to provide an additional word or two that describes what’s being undone or redone, to appear after this prefix. For example, you might create alert titles such as “Undo Name” or “Redo Address Change.”

### Virtual keyboards
<sub>`pages/virtual-keyboards.md` — upstream heading: iOS, iPadOS</sub>

**Use the keyboard layout guide to make the keyboard feel like an integrated part of your interface.** Using the layout guide also helps you keep important parts of your interface visible while the virtual keyboard is onscreen. For developer guidance, see [Adjusting your layout with keyboard layout guide](https://developer.apple.com/documentation/uikit/adjusting-your-layout-with-keyboard-layout-guide).

![An illustration of an app layout on iPhone, showing two stacked text fields and a button above the keyboard.](/images/com.apple.HIG/ui-fully-visible@2x.png)

![A checkmark in a circle to indicate a correct example.](/images/com.apple.HIG/checkmark@2x.png)

![An illustration of an app layout on iPhone, showing two stacked text fields. The keyboard covers part of the bottom text field.](/images/com.apple.HIG/text-field-hidden@2x.png)

![An X in a circle to indicate an incorrect example.](/images/com.apple.HIG/crossout@2x.png)

![An illustration of an app layout on iPhone, showing two stacked text fields and a button above the keyboard. The keyboard covers part of the button.](/images/com.apple.HIG/button-hidden@2x.png)

![An X in a circle to indicate an incorrect example.](/images/com.apple.HIG/crossout@2x.png)

**Place custom controls above the keyboard thoughtfully.** Some apps position an input accessory view containing custom controls above the keyboard to offer app-specific functionality related to the data people are working with. For example, Numbers displays controls that help people apply standard or custom calculations to spreadsheet data. If your app offers custom controls that augment the keyboard, make sure they’re relevant to the current task. If other views in your app use Liquid Glass, or if your view looks out of place above the keyboard, apply Liquid Glass to the view that contains your controls to maintain consistency. If you use a standard toolbar to contain your controls, it automatically adopts Liquid Glass. Use the keyboard layout guide and standard padding to ensure the system positions your controls as expected within the view. For developer guidance, see [ToolbarItemPlacement](https://developer.apple.com/documentation/swiftui/toolbaritemplacement) (SwiftUI), [inputAccessoryView](https://developer.apple.com/documentation/uikit/uiresponder/inputaccessoryview) (UIKit), and [UIKeyboardLayoutGuide](https://developer.apple.com/documentation/uikit/uikeyboardlayoutguide) (UIKit).

### Widgets
<sub>`pages/widgets.md` — upstream heading: iOS, iPadOS</sub>

On iPhone in StandBy, the system displays two small system family widgets side-by-side, scaled up so they fill the Lock Screen. By supporting StandBy, you also ensure your widgets work well in CarPlay. CarPlay and StandBy widgets both use the small system family widget with the background removed and scaled up to best fit the grid on the Widgets screen. Glanceable information and large text are especially important in CarPlay to make your widget easy to read on a car’s display.

**Limit usage of rich images or color to convey meaning in StandBy.** Instead, make use of the additional space by scaling up and rearranging text so people can glance at the widget content from a greater distance. To seamlessly blend with the black background, don’t use background colors for your widget when it appears in StandBy.

**Correct usage**

![An image of iPhone in StandBy. It shows a Clock widget on the left that displays the time as 9:41 a.m. and a Weather widget set to Cupertino with the temperature at 70 degrees Fahrenheit on the right.](/images/com.apple.HIG/widgets-standby-removed-background-correct@2x.png)

![A checkmark in a circle to indicate correct usage.](/images/com.apple.HIG/checkmark@2x.png)

**Incorrect usage**

![An image of iPhone in StandBy. It shows a Clock widget on the left that displays the time as 9:41 a.m. and a Weather widget set to Cupertino with the temperature at 70 degrees Fahrenheit on the right. The Watch widget appears with the background removed and the Weather widget isn't optimized for StandBy.](/images/com.apple.HIG/widgets-standby-with-background-incorrect@2x.png)

![An X in a circle to indicate incorrect usage.](/images/com.apple.HIG/crossout@2x.png)


For developer guidance, see [Displaying the right widget background](https://developer.apple.com/documentation/widgetkit/displaying-the-right-widget-background).

On iPhone in StandBy in low-light conditions, the system renders widgets in a monochromatic look with a red tint.

![An image of iPhone in low-light conditions. It shows a Clock widget on the left that displays the time as 9:41 a.m. and a Weather widget set to Cupertino with the temperature at 70 degrees Fahrenheit on the right.](/images/com.apple.HIG/widgets-standby-low-light@2x.png)

### Widgets
<sub>`pages/widgets.md` — upstream heading: iOS, iPadOS</sub>

Widgets on the Lock Screen are functionally similar to watch complications and follow design principles for [Complications](https://developer.apple.com/design/human-interface-guidelines/complications) in addition to design principles for widgets. Provide useful information in your Lock Screen widget, and don’t treat it only as an additional way for people to launch into your app. In many cases, a design for complications also works well for widgets on the Lock Screen (and vice versa), so consider creating them in tandem.

Your app can offer widgets on the Lock Screen in three different shapes: as inline text that appears above the clock, and as circular and rectangular shapes that appear below the clock.

![A partial screenshot of the Lock Screen on iPhone that shows a Calendar widget and two Weather widgets below the time. From the left, the widgets are an inline text widget and two circular widgets.](/images/com.apple.HIG/widget-lock-screen-display-appearances@2x.png)

**Support the Always-On display on iPhone.** Devices with the Always-On display render widgets on the Lock Screen with reduced luminance. Use levels of gray that provide enough contrast in the Always-On display, and make sure your content remains legible.

For developer guidance, see [Creating accessory widgets and watch complications](https://developer.apple.com/documentation/widgetkit/creating-accessory-widgets-and-watch-complications).

**Offer Live Activities to show real-time updates.** Widgets don’t show real-time information. If your app allows people to track the progress of a task or event for a limited amount of time with frequent updates, consider offering Live Activities. Widgets and Live Activities use the same underlying frameworks and share design similarities. As a result, it can be a good idea to develop widgets and Live Activities in tandem and reuse code and design components for both features. For design guidance on Live Activities, see [Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities); for developer guidance, see [ActivityKit](https://developer.apple.com/documentation/activitykit).

## iPadOS

### Action sheets
<sub>`pages/action-sheets.md` — upstream heading: iOS, iPadOS</sub>

**Use an action sheet — not a menu — to provide choices related to an action.** People are accustomed to having an action sheet appear when they perform an action that might require clarifying choices. In contrast, people expect a menu to appear when they choose to reveal it.

**Avoid letting an action sheet scroll.** The more buttons an action sheet has, the more time and effort it takes for people to make a choice. Also, scrolling an action sheet can be hard to do without inadvertently tapping a button.

### Alerts
<sub>`pages/alerts.md` — upstream heading: iOS, iPadOS</sub>

**Use an action sheet — not an alert — to offer choices related to an intentional action.** For example, when people cancel the Mail message they’re editing, an action sheet provides three choices: delete the edits (or the entire draft), save the draft, or return to editing. Although an alert can also help people confirm or cancel an action that has destructive consequences, it doesn’t provide additional choices related to the action. For guidance, see [Action sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets).

**When possible, avoid displaying an alert that scrolls.** Although an alert might scroll if the text size is large enough, be sure to minimize the potential for scrolling by keeping alert titles short and including a brief message only when necessary.

### App Shortcuts
<sub>`pages/app-shortcuts.md` — upstream heading: iOS, iPadOS</sub>

App Shortcuts can appear in the Top Hit area of Spotlight when people search for your app, or in the Shortcuts area below. Each App Shortcut includes a symbol from [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) that you choose to represent its functionality, or a preview image of an item that the shortcut links to directly.

**Order shortcuts based on importance.** The order you choose determines how App Shortcuts initially appear in both Spotlight and the Shortcuts app, so it’s helpful to include the most generally useful ones first. Once people start using your App Shortcuts, the system updates to prioritize the ones they use most frequently.

### Boxes
<sub>`pages/boxes.md` — upstream heading: iOS, iPadOS</sub>

By default, iOS and iPadOS use the secondary and tertiary background [colors](https://developer.apple.com/design/human-interface-guidelines/color) in boxes.

### Buttons
<sub>`pages/buttons.md` — upstream heading: iOS, iPadOS</sub>

**Configure a button to display an activity indicator when you need to provide feedback about an action that doesn’t instantly complete.** Displaying an activity indicator within a button can save space in your user interface while clearly communicating the reason for the delay. To help clarify what’s happening, you can also configure the button to display a different label alongside the activity indicator. For example, the label “Checkout” could change to “Checking out…” while the activity indicator is visible. When a delay occurs after people click or tap your configured button, the system displays the activity indicator next to the original or alternative label, hiding the button image, if there is one.

![An illustration of a button labeled Checkout.](/images/com.apple.HIG/button-activity-indicator-hidden@2x.png)

![An illustration of a button labeled Checking out, with an activity indicator on the leading side of the label.](/images/com.apple.HIG/button-activity-indicator-visible@2x.png)

### Collections
<sub>`pages/collections.md` — upstream heading: iOS, iPadOS</sub>

**Use caution when making dynamic layout changes.** The layout of a collection can change dynamically. Be sure any changes make sense and are easy to track. If possible, try to avoid changing the layout while people are viewing and interacting with it, unless it’s in response to an explicit action.

### Color
<sub>`pages/color.md` — upstream heading: iOS, iPadOS</sub>

iOS defines two sets of dynamic background colors — *system* and *grouped* — each of which contains primary, secondary, and tertiary variants that help you convey a hierarchy of information. In general, use the grouped background colors ([systemGroupedBackground](https://developer.apple.com/documentation/uikit/uicolor/systemgroupedbackground), [secondarySystemGroupedBackground](https://developer.apple.com/documentation/uikit/uicolor/secondarysystemgroupedbackground), and [tertiarySystemGroupedBackground](https://developer.apple.com/documentation/uikit/uicolor/tertiarysystemgroupedbackground)) when you have a grouped table view; otherwise, use the system set of background colors ([systemBackground](https://developer.apple.com/documentation/uikit/uicolor/systembackground), [secondarySystemBackground](https://developer.apple.com/documentation/uikit/uicolor/secondarysystembackground), and [tertiarySystemBackground](https://developer.apple.com/documentation/uikit/uicolor/tertiarysystembackground)).

With both sets of background colors, you generally use the variants to indicate hierarchy in the following ways:

- Primary for the overall view
- Secondary for grouping content or elements within the overall view
- Tertiary for grouping content or elements within secondary elements

For foreground content, iOS defines the following dynamic colors:

| Color | Use for… | UIKit API |
| --- | --- | --- |
| Label | A text label that contains primary content. | [label](https://developer.apple.com/documentation/uikit/uicolor/label) |
| Secondary label | A text label that contains secondary content. | [secondaryLabel](https://developer.apple.com/documentation/uikit/uicolor/secondarylabel) |
| Tertiary label | A text label that contains tertiary content. | [tertiaryLabel](https://developer.apple.com/documentation/uikit/uicolor/tertiarylabel) |
| Quaternary label | A text label that contains quaternary content. | [quaternaryLabel](https://developer.apple.com/documentation/uikit/uicolor/quaternarylabel) |
| Placeholder text | Placeholder text in controls or text views. | [placeholderText](https://developer.apple.com/documentation/uikit/uicolor/placeholdertext) |
| Separator | A separator that allows some underlying content to be visible. | [separator](https://developer.apple.com/documentation/uikit/uicolor/separator) |
| Opaque separator | A separator that doesn’t allow any underlying content to be visible. | [opaqueSeparator](https://developer.apple.com/documentation/uikit/uicolor/opaqueseparator) |
| Link | Text that functions as a link. | [link](https://developer.apple.com/documentation/uikit/uicolor/link) |

### Context menus
<sub>`pages/context-menus.md` — upstream heading: iOS, iPadOS</sub>

**Provide either a context menu or an edit menu for an item, but not both.** If you provide both features for the same item, it can be confusing to people — and difficult for the system to detect their intent. See [Edit menus](https://developer.apple.com/design/human-interface-guidelines/edit-menus).

**In iPadOS, consider using a context menu to let people create a new object in your app.** iPadOS lets you reveal a context menu when people perform a long press on the touchscreen or use a secondary click with an attached trackpad or keyboard. For example, Files lets people create a new folder by revealing a context menu in an area between existing files and folders.

In iOS and iPadOS, a context menu can display a preview of the current content near the list of commands. People can choose a command in the menu or — in some cases — they can tap the preview to open it or drag it to another area.

**Prefer a graphical preview that clarifies the target of a context menu’s commands.** For example, when people reveal a context menu on a list item in Notes or Mail, the preview shows a condensed version of the actual content to help people confirm that they’re working with the item they intend.

**Ensure that your preview looks good as it animates.** As people reveal a context menu on an onscreen object, the system animates the preview image as it emerges from the content, dimming the screen behind the preview and the menu. It’s important to adjust the preview’s clipping path to match the shape of the preview image so that its contours, such as the rounded corners, don’t appear to change during animation. For developer guidance, see [UIContextMenuInteractionDelegate](https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate).

### Dark Mode
<sub>`pages/dark-mode.md` — upstream heading: iOS, iPadOS</sub>

In Dark Mode, the system uses two sets of background colors — called *base* and *elevated* — to enhance the perception of depth when one dark interface is layered above another. The base colors are dimmer, making background interfaces appear to recede, and the elevated colors are brighter, making foreground interfaces appear to advance.

![A diagram that shows a stack of 4 terms on top of a black background. The term at the top shows the most contrast with the background and the term at the bottom shows the least.](/images/com.apple.HIG/base-with-four-semantic-colors@2x.png)

![A diagram that shows a stack of 4 terms on top of a nearly black background. The term at the top shows the most contrast with the background and the term at the bottom shows the least.](/images/com.apple.HIG/elevated-with-four-semantic-colors@2x.png)

![A diagram that shows a stack of 4 terms on top of a white background. The term at the top shows the most contrast with the background and the term at the bottom shows the least.](/images/com.apple.HIG/light-with-four-semantic-colors@2x.png)

**Prefer the system background colors.** Dark Mode is dynamic, which means that the background color automatically changes from base to elevated when an interface is in the foreground, such as a popover or modal sheet. The system also uses the elevated background color to provide visual separation between apps in a multitasking environment and between windows in a multiple-window context. Using a custom background color can make it harder for people to perceive these system-provided visual distinctions.

### Disclosure controls
<sub>`pages/disclosure-controls.md` — upstream heading: iOS, iPadOS, visionOS</sub>

Disclosure controls are available in iOS, iPadOS, and visionOS with the SwiftUI [DisclosureGroup](https://developer.apple.com/documentation/swiftui/disclosuregroup) view.

### Drag and drop
<sub>`pages/drag-and-drop.md` — upstream heading: iOS, iPadOS</sub>

**Let people perform multiple simultaneous drag activities.** In iPadOS, people can sequentially add items to an in-progress drag session, gathering as many items as their fingers can handle. For example, people can select an app icon on the Home Screen, start dragging it, and select additional app icons before dropping all of them in a different Home Screen or in a folder. To support this interaction, you need to let people add items during a drag — providing visual feedback through flocking — and accept multiple, simultaneous drops.

### Edit menus
<sub>`pages/edit-menus.md` — upstream heading: iOS, iPadOS</sub>

**Ensure your edit menu works well in both styles.** The system displays the compact, horizontal style when people use Multi-Touch gestures to reveal the edit menu, and the vertical style when people use a keyboard or pointing device to reveal it. For guidance using the vertical menu layout, see [iOS, iPadOS](https://developer.apple.com/design/human-interface-guidelines/menus#iOS-iPadOS).

**Adjust an edit menu’s placement, if necessary.** Depending on available space, the default menu position is above or below the insertion point or selection. The system also displays a visual indicator that points to the targeted content. Although you can’t change the shape of the menu or its pointer, you can change the menu’s position. For example, you might need to move the menu to prevent it from covering important content or parts of your interface.

### File management
<sub>`pages/file-management.md` — upstream heading: iOS, iPadOS</sub>

If your app can share its files with other apps, you can create a file provider app extension that displays a custom interface for importing, exporting, opening, and moving your app’s documents. For developer guidance, see [File Provider](https://developer.apple.com/documentation/fileprovider). An *app extension* is code you provide that people can install and use to extend the functionality of a specific area of the system; to learn more, see [App extensions](https://developer.apple.com/app-extensions/).

**When someone uses your file provider extension to open or import documents, display only documents that are appropriate in the current context.** For example, if a PDF-editing app loads your extension, only list PDF files for opening or import. You might also want to display additional information, such as modification dates, sizes, and whether documents are local or remote.

**Let people select a destination when exporting and moving documents.** Unless your app stores documents in a single directory, let people navigate to a specific destination in your directory hierarchy. You could also provide a way to add new subdirectories.

**Avoid including a custom top toolbar.** Your extension loads within a modal view that already includes a toolbar. Providing a second toolbar is confusing and takes space away from your content.

Your app can also let people browse and open files from other apps. For developer guidance, see [Adding a document browser to your app](https://developer.apple.com/documentation/uikit/adding-a-document-browser-to-your-app).

### File management
<sub>`pages/file-management.md` — upstream heading: iOS, iPadOS</sub>

Starting in iOS 18 and iPadOS 18, document-based apps can use the system’s document launcher to give people a consistent, highly graphical way to browse, open, and create files. The document launcher presents a full-screen experience that highlights key elements of your app’s theme, while making it easy for people to create new documents. For developer guidance, see [DocumentGroupLaunchScene](https://developer.apple.com/documentation/swiftui/documentgrouplaunchscene).

The document launcher consists of three main parts:

- A *title card* that displays the app title and two app-specific buttons
- A background image that appears behind the title card and additional images — called *accessories* — that can appear around it
- A sheet that contains a file browser and optional app-specific controls

You can customize all three parts of the document launcher. Although the system automatically displays your app name in the title card, you specify the text and functions of the card’s primary and secondary buttons. You can also create a custom background image, one or more accessory images to surround the title card, and provide some custom controls that can appear in the file browser’s toolbar.

![A screenshot of a writing app's document launcher on iPad in landscape orientation. The document launcher displays a custom background and two accessory images. At the bottom, the file browser sheet provides 3 tabs: Recents, Shared, and Browse.](/images/com.apple.HIG/file-management-document-launcher@2x.png)

**Assign the title card’s buttons to your app’s most important functions.** The primary button typically creates a new document, and the secondary button can provide additional options. For example, the primary button in Numbers is Start Writing and the secondary button is Choose a Template.

**Provide a background that’s clearly distinct from the accessories and title card.** You can use a solid color, a gradient, or a pattern. Avoid including complex images or patterns that might distract from foreground elements.

**Be mindful of accessory placement.** For example, you can place accessories both in front of and behind the title card to create the appearance of depth, but you need to make sure that your app name and both buttons remain clearly visible. Avoid cluttering the title card with too many accessories, and be sure to test its overall appearance across the range of screen sizes and device orientations that you support.

**Use animation sparingly.** Too much motion on the display can confuse or disorient people. If you want to animate your accessories, consider creating gentle, repeating animations that subtly highlight and enhance your app’s content. For example, you might create an animation that makes an accessory appear to breathe or sway softly. For guidance, see [Motion](https://developer.apple.com/design/human-interface-guidelines/motion).

### Focus and selection
<sub>`pages/focus-and-selection.md`</sub>

iPadOS 15 and later defines a focus system that supports keyboard interactions for navigating text fields, text views, and sidebars, in addition to various types of collection views and other custom views in your app.

The iPadOS and tvOS focus systems are similar. People perform actions by moving a focus indicator to an item and then selecting it (for guidance, see [tvOS](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection#tvOS)). Although the underlying system is the same, the user experiences are a little different. tvOS uses *directional focus*, which means people can use the same interaction — that is, swiping the Siri Remote or using only the arrow keys on a connected keyboard — to navigate to every onscreen component. In contrast, iPadOS defines *focus groups*, which represent specific areas within an app, like a sidebar, grid, or list. Using focus groups, iPadOS can support two different keyboard interactions.

- Pressing the Tab key moves focus among focus groups, letting people navigate to sidebars, grids, and other app areas.
- Pressing an arrow key supports a directional focus interaction that’s similar to tvOS, but limited to navigation among items in the same focus group. For example, people can use an arrow key to move through the items in a list or a sidebar.

Onscreen components can indicate focus by using the halo effect or the highlighted appearance.

The *halo* focus effect — also known as the *focus ring* — displays a customizable outline around the component. You can apply the halo effect to custom views and to fully opaque content within a collection or list cell, such as an image.

![An illustration of a collection view of photos showing the standard halo effect that outlines the focused photo.](/images/com.apple.HIG/focus-and-selection-halo-focus-effect@2x.png)

**Customize the halo focus effect when necessary.** By default, the system uses an item’s shape to infer the shape of its halo. If the system-provided halo doesn’t give you the appearance you want, you can refine it to match contours like rounded corners or shapes defined by Bézier paths. You can also adjust a halo’s position if another component occludes or clips it. For example, you might need to ensure that a badge appears above the halo or that a parent view doesn’t clip it. For developer guidance, see [UIFocusHaloEffect](https://developer.apple.com/documentation/uikit/uifocushaloeffect).

![An illustration of a collection view of photos showing a rounded-rectangle halo effect that outlines the focused photo.](/images/com.apple.HIG/focus-and-selection-customized-halo@2x.png)

The *highlighted* appearance — in which the component’s text uses the app’s accent color — also indicates focus, but it’s not a focus effect. The highlight appearance occurs automatically when people select a collection view cell on which you’ve set content configurations (for developer guidance, see [UICollectionViewCell](https://developer.apple.com/documentation/uikit/uicollectionviewcell)).

![An illustration of a list of menu items with the second item highlighted. The item's title and icon are tinted with a red accent color.](/images/com.apple.HIG/focus-and-selection-highlighted-appearance@2x.png)

**Ensure that focus moves through your custom views in ways that make sense.** As people continue pressing the Tab key, focus moves through focus groups in reading order: leading to trailing, and top to bottom. Although focus moves through system-provided views in ways that people expect, you might need to adjust the order in which the focus system visits your custom views. For example, if you want focus to move down through a vertical stack of custom views before it moves in the trailing direction to the next view, you need to identify the stack container as a single focus group. For developer guidance, see [focusGroupIdentifier](https://developer.apple.com/documentation/uikit/uifocusenvironment/focusgroupidentifier).

**Adjust the priority of an item to reflect its importance within a focus group.** When a group receives focus, its *primary item* automatically receives focus too, making it easy for people to select the item they’re most likely to want. You can make an item primary by increasing its priority. For developer guidance, see [UIFocusGroupPriority](https://developer.apple.com/documentation/uikit/uifocusgrouppriority).

### Gestures
<sub>`pages/gestures.md` — upstream heading: iOS, iPadOS</sub>

In addition to the [Standard gestures](https://developer.apple.com/design/human-interface-guidelines/gestures#Standard-gestures) supported in all platforms, iOS and iPadOS support a few other gestures that people expect.

| Gesture | Common action |
| --- | --- |
| Three-finger swipe | Initiate undo (left swipe); initiate redo (right swipe). |
| Three-finger pinch | Copy selected text (pinch in); paste copied text (pinch out). |
| Four-finger swipe (iPadOS only) | Switch between apps. |
| Shake | Initiate undo; initiate redo. |

**Consider allowing simultaneous recognition of multiple gestures if it enhances the experience.** Although simultaneous gestures are unlikely to be useful in nongame apps, a game might include multiple onscreen controls — such as a joystick and firing buttons — that people can operate at the same time. For guidance on integrating touchscreen input with Apple Pencil input in your iPadOS app, see [Apple Pencil and Scribble](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble).

### Going full screen
<sub>`pages/going-full-screen.md` — upstream heading: iOS, iPadOS</sub>

**Consider deferring system gestures to prevent accidental exits in a full-screen app or game.** By default, the Home Screen indicator automatically hides shortly after someone switches to your app or game. It reappears when someone interacts with the bottom portion of the screen, allowing them to swipe once to exit. Whenever possible, retain this behavior because it’s familiar and what people expect. If supporting this results in unexpected exits, you can enable two swipes rather than one to exit. For developer guidance, see [preferredScreenEdgesDeferringSystemGestures](https://developer.apple.com/documentation/swiftui/uihostingcontroller/preferredscreenedgesdeferringsystemgestures).

### Launching
<sub>`pages/launching.md` — upstream heading: iOS, iPadOS</sub>

**Launch in the appropriate orientation.** If your app or game supports both portrait and landscape modes, launch using the device’s current orientation. If your interface only runs in one orientation, launch in that orientation and let people rotate the device if necessary. Ensure a landscape-only interface responds correctly, regardless of whether people enter landscape orientation by rotating the device left or right. For guidance, see [Layout](https://developer.apple.com/design/human-interface-guidelines/layout).

### Layout
<sub>`pages/layout.md`</sub>

People can freely resize windows down to a minimum width and height, similar to window behavior in macOS. It’s important to account for this resizing behavior and the full range of possible window sizes when designing your layout. For guidance, see [iPadOS](https://developer.apple.com/design/human-interface-guidelines/multitasking#iPadOS) and [iPadOS](https://developer.apple.com/design/human-interface-guidelines/windows#iPadOS).

**As someone resizes a window, defer switching to a compact view for as long as possible.** Design for a full-screen view first, and only switch to a compact view when a version of the full layout no longer fits. This helps the UI feel more stable and familiar in as many situations as possible. For more complex layouts such as [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views), prefer hiding tertiary columns such as inspectors as the view narrows.

**Test your layout at common system-provided sizes, and provide smooth transitions.** Window controls provide the option to arrange windows to fill halves, thirds, and quadrants of the screen, so it’s important to check your layout at each of these sizes on a variety of devices. Be sure to minimize unexpected UI changes as people adjust down to the minimum and up to the maximum window size.

**Consider a convertible tab bar for adaptive navigation.** For many apps, you don’t need to choose between a tab bar or sidebar for navigation; instead, you can adopt a style of tab bar that provides both. The app first launches with your choice of a sidebar or a tab bar, and then people can tap to switch between them. As the view resizes, the presentation style changes to fit the width of the view. For guidance, see [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars). For developer guidance, see [sidebarAdaptable](https://developer.apple.com/documentation/swiftui/tabviewstyle/sidebaradaptable).

### Lists and tables
<sub>`pages/lists-and-tables.md` — upstream heading: iOS, iPadOS, visionOS</sub>

**Use an info button only to reveal more information about a row’s content.** An info button — called a *detail disclosure button* when it appears in a list row — doesn’t support navigation through a hierarchical table or list. If you need to let people drill into a list or table row’s subviews, use a disclosure indicator accessory control. For developer guidance, see [UITableViewCell.AccessoryType.disclosureIndicator](https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype-swift.enum/disclosureindicator).

![An illustration of a grouped list of rows. Each list item includes an info button at the trailing end of the row.](/images/com.apple.HIG/info-button-in-list@2x.png)

![An illustration of a grouped list of rows. Each list item includes a right-pointing chevron at the trailing end of the row.](/images/com.apple.HIG/disclosure-indicator-in-list@2x.png)

**Avoid adding an index to a table that displays controls — like disclosure indicators — in the trailing ends of its rows.** An *index* typically consists of the letters in an alphabet, displayed vertically at the trailing side of a list. People can jump to a specific section in the list by choosing the index letter that maps to it. Because both the index and elements like disclosure indicators appear on the trailing side of a list, it can be difficult for people to use one element without activating the other.

### Materials
<sub>`pages/materials.md` — upstream heading: iOS, iPadOS</sub>

In addition to Liquid Glass, iOS and iPadOS continue to provide four standard materials — ultra-thin, thin, regular (default), and thick — which you can use in the content layer to help create visual distinction.

![An illustration of the iOS and iPadOS ultraThin material above a colorful background. Where the material overlaps the background, it provides a diffuse gradient of the background colors.](/images/com.apple.HIG/materials-ios-material-background-ultrathin@2x.png)

![An illustration of the iOS and iPadOS thin material above a colorful background. Where the material overlaps the background, it provides a diffuse and slightly darkened gradient of the background colors.](/images/com.apple.HIG/materials-ios-material-background-thin@2x.png)

![An illustration of the iOS and iPadOS regular material above a colorful background. Where the material overlaps the background, it provides a diffuse and darkened gradient of the background colors.](/images/com.apple.HIG/materials-ios-material-background-regular@2x.png)

![An illustration of the iOS and iPadOS thick material above a colorful background. Where the material overlaps the background, it provides a dark, muted gradient of the background colors.](/images/com.apple.HIG/materials-ios-material-background-thick@2x.png)

iOS and iPadOS also define vibrant colors for labels, fills, and separators that are specifically designed to work with each material. Labels and fills both have several levels of vibrancy; separators have one level. The name of a level indicates the relative amount of contrast between an element and the background: The default level has the highest contrast, whereas quaternary (when it exists) has the lowest contrast.

Except for quaternary, you can use the following vibrancy values for labels on any material. In general, avoid using quaternary on top of the [thin](https://developer.apple.com/documentation/swiftui/material/thin) and [ultraThin](https://developer.apple.com/documentation/swiftui/material/ultrathin) materials, because the contrast is too low.

- [UIVibrancyEffectStyle.label](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/label) (default)
- [UIVibrancyEffectStyle.secondaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/secondarylabel)
- [UIVibrancyEffectStyle.tertiaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/tertiarylabel)
- [UIVibrancyEffectStyle.quaternaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/quaternarylabel)

You can use the following vibrancy values for fills on all materials.

- [UIVibrancyEffectStyle.fill](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/fill) (default)
- [UIVibrancyEffectStyle.secondaryFill](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/secondaryfill)
- [UIVibrancyEffectStyle.tertiaryFill](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/tertiaryfill)

The system provides a single, default vibrancy value for a [UIVibrancyEffectStyle.separator](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/separator), which works well on all materials.

### Menus
<sub>`pages/menus.md` — upstream heading: iOS, iPadOS</sub>

In iOS and iPadOS, a menu can display items in one of the following three layouts.

![A diagram showing small, medium, and large menu layouts, each containing the same set of menu items.](/images/com.apple.HIG/small-medium-large-menu-layouts@2x.png)

- **Small.** A row of four items appears at the top of the menu, above a list that contains the remaining items. For each item in the top row, the menu displays a symbol or icon, but no label.
- **Medium.** A row of three items appears at the top of the menu, above a list that contains the remaining items. For each item in the top row, the menu displays a symbol or icon above a short label.
- **Large (the default).** The menu displays all items in a list.

For developer guidance, see [preferredElementSize](https://developer.apple.com/documentation/uikit/uimenu/preferredelementsize).

**Choose a small or medium menu layout when it can help streamline people’s choices.** Consider using the medium layout if your app has three important actions that people often want to perform. For example, Notes uses the medium layout to give people a quick way to perform the Scan, Lock, and Pin actions. Use the small layout only for closely related actions that typically appear as a group, such as Bold, Italic, Underline, and Strikethrough. For each action, use a recognizable symbol that helps people identify the action without a label.

### Multitasking
<sub>`pages/multitasking.md`</sub>

On iPad, people can view and interact with the [Windows](https://developer.apple.com/design/human-interface-guidelines/windows) of several different apps at the same time. An individual app can also support multiple open windows, which lets people view and interact with more than one window in the same app at one time.

People can use iPad with either full-screen or windowed apps. When full screen, apps occupy the full screen, and people can switch between individual app windows using the app switcher.

![A screenshot of the iPad app switcher in landscape orientation, showing five open apps. Thumbnail representations of the apps are arranged in a grid.](/images/com.apple.HIG/multitasking-ipad-app-switcher@2x.png)

When using windowed apps, app windows are resizable, and people can arrange them to suit their needs with behavior similar to macOS. The system provides window controls for common tiling configurations, entering full screen, minimizing, and closing windows. The system identifies the frontmost window by coloring its window controls and casting a drop shadow on windows behind it. For guidance, see [iPadOS](https://developer.apple.com/design/human-interface-guidelines/windows#iPadOS).

![A screenshot of two windowed apps on iPad in landscape orientation. The frontmost app window overlaps and casts a shadow on the one behind it, and has colored window controls to indicate that the window is active. Both windows sit atop the Home Screen background, and the Dock appears at the bottom.](/images/com.apple.HIG/multitasking-ipad-windows-maps-landmarks@2x.png)

Additionally, videos and FaceTime calls can also play in a Picture in Picture overlay above other content regardless of whether apps are full screen or windowed.

> **Note:** Apps don’t control multitasking configurations or receive any indication of the ones that people choose.

To help your app respond correctly when people open it while windowed, make sure it adapts gracefully to different screen sizes. For guidance, see [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) and [Windows](https://developer.apple.com/design/human-interface-guidelines/windows); for developer guidance, see [Multitasking on iPad, Mac, and Apple Vision Pro](https://developer.apple.com/documentation/uikit/multitasking-on-ipad-mac-and-apple-vision-pro). To learn more about how people use iPad multitasking features, see [Use multitasking on your iPad](https://support.apple.com/en-us/HT207582).

### Page controls
<sub>`pages/page-controls.md` — upstream heading: iOS, iPadOS</sub>

A page control can adjust the appearance of indicators to provide more information about the list. For example, the control highlights the indicator of the current page so people can estimate the page’s relative position in the list. When there are more indicators than fit in the space, the control can shrink indicators at both sides to suggest that more pages are available.

![An illustration of a page control. The page control displays a total of 9 dots. The center 5 dots use the default size; the second and eighth dots are about half the default size and the first and ninth dots are about one quarter the default size. The center dot is filled, indicating the location of the current page in the list.](/images/com.apple.HIG/page-controls-many-indicators@2x.png)

People interact with page controls by tapping or scrubbing (to *scrub*, people touch the control and drag left or right). Tapping on the leading or trailing side of the current-page indicator reveals the next or previous page; in iPadOS, people can also use the pointer to target a specific indicator. Scrubbing opens pages in sequence, and scrubbing past the leading or trailing edge of the control helps people quickly reach the first or last page.

> **Note:** In the API, *tapping* is a *discrete interaction*, whereas *scrubbing* is a *continuous interaction*; for developer guidance, see [UIPageControl.InteractionState](https://developer.apple.com/documentation/uikit/uipagecontrol/interactionstate-swift.enum).

**Avoid animating page transitions during scrubbing.** People can scrub very quickly, and using the scrolling animation for every transition can make your app lag and cause distracting visual flashes. Use the animated scrolling transition only for tapping.

A page control can include a translucent, rounded-rectangle background appearance that provides visual contrast for the indicators. You can choose one of the following background styles:

- Automatic — Displays the background only when people interact with the control. Use this style when the page control isn’t the primary navigational element in the UI.
- Prominent — Always displays the background. Use this style only when the control is the primary navigational control in the screen.
- Minimal — Never displays the background. Use this style when you just want to show the position of the current page in the list and you don’t need to provide visual feedback during scrubbing.

For developer guidance, see [backgroundStyle](https://developer.apple.com/documentation/uikit/uipagecontrol/backgroundstyle-swift.property).

**Avoid supporting the scrubber when you use the minimal background style.** The minimal style doesn’t provide visual feedback during scrubbing. If you want to let people scrub a list of pages in your app, use the automatic or prominent background styles.

### Pickers
<sub>`pages/pickers.md` — upstream heading: iOS, iPadOS</sub>

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

**Compact**

![An illustration of a compact date picker, with a single inline row showing the currently selected date. The picker opens as a popover extending down from the row, and includes a full calendar month for choosing the date.](/images/com.apple.HIG/pickers-date-picker-compact-expanded@2x.png)

**Inline**

![An illustration of an inline date picker, titled 'Date'. A toggle at the top is switched on, and a calendar month for choosing the date appears below the title and toggle.](/images/com.apple.HIG/pickers-date-picker-inline-expanded@2x.png)

**Wheels**

![An illustration of an inline time picker, titled 'Time'. The currently selected time appears in the title row, and three vertical wheels appear below the title row for choosing the hour, minute, and AM or PM value.](/images/com.apple.HIG/pickers-time-picker-inline-wheel@2x.png)


**Use a compact date picker when space is constrained.** The compact style displays a button that shows the current value in your app’s accent color. When people tap the button, the date picker opens a modal view, providing access to a familiar calendar-style editor and time picker. Within the modal view, people can make multiple edits to dates and times before tapping outside the view to confirm their choices.

### Playing audio
<sub>`pages/playing-audio.md` — upstream heading: iOS, iPadOS</sub>

**Use the system’s sound services to play short sounds and vibrations.** For developer guidance, see [Audio Services](https://developer.apple.com/documentation/audiotoolbox/audio-services).

### Pointing devices
<sub>`pages/pointing-devices.md`</sub>

**Prefer system-provided pointer effects for custom elements that behave like standard elements.** When a custom element behaves like a standard one, people generally expect to interact with it using familiar pointer interactions. For example, if buttons in a custom toolbar don’t use the standard highlight effect, people might think they’re broken.

**Use pointer effects in consistent ways throughout your app.** For example, if your app helps people draw, provide a similar pointer experience for every drawing area in your app so that people can apply the knowledge they gain in one area to the others.

**Avoid creating gratuitous pointer and content effects.** People notice when the appearance of the pointer or the UI element beneath it changes, and they expect the changes to be useful. Creating a purely decorative pointer effect can distract and even irritate people without providing any practical value.

**Keep custom pointer shapes simple.** Ideally, the pointer’s shape signals the action people can take in the current context without drawing too much attention to itself. If people don’t instantly understand your custom pointer shape, they’re likely to waste time trying to discover what the shape means.

**Consider enhancing the pointer experience by displaying custom annotations that provide useful information.** For example, you could display X and Y values when people hold the pointer over a graphing area in your app. Keynote uses annotations to display the current width and height of a resizable image.

![An illustration of a custom pointer hovering over a resize handle on the edge of a shaded rectangle. Above the pointer is a small annotation that displays the image’s width and height values against a dark background.](/images/com.apple.HIG/useful-pointer-annotation@2x.png)

**Avoid displaying instructional text with a pointer.** A pointer that displays instructional text can make an app seem complicated and difficult to use. Instead of providing instructions, prioritize clarity and simplicity in your interface, so that people can quickly grasp how to use your app whether they’re using the pointer or touching the screen.

**Consider the interplay of shadow, scale, and element spacing when defining custom hover effects.** In general, reserve scaling for elements that can increase in size without crowding nearby elements. For example, scaling doesn’t work well for a table row because a row can’t expand without overlapping adjacent rows. For an element that has little space around it, consider using a hover effect that includes tint, but not scale and shadow. Note that it doesn’t work well to use shadow without including scale, because an unscaled element doesn’t appear to get closer to the viewer even when its shadow implies that it’s elevated above the screen.

### Pointing devices
<sub>`pages/pointing-devices.md`</sub>

**When possible, support the system-provided content effects.** People quickly become accustomed to the content effects they see throughout the system and generally expect their experience to apply to every app they use. To provide a consistent user experience, align your interactions with the design intent of each effect. Specifically:

- Use highlight for a small element that has a transparent background.
- Use lift for a small element that has an opaque background.
- Use hover for large elements and customize the scale, tint, and shadow attributes as needed (for guidance, see [Customizing pointers](https://developer.apple.com/design/human-interface-guidelines/pointing-devices#Customizing-pointers)).

**Prefer the system-provided pointer appearances for standard buttons and text-entry areas.** You can help people feel more comfortable with your app when the pointer behaves in ways they expect.

**Add padding around interactive elements to create comfortable hit regions.** You might need to experiment to determine the right size for an element’s hit region. If the hit region is too small, it can make people feel that they have to be extra precise when interacting with the element. On the other hand, when an element’s hit region is too large, people can feel that it takes a lot of effort to pull the pointer away from the element. In general, it works well to add about 12 points of padding around elements that include a bezel; for elements without a bezel, it works well to add about 24 points of padding around the element’s visible edges.

![An illustration of a button that has a filled, rounded-rectangle bezel. The button is centered on top of a shaded rectangle that extends beyond the button by the same distance on all sides. Centered on each side, a callout indicates that the padding between the button and each edge of the shaded rectangle is 12 points.](/images/com.apple.HIG/padding-for-button-with-bezel@2x.png)

![An illustration of a symbol centered on top of a shaded rectangle that extends beyond the symbol by the same distance on all sides. Centered on each side, a callout indicates that the padding between the symbol and each edge of the shaded rectangle is 24 points.](/images/com.apple.HIG/padding-for-glyph@2x.png)

![An illustration of a button without a bezel, centered on top of a shaded rectangle that extends beyond the button by the same distance on all sides. Centered on each side, a callout indicates that the padding between the button and each edge of the shaded rectangle is 24 points.](/images/com.apple.HIG/padding-for-button-without-bezel@2x.png)

**Create contiguous hit regions for custom bar buttons.** If there’s space between the hit regions of adjacent buttons in a bar, people may experience a distracting motion when the pointer reverts briefly to its default shape as it moves between buttons.

**Specify the corner radius of a nonstandard element that receives the lift effect.** With the system-provided lift effect, the pointer transforms to match the element’s shape as it fades out. By default, the pointer uses the system-defined corner radius to transform into a rounded rectangle. If your element is a different shape — if it’s a circle, for example — you need to provide the radius so the pointer can animate seamlessly into the shape of the element. For developer guidance, see [UIPointerShape.roundedRect(_:radius:)](https://developer.apple.com/documentation/uikit/uipointershape-swift.enum/roundedrect(_:radius:)).

### Pointing devices
<sub>`pages/pointing-devices.md`</sub>

Pointer accessories are visual indicators that help people understand how they can use the pointer to interact with the current UI element. For example, a pointer approaching a resizable element might display small arrows to indicate that the element allows resizing along a certain axis.

Unlike pointer shapes and content effects, accessories are secondary items that can combine with any pointer to communicate additional information. For developer guidance, see [UIPointerAccessory](https://developer.apple.com/documentation/uikit/uipointeraccessory).

**Use clear, simple images to create custom accessories.** A pointer accessory is small, so it’s essential to create an image that communicates the pointer interaction without using too many details.

**Consider using the accessory transition to signal a change in an element’s state or behavior.** In addition to animating the appearance and disappearance of pointer accessories, the system also animates the transitions among accessory shapes and positions that can accompany content effects. For example, you could communicate that an add action has become unavailable by transitioning the pointer accessory from the `plus` symbol to the `circle.slash` symbol.

### Pointing devices
<sub>`pages/pointing-devices.md`</sub>

iPadOS builds on the traditional pointer experience, automatically adapting the pointer to the current context and providing rich visual feedback at a level of precision that enhances productivity and simplifies common tasks on a touchscreen device. The iPadOS pointing system gives people an additional way to interact with apps and content — it doesn’t replace touch.

**Allow multiple selection in custom views when necessary.** In iPadOS 15 and later, people can click and drag the pointer over multiple items to select them. As people use the pointer in this way, it expands into a visible rectangle that selects the items it encompasses. Standard nonlist collection views support this interaction by default; if you want to support multiple selection in custom views, you need to implement it yourself. For developer guidance, see [UIBandSelectionInteraction](https://developer.apple.com/documentation/uikit/uibandselectioninteraction).

**Distinguish between pointer and finger input only if it provides value.** For example, a scrubber can give people an additional way to target a location in a video when they’re using the pointer. In this scenario, people can drag the playhead using either the pointer or touch, but they can use the pointer to click a precise seek destination.

### Pointing devices
<sub>`pages/pointing-devices.md`</sub>

iPadOS helps people use the pointer to target an element by making the element appear to attract the pointer. People can experience this magnetic effect when they move the pointer close to an element and when they flick the pointer toward an element.

When people move the pointer close to an element, the system starts transforming the pointer’s shape as soon as it reaches the element’s hit region. Because an element’s hit region typically extends beyond its visible boundaries, the pointer begins to transform before it appears to touch the element itself, creating the illusion that the element is pulling the pointer toward it.

*(video: A video snippet showing an area at the bottom of Clock. The World Clock tab is selected and clock images and information for San Francisco, New York, and London are partially visible in the window. As the pointer moves in the tab bar, its highlighted rounded rectangle appearance seems to show a slight resistance as it slides from the World Clock tab to the Alarm tab and back again.)*

When people flick the pointer toward an element, iPadOS examines the pointer’s trajectory to discover the element that’s the most likely target. When there’s an element in the pointer’s path, the system uses magnetism to pull the pointer toward the element’s center.

By default, iPadOS applies magnetism to elements that use the lift effect (like app icons) and the highlight effect (like bar buttons), but not to elements that use hover. Because an element that supports hover doesn’t transform the default pointer shape, adding magnetism could be jarring and might make people feel that they’ve lost control of the pointer.

The system also applies magnetism to text-entry areas, where it can help people avoid skipping to another line if they make unintended vertical movements while they’re selecting text.

### Pointing devices
<sub>`pages/pointing-devices.md`</sub>

iPadOS integrates the appearance and behavior of both the pointer and the element it moves over, bringing focus to the item the pointer is targeting. You can support the system-provided pointer effects or modify them to suit your experience.

By default, the pointer’s shape is a circle, but it can display a system-defined or custom shape when people move it over specific elements or regions. For example, the pointer automatically uses the familiar I-beam shape when people move it over a text-entry area.

*(video: A video snippet showing the bottom half of a new event popover in Calendar. At the beginning of the video, the pointer is within the URL field and it uses the I-beam shape. As the pointer moves between the URL and Notes fields, it briefly reverts to its default circular shape; when the pointer enters the Notes field, it uses the I-beam shape again.)*

With a *content effect*, the UI element or region beneath the pointer can also change its appearance when people hold the pointer over it. Depending on the type of content effect, the pointer can retain its current shape or transform into a shape that integrates with the element’s new appearance.

iPadOS defines three content effects that bring focus to different types of interactive elements in your app: highlight, lift, and hover.

The *highlight* effect transforms the pointer into a translucent, rounded rectangle that acts as a background for a control and includes a gentle parallax. The subtle highlighting and movement bring focus to the control without distracting people from their task. By default, iPadOS applies the highlight effect to bar buttons, tab bars, segmented controls, and edit menus.

*(video: A video snippet showing a small area at the bottom of a Photos window. Nature photos that show purple flowers, rocks in a stream, and grass are visible just above the tab bar, which shows the Photos and For You tabs. At the beginning of the video, the Photos tab is highlighted. Because bar items receive the highlight effect, the pointer becomes the highlighted rounded rectangle that surrounds the tab’s glyph and title. The highlighted rounded rectangle slides from one tab to the other as the pointer moves.)*

The *lift* effect combines a subtle parallax with the appearance of elevation to make an element seem like it’s floating above the screen. As the pointer fades out beneath the element, iPadOS creates the illusion of lift by scaling the element up while adding a shadow below it and a soft specular highlight on top of it. By default, iPadOS applies the lift effect to app icons and to buttons in Control Center.

*(video: A video snippet showing the left end of the Dock in front of the Home Screen. From the left, the visible app icons are Messages, Safari, Music, Mail, and Files. As the pointer moves across the first three icons from the left, it disappears beneath each icon in turn, lifting it slightly and letting it return to its original position before moving to the next icon.)*

*Hover* is a generic effect that lets you apply custom scale, tint, or shadow values to an element as the pointer moves over it. The hover effect combines your custom values to bring focus to an item, but it doesn’t transform the default pointer shape.

*(video: A video snippet showing an alert floating above the top half of a new event popover in Calendar. The alert contains text that reads Are you sure you want to discard this new event? and a button titled Discard Changes. As the pointer moves into the alert button, the button background darkens.)*

### Pop-up buttons
<sub>`pages/pop-up-buttons.md`</sub>

**Within a popover or modal view, consider using a pop-up button instead of a disclosure indicator to present multiple options for a list item.** For example, people can quickly choose an option from the pop-up button’s menu without navigating to a detail view. Consider using a pop-up button in this scenario when you have a fairly small, well-defined set of options that work well in a menu.

### Popovers
<sub>`pages/popovers.md` — upstream heading: iOS, iPadOS</sub>

**Avoid displaying popovers in compact views.** Make your app or game dynamically adjust its layout based on the size class of the content area. Reserve popovers for wide views; for compact views, use all available screen space by presenting information in a full-screen modal view like a sheet instead. For related guidance, see [Modality](https://developer.apple.com/design/human-interface-guidelines/modality).

### Progress indicators
<sub>`pages/progress-indicators.md` — upstream heading: iOS, iPadOS</sub>

A refresh control lets people immediately reload content, typically in a table view, without waiting for the next automatic content update to occur. A refresh control is a specialized type of activity indicator that’s hidden by default, becoming visible when people drag down the view they want to reload. In Mail, for example, people can drag down the list of Inbox messages to check for new messages.

![A screenshot of a refresh content control spinning while Mail checks for new messages.](/images/com.apple.HIG/refresh-controls@2x.png)

**Perform automatic content updates.** Although people appreciate being able to do an immediate content refresh, they also expect automatic refreshes to occur periodically. Don’t make people responsible for initiating every update. Keep data fresh by updating it regularly.

**Supply a short title only if it adds value.** Optionally, a refresh control can include a title. In most cases, this is unnecessary, as the animation of the control indicates that content is loading. If you do include a title, don’t use it to explain how to perform a refresh. Instead, provide information of value about the content being refreshed. A refresh control in Podcasts, for example, uses a title to tell people when the last podcast update occurred.

For developer guidance, see [UIRefreshControl](https://developer.apple.com/documentation/uikit/uirefreshcontrol).

### Pull-down buttons
<sub>`pages/pull-down-buttons.md` — upstream heading: iOS, iPadOS</sub>

> **Note:** You can also let people reveal a pull-down menu by performing a specific gesture on a button. For example, in iOS 14 and later, Safari responds to a touch and hold gesture on the Tabs button by displaying a menu of tab-related actions, like New Tab and Close All Tabs.

**Consider using a More pull-down button to present items that don’t need prominent positions in the main interface.** A More button can help you offer a range of items where space is constrained, but it can also hinder discoverability. Although people generally understand that a More button offers additional functionality related to the current context, the ellipsis icon doesn’t necessarily help them predict its contents. To design an effective More button, weigh the convenience of its size against its impact on discoverability to find a balance that works in your app.

![A screenshot of the Notes app on iPhone, open to a Notes document titled Nature Walks. The top toolbar includes a More button on the trailing edge.](/images/com.apple.HIG/menu-secondary-actions-collapsed@2x.png)

![A screenshot of the Notes app on iPhone, open to a Notes document titled Nature Walks. The More button in the top toolbar is expanded, revealing the More menu with additional funtionality.](/images/com.apple.HIG/menu-secondary-actions-expanded@2x.png)

### Scroll views
<sub>`pages/scroll-views.md` — upstream heading: iOS, iPadOS</sub>

**Consider showing a page control when a scroll view is in page-by-page mode.** [Page controls](https://developer.apple.com/design/human-interface-guidelines/page-controls) show how many pages, screens, or other chunks of content are available and indicates which one is currently visible. For example, Weather uses a page control to indicate movement between people’s saved locations. If you show a page control with a scroll view, don’t show the scrolling indicator on the same axis to avoid confusing people with redundant controls.

### Search fields
<sub>`pages/search-fields.md` — upstream heading: iPadOS, macOS</sub>

The placement and behavior of the search field in iPadOS and macOS is similar. If your app is available on both iPad and Mac, try to keep the search experience as consistent as possible across both platforms.

![An illustration of an iPad screen with a search field on the trailing edge of the top toolbar. The search field has the word Design entered into the field, and three search suggestions appear in a list beneath the field.](/images/com.apple.HIG/search-fields-toolbar-search-ipad@2x.png)

![An illustration of a Mac screen with a search field on the trailing edge of the toolbar. The search field has the word Design entered into the field, and three search suggestions appear in a list beneath the field.](/images/com.apple.HIG/search-fields-toolbar-search-mac@2x.png)

**Put a search field at the trailing side of the toolbar for many common uses.** Many apps benefit from the familiar pattern of search in the toolbar, particularly apps with split views that need to search across multiple columns of information, like Mail, Notes, and Voice Memos. This placement makes great use of space because it lets people navigate results while keeping their selection visible in the detail view. Additionally, consider placing search in the toolbar if results appear in the detail view of your app, like in Freeform, where search in the toolbar filters the boards in the detail view below.

**Include search at the top of the sidebar when filtering content or navigation there.** Apps such as Settings take advantage of search to quickly filter the sidebar and expose sections that may be multiple levels deep, providing a simple way for people to search, preview, and navigate to the section or setting they’re looking for. This approach is useful if your app has a rich detail view and you need to create a distinct separation between the sidebar you’re filtering and the adjacent view.

![An illustration of an iPad screen with a search field at the top of the sidebar on the leading edge of the screen.](/images/com.apple.HIG/search-fields-ipad-search-in-sidebar@2x.png)

**Include search as an item in the sidebar or tab bar when you want an area dedicated to discovery.** If your search is paired with rich suggestions, categories, or content that needs more space, it can be helpful to have a dedicated area for it. This is particularly useful for apps where browsing and search go hand in hand, like Music and TV, where it provides a unified location to highlight suggested content, categories, and recent searches. A dedicated area also ensures search is always available as people navigate and switch sections of your app.

![An illustration of an iPad screen with a tab bar at the top edge. The trailing side of the tab bar includes a Search tab with a distinct background color to differentiate it from other tab areas.](/images/com.apple.HIG/search-fields-ipad-search-in-tab-bar@2x.png)

**In a search field in a dedicated area, consider immediately focusing the field when a person navigates to the area to help them search faster and locate the field more easily.** An exception to this is on iPad when only a virtual keyboard is available, in which case it’s better to leave the field unfocused to prevent the keyboard from unexpectedly covering the view.

**Account for window resizing with the placement of the search field.** On iPad, the search field fluidly resizes with the app window like it does on Mac. However, for compact views on iPad, itʼs important to ensure that search is available where it’s most contextually useful. For example, Notes and Mail place search above the column for the content list when they resize down to a compact view.

### Segmented controls
<sub>`pages/segmented-controls.md` — upstream heading: iOS, iPadOS</sub>

**Consider a segmented control to switch between closely related subviews.** A segmented control can be useful as a way to quickly switch between related subviews. For example, the segmented control in Calendar’s New Event sheet switches between the subviews for creating a new event and a new reminder. For switching between completely separate sections of an app, use a [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) instead.

![A screenshot of the top half of the iOS Calendar app, showing the New Event sheet. A segmented control provides the ability to switch between adding a new event and a new reminder.](/images/com.apple.HIG/segmented-controls-calendar-new-event@2x.png)

### Sheets
<sub>`pages/sheets.md` — upstream heading: iOS, iPadOS</sub>

In iOS and iPadOS, for sheets with a single view, the Cancel button belongs on the leading edge of the top toolbar. When present, the Done button belongs on the trailing edge.

![An illustration of the top half of a sheet on iPhone. A Cancel button appears in the top-left corner of the view, and a Done button appears in the top-right corner.](/images/com.apple.HIG/sheets-buttons-placement-cancel-done@2x.png)

For sheets with a multi-step flow, the placement of buttons can vary across steps.

**First step**

![An illustration of the top half of a sheet on iPhone. A Cancel button appears in the top-left corner of the view, and an inactive Done button appears in the top-right corner.](/images/com.apple.HIG/sheets-buttons-placement-navigation-first-page@2x.png)

**Subsequent step**

![An illustration of the top half of a sheet on iPhone. A Back button appears in the top-left corner of the view, and an inactive Done button appears in the top-right corner.](/images/com.apple.HIG/sheets-buttons-placement-navigation-subsequent-page@2x.png)

**Final step**

![An illustration of the top half of a sheet on iPhone. A Back button appears in the top-left corner of the view, and a Done button appears in the top-right corner.](/images/com.apple.HIG/sheets-buttons-placement-navigation-final-page@2x.png)


A resizable sheet expands when people scroll its contents or drag the *grabber*, which is a small horizontal indicator that can appear at the top edge of a sheet. Sheets resize according to their *detents*, which are particular heights at which a sheet naturally rests. Designed for iPhone, detents specify particular heights at which a sheet naturally rests. The system defines two detents: *large* is the height of a fully expanded sheet and *medium* is about half of the fully expanded height. Sheets can have one or more custom detent values.

![An illustration showing an iPhone screen in portrait orientation containing a solid rounded rectangle that occupies almost all of the screen, representing a full-screen sheet. A rounded close button appears in the upper-left corner of the sheet.](/images/com.apple.HIG/sheets-large-detent@2x.png)

![An illustration showing an iPhone screen in portrait orientation containing a solid rounded rectangle that occupies half of the screen, representing a half-screen sheet. A rounded close button appears in the upper-left corner of the sheet.](/images/com.apple.HIG/sheets-medium-detent@2x.png)

Sheets automatically support the large detent. Adding the medium detent allows the sheet to rest at both heights, whereas specifying only medium prevents the sheet from expanding to full height. For developer guidance, see [detents](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/detents).

**In an iPhone app, consider supporting the medium detent to allow progressive disclosure of the sheet’s content.** For example, a share sheet displays the most relevant items within the medium detent, where they’re visible without resizing. To view more items, people can scroll or expand the sheet. In contrast, you might not want to support the medium detent if a sheet’s content is more useful when it displays at full height. For example, the compose sheets in Messages and Mail display only at full height to give people enough room to create content.

**Include a grabber in a resizable sheet.** A grabber shows people that they can drag the sheet to resize it; they can also tap it to cycle through the detents. In addition to providing a visual indicator of resizability, a grabber also works with VoiceOver so people can resize the sheet without seeing the screen. For developer guidance, see [prefersGrabberVisible](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/prefersgrabbervisible).

**Support swiping to dismiss a sheet.** People expect to swipe vertically to dismiss a sheet instead of tapping a dismiss button. If people have unsaved changes in the sheet when they begin swiping to dismiss it, use an action sheet to let them confirm their action.

**Prefer using the page or form sheet presentation styles in an iPadOS app.** Each style uses a default size for the sheet, centering its content on top of a dimmed background view and providing a consistent experience. For developer guidance, see [UIModalPresentationStyle](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle).

### Sidebars
<sub>`pages/sidebars.md` — upstream heading: iOS, iPadOS</sub>

When you use the [sidebarAdaptable](https://developer.apple.com/documentation/swiftui/tabviewstyle/sidebaradaptable) style of tab view to present a sidebar, you choose whether to display a sidebar or a tab bar when your app opens. Both variations include a button that people can use to switch between them. This style also adapts its appearance depending on the platform, and responds automatically to rotation and window resizing, providing a version of the control that’s appropriate to the width of the view.

> **Note:** To display a sidebar only, use [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview) to present a sidebar in the primary pane of a split view, or use [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller).

**Consider using a tab bar first.** A tab bar provides more space to feature content, and offers enough flexibility to navigate between many apps’ main areas. If you need to expose more areas than fit in a tab bar, the tab bar’s convertible sidebar-style appearance can provide access to content that people use less frequently. For guidance, see [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars).

**If necessary, apply the correct appearance to a sidebar.** If you’re not using SwiftUI to create a sidebar, you can use the [UICollectionLayoutListConfiguration.Appearance.sidebar](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebar) appearance of a collection view list layout. For developer guidance, see [UICollectionLayoutListConfiguration.Appearance](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum).

### Sliders
<sub>`pages/sliders.md` — upstream heading: iOS, iPadOS</sub>

**Don’t use a slider to adjust audio volume.** If you need to provide volume control in your app, use a volume view, which is customizable and includes a volume-level slider and a control for changing the active audio output device. For guidance, see [Playing audio](https://developer.apple.com/design/human-interface-guidelines/playing-audio).

### Split views
<sub>`pages/split-views.md`</sub>

In iPadOS, a split view can include either two vertical panes, like Mail, or three vertical panes, like Keynote.

**Account for narrow, compact, and intermediate window widths.** Since iPad windows are fluidly resizable, it’s important to consider the design of a split view layout at multiple widths. In particular, ensure that it’s possible to navigate between the various panes in a logical way. For guidance, see [Layout](https://developer.apple.com/design/human-interface-guidelines/layout). For developer guidance, see [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview) and [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller).

### Tab bars
<sub>`pages/tab-bars.md`</sub>

The system displays a tab bar near the top of the screen. You can choose to have the tab bar appear as a fixed element, or with a button that converts it to a sidebar. For developer guidance, see [tabBarOnly](https://developer.apple.com/documentation/swiftui/tabviewstyle/tabbaronly) and [sidebarAdaptable](https://developer.apple.com/documentation/swiftui/tabviewstyle/sidebaradaptable).

**Tab bar**

![A screenshot showing the Music app on iPad with the tab bar near the top of the screen.](/images/com.apple.HIG/ipad-tab-bar-music-app@2x.png)

**Sidebar**

![A screenshot showing the Music app on iPad with the tab bar converted to a sidebar on the leading edge of the screen.](/images/com.apple.HIG/ipad-sidebar-music-app@2x.png)


> **Note:** To present a sidebar without the option to convert it to a tab bar, use a [navigation split view](https://developer.apple.com/documentation/swiftui/navigationsplitview) instead of a tab view. For guidance, see [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars).

**Prefer a tab bar for navigation.** A tab bar provides access to the sections of your app that people use most. If your app is more complex, you can provide the option to convert the tab bar to a sidebar so people can access a wider set of navigation options.

**Let people customize the tab bar.** In apps with a lot of sections that people might want to access, it can be useful to let people select items that they use frequently and add them to the tab bar, or remove items that they use less frequently. For example, in the Music app, a person can choose a favorite playlist to display in the tab bar. If you let people select their own tabs, aim for a default list of five or fewer to preserve continuity between compact and regular view sizes. For developer guidance, see [TabViewCustomization](https://developer.apple.com/documentation/swiftui/tabviewcustomization) and [UITab.Placement](https://developer.apple.com/documentation/uikit/uitab/placement).

### Tab views
<sub>`pages/tab-views.md` — upstream heading: iOS, iPadOS</sub>

For similar functionality, consider using a [segmented control](https://developer.apple.com/design/human-interface-guidelines/segmented-controls) instead.

### Text fields
<sub>`pages/text-fields.md` — upstream heading: iOS, iPadOS</sub>

**Display a Clear button in the trailing end of a text field to help people erase their input.** When this element is present, people can tap it to clear the text field’s contents, without having to keep tapping the Delete key.

**Use images and buttons to provide clarity and functionality in text fields.** You can display custom images in both ends of a text field, or you can add a system-provided button, such as the Bookmarks button. In general, use the leading end of a text field to indicate a field’s purpose and the trailing end to offer additional features, such as bookmarking.

### Text views
<sub>`pages/text-views.md` — upstream heading: iOS, iPadOS</sub>

**Show the appropriate keyboard type.** Several different keyboard types are available, each designed to facilitate a different type of input. To streamline data entry, the keyboard you display when editing a text view needs to be appropriate for the type of content. For guidance, see [Virtual keyboards](https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards).

### The menu bar
<sub>`pages/the-menu-bar.md`</sub>

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

### Toggles
<sub>`pages/toggles.md` — upstream heading: iOS, iPadOS</sub>

**Use the switch toggle style only in a list row.** You don’t need to supply a label in this situation because the content in the row provides the context for the state the switch controls.

**Change the default color of a switch only if necessary.** The default green color tends to work well in most cases, but you might want to use your app’s accent color instead. Be sure to use a color that provides enough contrast with the uncolored appearance to be perceptible.

![An illustration of two list rows, one with an active switch toggle and one with an inactive switch toggle. The active toggle is tinted green with the standard switch color.](/images/com.apple.HIG/toggles-ios-default-color@2x.png)

![An illustration of two list rows, one with an active switch toggle and one with an inactive switch toggle. The active toggle is tinted purple with a custom switch color.](/images/com.apple.HIG/toggles-ios-custom-color@2x.png)

**Outside of a list, use a button that behaves like a toggle, not a switch.** For example, the Phone app uses a toggle on the filter button to let users filter their recent calls.  The app adds a blue highlight to indicate when the toggle is active, and removes it when the toggle is inactive.

![A screenshot of the top half of the Phone app on iPhone, showing the filtered list of recent missed calls. The filter button in the top trailing corner has a blue highlight, indicating that the toggle is active.](/images/com.apple.HIG/toggles-ios-phone-filter-on@2x.png)

![A screenshot of the top half of the Phone app on iPhone, showing all recent calls. The filter button in the top trailing corner has no highlight, indicating that the toggle is inactive.](/images/com.apple.HIG/toggles-ios-phone-filter-off@2x.png)

**Avoid supplying a label that explains the button’s purpose.** The interface icon you create — combined with the alternative background appearances you supply — help people understand what the button does. For developer guidance, see [changesSelectionAsPrimaryAction](https://developer.apple.com/documentation/uikit/uibutton/changesselectionasprimaryaction).

### Toolbars
<sub>`pages/toolbars.md`</sub>

**Consider combining a toolbar with a tab bar.** In iPadOS, a toolbar and a [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) can coexist in the same horizontal space at the top of the view. This is particularly useful for layouts where you want to navigate between a few main app areas while keeping the full width of the window available for content. For guidance, see [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) and [Windows](https://developer.apple.com/design/human-interface-guidelines/windows).

### Typography
<sub>`pages/typography.md` — upstream heading: iOS, iPadOS</sub>

SF Pro is the system font in iOS and iPadOS. iOS and iPadOS apps can also use NY.

### Undo and redo
<sub>`pages/undo-and-redo.md` — upstream heading: iOS, iPadOS</sub>

**Avoid redefining standard gestures for undo and redo.** For example, people can use a three-finger swipe to initiate an undo or redo, or shake their iPhone. As with all standard gestures, redefining them in your interface runs the risk of confusing people and making your experience unpredictable.

**Briefly and precisely describe the operation to be undone or redone.** The undo and redo alert title automatically includes a prefix of “Undo ” or “Redo ” (including the trailing space). You need to provide an additional word or two that describes what’s being undone or redone, to appear after this prefix. For example, you might create alert titles such as “Undo Name” or “Redo Address Change.”

### Virtual keyboards
<sub>`pages/virtual-keyboards.md` — upstream heading: iOS, iPadOS</sub>

**Use the keyboard layout guide to make the keyboard feel like an integrated part of your interface.** Using the layout guide also helps you keep important parts of your interface visible while the virtual keyboard is onscreen. For developer guidance, see [Adjusting your layout with keyboard layout guide](https://developer.apple.com/documentation/uikit/adjusting-your-layout-with-keyboard-layout-guide).

![An illustration of an app layout on iPhone, showing two stacked text fields and a button above the keyboard.](/images/com.apple.HIG/ui-fully-visible@2x.png)

![A checkmark in a circle to indicate a correct example.](/images/com.apple.HIG/checkmark@2x.png)

![An illustration of an app layout on iPhone, showing two stacked text fields. The keyboard covers part of the bottom text field.](/images/com.apple.HIG/text-field-hidden@2x.png)

![An X in a circle to indicate an incorrect example.](/images/com.apple.HIG/crossout@2x.png)

![An illustration of an app layout on iPhone, showing two stacked text fields and a button above the keyboard. The keyboard covers part of the button.](/images/com.apple.HIG/button-hidden@2x.png)

![An X in a circle to indicate an incorrect example.](/images/com.apple.HIG/crossout@2x.png)

**Place custom controls above the keyboard thoughtfully.** Some apps position an input accessory view containing custom controls above the keyboard to offer app-specific functionality related to the data people are working with. For example, Numbers displays controls that help people apply standard or custom calculations to spreadsheet data. If your app offers custom controls that augment the keyboard, make sure they’re relevant to the current task. If other views in your app use Liquid Glass, or if your view looks out of place above the keyboard, apply Liquid Glass to the view that contains your controls to maintain consistency. If you use a standard toolbar to contain your controls, it automatically adopts Liquid Glass. Use the keyboard layout guide and standard padding to ensure the system positions your controls as expected within the view. For developer guidance, see [ToolbarItemPlacement](https://developer.apple.com/documentation/swiftui/toolbaritemplacement) (SwiftUI), [inputAccessoryView](https://developer.apple.com/documentation/uikit/uiresponder/inputaccessoryview) (UIKit), and [UIKeyboardLayoutGuide](https://developer.apple.com/documentation/uikit/uikeyboardlayoutguide) (UIKit).

### Widgets
<sub>`pages/widgets.md` — upstream heading: iOS, iPadOS</sub>

On iPhone in StandBy, the system displays two small system family widgets side-by-side, scaled up so they fill the Lock Screen. By supporting StandBy, you also ensure your widgets work well in CarPlay. CarPlay and StandBy widgets both use the small system family widget with the background removed and scaled up to best fit the grid on the Widgets screen. Glanceable information and large text are especially important in CarPlay to make your widget easy to read on a car’s display.

**Limit usage of rich images or color to convey meaning in StandBy.** Instead, make use of the additional space by scaling up and rearranging text so people can glance at the widget content from a greater distance. To seamlessly blend with the black background, don’t use background colors for your widget when it appears in StandBy.

**Correct usage**

![An image of iPhone in StandBy. It shows a Clock widget on the left that displays the time as 9:41 a.m. and a Weather widget set to Cupertino with the temperature at 70 degrees Fahrenheit on the right.](/images/com.apple.HIG/widgets-standby-removed-background-correct@2x.png)

![A checkmark in a circle to indicate correct usage.](/images/com.apple.HIG/checkmark@2x.png)

**Incorrect usage**

![An image of iPhone in StandBy. It shows a Clock widget on the left that displays the time as 9:41 a.m. and a Weather widget set to Cupertino with the temperature at 70 degrees Fahrenheit on the right. The Watch widget appears with the background removed and the Weather widget isn't optimized for StandBy.](/images/com.apple.HIG/widgets-standby-with-background-incorrect@2x.png)

![An X in a circle to indicate incorrect usage.](/images/com.apple.HIG/crossout@2x.png)


For developer guidance, see [Displaying the right widget background](https://developer.apple.com/documentation/widgetkit/displaying-the-right-widget-background).

On iPhone in StandBy in low-light conditions, the system renders widgets in a monochromatic look with a red tint.

![An image of iPhone in low-light conditions. It shows a Clock widget on the left that displays the time as 9:41 a.m. and a Weather widget set to Cupertino with the temperature at 70 degrees Fahrenheit on the right.](/images/com.apple.HIG/widgets-standby-low-light@2x.png)

### Widgets
<sub>`pages/widgets.md` — upstream heading: iOS, iPadOS</sub>

Widgets on the Lock Screen are functionally similar to watch complications and follow design principles for [Complications](https://developer.apple.com/design/human-interface-guidelines/complications) in addition to design principles for widgets. Provide useful information in your Lock Screen widget, and don’t treat it only as an additional way for people to launch into your app. In many cases, a design for complications also works well for widgets on the Lock Screen (and vice versa), so consider creating them in tandem.

Your app can offer widgets on the Lock Screen in three different shapes: as inline text that appears above the clock, and as circular and rectangular shapes that appear below the clock.

![A partial screenshot of the Lock Screen on iPhone that shows a Calendar widget and two Weather widgets below the time. From the left, the widgets are an inline text widget and two circular widgets.](/images/com.apple.HIG/widget-lock-screen-display-appearances@2x.png)

**Support the Always-On display on iPhone.** Devices with the Always-On display render widgets on the Lock Screen with reduced luminance. Use levels of gray that provide enough contrast in the Always-On display, and make sure your content remains legible.

For developer guidance, see [Creating accessory widgets and watch complications](https://developer.apple.com/documentation/widgetkit/creating-accessory-widgets-and-watch-complications).

**Offer Live Activities to show real-time updates.** Widgets don’t show real-time information. If your app allows people to track the progress of a task or event for a limited amount of time with frequent updates, consider offering Live Activities. Widgets and Live Activities use the same underlying frameworks and share design similarities. As a result, it can be a good idea to develop widgets and Live Activities in tandem and reuse code and design components for both features. For design guidance on Live Activities, see [Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities); for developer guidance, see [ActivityKit](https://developer.apple.com/documentation/activitykit).

### Windows
<sub>`pages/windows.md`</sub>

Windows present in one of two ways depending on a person’s choice in Multitasking & Gestures settings.

- **Full screen.** App windows fill the entire screen, and people switch between them — or between multiple windows of the same app — using the app switcher.
- **Windowed.** People can freely resize app windows. Multiple windows can be onscreen at once, and people can reposition them and bring them to the front. The system remembers window size and placement even when an app is closed.

**Full screen**

![A screenshot of the Notes app in full screen on iPad, with an open document titled Nature Walks. The app interface fills the entire screen, with no visible border to the window.](/images/com.apple.HIG/windows-ipad-notes-fullscreen@2x.png)

**Windowed**

![A screenshot of the Notes app  in a window on iPad, with an open document titled Nature Walks. The document window occupies the center of the screen, with the Home Screen background filling the rest of the screen behind it, and the Dock at the bottom.](/images/com.apple.HIG/windows-ipad-notes-windowed@2x.png)


**Make sure window controls don’t overlap toolbar items.** When windowed, app windows include window controls at the leading edge of the toolbar. If your app has toolbar buttons at the leading edge, they might be hidden by window controls when they appear. To prevent this, instead of placing buttons directly on the leading edge, move them inward when the window controls appear.

**Consider letting people use a gesture to open content in a new window.** For example, people can use the pinch gesture to expand a Notes item into a new window. For developer guidance, see [collectionView(_:sceneActivationConfigurationForItemAt:point:)](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:sceneactivationconfigurationforitemat:point:)) (to transition from a collection view item), or [UIWindowScene.ActivationInteraction](https://developer.apple.com/documentation/uikit/uiwindowscene/activationinteraction) (to transition from an item in any other view).

> **Tip:** If you only need to let people view one file, you can present it without creating your own window, but you must support multiple windows in your app. For developer guidance, see [QLPreviewSceneActivationConfiguration](https://developer.apple.com/documentation/quicklook/qlpreviewsceneactivationconfiguration).

## macOS

### Alerts
<sub>`pages/alerts.md`</sub>

macOS automatically displays your app icon in an alert, but you can supply an alternative icon or symbol. In addition, macOS lets you:

- Configure repeating alerts to let people suppress subsequent occurrences of the same alert.
- Append a custom view if it’s necessary to provide additional information (for developer guidance, see [accessoryView](https://developer.apple.com/documentation/appkit/nsalert/accessoryview)).
- Include a Help button that opens your help documentation (see [Help buttons](https://developer.apple.com/design/human-interface-guidelines/buttons#Help-buttons)).

**Use a caution symbol sparingly.** Using a caution symbol like `exclamationmark.triangle` too frequently in your alerts diminishes its significance. Use the symbol only when extra attention is really needed, as when confirming an action that might result in unexpected loss of data. Don’t use the symbol for tasks whose only purpose is to overwrite or remove data, such as a save or empty trash.

### App Shortcuts
<sub>`pages/app-shortcuts.md`</sub>

App Shortcuts aren’t supported in macOS. However, actions you create for your app using App Intents are supported, and people can build custom shortcuts using them with the Shortcuts app on Mac.

### Boxes
<sub>`pages/boxes.md`</sub>

By default, macOS displays a box’s title above it.

### Buttons
<sub>`pages/buttons.md`</sub>

A *help button* appears within a view and opens app-specific help documentation.

Help buttons are circular, consistently sized buttons that contain a question mark. For guidance on creating help documentation, see [Offering help](https://developer.apple.com/design/human-interface-guidelines/offering-help).

**Use the system-provided help button to display your help documentation.** People are familiar with the appearance of the standard help button and know that choosing it opens help content.

**When possible, open the help topic that’s related to the current context.** For example, the help button in the Rules pane of Mail settings opens the Mail User Guide to a help topic that explains how to change these settings. If no specific help topic applies directly to the current context, open the top level of your app’s help documentation when people choose a help button.

**Include no more than one help button per window.** Multiple help buttons in the same context make it hard for people to predict the result of clicking one.

**Position help buttons where people expect to find them.** Use the following locations for guidance.

| View style | Help button location |
| --- | --- |
| Dialog with dismissal buttons (like OK and Cancel) | Lower corner, opposite to the dismissal buttons and vertically aligned with them |
| Dialog without dismissal buttons | Lower-left or lower-right corner |
| Settings window or pane | Lower-left or lower-right corner |

**Use a help button within a view, not in the window frame.** For example, avoid placing a help button in a toolbar or status bar.

**Avoid displaying text that introduces a help button.** People know what a help button does, so they don’t need additional descriptive text.

### Buttons
<sub>`pages/buttons.md`</sub>

A *square button* (also known as a *gradient button*) initiates an action related to a view, like adding or removing rows in a table.

Square buttons contain symbols or icons — not text — and you can configure them to behave like push buttons, toggles, or pop-up buttons. The buttons appear in close proximity to their associated view — usually within or beneath it — so people know which view the buttons affect.

**Use square buttons in a view, not in the window frame.** Square buttons aren’t intended for use in toolbars or status bars. If you need a button in a [toolbar](https://developer.apple.com/design/human-interface-guidelines/toolbars), use a toolbar item.

**Prefer using a symbol in a square button.** [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) provides a wide range of symbols that automatically receive appropriate coloring in their default state and in response to user interaction.

**Avoid using labels to introduce square buttons.** Because square buttons are closely connected with a specific view, their purpose is generally clear without the need for descriptive text.

For developer guidance, see [NSButton.BezelStyle.smallSquare](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/smallsquare).

### Buttons
<sub>`pages/buttons.md`</sub>

An *image button* appears in a view and displays an image, symbol, or icon. You can configure an image button to behave like a push button, toggle, or pop-up button.

**Use an image button in a view, not in the window frame.** For example, avoid placing an image button in a toolbar or status bar. If you need to use an image as a button in a toolbar, use a toolbar item. See [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars).

**Include about 10 pixels of padding between the edges of the image and the button edges.** An image button’s edges define its clickable area even when they aren’t visible. Including padding ensures that a click registers correctly even if it’s not precisely within the image. In general, avoid including a system-provided border in an image button; for developer guidance, see [isBordered](https://developer.apple.com/documentation/appkit/nsbutton/isbordered).

**If you need to include a label, position it below the image button.** For related guidance, see [Labels](https://developer.apple.com/design/human-interface-guidelines/labels).

### Buttons
<sub>`pages/buttons.md`</sub>

Several specific button types are unique to macOS.

### Buttons
<sub>`pages/buttons.md`</sub>

The standard button type in macOS is known as a *push button*. You can configure a push button to display text, a symbol, an icon, or an image, or a combination of text and image content. Push buttons can act as the default button in a view and you can tint them.

**Use a flexible-height push button only when you need to display tall or variable height content.** Flexible-height buttons support the same configurations as regular push buttons — and they use the same corner radius and content padding — so they look consistent with other buttons in your interface. If you need to present a button that contains two lines of text or a tall icon, use a flexible-height button; otherwise, use a standard push button. For developer guidance, see [NSButton.BezelStyle.flexiblePush](https://developer.apple.com/documentation/appkit/nsbutton/bezelstyle-swift.enum/flexiblepush).

**Append a trailing ellipsis to the title when a push button opens another window, view, or app.** Throughout the system, an ellipsis in a control title signals that people can provide additional input. For example, the Edit buttons in the AutoFill pane of Safari Settings include ellipses because they open other views that let people modify autofill values.

**Consider supporting spring loading.** On systems with a Magic Trackpad, *spring loading* lets people activate a button by dragging selected items over it and force clicking — that is, pressing harder — without dropping the selected items. After force clicking, people can continue dragging the items, possibly to perform additional actions.

### Color
<sub>`pages/color.md`</sub>

Beginning in macOS 11, you can specify an *accent color* to customize the appearance of your app’s buttons, selection highlighting, and sidebar icons. The system applies your accent color when the current value in General > Accent color settings is *multicolor*.

![A screenshot of the accent color picker in the System Settings app.](/images/com.apple.HIG/colors-accent-colors-picker-multicolor@2x.png)

If people set their accent color setting to a value other than multicolor, the system applies their chosen color to the relevant items throughout your app, replacing your accent color. The exception is a sidebar icon that uses a fixed color you specify. Because a fixed-color sidebar icon uses a specific color to provide meaning, the system doesn’t override its color when people change the value of accent color settings. For guidance, see [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars).

### Color
<sub>`pages/color.md`</sub>

macOS defines the following dynamic system colors (you can also view them in the Developer palette of the standard Color panel):

| Color | Use for… | AppKit API |
| --- | --- | --- |
| Alternate selected control text color | The text on a selected surface in a list or table. | [alternateSelectedControlTextColor](https://developer.apple.com/documentation/appkit/nscolor/alternateselectedcontroltextcolor) |
| Alternating content background colors | The backgrounds of alternating rows or columns in a list, table, or collection view. | [alternatingContentBackgroundColors](https://developer.apple.com/documentation/appkit/nscolor/alternatingcontentbackgroundcolors) |
| Control accent | The accent color people select in System Settings. | [controlAccentColor](https://developer.apple.com/documentation/appkit/nscolor/controlaccentcolor) |
| Control background color | The background of a large interface element, such as a browser or table. | [controlBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/controlbackgroundcolor) |
| Control color | The surface of a control. | [controlColor](https://developer.apple.com/documentation/appkit/nscolor/controlcolor) |
| Control text color | The text of a control that is available. | [controlTextColor](https://developer.apple.com/documentation/appkit/nscolor/controltextcolor) |
| Current control tint | The system-defined control tint. | [currentControlTint](https://developer.apple.com/documentation/appkit/nscolor/currentcontroltint) |
| Unavailable control text color | The text of a control that’s unavailable. | [disabledControlTextColor](https://developer.apple.com/documentation/appkit/nscolor/disabledcontroltextcolor) |
| Find highlight color | The color of a find indicator. | [findHighlightColor](https://developer.apple.com/documentation/appkit/nscolor/findhighlightcolor) |
| Grid color | The gridlines of an interface element, such as a table. | [gridColor](https://developer.apple.com/documentation/appkit/nscolor/gridcolor) |
| Header text color | The text of a header cell in a table. | [headerTextColor](https://developer.apple.com/documentation/appkit/nscolor/headertextcolor) |
| Highlight color | The virtual light source onscreen. | [highlightColor](https://developer.apple.com/documentation/appkit/nscolor/highlightcolor) |
| Keyboard focus indicator color | The ring that appears around the currently focused control when using the keyboard for interface navigation. | [keyboardFocusIndicatorColor](https://developer.apple.com/documentation/appkit/nscolor/keyboardfocusindicatorcolor) |
| Label color | The text of a label containing primary content. | [labelColor](https://developer.apple.com/documentation/appkit/nscolor/labelcolor) |
| Link color | A link to other content. | [linkColor](https://developer.apple.com/documentation/appkit/nscolor/linkcolor) |
| Placeholder text color | A placeholder string in a control or text view. | [placeholderTextColor](https://developer.apple.com/documentation/appkit/nscolor/placeholdertextcolor) |
| Quaternary label color | The text of a label of lesser importance than a tertiary label, such as watermark text. | [quaternaryLabelColor](https://developer.apple.com/documentation/appkit/nscolor/quaternarylabelcolor) |
| Secondary label color | The text of a label of lesser importance than a primary label, such as a label used to represent a subheading or additional information. | [secondaryLabelColor](https://developer.apple.com/documentation/appkit/nscolor/secondarylabelcolor) |
| Selected content background color | The background for selected content in a key window or view. | [selectedContentBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/selectedcontentbackgroundcolor) |
| Selected control color | The surface of a selected control. | [selectedControlColor](https://developer.apple.com/documentation/appkit/nscolor/selectedcontrolcolor) |
| Selected control text color | The text of a selected control. | [selectedControlTextColor](https://developer.apple.com/documentation/appkit/nscolor/selectedcontroltextcolor) |
| Selected menu item text color | The text of a selected menu. | [selectedMenuItemTextColor](https://developer.apple.com/documentation/appkit/nscolor/selectedmenuitemtextcolor) |
| Selected text background color | The background of selected text. | [selectedTextBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/selectedtextbackgroundcolor) |
| Selected text color | The color for selected text. | [selectedTextColor](https://developer.apple.com/documentation/appkit/nscolor/selectedtextcolor) |
| Separator color | A separator between different sections of content. | [separatorColor](https://developer.apple.com/documentation/appkit/nscolor/separatorcolor) |
| Shadow color | The virtual shadow cast by a raised object onscreen. | [shadowColor](https://developer.apple.com/documentation/appkit/nscolor/shadowcolor) |
| Tertiary label color | The text of a label of lesser importance than a secondary label. | [tertiaryLabelColor](https://developer.apple.com/documentation/appkit/nscolor/tertiarylabelcolor) |
| Text background color | The background color behind text. | [textBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/textbackgroundcolor) |
| Text color | The text in a document. | [textColor](https://developer.apple.com/documentation/appkit/nscolor/textcolor) |
| Under page background color | The background behind a document’s content. | [underPageBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/underpagebackgroundcolor) |
| Unemphasized selected content background color | The selected content in a non-key window or view. | [unemphasizedSelectedContentBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/unemphasizedselectedcontentbackgroundcolor) |
| Unemphasized selected text background color | A background for selected text in a non-key window or view. | [unemphasizedSelectedTextBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/unemphasizedselectedtextbackgroundcolor) |
| Unemphasized selected text color | Selected text in a non-key window or view. | [unemphasizedSelectedTextColor](https://developer.apple.com/documentation/appkit/nscolor/unemphasizedselectedtextcolor) |
| Window background color | The background of a window. | [windowBackgroundColor](https://developer.apple.com/documentation/appkit/nscolor/windowbackgroundcolor) |
| Window frame text color | The text in the window’s title bar area. | [windowFrameTextColor](https://developer.apple.com/documentation/appkit/nscolor/windowframetextcolor) |

### Color wells
<sub>`pages/color-wells.md`</sub>

When people click a color well, it receives a highlight to provide visual confirmation that it’s active. It then opens a color picker so people can choose a color. After they make a selection, the color well updates to show the new color.

Color wells also support drag and drop, so people can drag colors from one color well to another, and from the color picker to a color well.

### Context menus
<sub>`pages/context-menus.md`</sub>

On a Mac, a context menu is sometimes called a *contextual* menu.

### Dark Mode
<sub>`pages/dark-mode.md`</sub>

When people choose the graphite accent color in General settings, macOS causes window backgrounds to pick up color from the current desktop picture. The result — called *desktop tinting* — is a subtle effect that helps windows blend more harmoniously with their surrounding content.

**Include some transparency in custom component backgrounds when appropriate.** Transparency lets your components pick up color from the window background when desktop tinting is active, creating a visual harmony that can persist even when the desktop picture changes. To help achieve this harmony, add transparency only to a custom component that has a visible background or bezel, and only when the component is in a neutral state, such as state that doesn’t use color. You don’t want to add transparency when the component is in a state that uses color, because doing so can cause the component’s color to fluctuate when the window background adjusts to a different location on the desktop or when the desktop picture changes.

### Drag and drop
<sub>`pages/drag-and-drop.md`</sub>

**Consider letting people drag content from your app into the Finder.** When you support this, be sure to present the content in a format your app can open later. For example, Calendar lets people drag an event to the Finder as a `.ics` file. People can share this file with others or drag it back to Calendar to open it. When necessary, you can output dragged content in a *clipping*, which is a temporary container for storing dragged content. For example, most system apps let people drag text to the Finder, where it appears as a clipping. Later, people can drag the clipping into a text field or other location that accepts text. Note that a drag-and-drop clipping isn’t related to the Clipboard.

**Let people drag selected content from an inactive window without first making the window active.** Selected content in an inactive window is known as a *background selection* and has a different appearance from selected content in the active window. In general, people expect to drag a background selection to the active window without bringing the inactive window forward.

**When possible, let people drag individual items from an inactive window without affecting an existing background selection.** For example, people can drag an unselected file from an inactive Finder window without deselecting any of the window’s selected files.

**Consider displaying a badge during multi-item drag operations.** A badge is a small filled oval containing a number you can use to indicate the number of items people are dragging. If a destination can accept only a subset of dragged items, update the badge to show the new number.

**Consider changing the pointer appearance to indicate what will happen when people drop content.** In addition to using the *copy* pointer, you might want to use the *drag link*, *disappearing item*, and *operation not allowed* pointers, depending on the situation. For guidance, see [Pointers](https://developer.apple.com/design/human-interface-guidelines/pointing-devices#Pointers).

**As much as possible, let people select and drag content with a single motion.** Unless people are selecting multiple items, they appreciate it when they don’t have to pause between making a selection and starting the drag operation.

### Edit menus
<sub>`pages/edit-menus.md`</sub>

To learn about the order of items in a macOS app’s Edit menu, see [Edit menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Edit-menu).

### Entering data
<sub>`pages/entering-data.md`</sub>

**Consider using an expansion tooltip to show the full version of clipped or truncated text in a field.** An *expansion tooltip* behaves like a regular tooltip, appearing when the pointer rests on top of a field. Apps running in macOS — including iOS and iPadOS apps running on a Mac — can use an expansion tooltip to help people view the complete data they entered when a text field is too small to display it. For guidance, see [Offering help > macOS, visionOS](https://developer.apple.com/design/human-interface-guidelines/offering-help#macOS-visionOS).

### File management
<sub>`pages/file-management.md`</sub>

If your app syncs local and remote files, you can create a Finder Sync app extension to express file synchronization status and control within the Finder. For developer guidance, see [Finder Sync](https://developer.apple.com/documentation/findersync).

For example, you can use a Finder Sync extension to:

- Display badges in the Finder to indicate the sync status of items
- Provide custom contextual menu items that perform file and folder management tasks, like favoriting and adding password-protection
- Provide custom toolbar buttons that perform global actions, like initiating a sync operation

**Help people avoid losing work if they turn off autosaving.** People can turn off autosaving by selecting the “Ask to keep changes when closing documents” toggle in Desktop & Dock settings. In this scenario, show that a document has unsaved changes and present a save dialog when people choose to close the document, quit your app, log out, or restart.

**When autosaving is off, make sure people know when a document has unsaved changes.** To show that there are unsaved changes, display a dot on the document window’s close button and next to the document’s name in your app’s Window menu. When autosaving is on, showing a dot in these locations is confusing, because it implies that people need to take action to avoid losing their work. Regardless of autosave status, you can append “Edited” to the document’s title in the title bar, but be sure to remove this suffix as soon as autosave occurs or when people explicitly save their work.

### File management
<sub>`pages/file-management.md`</sub>

People have strong associations with the familiar file browsing experience of the Finder and most document-based apps. Use the default file browser unless you have an important reason to create a custom one.

**Make your custom file-opening interface convenient.** For example, people might appreciate an “open recent” action in addition to the simple “open” action. You might also want to let people choose criteria on which to filter the file-browsing experience, or select multiple documents to open at once. In a macOS open panel, you can customize the title of the Open button to reflect the task — for example, if your app lets people insert a file’s contents into the current document, you might change the title to Insert.

**Provide a save interface to let people change a file’s name, format, or location.** By default, a new document’s title is “Untitled” until people choose a custom name. As with a document-opening interface, a save view can also provide a browsing experience that defaults to a logical location to help people place the saved document where they want. If you support saving content in different formats, also give people a way to choose a specific file format.

**Consider extending the functionality of the Save dialog.** If it makes sense in your app, you can add a custom accessory view containing useful settings or options to the Save dialog. For example, the dialog for saving Mail messages as files contains an option to include attachments.

### Gauges
<sub>`pages/gauges.md`</sub>

In addition to supporting gauges, macOS also defines a level indicator that displays a specific numerical value within a range. You can configure a level indicator to convey capacity, rating, or — rarely — relevance.

The capacity style can depict discrete or continuous values.

![An image of a continuous capacity indicator that uses the default green fill to indicate an amount of about two-thirds of the total capacity.](/images/com.apple.HIG/indicators-continuous@2x.png)

**Continuous.** A horizontal translucent track that fills with a solid bar to indicate the current value.

![An image of a discrete capacity indicator that uses the default green fill to indicate an amount of three-quarters of the total capacity.](/images/com.apple.HIG/indicators-discrete@2x.png)

**Discrete.** A horizontal row of separate, equally sized, rectangular segments. The number of segments matches the total capacity, and the segments fill completely — never partially — with color to indicate the current value.

**Consider using the continuous style for large ranges.** A large value range can make the segments of a discrete capacity indicator too small to be useful.

**Consider changing the fill color to inform people about significant parts of the range.** By default, the fill color for both capacity indicator styles is green. If it makes sense in your app, you can change the fill color when the current value reaches certain levels, such as very low, very high, or just past the middle. You can change the fill color of the entire indicator or you can use the tiered state to show a sequence of several colors in one indicator, as shown below.

![An image of a continuous capacity indicator in which the leftmost one-eigth is red, the next three-eighths are yellow, the next one-fourth is green, and the last one-fourth is unfilled.](/images/com.apple.HIG/indicators-continuous-tiered@2x.png)

For guidance using the rating style to help people rank something, see [Rating indicators](https://developer.apple.com/design/human-interface-guidelines/rating-indicators).

Although rarely used, the relevance style can communicate relevancy using a shaded horizontal bar. For example, a relevance indicator might appear in a list of search results, helping people visualize the relevancy of the results when sorting or comparing multiple items.

### Gestures
<sub>`pages/gestures.md`</sub>

People primarily interact with macOS using a [Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards) and mouse. In addition, they can make [Standard gestures](https://developer.apple.com/design/human-interface-guidelines/gestures#Standard-gestures) on a Magic Trackpad, Magic Mouse, or a [Game controls](https://developer.apple.com/design/human-interface-guidelines/game-controls) that includes a touch surface.

### Going full screen
<sub>`pages/going-full-screen.md`</sub>

**Use the system-provided full-screen experience.** Using the system’s full-screen support ensures that your full-screen window works well in all contexts. For example, some Mac models include a camera housing that occupies an area at the top-center of the screen. Using the system’s full-screen support automatically accommodates this area. For developer guidance, see [toggleFullScreen(_:)](https://developer.apple.com/documentation/appkit/nswindow/togglefullscreen(_:)).

**In a game, don’t change the display mode when players go full screen.** People expect to be in control of their display mode, and changing it automatically doesn’t improve performance.

For additional developer guidance, see [Managing your game window for Metal in macOS](https://developer.apple.com/documentation/metal/managing-your-game-window-for-metal-in-macos).

**Always let people choose when to enter full-screen mode.** Prefer letting people use your window’s Enter Full Screen button, View menu item, or the Control-Command-F keyboard shortcut. Avoid offering a custom menu of window modes. In a game, you might also provide a custom [toggle](https://developer.apple.com/design/human-interface-guidelines/toggles) that turns full-screen mode on and off.

### Icons
<sub>`pages/icons.md`</sub>

If your macOS app can use a custom document type, you can create a document icon to represent it. Traditionally, a document icon looks like a piece of paper with its top-right corner folded down. This distinctive appearance helps people distinguish documents from apps and other content, even when icon sizes are small.

If you don’t supply a document icon for a file type you support, macOS creates one for you by compositing your app icon and the file’s extension onto the canvas. For example, Preview uses a system-generated document icon to represent JPG files.

![An image of the Preview document icon for a JPG file.](/images/com.apple.HIG/doc-icon-generated@2x.png)

In some cases, it can make sense to create a set of document icons to represent a range of file types your app handles. For example, Xcode uses custom document icons to help people distinguish projects, AR objects, and Swift code files.

![Image of an Xcode project document icon.](/images/com.apple.HIG/doc-icon-custom-1@2x.png)

![Image of a document icon for an AR object.](/images/com.apple.HIG/doc-icon-custom-2@2x.png)

![Image of a document icon for a Swift file.](/images/com.apple.HIG/doc-icon-custom-3@2x.png)

To create a custom document icon, you can supply any combination of background fill, center image, and text. The system layers, positions, and masks these elements as needed and composites them onto the familiar folded-corner icon shape.

![A square canvas that contains a grid of pink lines and a jagged white EKG line that runs horizontally across the middle. The pink grid gets lighter in color toward the bottom edge.](/images/com.apple.HIG/doc-icon-parts-background-fill@2x.png)

![A solid pink heart.](/images/com.apple.HIG/doc-icon-parts-center-image@2x.png)

![The word heart in all caps.](/images/com.apple.HIG/doc-icon-parts-text@2x.png)

![A custom document icon that displays the pink heart and the word heart on top of the pink grid and white EKG line.](/images/com.apple.HIG/doc-icon-parts@2x.png)

[Apple Design Resources](https://developer.apple.com/design/resources/#macos-apps) provides a template you can use to create a custom background fill and center image for a document icon. As you use this template, follow the guidelines below.

**Design simple images that clearly communicate the document type.** Whether you use a background fill, a center image, or both, prefer uncomplicated shapes and a reduced palette of distinct colors. Your document icon can display as small as 16x16 px, so you want to create designs that remain recognizable at every size.

**Designing a single, expressive image for the background fill can be a great way to help people understand and recognize a document type.** For example, Xcode and TextEdit both use rich background images that don’t include a center image.

![Image of an Xcode project document icon.](/images/com.apple.HIG/doc-icon-custom-1@2x.png)

![Image of a TextEdit rich text document icon.](/images/com.apple.HIG/doc-icon-fill-only@2x.png)

**Consider reducing complexity in the small versions of your document icon.** Icon details that are clear in large versions can look blurry and be hard to recognize in small versions. For example, to ensure that the grid lines in the custom heart document icon remain clear in intermediate sizes, you might use fewer lines and thicken them by aligning them to the reduced pixel grid. In the 16x16 px size, you might remove the lines altogether.

![Pixelated image of the heart document icon. The grid, the EKG line, the heart shape, and the word heart are visible but blurry.](/images/com.apple.HIG/doc-icon-fewer-details-1@2x.png)

![Pixelated image of the heart document icon, in which only the blurry heart shape and EKG line are visible.](/images/com.apple.HIG/doc-icon-fewer-details-2@2x.png)

![Pixelated image of the heart document icon, in which only the blurry heart shape is visible.](/images/com.apple.HIG/doc-icon-fewer-details-3@2x.png)

**Avoid placing important content in the top-right corner of your background fill.** The system automatically masks your image to fit the document icon shape and draws the white folded corner on top of the fill. Create a set of background images in the sizes listed below.

- 512x512 px @1x, 1024x1024 px @2x
- 256x256 px @1x, 512x512 px @2x
- 128x128 px @1x, 256x256 px @2x
- 32x32 px @1x, 64x64 px @2x
- 16x16 px @1x, 32x32 px @2x

**If a familiar object can convey a document’s type or its connection with your app, consider creating a center image that depicts it.** Design a simple, unambiguous image that’s clear and recognizable at every size. The center image measures half the size of the overall document icon canvas. For example, to create a center image for a 32x32 px document icon, use an image canvas that measures 16x16 px. You can provide center images in the following sizes:

- 256x256 px @1x, 512x512 px @2x
- 128x128 px @1x, 256x256 px @2x
- 32x32 px @1x, 64x64 px @2x
- 16x16 px @1x, 32x32 px @2x

**Define a margin that measures about 10% of the image canvas and keep most of the image within it.** Although parts of the image can extend into this margin for optical alignment, it’s best when the image occupies about 80% of the image canvas. For example, most of the center image in a 256x256 px canvas would fit in an area that measures 205x205 px.

![Diagram of the solid pink heart shape within blue margins that measure 10 percent of the canvas width.](/images/com.apple.HIG/doc-icon-parts-margins@2x.png)

**Specify a succinct term if it helps people understand your document type.** By default, the system displays a document’s extension at the bottom edge of the document icon, but if the extension is unfamiliar you can supply a more descriptive term. For example, the document icon for a SceneKit scene file uses the term *scene* instead of the file extension *scn*. The system automatically scales the extension text to fit in the document icon, so be sure to use a term that’s short enough to be legible at small sizes. By default, the system capitalizes every letter in the text.

![Image of a SceneKit scene document icon.](/images/com.apple.HIG/doc-icon-custom-extension@2x.png)

### Image views
<sub>`pages/image-views.md`</sub>

**If your app needs an editable image view, use an image well.** An [image well](https://developer.apple.com/design/human-interface-guidelines/image-wells) is an image view that supports copying, pasting, dragging, and using the Delete key to clear its content.

**Use an image button instead of an image view to make a clickable image.** An [image button](https://developer.apple.com/design/human-interface-guidelines/buttons#Image-buttons) contains an image or icon, appears in a view, and initiates an instantaneous app-specific action.

### Labels
<sub>`pages/labels.md`</sub>

> **Note:** To display uneditable text in a label, use the [isEditable](https://developer.apple.com/documentation/appkit/nstextfield/iseditable) property of [NSTextField](https://developer.apple.com/documentation/appkit/nstextfield).

### Layout
<sub>`pages/layout.md`</sub>

**Avoid placing controls or critical information at the bottom of a window.** People often move windows so that the bottom edge is below the bottom of the screen.

**Avoid displaying content within the camera housing at the top edge of the window.** For developer guidance, see [NSPrefersDisplaySafeAreaCompatibilityMode](https://developer.apple.com/documentation/bundleresources/information-property-list/nsprefersdisplaysafeareacompatibilitymode).

### Lists and tables
<sub>`pages/lists-and-tables.md`</sub>

**When it provides value, let people click a column heading to sort a table view based on that column**. If people click the heading of a column that’s already sorted, re-sort the data in the opposite direction.

**Let people resize columns.** Data displayed in a table view often varies in width. People appreciate resizing columns to help them concentrate on different areas or reveal clipped data.

**Consider using alternating row colors in a multicolumn table.** Alternating colors can help people track row values across columns, especially in a wide table.

**Use an outline view instead of a table view to present hierarchical data.** An [outline view](https://developer.apple.com/design/human-interface-guidelines/outline-views) looks like a table view, but includes disclosure triangles for exposing nested levels of data. For example, an outline view might display folders and the items they contain.

### Live Activities
<sub>`pages/live-activities.md`</sub>

Active Live Activities automatically appear in the Menu bar of a paired Mac using the compact, minimal, and expanded presentations. Clicking the Live Activity launches iPhone Mirroring to display your app.

### Materials
<sub>`pages/materials.md`</sub>

macOS provides several standard materials with designated purposes, and vibrant versions of all [Specifications](https://developer.apple.com/design/human-interface-guidelines/color#Specifications). For developer guidance, see [NSVisualEffectView.Material](https://developer.apple.com/documentation/appkit/nsvisualeffectview/material-swift.enum).

**Choose when to allow vibrancy in custom views and controls.** Depending on configuration and system settings, system views and controls use vibrancy to make foreground content stand out against any background. Test your interface in a variety of contexts to discover when vibrancy enhances the appearance and improves communication.

**Choose a background blending mode that complements your interface design.** macOS defines two modes that blend background content: behind window and within window. For developer guidance, see [NSVisualEffectView.BlendingMode](https://developer.apple.com/documentation/appkit/nsvisualeffectview/blendingmode-swift.enum).

### Multitasking
<sub>`pages/multitasking.md`</sub>

On Mac, multitasking is the default experience because people typically run more than one app at a time, switching between windows and tasks as they work. When multiple app windows are open, macOS applies drop shadows that make the windows appear layered on the desktop, and applies other visual effects to help people distinguish different window states; for guidance, see [macOS window states](https://developer.apple.com/design/human-interface-guidelines/windows#macOS-window-states).

### Offering help
<sub>`pages/offering-help.md` — upstream heading: macOS, visionOS</sub>

A *tooltip* (called a *help tag* in user documentation) displays a small, transient view that briefly describes how to use a component in the interface. In apps that run on a Mac — including iPhone and iPad apps — tooltips can appear when a person holds the pointer over an element; in visionOS apps, a tooltip can appear when a person looks at an element or holds the pointer over it. For developer guidance, see [help(_:)](https://developer.apple.com/documentation/swiftui/view/help(_:)-6oiyb).

![An illustration of a toolbar in macOS Finder with the pointer over the Back button. A tooltip with the title See folders you viewed previously appears beneath the pointer.](/images/com.apple.HIG/offering-help-macos-tooltip-help-tag@2x.png)

**Describe only the control that people indicate interest in.** When people want to know how to use a specific control, they don’t want to learn how to use nearby controls or how to perform a larger task.

**Explain the action or task the control initiates.** It often works well to begin the description with a verb — for example, “Restore default settings” or “Add or remove a language from the list.”

**In general, avoid repeating a control’s name in its tooltip.** Repeating the name takes up space in the tooltip and rarely adds value to the description.

**Be brief.** As much as possible, limit tooltip content to a maximum of 60 to 75 characters (note that localization often changes the length of text). To make a description brief and direct, consider using a sentence fragment and omitting articles. If you need a lot of text to describe a control, consider simplifying your interface design.

**Use sentence case.** Sentence case tends to appear more casual and approachable. If you write complete sentences, omit ending punctuation unless it’s required to be consistent with your app’s style.

**Consider offering context-sensitive tooltips.** For example, you could provide different text for a control’s different states.

### Pickers
<sub>`pages/pickers.md`</sub>

**Choose a date picker style that suits your app.** There are two styles of date pickers in macOS: textual and graphical. The textual style is useful when you’re working with limited space and you expect people to make specific date and time selections. The graphical style is useful when you want to give people the option of browsing through days in a calendar or selecting a range of dates, or when the look of a clock face is appropriate for your app.

For developer guidance, see [NSDatePicker](https://developer.apple.com/documentation/appkit/nsdatepicker).

### Playing audio
<sub>`pages/playing-audio.md`</sub>

In macOS, notification sounds mix with other audio by default.

### Playing haptics
<sub>`pages/playing-haptics.md`</sub>

When a Magic Trackpad is available, your app can provide one of the three following haptic patterns in response to a drag operation or force click.

| Haptic feedback pattern | Description |
| --- | --- |
| Alignment | Indicates the alignment of a dragged item. For example, this pattern could be used in a drawing app when the people drag a shape into alignment with another shape. Other scenarios where this type of feedback could be used might include scaling an object to fit within specific dimensions, positioning an object at a preferred location, or reaching the beginning/end or minimum/maximum of something like a scrubber in a video app. |
| Level change | Indicates movement between discrete levels of pressure. For example, as people press a fast-forward button on a video player, playback could increase or decrease and haptic feedback could be provided as different levels of pressure are reached. |
| Generic | Intended for providing general feedback when the other patterns don’t apply. |

For developer guidance, see [NSHapticFeedbackPerformer](https://developer.apple.com/documentation/appkit/nshapticfeedbackperformer).

### Pointing devices
<sub>`pages/pointing-devices.md`</sub>

macOS offers a variety of standard pointer styles, which your app can use to communicate the interactive state of an interface element or the result of a drag operation.

| Pointer | Name | Meaning | AppKit API |
| --- | --- | --- | --- |
| ![A pointer that resembles a diagonal arrow pointing up and to the left.](/images/com.apple.HIG/pointers-arrow@2x.png) | Arrow | Standard pointer for selecting and interacting with content and interface elements. | [arrow](https://developer.apple.com/documentation/appkit/nscursor/arrow) |
| ![A closed, gloved hand.](/images/com.apple.HIG/pointers-closed-hand@2x.png) | Closed hand | Dragging to reposition the display of content within a view—for example, dragging a map around in Maps. | [closedHand](https://developer.apple.com/documentation/appkit/nscursor/closedhand) |
| ![A pointer arrow with a small menu-like square to the right of the arrow.](/images/com.apple.HIG/pointers-contextual-menu@2x.png) | Contextual menu | A contextual menu is available for the content below the pointer. This pointer is generally shown only when the Control key is pressed. | [contextualMenu](https://developer.apple.com/documentation/appkit/nscursor/contextualmenu) |
| ![A plus symbol.](/images/com.apple.HIG/pointers-crosshair@2x.png) | Crosshair | Precise rectangular selection is possible, such as when viewing an image in Preview. | [crosshair](https://developer.apple.com/documentation/appkit/nscursor/crosshair) |
| ![A small pointer arrowhead with a circle underneath; the circle contains an Ex.](/images/com.apple.HIG/pointers-disappearing-item@2x.png) | Disappearing item | A dragged item will disappear when dropped. If the item references an original item, the original is unaffected. For example, when dragging a mailbox out of the favorites bar in Mail, the original mailbox isn’t removed. | [disappearingItem](https://developer.apple.com/documentation/appkit/nscursor/disappearingitem) |
| ![A small pointer arrowhead with a circle underneath; the circle contains a plus symbol.](/images/com.apple.HIG/pointers-drag-copy@2x.png) | Drag copy | Duplicates a dragged—not moved—item when dropped into the destination. Appears when pressing the Option key during a drag operation. | [dragCopy](https://developer.apple.com/documentation/appkit/nscursor/dragcopy) |
| ![A curved arrow, pointing up and to the right.](/images/com.apple.HIG/pointers-drag-link@2x.png) | Drag link | During a drag and drop operation, creates an alias of the selected file when dropped. The alias points to the original file, which remains unmoved. Appears when pressing the Option and Command keys during a drag operation. | [dragLink](https://developer.apple.com/documentation/appkit/nscursor/draglink) |
| ![Opposing veritcal braces, used to form an insertion marker.](/images/com.apple.HIG/pointers-horizontal-beam@2x.png) | Horizontal I beam | Selection and insertion of text is possible in a horizontal layout, such as a TextEdit or Pages document. | [iBeam](https://developer.apple.com/documentation/appkit/nscursor/ibeam) |
| ![An open, gloved hand.](/images/com.apple.HIG/pointers-open-hand@2x.png) | Open hand | Dragging to reposition content within a view is possible. | [openHand](https://developer.apple.com/documentation/appkit/nscursor/openhand) |
| ![A small pointer arrowhead with a do not enter symbol underneath.](/images/com.apple.HIG/pointers-operation-not-allowed@2x.png) | Operation not allowed | A dragged item can’t be dropped in the current location. | [operationNotAllowed](https://developer.apple.com/documentation/appkit/nscursor/operationnotallowed) |
| ![A gloved hand, with the index finger extended.](/images/com.apple.HIG/pointers-pointing-hand@2x.png) | Pointing hand | The content beneath the pointer is a URL link to a webpage, document, or other item. | [pointingHand](https://developer.apple.com/documentation/appkit/nscursor/pointinghand) |
| ![A horizontal bar with a downward-pointing arrow at its midpoint.](/images/com.apple.HIG/pointers-resize-down@2x.png) | Resize down | Resize or move a window, view, or element downward. | [resizeDown](https://developer.apple.com/documentation/appkit/nscursor/resizedown) |
| ![A vertical bar with a left-pointing arrow at its midpoint.](/images/com.apple.HIG/pointers-resize-left@2x.png) | Resize left | Resize or move a window, view, or element to the left. | [resizeLeft](https://developer.apple.com/documentation/appkit/nscursor/resizeleft) |
| ![A vertical bar with left- and right-pointing arrows extending from its midpoint.](/images/com.apple.HIG/pointers-resize-left-right@2x.png) | Resize left/right | Resize or move a window, view, or element to the left or right. | [resizeLeftRight](https://developer.apple.com/documentation/appkit/nscursor/resizeleftright) |
| ![A vertical bar with a right-pointing arrow at its midpoint.](/images/com.apple.HIG/pointers-resize-right@2x.png) | Resize right | Resize or move a window, view, or element to the right. | [resizeRight](https://developer.apple.com/documentation/appkit/nscursor/resizeright) |
| ![A horizontal bar with an up-pointing arrow at its midpoint.](/images/com.apple.HIG/pointers-resize-up@2x.png) | Resize up | Resize or move a window, view, or element upward. | [resizeUp](https://developer.apple.com/documentation/appkit/nscursor/resizeup) |
| ![A horizontal bar with up- and down-pointing arrows extending from its midpoint.](/images/com.apple.HIG/pointers-resize-up-down@2x.png) | Resize up/down | Resize or move a window, view, or element upward or downward. | [resizeUpDown](https://developer.apple.com/documentation/appkit/nscursor/resizeupdown) |
| ![Opposing horizontal braces, used to form an insertion marker.](/images/com.apple.HIG/pointers-vertical-beam@2x.png) | Vertical I beam | Selection and insertion of text is possible in a vertical layout. | [iBeamCursorForVerticalLayout](https://developer.apple.com/documentation/appkit/nscursor/ibeamcursorforverticallayout) |

### Pointing devices
<sub>`pages/pointing-devices.md`</sub>

macOS supports a wide range of standard mouse and trackpad interactions that people can customize. For example, when a click or gesture isn’t a primary way to interact with content, people can often turn it on or off based on their current workflow. People can also choose specific regions of a mouse or trackpad to invoke secondary clicks, and select specific finger combinations and movements for certain gestures.

| Click or gesture | Expected behavior | Mouse | Trackpad |
| --- | --- | --- | --- |
| Primary click | Select or activate an item, such as a file or button. | ● | ● |
| Secondary click | Reveal contextual menus. | ● | ● |
| Scrolling | Move content up, down, left, or right within a view. | ● | ● |
| Smart zoom | Zoom in or out on content, such as a web page or PDF. | ● | ● |
| Swipe between pages | Navigate forward or backward between individually displayed pages. | ● | ● |
| Swipe between full-screen apps | Navigate forward or backward between full-screen apps and spaces. | ● | ● |
| Mission Control (double-tap the mouse with two fingers or swipe up on the trackpad with three or four fingers) | Activate Mission Control. | ● | ● |
| Lookup and data detectors (force click with one finger or tap with three fingers) | Display a lookup window above selected content. |  | ● |
| Tap to click | Perform the primary click action using a tap rather than a click. |  | ● |
| Force click | Click then press firmly to display a Quick Look window or lookup window above selected content. Apply a variable amount of pressure to affect pressure-sensitive controls, such as variable speed media controls. |  | ● |
| Zoom in or out (pinch with two fingers) | Zoom in or out. |  | ● |
| Rotate (move two fingers in a circular motion) | Rotate content, such as an image. |  | ● |
| Notification Center (swipe from the edge of the trackpad) | Display Notification Center. |  | ● |
| App Exposé (swipe down with three or four fingers) | Display the current app’s windows in Exposé. |  | ● |
| Launchpad (pinch with thumb and three fingers) | Display the Launchpad. |  | ● |
| Show Desktop (spread with thumb and three fingers) | Slide all windows out of the way to reveal the desktop. |  | ● |

### Popovers
<sub>`pages/popovers.md`</sub>

You can make a popover detachable in macOS, which becomes a separate panel when people drag it. The panel remains visible onscreen while people interact with other content.

**Attached popover**

![An illustration of an event in Calendar with the attached version of the event's popover next to and pointing to it.](/images/com.apple.HIG/attached-popover@2x.png)

**Detached popover**

![An illustration of an event in Calendar with the detached version of the event's popover next to it.](/images/com.apple.HIG/detached-popover@2x.png)


**Consider letting people detach a popover.** People might appreciate being able to convert a popover into a panel if they want to view other information while the popover remains visible.

**Make minimal appearance changes to a detached popover.** A panel that looks similar to the original popover helps people maintain context.

### Printing
<sub>`pages/printing.md`</sub>

**If your macOS app offers app-specific print options that the system doesn’t offer, consider creating a custom category for the print panel.** By default, the print panel offers several categories of settings, such as Layout, Paper Handling, and Media & Quality. Give your custom category a unique name, such as your app name, and include options that help people have a great print experience in your app. For example, Keynote offers presentation-specific options, like the ability to print presenter notes, slide backgrounds, and skipped slides.

**If your app supports document-specific page settings, consider presenting a page setup dialog.** A *page setup dialog* includes rarely changed settings for page size, orientation, and scaling that apply to printing a particular document. If this makes sense in your app, avoid implementing features the system already provides. For example, you don’t need to include options like changing the page orientation or printing in reverse order because the system implements these options.

**Make sure interdependencies between options are clear.** For example, if double-sided printing is available, an option to print on transparencies becomes unavailable.

**Separate advanced features from frequently used features.** Consider using a disclosure control to hide advanced options until they’re needed. Label advanced options as *Advanced Options*.

**Consider letting people preview the effect of a setting.** For example, you could update a thumbnail image to show the effect of changing a tone control.

**Consider storing modified settings with the document.** At minimum, it makes sense to store print settings until the document is closed in case people want to print it again.

### Privacy
<sub>`pages/privacy.md`</sub>

**Sign your app with a valid Developer ID.** If you choose to distribute your app outside the store, signing your app with Developer ID identifies you as an Apple developer and confirms that your app is safe to use. For developer guidance, see [Xcode Help](https://developer.apple.com/go/?id=ios-app-distribution-guide).

**Protect people’s data with app sandboxing.** Sandboxing provides your app with access to system resources and user data while protecting it from malware. All apps submitted to the Mac App Store require sandboxing. For developer guidance, see [Configuring the macOS App Sandbox](https://developer.apple.com/documentation/xcode/configuring-the-macos-app-sandbox).

**Avoid making assumptions about who is signed in.** Because of fast user switching, multiple people may be active on the same system.

### Progress indicators
<sub>`pages/progress-indicators.md`</sub>

In macOS, an indeterminate progress indicator can have a bar or circular appearance. Both versions use an animated image to indicate that the app is performing a task.

![An image of a completely filled horizontal progress bar in macOS. The fill is animated to cycle through various shade changes as progress continues.](/images/com.apple.HIG/progress-indicator-intermediate-bar@2x.png)

![An image of a spinning, circular activity indicator in macOS.](/images/com.apple.HIG/progress-indicator-intermediate-spinner@2x.png)

**Prefer an activity indicator (spinner) to communicate the status of a background operation or when space is constrained.** Spinners are small and unobtrusive, so they’re useful for asynchronous background tasks, like retrieving messages from a server. Spinners are also good for communicating progress within a small area, such as within a text field or next to a specific control, such as a button.

**Avoid labeling a spinning progress indicator.** Because a spinner typically appears when people initiate a process, a label is usually unnecessary.

### Scroll views
<sub>`pages/scroll-views.md`</sub>

In macOS, a *scroll indicator* is commonly called a *scroll bar*.

**If necessary, use small or mini scroll bars in a panel.** When space is tight, you can use smaller scroll bars in panels that need to coexist with other windows. Be sure to use the same size for all controls in such a panel.

### Search fields
<sub>`pages/search-fields.md` — upstream heading: iPadOS, macOS</sub>

The placement and behavior of the search field in iPadOS and macOS is similar. If your app is available on both iPad and Mac, try to keep the search experience as consistent as possible across both platforms.

![An illustration of an iPad screen with a search field on the trailing edge of the top toolbar. The search field has the word Design entered into the field, and three search suggestions appear in a list beneath the field.](/images/com.apple.HIG/search-fields-toolbar-search-ipad@2x.png)

![An illustration of a Mac screen with a search field on the trailing edge of the toolbar. The search field has the word Design entered into the field, and three search suggestions appear in a list beneath the field.](/images/com.apple.HIG/search-fields-toolbar-search-mac@2x.png)

**Put a search field at the trailing side of the toolbar for many common uses.** Many apps benefit from the familiar pattern of search in the toolbar, particularly apps with split views that need to search across multiple columns of information, like Mail, Notes, and Voice Memos. This placement makes great use of space because it lets people navigate results while keeping their selection visible in the detail view. Additionally, consider placing search in the toolbar if results appear in the detail view of your app, like in Freeform, where search in the toolbar filters the boards in the detail view below.

**Include search at the top of the sidebar when filtering content or navigation there.** Apps such as Settings take advantage of search to quickly filter the sidebar and expose sections that may be multiple levels deep, providing a simple way for people to search, preview, and navigate to the section or setting they’re looking for. This approach is useful if your app has a rich detail view and you need to create a distinct separation between the sidebar you’re filtering and the adjacent view.

![An illustration of an iPad screen with a search field at the top of the sidebar on the leading edge of the screen.](/images/com.apple.HIG/search-fields-ipad-search-in-sidebar@2x.png)

**Include search as an item in the sidebar or tab bar when you want an area dedicated to discovery.** If your search is paired with rich suggestions, categories, or content that needs more space, it can be helpful to have a dedicated area for it. This is particularly useful for apps where browsing and search go hand in hand, like Music and TV, where it provides a unified location to highlight suggested content, categories, and recent searches. A dedicated area also ensures search is always available as people navigate and switch sections of your app.

![An illustration of an iPad screen with a tab bar at the top edge. The trailing side of the tab bar includes a Search tab with a distinct background color to differentiate it from other tab areas.](/images/com.apple.HIG/search-fields-ipad-search-in-tab-bar@2x.png)

**In a search field in a dedicated area, consider immediately focusing the field when a person navigates to the area to help them search faster and locate the field more easily.** An exception to this is on iPad when only a virtual keyboard is available, in which case it’s better to leave the field unfocused to prevent the keyboard from unexpectedly covering the view.

**Account for window resizing with the placement of the search field.** On iPad, the search field fluidly resizes with the app window like it does on Mac. However, for compact views on iPad, itʼs important to ensure that search is available where it’s most contextually useful. For example, Notes and Mail place search above the column for the content list when they resize down to a compact view.

### Segmented controls
<sub>`pages/segmented-controls.md`</sub>

**Consider using introductory text to clarify the purpose of a segmented control.** When the control uses symbols or interface icons, you could also add a label below each segment to clarify its meaning. If your app includes tooltips, provide one for each segment in a segmented control.

**Use a tab view in the main window area — instead of a segmented control — for view switching.** A [Tab views](https://developer.apple.com/design/human-interface-guidelines/tab-views) supports efficient view switching and is similar in appearance to a [Boxes](https://developer.apple.com/design/human-interface-guidelines/boxes) combined with a segmented control. Consider using a segmented control to help people switch views in a toolbar or inspector pane.

![A screenshot of the macOS Calendar app. The main window area shows a tab view that contains four tabs: Day, Week, Month, and Year. The sidebar shows a segmented control that contains two segments: New and Replied.](/images/com.apple.HIG/macos-calendar-tab-view-segmented-control-comparison@2x.png)

**Consider supporting spring loading.** On a Mac equipped with a Magic Trackpad, spring loading lets people activate a segment by dragging selected items over it and force clicking without dropping the selected items. People can also continue dragging the items after a segment activates.

### Settings
<sub>`pages/settings.md`</sub>

When people choose the Settings item in your app’s or game’s App menu, your custom settings window opens. Typically, a custom settings window contains a toolbar that includes buttons for switching between views — called *panes* — that each contain a group of related settings.

**Include a settings item in the [App menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#App-menu).** Avoid adding settings buttons to a window’s toolbar, because doing so decreases the space available for essential commands that people use frequently. If you provide document-level options, add this item to your app’s [File menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#File-menu).

**Dim a settings window’s minimize and maximize buttons.** It’s quick to open a custom settings window using the standard Command–Comma (,) keyboard command, so there’s no need to keep the window in the Dock, and because a settings window accommodates the size of the current pane, people don’t need to expand the window to see more.

**In your settings window, use a noncustomizable toolbar that remains visible and always indicates the active toolbar button.** A settings window’s toolbar identifies the areas people can customize and helps people navigate among those areas. People rely on a stable settings interface to help them find what they need.

**Update the window’s title to reflect the currently visible pane.** If your settings window doesn’t have multiple panes, use the title *App Name* Settings.

**Restore the most recently viewed pane.** People often adjust related settings more than once, so it can be convenient when a settings window opens to the last pane people used.

### Sheets
<sub>`pages/sheets.md`</sub>

In macOS, a sheet is a cardlike view with rounded corners that floats on top of its parent window. The parent window is dimmed while the sheet is onscreen, signaling that people can’t interact with it until they dismiss the sheet. However, people expect to interact with other app windows before dismissing a sheet.

![A screenshot of the Notes app, with the What's New in Notes sheet centered on top of a dimmed Notes document in the background.](/images/com.apple.HIG/sheets-macos-notes@2x.png)

**Present a sheet in a reasonable default size.** People don’t generally expect to resize sheets, so it’s important to use a size that’s appropriate for the content you display. In some cases, however, people appreciate a resizable sheet — such as when they need to expand the contents for a clearer view — so it’s a good idea to support resizing.

**Let people interact with other app windows without first dismissing a sheet.** When a sheet opens, you bring its parent window to the front — if the parent window is a document window, you also bring forward its modeless document-related panels. When people want to interact with other windows in your app, make sure they can bring those windows forward even if they haven’t dismissed the sheet yet.

**Use a panel instead of a sheet if people need to repeatedly provide input and observe results.** A find and replace panel, for example, might let people initiate replacements individually, so they can observe the result of each search for correctness. For guidance, see [Panels](https://developer.apple.com/design/human-interface-guidelines/panels).

### Sidebars
<sub>`pages/sidebars.md`</sub>

A sidebar’s row height, text, and glyph size depend on its overall size, which can be small, medium, or large. You can set the size programmatically, but people can also change it by selecting a different sidebar icon size in General settings.

**Consider automatically hiding and revealing a sidebar when its container window resizes.** For example, reducing the size of a Mail viewer window can automatically collapse its sidebar, making more room for message content.

**Avoid putting critical information or actions at the bottom of a sidebar.** People often relocate a window in a way that hides its bottom edge.

### Sliders
<sub>`pages/sliders.md`</sub>

Sliders in macOS can also include tick marks, making it easier for people to pinpoint a specific value within the range.

In a linear slider either with or without tick marks, the thumb is a narrow lozenge shape, and the portion of track between the minimum value and the thumb is filled with color. A linear slider often includes supplementary icons that illustrate the meaning of the minimum and maximum values.

In a circular slider, the thumb appears as a small circle. Tick marks, when present, appear as evenly spaced dots around the circumference of the slider.

![An illustration of a horizontal slider with the thumb in the middle. The leading portion of the track up to the thumb is filled with a blue highlight color.](/images/com.apple.HIG/sliders-no-tick-marks@2x.png)

![An illustration of a horizontal slider with the thumb between two tick marks in the middle of the slider. The leading portion of the track up to the thumb is filled with a blue highlight color.](/images/com.apple.HIG/sliders-tick-marks@2x.png)

![An illustration of a circular slider with the thumb at the 12 o'clock position.](/images/com.apple.HIG/sliders-circular@2x.png)

**Consider giving live feedback as the value of a slider changes.** Live feedback shows people results in real time. For example, your Dock icons are dynamically scaled when adjusting the Size slider in Dock settings.

**Choose a slider style that matches peoples’ expectations.** A horizontal slider is ideal when moving between a fixed starting and ending point. For example, a graphics app might offer a horizontal slider for setting the opacity level of an object between 0 and 100 percent. Use circular sliders when values repeat or continue indefinitely. For example, a graphics app might use a circular slider to adjust the rotation of an object between 0 and 360 degrees. An animation app might use a circular slider to adjust how many times an object spins when animated — four complete rotations equals four spins, or 1440 degrees of rotation.

**Consider using a label to introduce a slider.** Labels generally use [sentence-style capitalization](https://help.apple.com/applestyleguide/#/apsgb744e4a3?sub=apdca93e113f1d64) and end with a colon. For guidance, see [Labels](https://developer.apple.com/design/human-interface-guidelines/labels).

**Use tick marks to increase clarity and accuracy.** Tick marks help people understand the scale of measurements and make it easier to locate specific values.

![A partial screenshot of the Energy Saver settings pane in macOS, cropped to show the slider that controls how long the display remains on after inactivity.](/images/com.apple.HIG/sliders-labels@2x.png)

**Consider adding labels to tick marks for even greater clarity.** Labels can be numbers or words, depending on the slider’s values. It’s unnecessary to label every tick mark unless doing so is needed to reduce confusion. In many cases, labeling only the minimum and maximum values is sufficient. When the values of the slider are nonlinear, like in the Energy Saver settings pane, periodic labels provide context. It’s also a good idea to provide a [tooltip](https://developer.apple.com/design/human-interface-guidelines/offering-help#macOS-visionOS) that displays the value of the thumb when people hold their pointer over it.

### Split views
<sub>`pages/split-views.md`</sub>

In macOS, you can arrange the panes of a split view vertically, horizontally, or both. A split view includes dividers between panes that can support dragging to resize them. For developer guidance, see [VSplitView](https://developer.apple.com/documentation/swiftui/vsplitview) and [HSplitView](https://developer.apple.com/documentation/swiftui/hsplitview).

**Vertical**

![An illustration of a laptop screen that shows two panes stacked vertically.](/images/com.apple.HIG/vertical-split-view@2x.png)

**Horizontal**

![An illustration of a laptop screen that shows two panes arranged side by side, with a narrower pane on the left and a wider pane on the right.](/images/com.apple.HIG/horizontal-split-view@2x.png)

**Multiple**

![An illustration of a laptop screen divided into three panes, split both vertically and horizontally.](/images/com.apple.HIG/multiple-split-view@2x.png)


**Set reasonable defaults for minimum and maximum pane sizes.** If people can resize the panes in your app’s split view, make sure to use sizes that keep the divider visible. If a pane gets too small, the divider can seem to disappear, becoming difficult to use.

**Consider letting people hide a pane when it makes sense.** If your app includes an editing area, for example, consider letting people hide other panes to reduce distractions or allow more room for editing — in Keynote, people can hide the navigator and presenter notes panes when they want to edit slide content.

**Provide multiple ways to reveal hidden panes.** For example, you might provide a toolbar button or a menu command — including a keyboard shortcut — that people can use to restore a hidden pane.

**Prefer the thin divider style.** The thin divider measures one point in width, giving you maximum space for content while remaining easy for people to use. Avoid using thicker divider styles unless you have a specific need. For example, if both sides of a divider present table rows that use strong linear elements that might make a thin divider hard to distinguish, it might work to use a thicker divider. For developer guidance, see [NSSplitView.DividerStyle](https://developer.apple.com/documentation/appkit/nssplitview/dividerstyle-swift.enum).

### Steppers
<sub>`pages/steppers.md`</sub>

**For large value ranges, consider supporting Shift-click to change the value quickly.** If your app benefits from larger changes in a stepper’s value, it can be useful to let people Shift-click the stepper to change the value by more than the default increment (by 10 times the default, for example).

### Text fields
<sub>`pages/text-fields.md`</sub>

**Consider using a combo box if you need to pair text input with a list of choices.** For related guidance, see [Combo boxes](https://developer.apple.com/design/human-interface-guidelines/combo-boxes).

### The menu bar
<sub>`pages/the-menu-bar.md`</sub>

A menu bar extra exposes app-specific functionality using an icon that appears in the menu bar when your app is running, even when it’s not the frontmost app. Menu bar extras are on the opposite side of the menu bar from your app’s menus. For developer guidance, see [MenuBarExtra](https://developer.apple.com/documentation/swiftui/menubarextra).

When necessary, the system hides menu bar extras to make room for app menus. Similarly, if there are too many menu bar extras, the system may hide some to avoid crowding app menus.

![A screenshot of the Input menu bar extra and its menu.](/images/com.apple.HIG/menu-bar-extras@2x.png)

**Consider using a symbol to represent your menu bar extra.** You can create an [Icons](https://developer.apple.com/design/human-interface-guidelines/icons) or you can choose one of the [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols), using it as-is or customizing it to suit your needs. Both interface icons and symbols use black and clear colors to define their shapes; the system can apply other colors to the black areas in each image so it looks good on both dark and light menu bars, and when your menu bar extra is selected. The menu bar’s height is 24 pt.

**Display a menu — not a popover — when people click your menu bar extra.** Unless the app functionality you want to expose is too complex for a menu, avoid presenting it in a [Popovers](https://developer.apple.com/design/human-interface-guidelines/popovers).

**Let people — not your app — decide whether to put your menu bar extra in the menu bar.** Typically, people add a menu bar extra to the menu bar by changing a setting in an app’s settings window. To ensure discoverability, however, consider giving people the option of doing so during setup.

**Avoid relying on the presence of menu bar extras.** The system hides and shows menu bar extras regularly, and you can’t be sure which other menu bar extras people have chosen to display or predict the location of your menu bar extra.

**Consider exposing app-specific functionality in other ways, too.** For example, you can provide a [Dock menu](https://developer.apple.com/design/human-interface-guidelines/dock-menus) that appears when people Control-click your app’s Dock icon. People can hide or choose not to use your menu bar extra, but a Dock menu is aways available when your app is running.

### The menu bar
<sub>`pages/the-menu-bar.md`</sub>

The menu bar in macOS includes the Apple menu, which is always the first item on the leading side of the menu bar. The Apple menu includes system-defined menu items that are always available, and you can’t modify or remove it. Space permitting, the system can also display menu bar extras in the trailing end of the menu bar. For guidance, see [Menu bar extras](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Menu-bar-extras).

When menu bar space is constrained, the system prioritizes the display of menus and essential menu bar extras. To ensure that menus remain readable, the system may decrease the space between the titles, truncating them if necessary.

When people enter full-screen mode, the menu bar typically hides until they reveal it by moving the pointer to the top of the screen. For guidance, see [Going full screen](https://developer.apple.com/design/human-interface-guidelines/going-full-screen).

### Toggles
<sub>`pages/toggles.md`</sub>

**Prefer a switch for settings that you want to emphasize.** A switch has more visual weight than a checkbox, so it looks better when it controls more functionality than a checkbox typically does. For example, you might use a switch to let people turn on or off a group of settings, instead of just one setting. For developer guidance, see [switch](https://developer.apple.com/documentation/swiftui/togglestyle/switch).

**Within a grouped form, consider using a mini switch to control the setting in a single row.** The height of a mini switch is similar to the height of buttons and other controls, resulting in rows that have a consistent height. If you need to present a hierarchy of settings within a grouped form, you can use a regular switch for the primary setting and mini switches for the subordinate settings. For developer guidance, see [GroupedFormStyle](https://developer.apple.com/documentation/swiftui/groupedformstyle) and [ControlSize](https://developer.apple.com/documentation/swiftui/controlsize).

**In general, don’t replace a checkbox with a switch.** If you’re already using a checkbox in your interface, it’s probably best to keep using it.

### Toggles
<sub>`pages/toggles.md`</sub>

A checkbox is a small, square button that’s empty when the button is off, contains a checkmark when the button is on, and can contain a dash when the button’s state is mixed. Typically, a checkbox includes a title on its trailing side. In an editable checklist, a checkbox can appear without a title or any additional content.

**Use a checkbox instead of a switch if you need to present a hierarchy of settings.** The visual style of checkboxes helps them align well and communicate grouping. By using alignment — generally along the leading edge of the checkboxes — and indentation, you can show dependencies, such as when the state of a checkbox governs the state of subordinate checkboxes.

![An illustration showing a layout that includes two levels of checkboxes.](/images/com.apple.HIG/checkbox-alignment@2x.png)

**Consider using radio buttons if you need to present a set of more than two mutually exclusive options.** When people need to choose from options in addition to just “on” or “off,” using multiple radio buttons can help you clarify each option with a unique label.

**Consider using a label to introduce a group of checkboxes if their relationship isn’t clear.** Describe the set of options, and align the label’s baseline with the first checkbox in the group.

**Accurately reflect a checkbox’s state in its appearance.** A checkbox’s state can be on, off, or mixed. If you use a checkbox to globally turn on and off multiple subordinate checkboxes, show a mixed state when the subordinate checkboxes have different states. For example, you might need to present a text-style setting that turns all styles on or off, but also lets people choose a subset of individual style settings like bold, italic, or underline. For developer guidance, see [allowsMixedState](https://developer.apple.com/documentation/appkit/nsbutton/allowsmixedstate).

![An illustration that shows a checkbox with the on state, which looks like a small rounded square with blue fill and a white checkmark.](/images/com.apple.HIG/checkbox-selected@2x.png)

![An illustration that shows a checkbox with the off state, which looks like a small rounded square with no fill.](/images/com.apple.HIG/checkbox-deselected@2x.png)

![An illustration that shows a checkbox with the mixed state, which looks like a small rounded square with blue fill and a white hyphen.](/images/com.apple.HIG/checkbox-mixed@2x.png)

### Toggles
<sub>`pages/toggles.md`</sub>

A radio button is a small, circular button followed by a label. Typically displayed in groups of two to five, radio buttons present a set of mutually exclusive choices.

![An illustration that shows five items in a column, each with a radio button preceding the text Radio Button Label. The radio button for the third item is filled, indicating that it's selected.](/images/com.apple.HIG/radio-button-example@2x.png)

A radio button’s state is either selected (a filled circle) or deselected (an empty circle). Although a radio button can also display a mixed state (indicated by a dash), this state is rarely useful because you can communicate multiple states by using additional radio buttons. If you need to show that a setting or item has a mixed state, consider using a checkbox instead.

![An illustration that shows a selected radio button, which looks like a white dot centered in a small circle with a dark fill.](/images/com.apple.HIG/radio-button-selected@2x.png)

![An illustration that shows a deselected radio button, which looks like a small, empty circle.](/images/com.apple.HIG/radio-button-deselected@2x.png)

**Prefer a set of radio buttons to present mutually exclusive options.** If you need to let people choose multiple options in a set, use checkboxes instead.

**Avoid listing too many radio buttons in a set.** A long list of radio buttons takes up a lot of space in the interface and can be overwhelming. If you need to present more than about five options, consider using a component like a [Pop-up buttons](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons) instead.

**To present a single setting that can be on or off, prefer a checkbox.** Although a single radio button can also turn something on or off, the presence or absence of the checkmark in a checkbox can make the current state easier to understand at a glance. In rare cases where a single checkbox doesn’t clearly communicate the opposing states, you can use a pair of radio buttons, each with a label that specifies the state it controls.

**Use consistent spacing when you display radio buttons horizontally.** Measure the space needed to accommodate the longest button label, and use that measurement consistently.

![An illustration that shows three items in a row, with a radio button preceding each item. The first and third items have long text labels, while the second has a short label. The horizontal space each item occupies is equal. A filled radio button precedes the second item, indicating that it's selected.](/images/com.apple.HIG/radio-button-equal-spacing@2x.png)

### Toggles
<sub>`pages/toggles.md`</sub>

In addition to the switch toggle style, macOS supports the checkbox style and also defines radio buttons that can provide similar behaviors.

**Use switches, checkboxes, and radio buttons in the window body, not the window frame.** In particular, avoid using these components in a toolbar or status bar.

### Toolbars
<sub>`pages/toolbars.md`</sub>

In a macOS app, the toolbar resides in the frame at the top of a window, either below or integrated with the title bar. Note that window titles can display inline with controls, and toolbar items don’t include a bezel.

![A diagram of a Finder window in macOS with callouts showing the location of the toolbar and the window frame.](/images/com.apple.HIG/toolbars-mac-window-anatomy@2x.png)

**Make every toolbar item available as a command in the menu bar.** Because people can customize the toolbar or hide it, it can’t be the only place that presents a command. In contrast, it doesn’t make sense to provide a toolbar item for every menu item, because not all menu commands are important enough or used often enough to warrant space in the toolbar.

### Typography
<sub>`pages/typography.md`</sub>

SF Pro is the system font in macOS. NY is available for Mac apps built with Mac Catalyst. macOS doesn’t support Dynamic Type.

**When necessary, use dynamic system font variants to match the text in standard controls.** Dynamic system font variants give your text the same look and feel of the text that appears in system-provided controls. Use the variants listed below to achieve a look that’s consistent with other apps on the platform.

| Dynamic font variant | API |
| --- | --- |
| Control content | [controlContentFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/controlcontentfont(ofsize:)) |
| Label | [labelFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/labelfont(ofsize:)) |
| Menu | [menuFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/menufont(ofsize:)) |
| Menu bar | [menuBarFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/menubarfont(ofsize:)) |
| Message | [messageFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/messagefont(ofsize:)) |
| Palette | [paletteFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/palettefont(ofsize:)) |
| Title | [titleBarFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/titlebarfont(ofsize:)) |
| Tool tips | [toolTipsFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/tooltipsfont(ofsize:)) |
| Document text (user) | [userFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/userfont(ofsize:)) |
| Monospaced document text (user fixed pitch) | [userFixedPitchFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/userfixedpitchfont(ofsize:)) |
| Bold system font | [boldSystemFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/boldsystemfont(ofsize:)) |
| System font | [systemFont(ofSize:)](https://developer.apple.com/documentation/appkit/nsfont/systemfont(ofsize:)) |

### Undo and redo
<sub>`pages/undo-and-redo.md`</sub>

**Place undo and redo commands in the Edit menu and support the standard keyboard shortcuts.** Mac users expect to find undo and redo at the top of the Edit menu; they also expect to use Command–Z and Shift–Command–Z to perform undo and redo, respectively.

### Windows
<sub>`pages/windows.md`</sub>

A macOS window can have one of three states:

- **Main.** The frontmost window that people view is an app’s main window. There can be only one main window per app.
- **Key.** Also called the *active window*, the key window accepts people’s input. There can be only one key window onscreen at a time. Although the front app’s main window is usually the key window, another window — such as a panel floating above the main window — might be key instead. People typically click a window to make it key; when people click an app’s Dock icon to bring all of that app’s windows forward, only the most recently accessed window becomes key.
- **Inactive.** A window that’s not in the foreground is an inactive window.

The system gives main, key, and inactive windows different appearances to help people visually identify them. For example, the key window uses color in the title bar options for closing, minimizing, and zooming; inactive windows and main windows that aren’t key use gray in these options. Also, inactive windows don’t use [Materials](https://developer.apple.com/design/human-interface-guidelines/materials) (an effect that can pull color into a window from the content underneath it), which makes them appear subdued and seem visually farther away than the main and key windows.

![An illustration of a stack of three windows, as follows: An inactive window in the background, an app’s main window in the middle, and a key window appearing above the other two windows.](/images/com.apple.HIG/window-states@2x.png)

> **Note:** Some windows — typically, panels like Colors or Fonts — become the key window only when people click the window’s title bar or a component that requires keyboard input, such as a text field.

**Make sure custom windows use the system-defined appearances.** People rely on the visual differences between windows to help them identify the foreground window and know which window will accept their input. When you use system-provided components, a window’s background and button appearances update automatically when the window changes state; if you use custom implementations, you need to do this work yourself.

**Avoid putting critical information or actions in a bottom bar, because people often relocate a window in a way that hides its bottom edge.** If you must include one, use it only to display a small amount of information directly related to a window’s contents or to a selected item within it. For example, Finder uses a bottom bar (called the status bar) to display the total number of items in a window, the number of selected items, and how much space is available on the disk. A bottom bar is small, so if you have more information to display, consider using an inspector, which typically presents information on the trailing side of a split view.

### Windows
<sub>`pages/windows.md`</sub>

A macOS window consists of a frame and a body area. People can move a window by dragging the frame and can often resize the window by dragging its edges.

The *frame* of a window appears above the body area and can include window controls and a  [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars). In rare cases, a window can also display a bottom bar, which is a part of the frame that appears below body content.

### Windows
<sub>`pages/windows.md`</sub>

In macOS, people typically run several apps at the same time, often viewing windows from multiple apps on one desktop and switching frequently between different windows — moving, resizing, minimizing, and revealing the windows to suit their work style.

To learn about setting up a window to display your game in macOS, see [Managing your game window for Metal in macOS](https://developer.apple.com/documentation/metal/managing-your-game-window-for-metal-in-macos).

## tvOS

### App icons
<sub>`pages/app-icons.md`</sub>

**Include a safe zone to ensure the system doesn’t crop your content.** When someone focuses your app icon, the system may crop content around the edges as the icon scales and moves. To ensure that your icon’s content is always visible, keep a safe zone around it. Be aware that the safe zone can vary, depending on the image size, layer depth, and motion, and the system crops foreground layers more than background layers.

![A diagram of the Settings icon in tvOS with a white dotted line inside the outer border, which indicates the safe zone.](/images/com.apple.HIG/tvos-app-icon-safe-zone@2x.png)

### Color
<sub>`pages/color.md`</sub>

**Consider choosing a limited color palette that coordinates with your app logo.** Subtle use of color can help you communicate your brand while deferring to the content.

**Avoid using only color to indicate focus.** Subtle scaling and responsive animation are the primary ways to denote interactivity when an element is in focus.

### Focus and selection
<sub>`pages/focus-and-selection.md`</sub>

**In a full-screen experience, let people use gestures to interact with the content, not to move focus.** When an item displays in full screen, it doesn’t show focus, so people naturally assume that their gestures will affect the object, and not its focus state.

**Avoid displaying a pointer.** People expect to navigate a fixed number of items by changing focus, not by trying to drag a tiny pointer around a huge screen. While free-form movement might make sense during gameplay, such as when looking for a hidden object or flying a plane, use the focus model when people navigate menus and other interface elements. If your app requires a pointer, make sure it’s highly visible and feels integrated with your experience.

**Design your interface to accommodate components in various focus states.** In tvOS, focusable items can have up to five different states, each of which is visually distinct. Because focusing an item often increases its scale, you need to supply assets for the larger, focused size to ensure they always look sharp, and you need to make sure the larger item doesn’t crowd the surrounding interface.

| State | Description |
| --- | --- |
| ![An image of an unfocused button on top of a photograph. A small drop shadow makes it appear very close to the content behind it, with a translucent background infused by the colors of the content, and a high-contrast text color.](/images/com.apple.HIG/focus-and-selection-state-unfocused@2x.png) | The viewer hasn’t brought focus to the item. Unfocused items appear less prominent than focused items. |
| ![An image of a focused button on top of a photograph. It’s larger than an unfocused button, and a drop shadow makes it appear farther away from the content behind it, with an opaque white background and a black text label.](/images/com.apple.HIG/focus-and-selection-state-focused@2x.png) | The viewer brings focus to the item. A focused item visually stands out from the other onscreen content through elevation to the foreground, illumination, and animation. |
| ![An image of a highlighted button on top of a photograph. It’s the same size as an unfocused button, and a drop shadow makes it appear a little farther away from the surface of the content behind it, with an opaque white background and a black text label.](/images/com.apple.HIG/focus-and-selection-state-highlighted@2x.png) | The viewer chooses the focused item. A focused item provides instant visual feedback when people choose it. For example, a button might briefly invert its colors and animate before it transitions to its selected appearance. |
| ![An image of a selected button on top of a photograph. It’s the same size as an unfocused button, and a small drop shadow makes it appear very close to the content behind it, with an opaque white background and a black text label.](/images/com.apple.HIG/focus-and-selection-state-selected@2x.png) | The viewer has chosen or activated the item in some way. For example, a heart-shaped button that people can use to favorite a photo might appear filled in the selected state and empty in the deselected state. |
| ![An image of an unavailable button on top of a photograph. It’s the same size as an unfocused button. It lacks a drop shadow and appears to rest directly on the content behind it, with a translucent background tinted by the the colors of nearby content, and a low-contrast text color.](/images/com.apple.HIG/focus-and-selection-state-unavailable@2x.png) | The viewer can’t bring focus to the item or choose it. An unavailable item appears inactive. |

For developer guidance, see [Adding user-focusable elements to a tvOS app](https://developer.apple.com/documentation/uikit/adding-user-focusable-elements-to-a-tvos-app).

### Game Center
<sub>`pages/game-center.md`</sub>

**Display an optional image at the top of the dashboard.** In tvOS, you can add an additional piece of artwork to the dashboard to highlight your game’s aesthetic. Use a simple, easily recognizable image that looks great at a distance. Consider using your game’s logo or word mark; however, don’t use your app icon for this image. Use the following specifications to create a dashboard image.

![A diagram of the layout for a tvOS dashboard image, with a callout indicating the image size.](/images/com.apple.HIG/tvos-dashboard-image@2x.png)

| Attribute | Value |
| --- | --- |
| Image size | 600x180 pt (1200x360 px @2x) |
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |

### Gestures
<sub>`pages/gestures.md`</sub>

People expect to use [Standard gestures](https://developer.apple.com/design/human-interface-guidelines/gestures#Standard-gestures) to navigate tvOS apps and games with a compatible remote, Siri Remote, or [Game controls](https://developer.apple.com/design/human-interface-guidelines/game-controls) that includes a touch surface. For guidance, see [Remotes](https://developer.apple.com/design/human-interface-guidelines/remotes).

### Image views
<sub>`pages/image-views.md`</sub>

Many tvOS images combine multiple layers with transparency to create a feeling of depth. For guidance, see [Layered images](https://developer.apple.com/design/human-interface-guidelines/images#Layered-images).

### Images
<sub>`pages/images.md`</sub>

*Parallax* is a subtle visual effect the system uses to convey depth and dynamism when an element is in focus. As an element comes into focus, the system elevates it to the foreground, gently swaying it while applying illumination that makes the element’s surface appear to shine. After a period of inactivity, out-of-focus content dims and the focused element expands.

Layered images are required to support the parallax effect.

*(video: An animation of a tvOS app icon moving to show the parallax effect.)*

### Images
<sub>`pages/images.md`</sub>

A *layered image* consists of two to five distinct layers that come together to form a single image. The separation between layers, along with use of transparency, creates a feeling of depth. As someone interacts with an image, layers closer to the surface elevate and scale, overlapping lower layers farther back and producing a 3D effect.

> **Important:** Your tvOS [tvOS](https://developer.apple.com/design/human-interface-guidelines/app-icons#tvOS) must use a layered image. For other focusable images in your app, including [Top Shelf](https://developer.apple.com/design/human-interface-guidelines/top-shelf) images, layered images are strongly encouraged, but optional.

You can embed layered images in your app or retrieve them from a content server at runtime. For guidance on adding layered images to your app, see the [Parallax Previewer User Guide](https://help.apple.com/itc/parallaxpreviewer/).

> **Note:** If your app retrieves layered images from a content server at runtime, you must provide runtime layered images (`.lcr`). You can generate them from LSR files or Photoshop files using the `layerutil` command-line tool that Xcode provides. Runtime layered images are intended to be downloaded — don’t embed them in your app.

**Use standard interface elements to display layered images.** If you use standard views and system-provided focus APIs — such as [FocusState](https://developer.apple.com/documentation/swiftui/focusstate) — layered images automatically get the parallax treatment when people bring them into focus.

**Identify logical foreground, middle, and background elements.** In foreground layers, display prominent elements like a character in a game, or text on an album cover or movie poster. Middle layers are perfect for secondary content and effects like shadows. Background layers are opaque backdrops that showcase the foreground and middle layers without upstaging them.

**Generally, keep text in the foreground.** Unless you want to obscure text, bring it to the foreground layer for clarity.

**Keep the background layer opaque.** Using varying levels of opacity to let content shine through higher layers is fine, but your background layer must be opaque — you’ll get an error if it’s not. An opaque background layer ensures your artwork looks great with parallax, drop shadows, and system backgrounds.

**Keep layering simple and subtle.** Parallax is designed to be almost unnoticeable. Excessive 3D effects can appear unrealistic and jarring. Keep depth simple to bring your content to life and add delight.

**Leave a safe zone around the foreground layers of your image.** When focused, content on some layers may be cropped as the layered image scales and moves. To ensure that essential content is always visible, keep it within a safe zone. For guidance, see [App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons).

**Always preview layered images.** To ensure your layered images look great on Apple TV, preview them throughout your design process using Xcode, the Parallax Previewer app for macOS, or the Parallax Exporter plug-in for Adobe Photoshop. Pay special attention as scaling and clipping occur, and readjust your images as needed to keep important content safe. After your layered images are final, preview them on an actual TV for the most accurate representation of what people will see. To download Parallax Previewer and Parallax Exporter, see [Resources](https://developer.apple.com/design/resources/#parallax-previewer).

### Images
<sub>`pages/images.md`</sub>

Layered images are at the heart of the Apple TV user experience. The system combines layered images, transparency, scaling, and motion to produce a sense of realism and vigor that evokes a personal connection as people interact with onscreen content.

### Launching
<sub>`pages/launching.md`</sub>

> **Note:** Unlike the [Layered images](https://developer.apple.com/design/human-interface-guidelines/images#Layered-images) throughout much of a tvOS app, the launch screen is static.

**In a live-viewing app, consider automatically starting playback soon after people start the app.** People come to your app to watch TV, so you might want to start playing new or recently viewed live content after a few seconds of inactivity. For guidance, see [Live-viewing apps](https://developer.apple.com/design/human-interface-guidelines/live-viewing-apps).

### Layout
<sub>`pages/layout.md`</sub>

**Be prepared for a wide range of TV sizes.** On Apple TV, layouts don’t automatically adapt to the size of the screen like they do on iPhone or iPad. Instead, apps and games show the same interface on every display. Take extra care in designing your layout so that it looks great in a variety of screen sizes.

**Adhere to the screen’s safe area.** Inset primary content 60 points from the top and bottom of the screen, and 80 points from the sides. It can be difficult for people to see content that close to the edges, and unintended cropping can occur due to overscanning on older TVs. Allow only partially displayed offscreen content and elements that deliberately flow offscreen to appear outside this zone.

![An illustration of a TV with a safe zone border on all sides. In width, the top and bottom borders measure 60 points, and the side borders both measure 80 points.](/images/com.apple.HIG/visual-design-safe-zone@2x.png)

**Include appropriate padding between focusable elements.** When you use UIKit and the focus APIs, an element gets bigger when it comes into focus. Consider how elements look when they’re focused, and make sure you don’t let them overlap important information. For developer guidance, see [About focus interactions for Apple TV](https://developer.apple.com/documentation/uikit/about-focus-interactions-for-apple-tv).

![An illustration that uses vertical shaded rectangles to show padding between focusable items.](/images/com.apple.HIG/visual-design-padding@2x.png)

### Layout
<sub>`pages/layout.md`</sub>

The following grid layouts provide an optimal viewing experience. Be sure to use appropriate spacing between unfocused rows and columns to prevent overlap when an item comes into focus.

If you use the UIKit collection view flow element, the number of columns in a grid is automatically determined based on the width and spacing of your content. For developer guidance, see [UICollectionViewFlowLayout](https://developer.apple.com/documentation/uikit/uicollectionviewflowlayout).

**Two-column**

![An illustration of Apple TV, displaying a two-column grid of media items. Additional media items are partially visible on the right side and bottom edge of the screen.](/images/com.apple.HIG/visual-design-grid-2-column@2x.png)

### Layout
<sub>`pages/layout.md`</sub>

| Attribute | Value |
| --- | --- |
| Unfocused content width | 160 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |


**Include additional vertical spacing for titled rows.** If a row has a title, provide enough spacing between the bottom of the previous unfocused row and the center of the title to avoid crowding. Also provide spacing between the bottom of the title and the top of the unfocused items in the row.

**Use consistent spacing.** When content isn’t consistently spaced, it no longer looks like a grid and it’s harder for people to scan.

**Make partially hidden content look symmetrical.** To help direct attention to the fully visible content, keep partially hidden offscreen content the same width on each side of the screen.

### Layout
<sub>`pages/layout.md`</sub>

| Attribute | Value |
| --- | --- |
| Unfocused content width | 184 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Nine-column**

![An illustration of Apple TV, displaying a nine-column grid of media items.](/images/com.apple.HIG/visual-design-grid-9-column@2x.png)

### Layout
<sub>`pages/layout.md`</sub>

| Attribute | Value |
| --- | --- |
| Unfocused content width | 217 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Eight-column**

![An illustration of Apple TV, displaying an eight-column grid of media items. Additional media items are partially visible on the right side and bottom edge of the screen.](/images/com.apple.HIG/visual-design-grid-8-column@2x.png)

### Layout
<sub>`pages/layout.md`</sub>

| Attribute | Value |
| --- | --- |
| Unfocused content width | 260 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Seven-column**

![An illustration of Apple TV, displaying a seven-column grid of media items. Additional media items are partially visible on the right side of the screen.](/images/com.apple.HIG/visual-design-grid-7-column@2x.png)

### Layout
<sub>`pages/layout.md`</sub>

| Attribute | Value |
| --- | --- |
| Unfocused content width | 320 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Six-column**

![An illustration of Apple TV, displaying a six-column grid of media items. Additional media items are partially visible on the right side and bottom edge of the screen.](/images/com.apple.HIG/visual-design-grid-6-column@2x.png)

### Layout
<sub>`pages/layout.md`</sub>

| Attribute | Value |
| --- | --- |
| Unfocused content width | 410 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Five-column**

![An illustration of Apple TV, displaying a five-column grid of media items. Additional media items are partially visible on the right side and bottom edge of the screen.](/images/com.apple.HIG/visual-design-grid-5-column@2x.png)

### Layout
<sub>`pages/layout.md`</sub>

| Attribute | Value |
| --- | --- |
| Unfocused content width | 560 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Four-column**

![An illustration of Apple TV, displaying a four-column grid of media items. Additional media items are partially visible on the right side of the screen.](/images/com.apple.HIG/visual-design-grid-4-column@2x.png)

### Layout
<sub>`pages/layout.md`</sub>

| Attribute | Value |
| --- | --- |
| Unfocused content width | 860 pt |
| Horizontal spacing | 40 pt |
| Minimum vertical spacing | 100 pt |

**Three-column**

![An illustration of Apple TV, displaying a three-column grid of media items. Additional media items are partially visible on the right side and bottom edge of the screen.](/images/com.apple.HIG/visual-design-grid-3-column@2x.png)

### Lists and tables
<sub>`pages/lists-and-tables.md`</sub>

**Confirm that images near a table still look good as each row highlights and slightly increases in size when it becomes focused.** A focused row’s corners can also become rounded, which may affect the appearance of images on either side of it. Account for this effect as you prepare images, and don’t add your own masks to round the corners.

### Managing accounts
<sub>`pages/managing-accounts.md`</sub>

Most people interact with Apple TV using a remote, not a keyboard, so ask for the minimum amount of information necessary.

**Prefer letting people use another device to sign up or authenticate.** When you configure your app’s associated domains, Apple TV can work with other devices to safely suggest sign-in credentials, including [Sign in with Apple](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple). For developer guidance, see [Configuring an associated domain](https://developer.apple.com/documentation/xcode/configuring-an-associated-domain).

**When people are signed in to a shared account, avoid asking them to choose their profile every time they become the current user.** In tvOS 16 and later, your app can share its credentials with all users while storing each individual’s profile and user data separately. When you support this type of sharing, your app can automatically use the current user’s profile without asking each person to sign in separately to a shared account. For developer guidance, see [kSecUseUserIndependentKeychain](https://developer.apple.com/documentation/security/ksecuseuserindependentkeychain) and [User Management Entitlement](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.user-management).

**Minimize data entry.** If you need to gather more than a small amount of information, ask people to visit a website from another device. If you need an email address, show the email keyboard screen, which includes a list of recently entered addresses.

### Materials
<sub>`pages/materials.md`</sub>

In tvOS, Liquid Glass appears throughout navigation elements and system experiences such as Top Shelf and Control Center. Certain interface elements, like image views and buttons, adopt Liquid Glass when they gain focus.

![A screenshot of the Destination Video app running in tvOS. The app shows a screen with details about a video called A BOT-anist Adventure. The background is a colorful image of the main character in a scene from the video. The interface elements floating above the background adopt a Liquid Glass appearance to allow background color to show through and create a more immersive media experience.](/images/com.apple.HIG/materials-tvos-media-player@2x.png)

In addition to Liquid Glass, tvOS continues to provide standard materials, which you can use to help define structure in the content layer. The thickness of a standard material affects how prominently the underlying content shows through. For example, consider using standard materials in the following ways:

| Material | Recommended for |
| --- | --- |
| [ultraThin](https://developer.apple.com/documentation/swiftui/material/ultrathin) | Full-screen views that require a light color scheme |
| [thin](https://developer.apple.com/documentation/swiftui/material/thin) | Overlay views that partially obscure onscreen content and require a light color scheme |
| [regular](https://developer.apple.com/documentation/swiftui/material/regular) | Overlay views that partially obscure onscreen content |
| [thick](https://developer.apple.com/documentation/swiftui/material/thick) | Overlay views that partially obscure onscreen content and require a dark color scheme |

### Multitasking
<sub>`pages/multitasking.md`</sub>

On Apple TV, people can play or browse content while also playing movies or TV shows in Picture in Picture (where supported).

### Page controls
<sub>`pages/page-controls.md`</sub>

**Use page controls on collections of full-screen pages.** A page control is designed to operate in a full-screen environment where multiple content-rich pages are peers in the page hierarchy. Inclusion of additional controls makes it difficult to maintain focus while moving between pages.

### Pickers
<sub>`pages/pickers.md`</sub>

Pickers are available in tvOS with SwiftUI. For developer guidance, see [Picker](https://developer.apple.com/documentation/swiftui/picker).

### Playing audio
<sub>`pages/playing-audio.md`</sub>

In tvOS, the system plays audio only when people initiate it, through interactions within apps and games or when performing device calibrations. For example, tvOS doesn’t play sounds to accompany components like alerts or notifications.

### Playing video
<sub>`pages/playing-video.md`</sub>

**Defer to content when displaying logos or noninteractive overlays above video.** A small, unobtrusive logo or countdown timer may be appropriate for your video, but avoid large, distracting overlays that don’t enhance the viewing experience. Also, be aware that some devices are prone to image retention, so it’s generally better to keep overlays short and to prefer translucent graphics in Standard Dynamic Range (SDR) to bright, opaque content.

**Show interactive overlays gracefully.** Some videos display interactive overlays, such as quizzes, surveys, and progress check-ins. For the best user experience, implement a minimum delay of 0.5 seconds to pause playing media, and display an interactive overlay. Give people a clear way to dismiss the overlay and resume media playback after they finish interacting.

### Scroll views
<sub>`pages/scroll-views.md`</sub>

Views in tvOS can scroll, but they aren’t treated as distinct objects with scroll indicators. Instead, when content exceeds the size of the screen, the system automatically scrolls the interface to keep focused items visible.

### Search fields
<sub>`pages/search-fields.md`</sub>

A search screen is a specialized keyboard screen that helps people enter search text, displaying search results beneath the keyboard in a fully customizable view. For developer guidance, see [UISearchController](https://developer.apple.com/documentation/uikit/uisearchcontroller).

![An illustration of a search screen in tvOS. The screen includes a field with a keyboard input area at the top, a scope bar, and a grid of top results at the bottom.](/images/com.apple.HIG/search-fields-tvos-search@2x.png)

**Provide suggestions to make searching easier.** People typically don’t want to do a lot of typing in tvOS. To improve the search experience, provide popular and context-specific search suggestions, including recent searches when available. For developer guidance, see [Using suggested searches with a search controller](https://developer.apple.com/documentation/uikit/using-suggested-searches-with-a-search-controller).

### Segmented controls
<sub>`pages/segmented-controls.md`</sub>

**Consider using a split view instead of a segmented control on screens that perform content filtering.** People generally find it easy to navigate back and forth between content and filtering options using a split view. Depending on its placement, a segmented control may not be as easy to access.

**Avoid putting other focusable elements close to segmented controls.** Segments become selected when focus moves to them, not when people click them. Carefully consider where you position a segmented control relative to other interface elements. If other focusable elements are too close, people might accidentally focus on them when attempting to switch between segments.

### Split views
<sub>`pages/split-views.md`</sub>

In tvOS, a split view can work well to help people filter content. When people choose a filter category in the primary pane, your app can display the results in the secondary pane.

**Choose a split view layout that keeps the panes looking balanced.** By default, a split view devotes a third of the screen width to the primary pane and two-thirds to the secondary pane, but you can also specify a half-and-half layout.

**Display a single title above a split view, helping people understand the content as a whole.** People already know how to use a split view to navigate and filter content; they don’t need titles that describe what each pane contains.

**Choose the title’s alignment based on the type of content the secondary pane contains.** Specifically, when the secondary pane contains a content collection, consider centering the title in the window. In contrast, if the secondary pane contains a single main view of important content, consider placing the title above the primary view to give the content more room.

### Tab bars
<sub>`pages/tab-bars.md`</sub>

A tab bar is highly customizable. For example, you can:

- Specify a tint, color, or image for the tab bar background
- Choose a font for tab items, including a different font for the selected item
- Specify tints for selected and unselected items
- Add button icons, like settings and search

By default, a tab bar is translucent, and only the selected tab is opaque. When people use the remote to focus on the tab bar, the selected tab includes a drop shadow that emphasizes its selected state. The height of a tab bar is 68 points, and its top edge is 46 points from the top of the screen; you can’t change either of these values.

If there are more items than can fit in the tab bar, the system truncates the rightmost item by applying a fade effect that begins at the right side of the tab bar. If there are enough items to cause scrolling, the system also applies a truncating fade effect that starts from the left side.

**Be aware of tab bar scrolling behaviors.** By default, people can scroll the tab bar offscreen when the current tab contains a single main view. You can see examples of this behavior in the Watch Now, Movies, TV Show, Sports, and Kids tabs in the TV app. The exception is when a screen contains a split view, such as the TV app’s Library tab or an app’s Settings screen. In this case, the tab bar remains pinned at the top of the view while people scroll the content within the primary and secondary panes of the split view. Regardless of a tab’s contents, focus always returns to the tab bar at the top of the page when people press Menu on the remote.

**In a live-viewing app, organize tabs in a consistent way.** For the best experience, organize content in live-streaming apps with tabs in the following order:

- Live content
- Cloud DVR or other recorded content
- Other content

For additional guidance, see [Live-viewing apps](https://developer.apple.com/design/human-interface-guidelines/live-viewing-apps).

### Text views
<sub>`pages/text-views.md`</sub>

You can display text in tvOS using a text view. Because text input in tvOS is minimal by design, tvOS uses [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields) for editable text instead.

### Typography
<sub>`pages/typography.md`</sub>

SF Pro is the system font in tvOS, and apps can also use NY.

### Virtual keyboards
<sub>`pages/virtual-keyboards.md`</sub>

tvOS displays a linear virtual keyboard when people select a text field using the Siri Remote.

> **Note:** A grid keyboard screen appears when people use devices other than the Siri Remote, and the layout of content automatically adapts to the keyboard.

When people activate a digit entry view, tvOS displays a digit-specific keyboard. For guidance, see [Digit entry views](https://developer.apple.com/design/human-interface-guidelines/digit-entry-views).

## visionOS

### Accessibility
<sub>`pages/accessibility.md`</sub>

visionOS offers a variety of accessibility features people can use to interact with their surroundings in ways that are comfortable and work best for them, including head and hand Pointer Control, and a Zoom feature.

**Pointer Control (hand)**

*(video: A recording of a person's hand using Pointer Control to interact with content in an app's visionOS window. A line with a pointer at the end extends from the person's hand. It changes position within the field of view as the person moves their hand.)*

**Pointer Control (head)**

*(video: A recording of someone using Pointer Control to interact with content in an app's visionOS window. The person isn't visible in the recording. Only the pointer is visible. It's centered in the field of view, and the person uses their head movement to position content beneath the pointer.)*

**Zoom**

![A screenshot of an app's window in visionOS. A zoom lens is visible above a portion of the window, and displays a zoomed-in version of the content beneath the lens.](/images/com.apple.HIG/visionos-accessibility-zoom-lens@2x.png)


**Prioritize comfort.** The immersive nature of visionOS means that interfaces, animations, and interactions have a greater chance of causing motion sickness, and visual and ergonomic discomfort for people. To ensure the most comfortable experience, consider these tips:

- Keep interface elements within a person’s field of view. Prefer horizontal layouts to vertical ones that might cause neck strain, and avoid demanding the viewer’s attention in different locations in quick succession.
- Reduce the speed and intensity of animated objects, particularly in someone’s peripheral vision.
- Be gentle with camera and video motion, and avoid situations where someone may feel like the world around them is moving without their control.
- Avoid anchoring content to the wearer’s head, which may make them feel stuck and confined, and also prevent them from using assistive technologies like Pointer Control.
- Minimize the need for large and repetitive gestures, as these can become tiresome and may be difficult depending on a person’s surroundings.

For additional guidance, see [Create accessible spatial experiences](https://developer.apple.com/videos/play/wwdc2023/10034) and [Design considerations for vision and motion](https://developer.apple.com/videos/play/wwdc2023/10078).

### Alerts
<sub>`pages/alerts.md`</sub>

When your app is running in the Shared Space, visionOS displays an alert in front of the app’s window, slightly forward along the z-axis.

*(video: A video of an alert in the Freeform app running in the Shared Space in visionOS. When the video plays, someone chooses to permanently delete a recently deleted Freeform board. An alert then appears in front of the Freeform window to ask for confirmation.)*

If someone moves a window without dismissing its alert, the alert remains anchored to the window. If your app is running in a Full Space, the system displays the alert centered in the wearer’s [Field of view](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Field-of-view).

*(video: A video of an alert in the Freeform app running in the Shared Space in visionOS. When the video plays, someone chooses to permanently delete a recently deleted Freeform board. An alert then appears in front of the Freeform window to ask for confirmation. The alert is not dismissed and remains anchored to the Freeform window as it’s moved around the Shared Space.)*

If you need to display an accessory view in a visionOS alert, create a view that has a maximum height of 154 pt and a 16-pt corner radius.

### App icons
<sub>`pages/app-icons.md`</sub>

**Avoid adding a shape that’s intended to look like a hole or concave area to the background layer.** The system-added shadow and specular highlights can make such a shape stand out instead of recede.

### Augmented reality
<sub>`pages/augmented-reality.md`</sub>

With the wearer’s [visionOS](https://developer.apple.com/design/human-interface-guidelines/privacy#visionOS), you can use ARKit in your visionOS app to detect surfaces in a person’s surroundings, use a person’s hand and finger postions to inform your [Designing custom gestures in visionOS](https://developer.apple.com/design/human-interface-guidelines/gestures#Designing-custom-gestures-in-visionOS), support interactions that incorporate nearby physical objects into your [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences), and more. For developer guidance, see [ARKit](https://developer.apple.com/documentation/arkit).

*(video: A recording showing a 3D model of a meteor in visionOS rotating above a physical table.)*

### Buttons
<sub>`pages/buttons.md`</sub>

A visionOS button typically includes a visible background that can help people see it, and the button plays sound to provide feedback when people interact with it.

*(video: A recording showing the top portion of a window in visionOS. The window contains several buttons, including a 'More' button, which receives the hover effect. The button is selected and a menu containing additional options appears.)*

There are three standard button shapes in visionOS. Typically, an icon-only button uses a [circle](https://developer.apple.com/documentation/swiftui/buttonbordershape/circle) shape, a text-only button uses a [roundedRectangle](https://developer.apple.com/documentation/swiftui/buttonbordershape/roundedrectangle) or [capsule](https://developer.apple.com/documentation/swiftui/buttonbordershape/capsule) shape, and a button that includes both an icon and text uses the capsule shape.

visionOS buttons use different visual styles to communicate four different interaction states.

![An image of a circular button that contains an icon of an outlined square with rounded corners. The button background is dark and the dashed outline is white.](/images/com.apple.HIG/visionos-button-state-idle@2x.png)

![An image of a circular button that contains an icon of an outlined square with rounded corners. The button background is medium dark and the outline is white.](/images/com.apple.HIG/visionos-button-state-hover@2x.png)

![An image of a circular button that contains an icon of an outlined square with rounded corners. The button background is white and the outline is black.](/images/com.apple.HIG/visionos-button-state-selected@2x.png)

![An image of a circular button that contains an icon of an outlined square with rounded corners. The button background is very dark and the outline is light.](/images/com.apple.HIG/visionos-button-state-unavailable@2x.png)

> **Note:** In visionOS, buttons don’t support custom hover effects.

In addition to the four states shown above, a button can also reveal a tooltip when people look at it for a brief time. In general, buttons that contain text don’t need to display a tooltip because the button’s descriptive label communicates what it does.

*(video: An animation showing a tooltip appearing beneath a visionOS button.)*

In visionOS, buttons can have the following sizes.

| Shape | Mini (28 pt) | Small (32 pt) | Regular (44 pt) | Large (52 pt) | Extra large (64 pt) |
| --- | --- | --- | --- | --- | --- |
| Circular | ![A checkmark denoting availability.](/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](/images/com.apple.HIG/table-availability-checkmark@2x.png) |
| Capsule (text only) |  | ![A checkmark denoting availability.](/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](/images/com.apple.HIG/table-availability-checkmark@2x.png) |  |
| Capsule (text and icon) |  |  | ![A checkmark denoting availability.](/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](/images/com.apple.HIG/table-availability-checkmark@2x.png) |  |
| Rounded rectangle |  | ![A checkmark denoting availability.](/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](/images/com.apple.HIG/table-availability-checkmark@2x.png) | ![A checkmark denoting availability.](/images/com.apple.HIG/table-availability-checkmark@2x.png) |  |

**Prefer buttons that have a discernible background shape and fill.** It tends to be easier for people to see a button when it’s enclosed in a shape that uses a contrasting background fill. The exception is a button in a toolbar, context menu, alert, or [Ornaments](https://developer.apple.com/design/human-interface-guidelines/ornaments) where the shape and material of the larger component make the button comfortably visible. The following guidelines can help you ensure that a button looks good in different contexts:

- When a button appears on top of a glass [visionOS](https://developer.apple.com/design/human-interface-guidelines/windows#visionOS), use the [thin](https://developer.apple.com/documentation/swiftui/material/thin) material as the button’s background.
- When a button appears floating in space, use the [visionOS](https://developer.apple.com/design/human-interface-guidelines/materials#visionOS) for its background.

**Avoid creating a custom button that uses a white background fill and black text or icons.** The system reserves this visual style to convey the toggled state.

**In general, prefer circular or capsule-shape buttons.** People’s eyes tend to be drawn toward the corners in a shape, making it difficult to keep looking at the shape’s center. The more rounded a button’s shape, the easier it is for people to look steadily at it. When you need to display a button by itself, prefer a capsule-shape button.

**Provide enough space around a button to make it easy for people to look at it.** Aim to place buttons so their centers are always at least 60 pts apart. If your buttons measure 60 pts or larger, add 4 pts of padding around them to keep the hover effect from overlapping. Also, it’s usually best to avoid displaying small or mini buttons in a vertical stack or horizontal row.

**Choose the right shape if you need to display text-labeled buttons in a stack or row.** Specifically, prefer the rounded-rectangle shape in a vertical stack of buttons and prefer the capsule shape in a horizontal row of buttons.

**Use standard controls to take advantage of the audible feedback sounds people already know.** Audible feedback is especially important in visionOS, because the system doesn’t play haptics.

### Collaboration and sharing
<sub>`pages/collaboration-and-sharing.md`</sub>

By default, the system supports screen sharing for an app running in the Shared Space by streaming the current window to other collaborators. If one person transitions the app to a Full Space while sharing is in progress, the system pauses the stream for other people until the app returns to the Shared Space. For guidance, see [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences).

### Color
<sub>`pages/color.md`</sub>

**Use color sparingly, especially on glass.** Standard visionOS windows typically use the system-defined glass [Materials](https://developer.apple.com/design/human-interface-guidelines/materials), which lets light and objects from people’s physical surroundings and their space show through. Because the colors in these physical and virtual objects are visible through the glass, they can affect the legibility of colorful app content in the window. Prefer using color in places where it can help call attention to important information or show the relationship between parts of the interface.

**Prefer using color in bold text and large areas.** Color in lightweight text or small areas can make them harder to see and understand.

**In a fully immersive experience, help people maintain visual comfort by keeping brightness levels balanced.** Although using high contrast can help direct people’s attention to important content, it can also cause visual discomfort if people’s eyes have adjusted to low light or darkness. Consider making content fully bright only when the rest of the visual context is also bright. For example, avoid displaying a bright object on a very dark or black background, especially if the object flashes or moves.

### Context menus
<sub>`pages/context-menus.md`</sub>

**Consider using a context menu instead of a panel or inspector window to present frequently used functionality.** Minimizing the number of separate views or windows your app opens can help people keep their space uncluttered.

**In general, avoid letting a context menu’s height exceed the height of the window.** In visionOS, a window includes system-provided components above and below its top and bottom edges, such as window-management controls and the Share menu, so a context menu that’s too tall could obscure them. As you consider the number of items to include, be guided by the ways people are likely to use your app. For example, people who use an app to accomplish in-depth, specialist tasks often expect to spend time learning a large number of sophisticated commands and might appreciate contextual access to them. On the other hand, people who use an app to perform a few simple actions may appreciate short contextual menus that are quick to scan and use.

### Disclosure controls
<sub>`pages/disclosure-controls.md` — upstream heading: iOS, iPadOS, visionOS</sub>

Disclosure controls are available in iOS, iPadOS, and visionOS with the SwiftUI [DisclosureGroup](https://developer.apple.com/documentation/swiftui/disclosuregroup) view.

### Drag and drop
<sub>`pages/drag-and-drop.md`</sub>

**When possible, launch your app to handle content that people drop into empty space.** When you associate a user activity with draggable app content, your app can open a window or scene that handles the content when people drop it. For example, when people drop a URL into empty space, it launches Safari; when people drop Quick Look–supported content, Quick Look launches to display it. For developer guidance, see [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity).

*(video: A recording that shows a wearer dragging a 3D file named meteor out of a Finder window. The wearer drags the file into empty space, dropping it in an area that's visually near a table in their physical surroundings. The dropped file opens, showing a 3D meteor that appears to float above the table.)*

### Focus and selection
<sub>`pages/focus-and-selection.md`</sub>

visionOS supports the same focus system as in iPadOS and tvOS, letting people use a connected input device like a keyboard or game controller to interact with apps and the system.

> **Note:** When people look at a virtual object to identify it as the object they want to interact with, the system uses the *hover effect*, not a focus effect, to provide visual feedback (for guidance, see [Eyes](https://developer.apple.com/design/human-interface-guidelines/eyes)). The hover effect isn’t related to the focus system.

### Game controls
<sub>`pages/game-controls.md`</sub>

**Match spatial game controller behavior to hand input.** In addition to supporting a wide array of wireless game controllers, your visionOS game can also support spatial game controllers such as PlayStation VR2 Sense controller. Allow players to interact with your game in a similar manner to how they interact using their hands. Specifically, support looking at an object and pressing the controller’s left or right trigger button to indirectly interact, or reaching out and pressing the left or right trigger button to directly interact. For more information, see [visionOS](https://developer.apple.com/design/human-interface-guidelines/gestures#visionOS).

### Gestures
<sub>`pages/gestures.md`</sub>

If you want to offer a specific interaction for your experience that people can’t perform using an existing system gesture, consider designing a custom gesture. To offer this type of interaction, your app needs to be running in a Full Space, and you must request people’s permission to access information about their hands. For developer guidance, see [Setting up access to ARKit data](https://developer.apple.com/documentation/visionos/setting-up-access-to-arkit-data).

![A screenshot of a person's hands performing a custom gesture, placing the two hands together to form a heart, while playing a visionOS game.](/images/com.apple.HIG/visionos-custom-spatial-gesture-happy-beam@2x.png)

**Prioritize comfort.** Continually test ergonomics of all interactions that require custom gestures. A custom interaction that requires people to keep their arms raised for even a little while can be physically tiring, and repeating very similar movements many times in succession can stress people’s muscles and joints.

**Carefully consider complex custom gestures that involve multiple fingers or both hands.** People may not always have both hands available when using your app or game. If you require a more complex gesture for your experience, consider also offering an alternative that requires less movement.

**Avoid custom gestures that require using a specific hand.** It can increase someone’s cognitive load if they need to remember which hand to use to trigger a custom gesture. It may also make your experience less welcoming to people with strong hand-dominance or limb differences.

### Gestures
<sub>`pages/gestures.md`</sub>

In visionOS 2 and later, people can look at the palm of one hand and use gestures to quickly access system overlays for Home and Control Center. These interactions are available systemwide, and are reserved solely for accessing system overlays.

> **Note:** The system overlay is the default method of accessing Control Center in visionOS 2 and later. The visionOS 1 behavior (looking upward) remains available as an accessibility setting.

When designing apps and games that use custom gestures or anchor content to a person’s hands, it’s important to take interactions with the system overlays into consideration.

**Reserve the area around a person’s hand for system overlays and their related gestures.** If possible, don’t anchor content to a person’s hands or wrists. If you’re designing a game that involves hand-anchored content, place it outside of the immediate area of someone’s hand to avoid colliding with the Home indicator.

![An illustration of a person's open hand with the palm facing upward. A dashed circular line above the hand indicates the area reserved for system overlays.](/images/com.apple.HIG/visionos-hand-area-of-focus@2x.png)

![An illustration of a person's open hand with the palm facing upward. A button with a circle icon representing the Home indicator appears above the palm.](/images/com.apple.HIG/visionos-spatial-gesture-home-indicator@2x.png)

![An illustration of a person's open hand with the palm facing downward. An overlay with the status bar appears above the hand.](/images/com.apple.HIG/visionos-spatial-gesture-control-center@2x.png)

**Consider deferring the system overlay behavior when designing an immersive app or game.** In certain circumstances, you may not want the Home indicator to appear when someone looks at the palm of their hand. For example, a game that uses virtual hands or gloves may want to keep someone within the world of the story, even if they happen to look at their hands from different angles. In such cases, when your app is running in a Full Space, you can choose to require a tap to reveal the Home indicator instead. For developer guidance, see [persistentSystemOverlays(_:)](https://developer.apple.com/documentation/swiftui/view/persistentsystemoverlays(_:)).

![An image of a person's open hand with the palm facing upward, shown from the person's perspective. A button with a circle icon representing the Home indicator appears above the palm. The image background shows the room that's the person's surroundings.](/images/com.apple.HIG/gestures-default-home-indicator@2x.png)

![An image of a person's open hand with the palm facing upward, shown from the person's perspective. A button with a circle icon representing the Home indicator appears above the palm. The image background shows a forest in a fully immersive space.](/images/com.apple.HIG/gestures-home-indicator-in-immersive-space@2x.png)

![An image of a person's open hand wearing a bulky space suit glove, shown from the person's perspective. The palm faces upward, and no button appears above it. The image background shows a starry sky in a fully immersive space.](/images/com.apple.HIG/gestures-fully-immersive-game-with-glove@2x.png)

> **Note:** Apps and games that you built for visionOS 1 defer the system overlay behavior by default. When a person looks at their palm with your app running in a Full Space, the Home indicator won’t appear unless they tap first.

**Use caution when designing custom gestures that involve a rolling motion of the hand, wrist, and forearm.** This specific motion is reserved for revealing system overlays. Since system overlays always display on top of app content and your app isn’t aware of when they’re visible, it’s important to test any custom gestures or content that might conflict.

### Gestures
<sub>`pages/gestures.md`</sub>

visionOS supports two categories of gestures: indirect and direct.

People use an *indirect* gesture by looking at an object to target it, and then manipulating that object from a distance — indirectly — with their hands. For example, a person can look at a button to focus it and select it by quickly tapping their finger and thumb together. Indirect gestures are comfortable to perform at any distance, and let people quickly change focus between different objects and select items with minimal movement.

*(video: A recording showing a closeup view of the top portion of a window in visionOS. A button in the window becomes highlighted. A picture-in-picture window is visible in the bottom-right corner of the recording. It shows a person's hand performing the indirect tap gesture. In response to the gesture, the highlighted button in the window activates.)*

People use a *direct* gesture to physically touch an interactive object. For example, people can directly type on the visionOS keyboard by tapping the virtual keys. Direct gestures work best when they are within reach. Because people may find it tiring to keep their arms raised for extended periods, direct gestures are best for infrequent use. visionOS also supports direct versions of all standard gestures, allowing people the choice to interact directly or indirectly with any standard component.

*(video: A recording showing a table with a vertical stack of three virtual cubic blocks on it in visionOS. A person moves their hand toward the blocks from right to left, and their extended fingers touch and push aside the center block. The center block falls to the side, and the other block also tumbles onto the tabletop.)*

Here are the standard direct gestures people use in visionOS; see [Specifications](https://developer.apple.com/design/human-interface-guidelines/gestures#Specifications) for a list of standard indirect gestures.

| Direct gesture | Common use |
| --- | --- |
| Touch | Directly select or activate an object. |
| Touch and hold | Open a contextual menu. |
| Touch and drag | Move an object to a new location. |
| Double touch | Preview an object or file; select a word in an editing context. |
| Swipe | Reveal actions and controls; dismiss views; scroll. |
| With two hands, pinch and drag together or apart | Zoom in or out. |
| With two hands, pinch and drag in a circular motion | Rotate an object. |

**Support standard gestures everywhere you can.** For example, as soon as someone looks at an object in your app or game, tap is the first gesture they’re likely to make when they want to select or activate it. Even if you also support custom gestures, supporting standard gestures such as tap helps people get comfortable with your app or game quickly.

**Offer both indirect and direct interactions when possible.** Prefer indirect gestures for UI and common components like buttons. Reserve direct gestures and custom gestures for objects that invite close-up interaction or specific motions in a game or interactive experience.

**Avoid requiring specific body movements or positions for input.** Not all people can perform specific body movements or position themselves in certain ways at all times, whether due to disability, spatial constraints, or other environmental factors. If your experience requires movement, consider supporting alternative inputs to let people choose the interaction method that works best for them.

### Image views
<sub>`pages/image-views.md`</sub>

Windows in visionOS apps and games can use image views to display 2D and stereoscopic images, as well as spatial photos. If your app uses RealityKit, you can also display images of any type outside of image views next to 3D content, or generate a spatial scene from an existing 2D image. For design guidance, see [visionOS](https://developer.apple.com/design/human-interface-guidelines/images#visionOS); for developer guidance, see [ImagePresentationComponent](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent).

For guidance on presenting other 3D content in a window or volume, see [visionOS](https://developer.apple.com/design/human-interface-guidelines/windows#visionOS).

### Images
<sub>`pages/images.md`</sub>

In addition to 2D and stereoscopic images, visionOS apps and games can use RealityKit to display spatial photos and spatial scenes. A *spatial photo* is a stereoscopic photo with additional spatial metadata, as captured on iPhone 15 Pro or later, Apple Vision Pro, or other compatible camera. A *spatial scene* is a 3D image generated from a 2D image to add a parallax effect that responds to head movement. For developer guidance, see [ImagePresentationComponent](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent).

**Make sure spatial photos render correctly in your app.** Use the stereo High-Efficiency Image Codec (HEIC) format to display a spatial photo in your app. When you add spatial metadata to a stereo HEIC, visionOS recognizes the photo as spatial and includes visual treatments that help minimize common causes of stereo-viewing discomfort.

**Prefer the feathered glass background effect to display text over spatial photos.** If you need to place text over a spatial photo in your app or game, use the feathered glass background effect. The effect adds contrast to make the text readable, and it blurs out detail to help reduce visual discomfort when people view text over spatial photos. For developer guidance, see [GlassBackgroundEffect](https://developer.apple.com/documentation/swiftui/glassbackgroundeffect).

**Take visual comfort into consideration when you make spatial photos from existing 2D content.** When adjusting the spatial metadata of a photo for your app or game, consider how you want people to view your content. Metadata like disparity adjustment can alter how people perceive the 3D scene, and can cause visual discomfort from certain viewing positions. For developer guidance, see [Creating spatial photos and videos with spatial metadata](https://developer.apple.com/documentation/imageio/creating-spatial-photos-and-videos-with-spatial-metadata).

**Display spatial photos and spatial scenes in standalone views.** Avoid displaying spatial photos inline with other content, as this can cause visual discomfort. Instead, showcase spatial photos or spatial scenes in a separate view, like a sheet or window. If you must display stereoscopic images inline, provide generous spacing between the image and any inline content to help people’s eyes adjust to the depth changes.

**Use spatial scenes in your app for specific moments.** Each spatial scene can take up to several seconds to generate from an existing image. Design experiences with this limitation in mind. For instance, the Photos app offers an explicit action to create a spatial scene while immersed in a single photo. Avoid displaying too many spatial scenes at once. Instead, use scroll views, pagination, or explicit actions to move to new photos and keep the visual information hierarchy simple.

**When displaying immersively, prefer minimal UI.** For example, the Spatial Gallery app displays a single piece of content with a small caption and a single Back button, relying on swipe gestures to navigate between items.

**Prefer displaying larger spatial scenes that you center in someone’s field of view.** When people view a spatial scene, they may move their head laterally to view the parallax effect. Smaller spatial scenes provide less of a parallax effect and may not be as impactful to viewers.

### Images
<sub>`pages/images.md`</sub>

In visionOS, people can view images at a much larger range of sizes than in any other platform, and the system dynamically scales the image resolution to match the current size. Because you can position images at specific angles within someone’s surroundings, image pixels may not line up 1:1 with screen pixels.

**Create a layered app icon.** App icons in visionOS are composed of two to three layers that provide the appearance of depth by moving at subtly different rates when the icon is in focus. For guidance, see [Layer design](https://developer.apple.com/design/human-interface-guidelines/app-icons#Layer-design).

**Prefer vector-based art for 2D images.** Avoid bitmap content because it might not look good when the system scales it up. If you use Core Animation layers, see [Drawing sharp layer-based content in visionOS](https://developer.apple.com/documentation/visionos/drawing-sharp-layer-based-content) for developer guidance.

**If you need to use rasterized images, balance quality with performance as you choose a resolution.** Although a @2x image looks fine at common viewing distances, its fixed resolution means that the system doesn’t dynamically scale it and it might not look sharp from close up. To help a rasterized image look sharp when people view it from a wide range of distances, you can use a higher resolution, but each increase in resolution results in a larger file size and may impact your app’s runtime performance, especially for resolutions over @6x. If you use images that have resolutions higher than @2x, be sure to also apply high-quality image filtering to help balance quality and performance (for developer guidance, see [filters](https://developer.apple.com/documentation/quartzcore/calayer/filters)).

### Keyboards
<sub>`pages/keyboards.md`</sub>

In visionOS, an app’s keyboard shortcuts appear in the shortcut interface that displays when people hold the Command key on a connected keyboard. Similar in organization to an app’s [The menu bar](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar) on iPad or Mac, the shortcut interface on Apple Vision Pro displays app commands in familiar system-defined menu categories such as File, Edit, and View. Unlike menu bar menus, the shortcut interface displays all relevant categories in one view, listing within each category only available commands that also have shortcuts.

**Write descriptive shortcut titles.** Because the shortcut interface displays a flat list of all items in each category, submenu titles aren’t available to provide context for their child items. Make sure each shortcut title is descriptive enough to convey its action without the additional context a submenu title might provide. For developer guidance, see [discoverabilityTitle](https://developer.apple.com/documentation/uikit/uikeycommand/discoverabilitytitle).

**Recognize that people see an overlay when they use a physical keyboard with your visionOS app or game.** When people connect a physical keyboard while using your visionOS app or game, the system displays a virtual keyboard overlay that provides typing completion and other controls.

*(video: A recording that shows two hands typing on a physical keyboard while the person runs an app in visionOS. A virtual window is visible above the physical keyboard, and displays the entered text and suggestions.)*

### Launching
<sub>`pages/launching.md`</sub>

**Consider launching in the Shared Space even if your app is fully immersive.** Opening a window in the Shared Space lets you provide more context about your app or game while giving it time to load, and it also lets you present a control that people can use to open your fully immersive experience. In general, people appreciate being able to choose when to transition to a Full Space, especially if they’re currently running other apps in the Shared Space. For guidance, see [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences).

### Layout
<sub>`pages/layout.md`</sub>

The guidance below can help you lay out content within the windows of your visionOS app or game, making it feel familiar and easy to use. For guidance on displaying windows in space and best practices for using depth, scale, and field of view in your visionOS app, see [Spatial layout](https://developer.apple.com/design/human-interface-guidelines/spatial-layout). To learn more about visionOS window components, see [visionOS](https://developer.apple.com/design/human-interface-guidelines/windows#visionOS).

> **Note:** When you add depth to content in a standard window, the content extends beyond the window’s bounds along the z-axis. If content extends too far along the z-axis, the system clips it.

**Consider centering the most important content and controls in your app or game.** Often, people can more easily discover and interact with content when it’s near the middle of a window, especially when the window is large.

**Keep a window’s content within its bounds.** In visionOS, the system displays window controls just outside a window’s bounds in the XY plane. For example, the Share menu appears above the window and the controls for resizing, moving, and closing the window appear below it. Letting 2D or 3D content encroach on these areas can make the system-provided controls, especially those below the window, difficult for people to use.

**If you need to display additional controls that don’t belong within a window, use an ornament.** An ornament lets you offer app controls that remain visually associated with a window without interfering with the system-provided controls. For example, a window’s toolbar and tab bar appear as ornaments. For guidance, see [Ornaments](https://developer.apple.com/design/human-interface-guidelines/ornaments).

**Make a window’s interactive components easy for people to look at.** You need to include enough space around an interactive component so that visually identifying it is easy and comfortable, and to prevent the system-provided hover effect from obscuring other content. For example, place buttons so their centers are at least 60 points apart. For guidance, see [Eyes](https://developer.apple.com/design/human-interface-guidelines/eyes), [Spatial layout](https://developer.apple.com/design/human-interface-guidelines/spatial-layout), and [visionOS](https://developer.apple.com/design/human-interface-guidelines/buttons#visionOS).

### Lists and tables
<sub>`pages/lists-and-tables.md` — upstream heading: iOS, iPadOS, visionOS</sub>

**Use an info button only to reveal more information about a row’s content.** An info button — called a *detail disclosure button* when it appears in a list row — doesn’t support navigation through a hierarchical table or list. If you need to let people drill into a list or table row’s subviews, use a disclosure indicator accessory control. For developer guidance, see [UITableViewCell.AccessoryType.disclosureIndicator](https://developer.apple.com/documentation/uikit/uitableviewcell/accessorytype-swift.enum/disclosureindicator).

![An illustration of a grouped list of rows. Each list item includes an info button at the trailing end of the row.](/images/com.apple.HIG/info-button-in-list@2x.png)

![An illustration of a grouped list of rows. Each list item includes a right-pointing chevron at the trailing end of the row.](/images/com.apple.HIG/disclosure-indicator-in-list@2x.png)

**Avoid adding an index to a table that displays controls — like disclosure indicators — in the trailing ends of its rows.** An *index* typically consists of the letters in an alphabet, displayed vertically at the trailing side of a list. People can jump to a specific section in the list by choosing the index letter that maps to it. Because both the index and elements like disclosure indicators appear on the trailing side of a list, it can be difficult for people to use one element without activating the other.

### Live Photos
<sub>`pages/live-photos.md`</sub>

In visionOS, people can view a Live Photo, but they can’t capture one.

### Materials
<sub>`pages/materials.md`</sub>

In visionOS, windows generally use an unmodifiable system-defined material called *glass* that helps people stay grounded by letting light, the current Environment, virtual content, and objects in people’s surroundings show through. Glass is an adaptive material that limits the range of background color information so a window can continue to provide contrast for app content while becoming brighter or darker depending on people’s physical surroundings and other virtual content.

*(video: A recording of the Music app window in visionOS. The window uses the glass material and adapts as the viewing angle and lighting change.)*

> **Note:** visionOS doesn’t have a distinct Dark Mode setting. Instead, glass automatically adapts to the luminance of the objects and colors behind it.

**Prefer translucency to opaque colors in windows.** Areas of opacity can block people’s view, making them feel constricted and reducing their awareness of the virtual and physical objects around them.

![An illustration of a field of view in visionOS with a window in the center. The window has an opaque background that obstructs its surroundings.](/images/com.apple.HIG/materials-visionos-opaque-window-incorrect@2x.png)

![An X in a circle to indicate incorrect usage](/images/com.apple.HIG/crossout@2x.png)

![An illustration of a field of view in visionOS with a window in the center. The window has a translucent material background that allows its surroundings to pass through.](/images/com.apple.HIG/materials-visionos-glass-window@2x.png)

![A checkmark in a circle to indicate correct usage](/images/com.apple.HIG/checkmark@2x.png)

**If necessary, choose materials that help you create visual separations or indicate interactivity in your app.** If you need to create a custom component, you may need to specify a system material for it. Use the following examples for guidance.

- The [thin](https://developer.apple.com/documentation/swiftui/material/thin) material brings attention to interactive elements like buttons and selected items.
- The [regular](https://developer.apple.com/documentation/swiftui/material/regular) material can help you visually separate sections of your app, like a sidebar or a grouped table view.
- The [thick](https://developer.apple.com/documentation/swiftui/material/thick) material lets you create a dark element that remains visually distinct when it’s on top of an area that uses a `regular` background.

![An illustration of a field of view in visionOS with a window in the center. The window is composed of a sidebar on the left and a content area on the right, with a text field at the top and a button in the lower-right corner. The sidebar uses regular material, while the text field uses thick material and the button uses thin material.](/images/com.apple.HIG/visionos-materials-window-example@2x.png)

To ensure foreground content remains legible when it displays on top of a material, visionOS applies vibrancy to text, symbols, and fills. Vibrancy enhances the sense of depth by pulling light and color forward from both virtual and physical surroundings.

visionOS defines three vibrancy values that help you communicate a hierarchy of text, symbols, and fills.

- Use [UIVibrancyEffectStyle.label](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/label) for standard text.
- Use [UIVibrancyEffectStyle.secondaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/secondarylabel) for descriptive text like footnotes and subtitles.
- Use [UIVibrancyEffectStyle.tertiaryLabel](https://developer.apple.com/documentation/uikit/uivibrancyeffectstyle/tertiarylabel) for inactive elements, and only when text doesn’t need high legibility.

![An illustration of a Share button with a translucent background material and a symbol. The symbol uses the default vibrant label color and has very high contrast against the background material.](/images/com.apple.HIG/materials-visionos-label-vibrant-primary@2x.png)

![An illustration of a Share button with a translucent background material and a symbol. The symbol uses the secondary vibrant label color and has high contrast against the background material.](/images/com.apple.HIG/materials-visionos-label-vibrant-secondary@2x.png)

![An illustration of a Share button with a translucent background material and a symbol. The symbol uses the tertiary vibrant label color and has muted contrast against the background material.](/images/com.apple.HIG/materials-visionos-label-vibrant-tertiary@2x.png)

### Menus
<sub>`pages/menus.md`</sub>

In visionOS, a menu can display items using the small or large layout styles that iOS and iPadOS define (for guidance, see [iOS, iPadOS](https://developer.apple.com/design/human-interface-guidelines/menus#iOS-iPadOS)). You can present a menu in your app or game from 3D content using a SwiftUI view. To ensure that your menu is always visible to people, even when other content occludes it, you can apply a [breakthrough effect](https://developer.apple.com/documentation/swiftui/view/presentationbreakthrougheffect(_:)). As in macOS, an open menu in a visionOS window can appear outside of the window’s boundaries.

**Prefer displaying a menu near the content it controls.** Because people need to look at a menu item before tapping it, they might miss the item’s effect if the content it controls is too far away.

![A partial screenshot showing an app window in visionOS. The window contains several buttons, including a 'More' button, which is selected. A menu containing a list of actions is displayed beneath the button.](/images/com.apple.HIG/visionos-notes-menu-popover-style@2x.png)

**Prefer the subtle breakthrough effect in most cases.** This effect blends the presentation with its surrounding content, to maintain legibility and usability while preserving the depth and context of the scene. When you select [automatic](https://developer.apple.com/documentation/swiftui/breakthrougheffect/automatic) for the breakthrough effect of a menu that overlaps with 3D content, the system applies [subtle](https://developer.apple.com/documentation/swiftui/breakthrougheffect/subtle) by default. You can use [prominent](https://developer.apple.com/documentation/swiftui/breakthrougheffect/prominent) if it’s important to display a menu prominently over the entire scene in your app or game, but this can disrupt the experience for people and potentially cause discomfort. Alternatively, you can use [none](https://developer.apple.com/documentation/swiftui/breakthrougheffect/none) to fully occlude your menu behind other 3D content — for example, in a puzzle game that requires people to navigate around barriers — but this may make it difficult for people to see and access the menu.

### Motion
<sub>`pages/motion.md`</sub>

In addition to subtly communicating context, drawing attention to information, and enriching immersive experiences, motion in visionOS can combine with [Depth](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Depth) to provide essential feedback when people look at interactive elements. Because motion is likely to be a large part of your visionOS experience, it’s crucial to avoid causing distraction, confusion, or discomfort.

**As much as possible, avoid displaying motion at the edges of a person’s field of view.** People can be particularly sensitive to motion that occurs in their peripheral vision: in addition to being distracting, such motion can even cause discomfort because it can make people feel like they or their surroundings are moving. If you need to show an object moving in the periphery during an immersive experience, make sure the object’s brightness level is similar to the rest of the visible content.

**Help people remain comfortable when showing the movement of large virtual objects.** If an object is large enough to fill a lot of the [Field of view](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Field-of-view), occluding most or all of [Immersion and passthrough](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences#Immersion-and-passthrough), people can naturally perceive it as being part of their surroundings. To help people perceive the object’s movement without making them think that they or their surroundings are moving, you can increase the object’s translucency, helping people see through it, or lower its contrast to make its motion less noticeable.

> **Note:** People can experience discomfort even when they’re the ones moving a large virtual object, such as a window. Although adjusting translucency and contrast can help in this scenario, consider also keeping a window’s size fairly small.

**Consider using fades when you need to relocate an object.** When an object moves from one location to another, people naturally watch the movement. If such movement doesn’t communicate anything useful to people, you can fade the object out before moving it and fade it back in after it’s in the new location.

**In general, avoid letting people rotate a virtual world.** When a virtual world rotates, the experience typically upsets people’s sense of stability, even when they control the rotation and the movement is subtle. Instead, consider using instantaneous directional changes during a quick fade-out.

**Consider giving people a stationary frame of reference.** It can be easier for people to handle visual movement when it’s contained within an area that doesn’t move. In contrast, if the entire surrounding area appears to move — for example, in a game that automatically moves a player through space — people can feel unwell.

**Avoid showing objects that oscillate in a sustained way.** In particular, you want to avoid showing an oscillation that has a frequency of around 0.2 Hz because people can be very sensitive to this frequency. If you need to show objects oscillating, aim to keep the amplitude low and consider making the content translucent.

### Multitasking
<sub>`pages/multitasking.md`</sub>

On Apple Vision Pro, people can run multiple apps at the same time in the Shared Space, viewing and switching between windows and volumes throughout the space.

Only one window is active at a time in the Shared Space. When people look from one window to another, the window they’re currently looking at becomes active while the previous window becomes more translucent and appears to recede along the z-axis. Closing an app window in the Shared Space transitions the app to the background without quitting it.

> **Note:** When an app is the Now Playing app, closing its window automatically pauses audio playback; if people want to resume playback, they can do so in Control Center without opening the window.

**Avoid interfering with the system-provided multitasking behavior.** When people look from one window to another, visionOS applies a feathered mask to the window they look away from to clarify its changed state. To avoid interfering with this visual feedback, don’t change the appearance of a window’s edges.

*(video: A recording showing the Notes app and the Settings app in the Shared Space in visionOS. The viewer first repositions the Notes window to slightly overlap the Settings window before activating Settings and then switching back to Notes. Each time an app becomes active, the system applies feathering to the inactive app's window.)*

**Don’t pause a window’s video playback when people look away from it.** In visionOS, as in macOS, people expect the playback they start in one window to continue while they view or perform a task in another window.

**Be prepared for situations where your audio can duck.** Unless an app is currently the Now Playing app, its audio can duck when people look away from it to another app.

### Offering help
<sub>`pages/offering-help.md` — upstream heading: macOS, visionOS</sub>

A *tooltip* (called a *help tag* in user documentation) displays a small, transient view that briefly describes how to use a component in the interface. In apps that run on a Mac — including iPhone and iPad apps — tooltips can appear when a person holds the pointer over an element; in visionOS apps, a tooltip can appear when a person looks at an element or holds the pointer over it. For developer guidance, see [help(_:)](https://developer.apple.com/documentation/swiftui/view/help(_:)-6oiyb).

![An illustration of a toolbar in macOS Finder with the pointer over the Back button. A tooltip with the title See folders you viewed previously appears beneath the pointer.](/images/com.apple.HIG/offering-help-macos-tooltip-help-tag@2x.png)

**Describe only the control that people indicate interest in.** When people want to know how to use a specific control, they don’t want to learn how to use nearby controls or how to perform a larger task.

**Explain the action or task the control initiates.** It often works well to begin the description with a verb — for example, “Restore default settings” or “Add or remove a language from the list.”

**In general, avoid repeating a control’s name in its tooltip.** Repeating the name takes up space in the tooltip and rarely adds value to the description.

**Be brief.** As much as possible, limit tooltip content to a maximum of 60 to 75 characters (note that localization often changes the length of text). To make a description brief and direct, consider using a sentence fragment and omitting articles. If you need a lot of text to describe a control, consider simplifying your interface design.

**Use sentence case.** Sentence case tends to appear more casual and approachable. If you write complete sentences, omit ending punctuation unless it’s required to be consistent with your app’s style.

**Consider offering context-sensitive tooltips.** For example, you could provide different text for a control’s different states.

### Page controls
<sub>`pages/page-controls.md`</sub>

In visionOS, page controls represent available pages and indicate the current page, but people don’t interact with them.

### Playing audio
<sub>`pages/playing-audio.md`</sub>

Subtle, expressive sounds are everywhere in visionOS, enhancing experiences and providing essential feedback when people look at a virtual object and use gestures to interact with it. The system combines audio algorithms with information about a person’s physical surroundings to produce *Spatial Audio*, which is sound that people can perceive as coming from specific locations in space, not just from speakers.

> **Important:** In visionOS, as in every platform, avoid communicating important information using only sound. Always provide additional ways to help people understand your app. For guidance, see [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility).

In visionOS, audio playback from the Now Playing app pauses automatically when people close the app’s window, and audio from an app that isn’t the Now Playing app can duck when people look away from it to different app.

**Prefer playing sound.** People generally choose to keep sounds audible while they’re wearing the device, so an app that doesn’t play sound — especially in an immersive moment — can feel lifeless and may even seem broken. Throughout the design process, look for opportunities to create meaningful sounds that aid navigation and help people understand the spatial qualities of your app.

**Design custom sounds for custom UI elements.** In general, a system-provided element plays sound to help people locate it and receive feedback when they interact with it. To help people interact with your custom elements, design sounds that provide feedback and enhance the spatial experience of your app.

**Use Spatial Audio to create an intuitive, engaging experience.** Because people can perceive Spatial Audio as coming from anywhere around them, it works especially well in a fully immersive context as a way to help an experience feel lifelike. *Ambient audio* provides pervasive sounds that can help anchor people in a virtual world and an *audio source* can sound like it comes from a specific object. As you build the soundscape for your app, consider using both types of audio.

**Consider defining a range of places from which your app sounds can originate.** Spatial Audio helps people locate the object that’s making sound, whether it’s stationary or moving in space. For example, when people move an app window that’s playing audio, the sound continues to come directly from the window, wherever people move it.

**Consider varying sounds that people could perceive as repetitive over time.** For example, the system subtly varies the pitch and volume of the virtual keyboard’s sounds, suggesting the different sounds a physical keyboard can make as people naturally vary the speed and forcefulness of their typing. An efficient way to achieve a pleasing variation in sound is to randomize a sound file’s pitch and volume during playback, instead of creating different files.

**Decide whether you need to play sound that’s fixed to the wearer or tracked by the wearer.** People perceive *fixed* sound as if it’s pointed at them, regardless of the direction they look or the virtual objects they move. In contrast, people tend to perceive *tracked* sound as coming from a particular object, so moving the object closer or farther away changes what they hear. In general, you want to use tracked sound to enhance the realism of your experience, but there could be cases where fixed sound is a good choice. For example, Mindfulness uses fixed sound to envelop the wearer in an engaging, peaceful setting.

### Playing video
<sub>`pages/playing-video.md`</sub>

**Help people stay comfortable when playing video in your app.** Often, an app doesn’t control the content in the videos it plays, but you can help people stay comfortable by:

- Letting them choose when to start playing a video
- Using a small window for playback, letting people resize it if they want
- Making sure people can see their surroundings during playback

**In a fully immersive experience, avoid letting virtual content obscure playback or transport controls.** In a fully immersive context, the system automatically places the video player at a predictable location that provides an optimal viewing experience. Use this location to help make sure that no virtual content occludes the default playback or transport controls in the ornament near the bottom of the player.

**Avoid automatically starting a fully immersive video playback experience.** People need control over their experience and they’re unlikely to appreciate being launched into a fully immersive video without warning.

**Create a thumbnail track if you want to support scrubbing.** The system displays thumbnails as people scrub to different times in the video, helping them choose the section they want. To improve performance, supply a set of thumbnails that each measure 160 px in width. For developer guidance, see [HTTP Live Streaming (HLS) Authoring Specification for Apple Devices > Trick Play](https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices#Trick-Play).

**Avoid expanding an inline video player to fill a window.** When you display the system-provided player view in a window, playback controls appear in the same plane as the player view and not in an ornament that floats above the window. Inline video needs to be 2D and you want to make sure that window content remains visible around the player so people don’t expect a more immersive playback experience. For developer guidance, see [AVPlayerViewController](https://developer.apple.com/documentation/avkit/avplayerviewcontroller).

**Use a RealityKit video player if you need to play video in a view like a splash screen or a transitional view.** In situations like these, people generally expect the video to lead into the next experience, so they don’t need playback controls or system-provided integration, like dimming and view anchoring. The RealityKit video player automatically uses the correct aspect ratio for both 2D and 3D video and supports closed captions. RealityKit can also help you play video as a special effect on the surface of a custom view or object. For developer guidance, see [RealityKit](https://developer.apple.com/documentation/realitykit).

### Pointing devices
<sub>`pages/pointing-devices.md`</sub>

In visionOS, people can attach an external pointing device or keyboard, and use both devices while they continue to use their eyes and hands. If people look at an element and then move the pointer, the system brings focus to the element under the pointer. Your app doesn’t have to do anything to support this behavior.

When a pointing device is attached, the area people are looking at determines the pointer’s context. For example, when people shift their eyes from one window to another, the pointer’s context seamlessly transitions to the new window.

*(video: A recording that shows a pointer moving around, highlighting items, and scrolling content within a Safari window in visionOS. A picture-in-picture window is visible in the bottom left corner of the recording. It shows a person's hand operating a trackpad next to a keyboard outside the field of view. The person's gestures on the trackpad correspond to the pointer movements.)*

When people use an attached pointing device that supports gestures, like a trackpad or mouse, the pointer hides while people are gesturing, minimizing visual distraction. In this scenario, the pointer remains hidden until people move it, when it reappears in the location they’re looking at.

### Privacy
<sub>`pages/privacy.md`</sub>

By default, visionOS uses ARKit algorithms to handle features like persistence, world mapping, segmentation, matting, and environment lighting. These algorithms are always running, allowing apps and games to automatically benefit from ARKit while in the Shared Space.

ARKit doesn’t send data to apps in the Shared Space; to access ARKit APIs, your app must open a Full Space. Additionally, features like Plane Estimation, Scene Reconstruction, Image Anchoring, and Hand Tracking require people’s permission to access any information. For developer guidance, see [Setting up access to ARKit data](https://developer.apple.com/documentation/visionos/setting-up-access-to-arkit-data).

In visionOS, user input is private by design. The system automatically displays hover effects when people look at interactive components you create using SwiftUI or RealityKit, giving people the visual feedback they need without exposing where they’re looking before they tap. For guidance, see [Eyes](https://developer.apple.com/design/human-interface-guidelines/eyes) and [visionOS](https://developer.apple.com/design/human-interface-guidelines/gestures#visionOS).

Developer access to device cameras works differently in visionOS than it does in other platforms. Specifically, the back camera provides blank input and is only available as a compatibility convenience; the front camera provides input for [visionOS](https://developer.apple.com/design/human-interface-guidelines/shareplay#visionOS), but only after people grant their permission. If the iOS or iPadOS app you’re bringing to visionOS includes a feature that needs camera access, remove it or replace it with an option for people to import content instead. For developer guidance, see [Making your existing app compatible with visionOS](https://developer.apple.com/documentation/visionos/making-your-app-compatible-with-visionos).

### Scroll views
<sub>`pages/scroll-views.md`</sub>

In views that support Look to Scroll, people can scroll using only their eyes. Scrolling starts when people look near the boundary of the scroll view — along the top and bottom for vertical scroll views, or along the sides for horizontal scroll views. For example, a person can look at the bottom edge of a Safari window to scroll the page down, or look at an album on the trailing edge in the Music app to scroll it horizontally toward the center of the page. Look to Scroll works in conjunction with existing behavior, so someone can choose whether to use a gesture or their eyes to scroll. For developer guidance, see [look](https://developer.apple.com/documentation/swiftui/scrollinputkind/look).

**Support Look to Scroll for reading or browsing views.** Because Look to Scroll doesn’t work by default, you need to add support for it to each individual scroll view. If your app contains reading or browsing views, add support for Look to Scroll to provide a comfortable and hands-free experience. For developer guidance, see [ScrollInputKind](https://developer.apple.com/documentation/swiftui/scrollinputkind).

**Avoid using Look to Scroll for secondary content.** In general, support standard gestures — but not Look to Scroll — in views that contain UI controls or dense information that requires quick, precise scrolling. For example, the Notes app offers Look to Scroll within the main view to let people easily read their content, but doesn’t support it for the list of notes.

**Maintain consistency across content.** If you support Look to Scroll for one view in your app, make sure to support it for all similar views. For example, if you offer several collection views of videos throughout your app, support Look to Scroll for each of these views so people know what to expect.

**Define clear scroll areas within your app.** In views that support Look to Scroll, prefer making the view the full width or full height of the window. This gives people generous space to scroll and provides clear edges. If you inset a scroll view from a window, like in the Notes app, provide clear boundaries so people know where to look.

**If your app uses custom scroll effects or animations, remove them before supporting Look to Scroll.** Custom effects that use scroll position to change content, such as parallax effects and animations, can cause Look to Scroll to behave unexpectedly.

### Scroll views
<sub>`pages/scroll-views.md`</sub>

In visionOS, the scroll indicator has a small, fixed size to help communicate that people can scroll efficiently without making large movements. To make it easy to find, the scroll indicator always appears in a predictable location with respect to the window: vertically centered at the trailing edge during vertical scrolling and horizontally centered at the window’s bottom edge during horizontal scrolling.

When people begin swiping content in the direction they want it to scroll, the scroll indicator appears at the window’s edge, visually reinforcing the effect of their gesture and providing feedback about the content’s current position and overall length. When people look at the scroll indicator and begin a drag gesture, the indicator enables a jog bar experience that lets people manipulate the scrolling speed instead of the content’s position. In this experience, the scroll indicator reveals tick marks that speed up or slow down as people make small adjustments to their gesture, providing visual feedback that helps people precisely control scrolling acceleration.

*(video: A recording showing a scroll indicator on a long page in the Notes app. As the viewer drags the page quickly, the indicator shows tick marks that match the scrolling speed.)*

**If necessary, account for the size of the scroll indicator.** Although the indicator’s overall size is small, it’s a little thicker than the same component in iOS. If your content uses tight margins, consider increasing them to prevent the scroll indicator from overlapping the content.

### Segmented controls
<sub>`pages/segmented-controls.md`</sub>

When people look at a segmented control that uses icons, the system displays a tooltip that contains the descriptive text you supply.

### SharePlay
<sub>`pages/shareplay.md`</sub>

People expect most visionOS apps to support SharePlay. While wearing Apple Vision Pro, people choose the Spatial option in FaceTime to share content and activities with others.

In a shared activity, FaceTime can show representations of other participants — called spatial Personas — within each wearer’s space, making everyone feel like they’re sharing the same experience in the same place. During a shared experience in FaceTime, people can interact with each other in natural ways through their spatial Personas. For example, people can speak or gesture directly to others, tell when someone is paying attention to them, and know which person is using a shared tool or resource.

visionOS uses the concept of *shared context* to describe the characteristics of a shared activity that help people feel physically present with others while connecting over the same content. A shared context helps give people confidence that they’re experiencing the same thing as everyone else.

When people feel that they’re truly sharing an experience, social dynamics can encourage authentic, intuitive interactions. For example, people can communicate verbally and nonverbally to make plans, take turns, and share resources.

> **Note:** During a shared activity, the system helps preserve people’s privacy by obscuring some visual details about wearers. In addition, a person can adjust their spatial Persona if they want. Although the system can place spatial Personas shoulder to shoulder and it supports shared gestures like a handshake or “high five,” spatial Personas remain apart.

**Choose the spatial Persona template that suits your shared activity.** When you design a shared activity, you can use a spatial Persona template to specify a layout for arranging spatial Personas in the shared activity space. The system provides three spatial Persona templates: side-by-side, surround, and conversational.

The side-by-side template places participants next to each other along a curved line segment, all facing the shared content. The side-by-side template gives everyone a great view of the content, making it a good choice for helping people watch media together. Because people aren’t facing each other in this arrangement, the side-by-side template can encourage less nonverbal interaction than other spatial Persona templates.

![An illustration representing a side-by-side shared activity in visionOS. Participants are positioned next to one another and facing a shared screen.](/images/com.apple.HIG/visionos-shareplay-side-by-side@2x.png)

The system-applied surround template arranges participants all the way around the shared content in the center. This spatial Persona template works especially well when the content is 3D, because each participant views it from a different angle. In the surround template, participants face each other as if they were grouped around a table, promoting both verbal and nonverbal interactions.

![An illustration representing a surround shared activity in visionOS. Participants are gathered in a circle around shared content.](/images/com.apple.HIG/visionos-shareplay-surround@2x.png)

The conversational template also groups participants around a center point, but places your content along the circle, not at its center. Because of this position, not everyone has the same view of your content, and it might not be convenient for everyone to interact with it. Consider using the conversational arrangement if your experience is more about people being together while your app performs a task in the background like playing music.

![An illustration representing a conversational shared activity in visionOS. Participants are positioned in a semi-circle formation around shared content.](/images/com.apple.HIG/visionos-shareplay-conversational@2x.png)

For developer guidance, see [SystemCoordinator](https://developer.apple.com/documentation/groupactivities/systemcoordinator) and [SpatialTemplatePreference](https://developer.apple.com/documentation/groupactivities/spatialtemplatepreference).

**Be prepared to launch directly into your shared activity.** When one person shares your activity with others on a FaceTime call, the system minimizes friction by automatically launching your app for everyone. In this scenario, you want to avoid displaying any windows that aren’t related to the shared activity. For example, if people need to sign in before joining the activity, be sure to present this task in an autodismissible window that disappears as soon as people finish providing the required input.

**Help people enter a shared activity together, but don’t force them.** When one participant changes their level of immersion, the system tells you so you can synchronize the experience for everyone. Before synchronizing, check whether changing a person’s level of immersion would disrupt their current task; if it would, offer them the choice to join the updated experience. For example, if someone is editing content in an unshared window, you might present an alert that lets them choose to transition. For guidance, see [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences).

**Smoothly update a shared activity when new participants join.** When someone joins an in-progress activity, you need to integrate them without disrupting the experience for everyone else. For example, it’s important to update shared immersive content to keep all participants synchronized. Also, consider designing ways to accommodate up to five participants in your arrangement, updating their positions as necessary.

### SharePlay
<sub>`pages/shareplay.md`</sub>

Sometimes, it makes sense to adjust the shared context of a shared activity so each participant can customize their experience, such as for comfort or accessibility. In other situations, strictly maintaining a shared context might decrease people’s enjoyment of the experience. For example, when content has only one ideal viewing angle, each participant might need their own.

**Let people personalize their experience without changing the experience for others.** For example, people might need to adjust various settings, like volume or subtitles, to make views and interactions accessible or make themselves more comfortable.

![An image of a TV window in visionOS. The image is split down the center to contrast the personalized experiences of two people: Person 1 has subtitles turned on, while Person 2 has subtitles turned off.](/images/com.apple.HIG/visionos-shareplay-subtitles-personalization@2x.png)

**Consider when to give each participant a unique view of the shared content.** Some content looks best when people view it from a specific perspective. For example, people can share a Spatial Capture in a standard window with other people’s spatial Personas visible around it. However, to perceive the depth in a Spatial Capture, each person needs to view it from the right angle. In this scenario, a person could temporarily transition to a Full Space that hides other participants and ensures the right viewing angle for them, even while everyone else continues to view the standard window and each other. If it makes sense to provide per-person versions of your shared content, be sure to continue synchronizing people’s positions and your app context to maintain the shared experience.

**Make it easy for people to exit and rejoin a shared activity.** Sometimes, people need to perform an unrelated task in your app or a different one, or engage with their physical  surroundings. When this happens, you need to present a control or other component that lets people quickly rejoin the shared activity. In addition, you might want to continue displaying the shared content so people can stay informed about the ongoing shared experience while they’re hiding their spatial Persona.

### SharePlay
<sub>`pages/shareplay.md`</sub>

When your shared activity runs in a Full Space, the system helps your app maintain a shared context by using a single coordinate system to arrange your content and all participants, automatically synchronizing the size, position, and orientation of your app for each person. You’re responsible for displaying objects, playing sounds, and supporting interactions in ways that enhance the feeling of sharing the experience.

**Make sure everyone views the same state of your app.** If your app has more than one state — such as a media app that provides both minimal and theater-like viewing modes — you need to avoid letting different participants view different states, because doing so can diminish people’s sense of being together in a shared space. The exception to this is when someone needs to temporarily exit a shared activity; for guidance, see [Adjusting a shared context](https://developer.apple.com/design/human-interface-guidelines/shareplay#Adjusting-a-shared-context).

**Use Spatial Audio to enrich your shared activity.** Playing Spatial Audio can help you strengthen the realism of the shared experience. For guidance, see [Playing audio](https://developer.apple.com/design/human-interface-guidelines/playing-audio).

**When possible, let people discover natural, social solutions to confusions or conflicts that might arise during a shared experience.** For example, if only one participant at a time can use a virtual tool, avoid displaying UI, like tool-use controls or notifications, and instead let people speak or gesture to the group when they want to use the tool. If conflicts can arise during your shared activity — for example, if multiple people try to change the same content at the same time — consider implementing a simple rule, like last change wins, and letting people use the rule to define behavior that’s acceptable to the group.

**Help people keep their private and shared content separate.** By default, the system clearly differentiates a shared window from windows that aren’t shared. For example, when people use Music to listen together, the shared Music window appears as a new window for everyone, while any individual’s open library window remains separate and unshared. If your app can open multiple windows, help people share the one they want and make it easy for them to distinguish shared from unshared windows. If possible, also let people drag content they want to share from a private window to a shared one.

**Private**

![An image of a private TV window in visionOS, with a translucent button above the window labeled Not Shared.](/images/com.apple.HIG/visionos-shareplay-status-idle@2x.png)

**Selected**

![An image of a private TV window in visionOS, with the button above the window selected. A menu emerges downward from the button with options for sharing the window.](/images/com.apple.HIG/visionos-shareplay-status-selected@2x.png)

**Shared**

![An image of a shared TV window in visionOS. The button above the window is labeled with the SharePlay icon and the text Shared.](/images/com.apple.HIG/visionos-shareplay-status-sharing@2x.png)

### Sheets
<sub>`pages/sheets.md`</sub>

While a sheet is visible in a visionOS app, it floats in front of its parent window, dimming it, and becoming the target of people’s interactions with the app.

*(video: A recording showing a sheet opening above a blank window in visionOS.)*

**Avoid displaying a sheet that emerges from the bottom edge of a window.** To help people view the sheet, prefer centering it in their [Field of view](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Field-of-view).

**Present a sheet in a default size that helps people retain their context.** Avoid displaying a sheet that covers most or all of its window, but consider letting people resize the sheet if they want.

### Sidebars
<sub>`pages/sidebars.md`</sub>

**If your app’s hierarchy is deep, consider using a sidebar within a tab in a tab bar.** In this situation, a sidebar can support secondary navigation within the tab. If you do this, be sure to prevent selections in the sidebar from changing which tab is currently open.

![A partial screenshot of the Music app in visionOS. The app's window includes a sidebar for navigating the music library, and the secondary pane includes a grid of playlists.](/images/com.apple.HIG/visionos-sidebar-music@2x.png)

### Sliders
<sub>`pages/sliders.md`</sub>

**Prefer horizontal sliders.** It’s generally easier for people to gesture from side to side than up and down.

### Split views
<sub>`pages/split-views.md`</sub>

**To display supplementary information, prefer a split view instead of a new window.** A split view gives people convenient access to more information without leaving the current context, whereas a new window may confuse people who are trying to navigate or reposition content. Opening more windows also requires you to carefully manage the relationship between views in your app or game. If you need to request a small amount of information or present a simple task that someone must complete before returning to their main task, use a [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets).

### Tab bars
<sub>`pages/tab-bars.md`</sub>

In visionOS, a tab bar is always vertical, floating in a position that’s fixed relative to the window’s leading side. When people look at a tab bar, it automatically expands; to open a specific tab, people look at the tab and tap. While a tab bar is expanded, it can temporarily obscure the content behind it.

*(video: A recording showing a closeup of a tab bar along the side of an app's window in visionOS. The tab bar includes only symbols. The currently selected tab receives the hover effect, showing that someone is looking at it, and the bar expands to display both symbols and labels.)*

**Supply a symbol and a text label for each tab.** A tab’s symbol is always visible in the tab bar. When people look at the tab bar, the system reveals tab labels, too. Even though the tab bar expands, you need to keep tab labels short so people can read them at a glance.

![A screenshot showing a collapsed tab bar containing only symbols.](/images/com.apple.HIG/visionos-tab-bar-collapsed@2x.png)

![A screenshot showing an expanded tab bar containing both symbols and labels.](/images/com.apple.HIG/visionos-tab-bar-expanded@2x.png)

**If it makes sense in your app, consider using a sidebar within a tab.** If your app’s hierarchy is deep, you might want to use a [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars) to support secondary navigation within a tab. If you do this, be sure to prevent selections in the sidebar from changing which tab is currently open.

### Toolbars
<sub>`pages/toolbars.md`</sub>

In visionOS, the system-provided toolbar appears along the bottom edge of a window, above the window-management controls, and in a parallel plane that’s slightly in front of the window along the z-axis.

![A screenshot of a toolbar along the bottom of the Notes app window in visionOS.](/images/com.apple.HIG/visionos-toolbar-notes-app@2x.png)

To maintain the legibility of toolbar items as content scrolls behind them, visionOS uses a variable blur in the bar background. The variable blur anchors the bar above the scrolling content while letting the view’s glass material remain uniform and undivided.

In visionOS, you can supply either a symbol or a text label for each toolbar item. When people look at a toolbar item that contains a symbol, visionOS reveals the text label, providing additional information.

**Prefer using a system-provided toolbar.** The standard toolbar has a consistent and familiar appearance and is optimized to work well with eye and hand input. In addition, the system automatically places a standard toolbar in the correct position in relation to its window.

![A screenshot of a toolbar in visionOS.](/images/com.apple.HIG/visionos-toolbar-standard-layout@2x.png)

**Avoid creating a vertical toolbar.** In visionOS, [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) are vertical, so presenting a vertical toolbar could confuse people.

**Try to prevent windows from resizing below the width of the toolbar.** visionOS doesn’t include a menu bar where each app lists all its actions, so it’s important for the toolbar to provide reliable access to essential controls regardless of a window’s size.

**If your app can enter a modal state, consider offering contextually relevant toolbar controls.** For example, a photo-editing app might enter a modal state to help people perform a multistep editing task. In this scenario, the controls in the modal editing view are different from the controls in the main window. Be sure to reinstate the window’s standard toolbar controls when the app exits the modal state.

**Avoid using a pull-down menu in a toolbar.** A pull-down menu lets you offer additional actions related to a toolbar item, but can be difficult for people to discover and may clutter your interface. Because a toolbar is located at the bottom edge of a window in visionOS, a pull-down menu might obscure the standard window controls that appear below the bottom edge. For guidance, see [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons).

### Typography
<sub>`pages/typography.md`</sub>

SF Pro is the system font in visionOS. If you use NY, you need to specify the type styles you want.

visionOS uses bolder versions of the Dynamic Type body and title styles and it introduces Extra Large Title 1 and Extra Large Title 2 for wide, editorial-style layouts. For guidance using vibrancy to indicate hierarchy in text and symbols, see [visionOS](https://developer.apple.com/design/human-interface-guidelines/materials#visionOS).

**In general, prefer 2D text.** The more visual depth text characters have, the more difficult they can be to read. Although a small amount of 3D text can provide a fun visual element that draws people’s attention, if you’re going to display content that people need to read and understand, prefer using text that has little or no visual depth.

![A screenshot that shows the correct placement of 2D text on a window in visionOS.](/images/com.apple.HIG/visionos-typography-2d-text-correct@2x.png)

![A checkmark in a circle to indicate correct usage.](/images/com.apple.HIG/checkmark@2x.png)

![A screenshot that shows the incorrect placement of 3D text on a window in visionOS.](/images/com.apple.HIG/visionos-typography-3d-text-incorrect@2x.png)

![An X in a circle to indicate incorrect usage.](/images/com.apple.HIG/crossout@2x.png)

**Make sure text looks good and remains legible when people scale it.** Use a text style that makes the text look good at full scale, then test it for legibility at different scales.

**Maximize the contrast between text and the background of its container.** By default, the system displays text in white, because this color tends to provide a strong contrast with the default system background material, making text easier to read. If you want to use a different text color, be sure to test it in a variety of contexts.

**If you need to display text that’s not on a background, consider making it bold to improve legibility.** In this situation, you generally want to avoid adding shadows to increase text contrast. The current space might not include a visual surface on which to cast an accurate shadow, and you can’t predict the size and density of shadow that would work well with a person’s current Environment.

**Keep text facing people as much as possible.** If you display text that’s associated with a point in space, such as a label for a 3D object, you generally want to use *billboarding* — that is, you want the text to face the wearer regardless of how they or the object move. If you don’t rotate text to remain facing the wearer, the text can become impossible to read because people may view it from the side or a highly oblique angle. For example, imagine a virtual lamp that appears to be on a physical desk with a label anchored directly above it. For the text to remain readable, the label needs to rotate around the y-axis as people move around the desk; in other words, the baseline of the text needs to remain perpendicular to the person’s line of sight.

### Virtual keyboards
<sub>`pages/virtual-keyboards.md`</sub>

In visionOS, the system-provided virtual keyboard supports both direct and indirect gestures and appears in a separate window that people can move where they want. You don’t need to account for the location of the keyboard in your layouts.

*(video: A recording showing a person typing on a virtual keyboard in visionOS.)*

### VoiceOver
<sub>`pages/voiceover.md`</sub>

**Be mindful that custom gestures aren’t always accessible.** When VoiceOver is turned on in visionOS, apps and games that define custom gestures don’t receive hand input by default. This ensures people can explore the interface using their voice, without an app responding to hand input at the same time. A person can opt out of this behavior by enabling Direct Gesture mode, which disables standard VoiceOver gestures and lets apps process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/documentation/visionos/improving-accessibility-support-in-your-app).

### Widgets
<sub>`pages/widgets.md`</sub>

In addition to size and mounting style, the system applies one of two treatment styles to visionOS widgets. Choosing the right treatment for your widget helps reinforce the experience you want to create.

- The [paper](https://developer.apple.com/documentation/widgetkit/widgettexture/paper) style creates a more grounded, print-like style that feels solid and makes the widget feel like part of its surroundings. When lighting conditions change, widgets in the paper style become darker or lighter in response.
- The [glass](https://developer.apple.com/documentation/widgetkit/widgettexture/glass) style creates a lighter, layered look that adds depth and visual separation between foreground and background elements to emphasize clarity and contrast. The foreground elements always stay bright and legible, and don’t dim or brighten, even as ambient light changes.

**Choose the paper style for a print-like look that feels more like a real object in the room.** The entire widget responds to the ambient lighting and blends naturally into its surroundings. For example, the Music poster widget uses the paper style to display albums and playlists like framed artwork on a wall.

**Choose the glass style for information-rich widgets.** Glass visually separates foreground and background elements, allowing you to decide which parts of your interface adapt to the surroundings and which stay visually consistent. Foreground elements appear in full color, unaffected by ambient lighting, to make sure important content stays sharp and legible. For example, a News widget appears with editorial images in the background with a soft, print-like look. Its headlines stay in the foreground, crisp and easy to read.

### Widgets
<sub>`pages/widgets.md`</sub>

The way a widget appears on a surface plays a big role in how a person perceives it. To make it feel intentional and integrated into their surroundings, people place a widget on surfaces in distinct mounting styles.

- **[elevated](https://developer.apple.com/documentation/widgetkit/widgetmountingstyle/elevated) style**.  On horizontal surfaces — for example, on a desk — the widget always appears elevated and gently tilts backward, providing a subtle angle that improves readability, and casts a soft shadow that helps it feel grounded on the surface. On vertical surfaces — for example, on a wall — the widget either appears elevated, sitting flush on the surface and similar to how you mount a picture frame.
- **[recessed](https://developer.apple.com/documentation/widgetkit/widgetmountingstyle/recessed) style**. On vertical surfaces — for example, on a wall — the widget can appear recessed, with content set back into the surface, creating a depth effect that gives the illusion of a cutout in the surface. Horizontal surfaces don’t use the recessed mounting style.

By default, widgets use the elevated mounting style, because it works for horizontal and vertical surfaces.

**Choose the mounting style that fits your content and the experience you want to create.** By default, visionOS widgets use the elevated mounting style, which is ideal for content that you want to stand out and feel present, like reminders, media, or glanceable data. Recessed widgets are ideal for immersive or ambient content, like weather or editorial content, and people can only place them on a vertical surface. If a style doesn’t suit your widget, you can opt out of it for each widget. If you choose to only support the recessed mounting style, people can’t place the widget on a horizontal surface. For example, a weather app might only support the recessed mounting style to give the illusion of looking out of a window for its large and extra-large system family widgets, and only support the elevated style for its small system family widget.

> **Note:** Use the [supportedMountingStyles(_:)](https://developer.apple.com/documentation/swiftui/widgetconfiguration/supportedmountingstyles(_:)) property of your [WidgetConfiguration](https://developer.apple.com/documentation/swiftui/widgetconfiguration) to  declare supported mounting styles — elevated, recessed, or both — for all widgets included in the configuration. To offer a widget that only supports one mounting style and other widgets that support both mounting styles, create separate widget configurations. For example, create one widget configuration for the widget that only supports the recessed mounting style, and a second configuration for the widgets that support both mounting styles.

**Test your elevated widget designs with each system-provided frame width.** People can choose from different system-defined frame widths for widgets that use the elevated mounting style. You can’t change your layout based on the frame width a person chooses, so make sure your widget layout stays visually balanced for each frame width.

### Widgets
<sub>`pages/widgets.md`</sub>

Widgets in visionOS are 3D objects that people place on a horizontal or vertical surface. When a person places a widget on a surface, the widget persists in that location even when the person turns Apple Vision Pro off and back on. Widgets have a consistent, real-world scale. Their size, *mounting style*, and *treatment style* impact how a person perceives them.

visionOS widgets appear in full-color by default, but they appear in the accented rendering mode when people personalize them with tint colors using a range of system-provided color palettes. Additionally, people can customize the frame width of widgets that use the elevated mounting style, and custom options that are unique to the widget. For example, visionOS doesn’t provide systemwide light or dark appearances. However, the Music poster widget offers its own customization option that lets people choose between a light and a dark theme that the app generates from the displayed album art.

For developer guidance, see [Updating your widgets for visionOS](https://developer.apple.com/documentation/widgetkit/updating-your-widgets-for-visionos).

**Adapt your design and content for the spatial experience Apple Vision Pro provides.** In visionOS, widgets don’t float in isolation but are part of living rooms, kitchens, offices, and more. Consider this context early and think of widgets as part of someone’s surroundings when you bring your existing widgets to visionOS or design them from scratch. For example, the Music widget adapts to a poster-like appearance that’s glanceable across the room with large typography and a high-resolution image, and a productivity app might offer a small widget that easily fits on a desk.

**Test your widgets across the full range of system color palettes and in different lighting conditions.** Make sure your widget’s tone, contrast, and legibility remain consistent and intentional. If you choose to exclude UI elements from tinting, test your widget in every provided tint color palette to make sure the untinted elements remain legible when a person customizes their widgets with tint colors.

### Widgets
<sub>`pages/widgets.md`</sub>

Widgets on Apple Vision Pro can adapt based on a person’s proximity, and visionOS provides widgets with two key thresholds to design for: the [simplified](https://developer.apple.com/documentation/widgetkit/levelofdetail/simplified) threshold for when a person views a widget at a distance, and the [default](https://developer.apple.com/documentation/widgetkit/levelofdetail/default) threshold when a person views it nearby.

![A placeholder image showing a widget viewed from a distance in visionOS.](/images/com.apple.HIG/widgets-extra-large-portrait-far-proximity@2x.png)

![A placeholder image showing a widget viewed from nearby in visionOS.](/images/com.apple.HIG/widgets-extra-large-portrait-close-proximity@2x.png)

Because widgets can appear throughout a person’s environment, it’s also important to match a widget’s size to the type of content it contains, and to be aware of how it appears at a variety of distances.

**Design a responsive layout that shows the right level of detail for each of the two thresholds.** When a person views the widget at a distance, display a simplified version of your widget that shows fewer details and has a larger type size, and remove interactive elements like buttons or toggles. When a person views the widget from nearby, show more details and use a smaller type size. To create a smooth and consistent experience and help your layout feel continuous, maintain shared elements across both distance thresholds.

**Offer widget family sizes that fit a person’s surroundings well.** Widgets map to real-world dimensions and have a permanent presence in a person’s spatial environment. Think about where people might place your widget — mounted to a wall, placed on a sideboard, or sitting next to a workplace — and choose a widget family size that’s right for that context. For example, offer a small system widget with content that people might place on a desk or an extra large widget to let people decorate their surroundings with something visually rich, like artwork or photography.

**Display content in a way that remains legible from a range of distances.** To make a widget feel intentional and proportionate to where they place it, people can scale a widget from 75 to 125 percent in size. Use print design principles like clear hierarchy, strong typography, and scale to make sure your content remains glanceable. Include high-resolution assets that look good scaled up to every size.

### Windows
<sub>`pages/windows.md`</sub>

The default window style consists of an upright plane that uses an unmodifiable background [Materials](https://developer.apple.com/design/human-interface-guidelines/materials) called *glass* and includes a close button, window bar, and resize controls that let people close, move, and resize the window. A window can also include a Share button, [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars), [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), and one or more [Ornaments](https://developer.apple.com/design/human-interface-guidelines/ornaments). By default, visionOS uses dynamic [Scale](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Scale) to help a window’s size appear to remain consistent regardless of its proximity to the viewer. For developer guidance, see [DefaultWindowStyle](https://developer.apple.com/documentation/swiftui/defaultwindowstyle).

![A screenshot of a window for an app named 'Hello World' in visionOS. The window includes text and buttons for entering different experiences.](/images/com.apple.HIG/visionos-window-2d@2x.png)

**Prefer using a window to present a familiar interface and to support familiar tasks.** Help people feel at home in your app by displaying an interface they’re already comfortable with, reserving more [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences) for the meaningful content and activities you offer. If you want to showcase bounded 3D content like a game board, consider using a [visionOS volumes](https://developer.apple.com/design/human-interface-guidelines/windows#visionOS-volumes).

**Retain the window’s glass background.** The default glass background helps your content feel like part of people’s surroundings while adapting dynamically to lighting and using specular reflections and shadows to communicate the window’s scale and position. Removing the glass material tends to cause UI elements and text to become less legible and to no longer appear related to each other; using an opaque background obscures people’s surroundings and can make a window feel constricting and heavy.

**Choose an initial window size that minimizes empty areas within it.** By default, a window measures 1280x720 pt. When a window first opens, the system places it about two meters in front of the wearer, giving it an apparent width of about three meters. Too much empty space inside a window can make it look unnecessarily large while also obscuring other content in people’s space.

**Aim for an initial shape that suits a window’s content.** For example, a default Keynote window is wide because slides are wide, whereas a default Safari window is tall because most webpages are much longer than they are wide. For games, a tower-building game is likely to open in a taller window than a driving game.

**Choose a minimum and maximum size for each window to help keep your content looking great.** People appreciate being able to resize windows as they customize their space, but you need to make sure your layout adjusts well across all sizes. If you don’t set a minimum and maximum size for a window, people could make it so small that UI elements overlap or so large that your app or game becomes unusable. For developer guidance, see [Positioning and sizing windows](https://developer.apple.com/documentation/visionos/positioning-and-sizing-windows).

![A screenshot of a window for an app in visionOS. The window includes text that discusses objects in orbit, and it includes buttons for viewing a satellite, the moon, and a telescope. The satellite button is selected and a 3D satellite is displayed.](/images/com.apple.HIG/visionos-window-2d-with-volume@2x.png)

**Minimize the depth of 3D content you display in a window.** The system adds highlights and shadows to the views and controls within a window, giving them the appearance of [Depth](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Depth) and helping them feel more substantial, especially when people view the window from an angle. Although you can display 3D content in a window, the system clips it if the content extends too far from the window’s surface. To display 3D content that has greater depth, use a volume.

### Windows
<sub>`pages/windows.md`</sub>

You can use a volume to display 2D or 3D content that people can view from any angle. A volume includes window-management controls just like a window, but unlike in a window, a volume’s close button and window bar shift position to face the viewer as they move around the volume. For developer guidance, see [VolumetricWindowStyle](https://developer.apple.com/documentation/swiftui/volumetricwindowstyle).

![A screenshot of a volume containing a 3D globe in visionOS, beside a window.](/images/com.apple.HIG/visionos-window-3d@2x.png)

**Prefer using a volume to display rich, 3D content.** In contrast, if you want to present a familiar, UI-centric interface, it generally works best to use a [visionOS windows](https://developer.apple.com/design/human-interface-guidelines/windows#visionOS-windows).

**Place 2D content so it looks good from multiple angles.** Because a person’s perspective changes as they move around a volume, the location of 2D content within it might appear to change in ways that don’t make sense. To pin 2D content to specific areas of 3D content inside a volume, you can use an attachment.

**In general, use dynamic scaling.** Dynamic scaling helps a volume’s content remain comfortably legible and easy to interact with, even when it’s far away from the viewer. On the other hand, if you want a volume’s content to represent a real-world object, like a product in a retail app, you can use fixed scaling (this is the default).

**Take advantage of the default baseplate appearance to help people discern the edges of a volume.** In visionOS 2 and later, the system automatically makes a volume’s horizontal “floor,” or *baseplate*, visible by displaying a gentle glow around its border when people look at it. If your content doesn’t fill the volume, the system-provided glow can help people become aware of the volume’s edges, which can be particularly useful in keeping the resize control easy to find. On the other hand, if your content is full bleed or fills the volume’s bounds — or if you display a custom baseplate appearance — you may not want the default glow.

**Consider offering high-value content in an ornament.** In visionOS 2 and later, a volume can include an ornament in addition to a toolbar and tab bar. You can use an ornament to reduce clutter in a volume and elevate important views or controls. When you use an attachment anchor to specify the ornament’s location, such as `topBack` or `bottomFront`, the ornament remains in the same position, relative to the viewer’s perspective, as they move around the volume. Be sure to avoid placing an ornament on the same edge as a toolbar or tab bar, and prefer creating only one additional ornament to avoid overshadowing the important content in your volume. For developer guidance, see [ornament(visibility:attachmentAnchor:contentAlignment:ornament:)](https://developer.apple.com/documentation/swiftui/view/ornament(visibility:attachmentanchor:contentalignment:ornament:)).

**Choose an alignment that supports the way people interact with your volume.** As people move a volume, the baseplate can remain parallel to the floor of a person’s surroundings, or it can tilt to match the angle at which a person is looking. In general, a volume that remains parallel to the floor works well for content that people don’t interact with much, whereas a volume that tilts to match where a person is looking can keep content comfortably usable, even when the viewer is reclining.

### Windows
<sub>`pages/windows.md`</sub>

visionOS defines two main window styles: default and volumetric. Both a default window (called a *window*) and a volumetric window (called a *volume*) can display 2D and 3D content, and people can view multiple windows and volumes at the same time in both the Shared Space and a Full Space.

![An illustration representing a window in visionOS. The illustration consists of two parallel rounded rectangles, slightly separated and displayed on an angle, positioned above a window bar.](/images/com.apple.HIG/visionos-window-style-2d-window@2x.png)

![An illustration representing a volume in visionOS. The illustration consists of a translucent cube. The base of the cube is darker than the other sides. The front of the cube is positioned above a window bar.](/images/com.apple.HIG/visionos-window-style-3d-volume@2x.png)

> **Note:** visionOS also defines the *plain* window style, which is similar to the default style, except that the upright plane doesn’t use the glass background. For developer guidance, see [PlainWindowStyle](https://developer.apple.com/documentation/swiftui/plainwindowstyle).

The system defines the initial position of the first window or volume people open in your app or game. In both the Shared Space and a Full Space, people can move windows and volumes to new locations.

## watchOS

### Action button
<sub>`pages/action-button.md`</sub>

In watchOS, a person can assign the Action button’s first press to drop a waypoint, start a dive, or begin a specific workout. Beyond a single button press, the Action button also supports secondary actions like marking a segment or transitioning to the next modality during a multi-part workout.

**Consider offering a secondary function that supports or advances the primary action people choose.** People often use the Action button without looking at the screen, so a subsequent button press needs to flow logically from the first press, while also making sense in the current context. If your app supports workout or dive actions, consider designing a simple, intuitive secondary function that people can easily learn and remember. Consider carefully before you offer more than one secondary function, because doing so can increase people’s cognitive load and make your app seem harder to use.

**Prefer using subsequent button presses to support additional functionality rather than to stop or conclude a function.** If you need to let people stop their main task — as opposed to pausing the current function — offer this option within your interface instead.

**Pause the current function when people press the Action button and side button together.** The exception is in a diving app where pausing a dive may be dangerous to the diver, causing them to lose track of their depth or not understand how long they’ve been underwater. Unless pausing the current function results in a negative experience, be sure to meet people’s expectations by letting them pause their current activity when they press both buttons at the same time.

### Action sheets
<sub>`pages/action-sheets.md`</sub>

The system-defined style for action sheets includes a title, an optional message, a Cancel button, and one or more additional buttons. The appearance of this interface is different depending on the device.

![An illustration of an action sheet on Apple Watch, showing content that represents text in the top half of the watch screen and two stacked buttons in the bottom half.](/images/com.apple.HIG/action-sheet-watch-system-defined@2x.png)

Each button has an associated style that conveys information about the button’s effect. There are three system-defined button styles:

| Style | Meaning |
| --- | --- |
| Default | The button has no special meaning. |
| Destructive | The button destroys user data or performs a destructive action in the app. |
| Cancel | The button dismisses the view without taking any action. |

**Avoid displaying more than four buttons in an action sheet, including the Cancel button.** When there are fewer buttons onscreen, it’s easier for people to view all their options at once. Because the Cancel button is required, aim to provide no more than three additional choices.

### App icons
<sub>`pages/app-icons.md`</sub>

**Avoid using black for your icon’s background.** Lighten a black background so the icon doesn’t blend into the display background.

### Buttons
<sub>`pages/buttons.md`</sub>

watchOS displays all inline buttons using the [capsule](https://developer.apple.com/documentation/swiftui/buttonbordershape/capsule) button shape. When you place a button inline with content, it gains a material effect that contrasts with the background to ensure legibility.

![An illustration that represents a screen on Apple Watch, which includes capsule-shaped Primary and Secondary buttons.](/images/com.apple.HIG/buttons-watch-full-width@2x.png)

**Use a toolbar to place buttons in the corners.** The system automatically moves the time and title to accommodate toolbar buttons. The system also applies the [Liquid Glass](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass) appearance to toolbar buttons, providing a clear visual distinction from the content beneath them.

![An illustration showing toolbar buttons in the top leading and trailing corners, as well as three toolbar buttons across the bottom of the screen.](/images/com.apple.HIG/buttons-watch-toolbar-corners@2x.png)

**Prefer buttons that span the width of the screen for primary actions in your app.** Full-width buttons look better and are easier for people to tap. If two buttons must share the same horizontal space, use the same height for both, and use images or short text titles for each button’s content.

**Use toolbar buttons to provide either navigation to related areas or contextual actions for the view’s content.** These buttons provide access to additional information or secondary actions for the view’s content.

**Use the same height for vertical stacks of one- and two-line text buttons.** As much as possible, use identical button heights for visual consistency.

### Charts
<sub>`pages/charts.md`</sub>

**In general, avoid requiring complex chart interactions in your watchOS app.** As much as possible, prefer displaying useful information people can get at a glance and supporting simple interactions when they add value. If you also offer a version of your app in another platform, consider using it to display more details and to support additional interactions with your chart. For example, Heart Rate in watchOS displays a chart of the wearer’s heart-rate data for the current day, whereas the Health app on iPhone displays heart-rate data for several different periods of time and lets people examine individual marks.

### Collaboration and sharing
<sub>`pages/collaboration-and-sharing.md`</sub>

In your SwiftUI app running in watchOS, use [ShareLink](https://developer.apple.com/documentation/swiftui/sharelink) to present the system-provided share sheet.

### Color
<sub>`pages/color.md`</sub>

**Use background color to support existing content or supply additional information.** Background color can establish a sense of place and help people recognize key content. For example, in Activity, each infographic view for the Move, Exercise, and Stand Activity rings has a background that matches the color of the ring. Use background color when you have something to communicate, rather than as a solely visual flourish. Avoid using full-screen background color in views that are likely to remain onscreen for long periods of time, such as in a workout or audio-playing app.

**Recognize that people might prefer graphic complications to use tinted mode instead of full color.** The system can use a single color that’s based on the wearer’s selected color in a graphic complication’s images, gauges, and text. For guidance, see [Complications](https://developer.apple.com/design/human-interface-guidelines/complications).

### Feedback
<sub>`pages/feedback.md`</sub>

**Avoid displaying an indeterminate progress indicator — such as a loading indicator — in a watchOS app.** An animated indicator can make people think they need to continue paying attention to the display, which isn’t a good user experience. To provide a better experience, reassure people that they’ll receive a notification when the process completes.

### Game Center
<sub>`pages/game-center.md`</sub>

**Be aware of Game Center support on watchOS.** While GameKit features and API are available for watchOS games, keep in mind that there’s no system-supported Game Center UI that you can invoke on watchOS. Instead, Game Center content for watchOS games appears on a connected iPhone.

### Gestures
<sub>`pages/gestures.md`</sub>

In watchOS 11 and later, people can use the double-tap gesture to scroll through lists and scroll views, and to advance between vertical tab views. Additionally, you can specify a toggle or button as the primary action in your app, or in your widget or Live Activity when the system displays it in the Smart Stack. Double-tapping in a view with a primary action highlights the control and then performs the action. The system also supports double tap for custom actions that you offer in [Notifications](https://developer.apple.com/design/human-interface-guidelines/notifications), where it acts on the first nondestructive action in the notification.

**Avoid setting a primary action in views with lists, scroll views, or vertical tabs.** This conflicts with the default navigation behaviors that people expect when they double-tap.

**Choose the button that people use most commonly as the primary action in a view.** Double tap is helpful in a nonscrolling view when it performs the action that people use the most. For example, in a media controls view, you could assign the primary action to the play/pause button. For developer guidance, see [handGestureShortcut(_:isEnabled:)](https://developer.apple.com/documentation/swiftui/view/handgestureshortcut(_:isenabled:)) and [primaryAction](https://developer.apple.com/documentation/swiftui/handgestureshortcut/primaryaction).

### Image views
<sub>`pages/image-views.md`</sub>

**Use SwiftUI to create animations when possible.** Alternatively, you can use WatchKit to animate a sequence of images within an image element if necessary. For developer guidance, see [WKImageAnimatable](https://developer.apple.com/documentation/watchkit/wkimageanimatable).

### Images
<sub>`pages/images.md`</sub>

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

### In-app purchase
<sub>`pages/in-app-purchase.md`</sub>

The sign-up screen in your watchOS app needs to display the same set of information about your subscription options that you display in other versions of your app. For the complete list of required items, see [Making signup effortless](https://developer.apple.com/design/human-interface-guidelines/in-app-purchase#Making-signup-effortless). The following guidelines can help you design a sign-up screen that feels at home on Apple Watch.

**Clearly describe the differences between versions of your app that run on different devices.** If your watchOS app supports different functionality or provides a subset of the content that’s available on other devices, be sure to clarify these differences in your description. Be straightforward about the advantages of accessing subscription content through your watchOS app without implying that the experience is identical to the ones in other versions of your app.

![A screenshot of an app running on Apple Watch. The screen includes text that reads: Intrepid Pro. Unlock 90,000 topographic maps, advanced GPS features, and offline access for trail guidance anywhere. A Close button appears in the top-left corner of the screen.](/images/com.apple.HIG/clarify-description-before@2x.png)

![A screenshot of an app running on Apple Watch. The screen includes text that reads: Intrepid Pro. Use advanced GPS features for trail guidance on Apple Watch. Unlock 90,000 topographic maps for use on iPhone and other devices. A Close button appears in the top-left corner of the screen.](/images/com.apple.HIG/clarify-description-after@2x.png)

**Consider using a modal sheet to display the required information.** After people respond to your call to action to learn more about your subscription offers, you can use a modal sheet to present all required items in a single view. Even though people must scroll the view to access all the information, displaying it in a modal sheet helps your app UI remain streamlined and concise. Also, a modal sheet’s default Close button makes it easy for people to return to your free content with one tap. If you create a custom sign-up view instead of using a modal sheet, design a complete, efficient flow and include a Close or Cancel button that lets people return to your free content.

**Make subscription options easy to compare on a small screen.** People need to understand the terms of each subscription option before they can choose one. Aim to display the duration and discount information for each option in a compact way that’s easy to scan and compare. Here are two ways you might present subscription options in your watchOS app:

- Display each option in a separate button. Using one button per payment option lets people start the signup process with one tap. In this design, it’s important to lock up each button with its description so that people can see how these elements are related, especially while scrolling.
- Display a list of options, followed by a button people tap to start the signup process. Using a list to display one option per row gives you a compact design that minimizes scrolling while making subscription choices easy to scan and understand. In this design, the button’s title can update to reflect the chosen option.

![A screenshot of an app running on Apple Watch. The screen includes two subscription buttons: $4.99 per month and $29.99 per year. A Close button appears in the top-left corner of the screen.](/images/com.apple.HIG/lock-up-option-information@2x.png)

![A screenshot of an app running on Apple Watch. The screen includes a list of subscription options: $4.99 billed monthly and $29.99 billed yearly. The $29.99 option is selected. A $29.99 per year button appears at the bottom of the screen, and a Close button appears in the top-left corner of the screen.](/images/com.apple.HIG/list-option-information@2x.png)

### Labels
<sub>`pages/labels.md`</sub>

Date and time text components (shown below on the left) display the current date, the current time, or a combination of both. You can configure a date text component to use a variety of formats, calendars, and time zones. A countdown timer text component (shown below on the right) displays a precise countdown or count-up timer. You can configure a timer text component to display its count value in a variety of formats.

![An illustration of date and time text components on Apple Watch, with the date aligned to the leading edge and the time aligned to the trailing edge.](/images/com.apple.HIG/labels-date-time-text-component@2x.png)

![An illustration of a countdown timer text component on Apple Watch, with the time value at the center.](/images/com.apple.HIG/labels-countdown-timer-text-component@2x.png)

When you use the system-provided date and timer text components, watchOS automatically adjusts the label’s presentation to fit the available space. The system also updates the content without further input from your app.

Consider using date and timer components in complications. For design guidance, see [Complications](https://developer.apple.com/design/human-interface-guidelines/components/system-experiences/complications); for developer guidance, see [Text](https://developer.apple.com/documentation/swiftui/text).

### Layout
<sub>`pages/layout.md`</sub>

**Design your content to extend from one edge of the screen to the other.** The Apple Watch bezel provides a natural visual padding around your content. To avoid wasting valuable space, consider minimizing the padding between elements.

![An illustration of the Workout app’s main list of workouts on Apple Watch. A callout indicates that the currently focused workout item spans the full width of the available screen area.](/images/com.apple.HIG/layout-full-width@2x.png)

**Avoid placing more than two or three controls side by side in your interface.** As a general rule, display no more than three buttons that contain glyphs — or two buttons that contain text — in a row. Although it’s usually better to let text buttons span the full width of the screen, two side-by-side buttons with short text labels can also work well, as long as the screen doesn’t scroll.

![A diagram of an Apple Watch screen showing two side-by-side buttons beneath three lines of text.](/images/com.apple.HIG/layout-controls@2x.png)

**Support autorotation in views people might want to show others.** When people flip their wrist away, apps typically respond to the motion by sleeping the display, but in some cases it makes sense to autorotate the content. For example, a wearer might want to show an image to a friend or display a QR code to a reader. For developer guidance, see [isAutorotating](https://developer.apple.com/documentation/watchkit/wkextension/isautorotating).

### Lists and tables
<sub>`pages/lists-and-tables.md`</sub>

**When possible, limit the number of rows.** Short lists are easier for people to scan, but sometimes people expect a long list of items. For example, if people subscribe to a large number of podcasts, they might think something’s wrong if they can’t view all their items. You can help make a long list more manageable by listing the most relevant items and providing a way for people to view more.

**Constrain the length of detail views if you want to support vertical page-based navigation.** People use vertical page-based navigation to swipe vertically among the detail items of different list rows. Navigating in this way saves time because people don’t need to return to the list to tap a new detail item, but it works only when detail views are short. If your detail views scroll, people won’t be able to use vertical page-based navigation to swipe among them.

### Live Activities
<sub>`pages/live-activities.md`</sub>

When a Live Activity begins on iPhone, it appears on a paired Apple Watch at the top of the Smart Stack. By default, the view displayed in the Smart Stack combines the leading and trailing elements from the Live Activity’s compact presentation on iPhone.

If you offer a watchOS app and someone taps the Live Activity in the Smart Stack, it opens your watchOS app. Without a watchOS app, tapping opens a full-screen view with a button to open your app on the paired iPhone.

**Consider creating a custom watchOS layout.** While the system provides a default view automatically, a custom layout designed for Apple Watch can show more information and add interactive functionality like a button or toggle.

**Carefully consider including buttons or toggles in your custom layout.** The custom watchOS layout also applies to your Live Activity in CarPlay where the system deactivates interactive elements. If people are likely to start or observe your Live Activity while driving, don’t include buttons or toggles in your custom watchOS layout. For developer guidance, see [Creating custom views for Live Activities](https://developer.apple.com/documentation/activitykit/creating-custom-views-for-live-activities).

![An illustration that shows the compact presentation of a Live Activity in the Dynamic Island on iPhone.](/images/com.apple.HIG/live-activities-ios-dynamic-island-default@2x.png)

![An illustration that shows the automatically generated default presentation of a Live Activity in a Smart Stack view, with the leading and trailing elements from the iPhone compact view spaced apart in the lower corners.](/images/com.apple.HIG/live-activity-watch-default-implementation@2x.png)

![An illustration that shows a custom presentation of a Live Activity in a Smart Stack view, with a balanced design that shows a graphical countdown timer balanced with explanatory text.](/images/com.apple.HIG/live-activity-watch-custom-implementation@2x.png)

**Focus on essential information and significant updates.** Use space in the Smart Stack as efficiently as possible and think of the most useful information that a Live Activity can convey:

- Progress, like the estimated arrival time of a delivery
- Interactive elements, like stopwatch or timer controls
- Significant updates, like sports score changes

### Loading
<sub>`pages/loading.md`</sub>

**As much as possible, avoid showing a loading indicator in your watchOS experience.** People expect quick interactions with their Apple Watch, so aim to display content immediately. In situations where content needs a second or two to load, it’s better to display a loading indicator than a blank screen.

### Managing accounts
<sub>`pages/managing-accounts.md`</sub>

Use iCloud synchronization to provide access to the Keychain, letting people autofill user names and passwords and preserve app settings.

### Managing notifications
<sub>`pages/managing-notifications.md`</sub>

By default, the notification settings people use for apps on their iPhone apply to the same apps on their Apple Watch. People can manage these settings in the Apple Watch app on iPhone, or they can access per-notification options — such as Mute 1 Hour or Turn off Time Sensitive — by swiping left when a notification arrives on their Apple Watch.

### Maps
<sub>`pages/maps.md`</sub>

On Apple Watch, maps are static snapshots of geographic locations. Place a map in your interface at design time and show the appropriate region at runtime. The displayed region isn’t interactive; tapping it opens the Maps app on Apple Watch. You can add up to five annotations to a map to highlight points of interest or other relevant information. For developer guidance, see [WKInterfaceMap](https://developer.apple.com/documentation/watchkit/wkinterfacemap).

![A screenshot of a map on Apple Watch, displaying Apple Park and some of the surrounding area.](/images/com.apple.HIG/maps-watch1@2x.png)

**Fit the map interface element to the screen.** The entire element needs to be visible on the Apple Watch display without requiring scrolling.

**Show the smallest region that encompasses the points of interest.** The content within a map interface element doesn’t scroll, so all key content must be visible within the displayed region.

For developer guidance, see [WKInterfaceMap](https://developer.apple.com/documentation/watchkit/wkinterfacemap).

### Materials
<sub>`pages/materials.md`</sub>

**Use materials to provide context in a full-screen modal view.** Because full-screen modal views are common in watchOS, the contrast provided by material layers can help orient people in your app and distinguish controls and system elements from other content. Avoid removing or replacing material backgrounds for modal sheets when they’re provided by default.

![An illustration of a modal view in watchOS with an example title, descriptive text, and a single action button. The modal completely covers the screen with a transparent material, and uses a thinner material for the button along with vibrant label text.](/images/com.apple.HIG/watchos-modal-view-material-background@2x.png)

### Motion
<sub>`pages/motion.md`</sub>

SwiftUI provides a powerful and streamlined way to add motion to your app. If you need to use WatchKit to animate layout and appearance changes — or create animated image sequences — see [WKInterfaceImage](https://developer.apple.com/documentation/watchkit/wkinterfaceimage).

> **Note:** All layout- and appearance-based animations automatically include built-in easing that plays at the start and end of the animation. You can’t turn off or customize easing.

### Nearby interactions
<sub>`pages/nearby-interactions.md`</sub>

On Apple Watch, Nearby Interaction APIs provide a peer device’s distance. Also, all watchOS apps participating in a nearby interaction experience must be in the foreground.

### Notifications
<sub>`pages/notifications.md`</sub>

A short look appears when the wearer’s wrist is raised and disappears when it’s lowered.

![An illustration that represents a short look notification from a generic app. It includes a large primary image in the center, a title, and a short preview of the notification content.](/images/com.apple.HIG/notifications-short-looks@2x.png)

**Avoid using a short look as the only way to communicate important information.** A short look appears only briefly, giving people just enough time to see what the notification is about and which app sent it. If your notification information is critical, make sure you deliver it in other ways, too.

**Keep privacy in mind.** Short looks are intended to be discreet, so it’s important to provide only basic information. Avoid including potentially sensitive information in the notification’s title.

### Notifications
<sub>`pages/notifications.md`</sub>

Long looks provide more detail about a notification. If necessary, people can swipe vertically or use the Digital Crown to scroll a long look. After viewing a long look, people can dismiss it by tapping it or simply by lowering their wrist.

![An illustration that represents a long look notification from a generic app. It includes a small primary image in the upper left corner, badging a platter with the notification title and content. Beneath the notification are two full width action buttons, the second of which extends off the screen to indicate that the view is scrollable.](/images/com.apple.HIG/notifications-long-looks@2x.png)

A custom long-look interface can be static or dynamic. The *static* interface lets you display a notification’s message along with additional static text and images. The *dynamic* interface gives you access to the notification’s full content and offers more options for configuring the appearance of the interface.

You can customize the content area for both static and dynamic long looks, but you can’t change the overall structure of the interface. The system-defined structure includes a *sash* at the top of the interface and a Dismiss button at the bottom, below all custom buttons.

**Consider using a rich, custom long-look notification to let people get the information they need without launching your app.** You can use SwiftUI [Animations](https://developer.apple.com/documentation/swiftui/animations) to create engaging, interruptible animations; alternatively, you can use [SpriteKit](https://developer.apple.com/documentation/spritekit) or [SceneKit](https://developer.apple.com/documentation/scenekit).

**At the minimum, provide a static interface; prefer providing a dynamic interface too.** The system defaults to the static interface when the dynamic interface is unavailable, such as when there is no network or the iPhone companion app is unreachable. Be sure to create the resources for your static interface in advance and package them with your app.

**Choose a background appearance for the sash.** The system-provided sash, at the top of the long-look interface, displays your app icon and name. You can customize the sash’s color or give it a blurred appearance. If you display a photo at the top of the content area, you’ll probably want to use the blurred sash, which has a light, translucent appearance that gives the illusion of overlapping the image.

**Choose a background color for the content area.** By default, the long look’s background is transparent. If you want to match the background color of other system notifications, use white with 18% opacity; otherwise, you can use a custom color, such as a color within your brand’s palette.

**Provide up to four custom actions below the content area.** For each long look, the system uses the notification’s type to determine which of your custom actions to display as buttons in the notification UI. In addition, the system always displays a Dismiss button at the bottom of the long-look interface, below all custom buttons. If your watchOS app has an iPhone companion that supports notifications, the system shares the actionable notification types already registered by your iPhone app and uses them to configure your custom action buttons.

### Notifications
<sub>`pages/notifications.md`</sub>

On Apple Watch, notifications occur in two stages: *short look* and *long look*. People can also view notifications in Notification Center. On supported devices, people can double-tap to respond to notifications.

You can help people have a great notification experience by designing app-specific assets and actions that are relevant on Apple Watch. If your watchOS app has an iPhone companion that supports notifications, watchOS can automatically provide default short-look and long-look interfaces if necessary.

### Notifications
<sub>`pages/notifications.md`</sub>

People can double-tap to respond to notifications on supported devices. When a person responds to a notification with a double tap, the system selects the first nondestructive action as the response.

**Keep double tap in mind when choosing the order of custom actions you present as responses to a notification.** Because a double tap runs the first nondestructive action, consider placing the action that people use most frequently at the top of the list. For example, a parking app that provides custom actions for extending the time on a paid parking spot could offer options to extend the time by 5 minutes, 15 minutes, or an hour, with the most common choice listed first.

### Page controls
<sub>`pages/page-controls.md`</sub>

In watchOS, page controls can be displayed at the bottom of the screen for horizontal pagination, or next to the Digital Crown when presenting a vertical [tab view](https://developer.apple.com/design/human-interface-guidelines/components/layout-and-organization/tab-views). When using vertical tab views, the page indicator shows people where they are in the navigation, both within the current page and within the set of pages. The page control transitions between scrolling through a page’s content and scrolling to other pages.

![An illustration representing a screen that includes a vertical tab view on Apple Watch. A page control next to the Digital Crown shows that the fourth tab is currently selected.](/images/com.apple.HIG/page-controls-watch-vertical@2x.png)

![An illustration representing a screen that includes a horizontal tab view on Apple Watch. A page control at the bottom shows that the second tab is currently selected.](/images/com.apple.HIG/page-controls-watch-horizontal@2x.png)

**Use vertical pagination to separate multiple views into distinct, purposeful pages.** Give each page a clear purpose, and let people scroll through the pages using the Digital Crown. In watchOS, this design is more effective than horizontal pagination or many levels of hierarchical navigation.

**Consider limiting the content of an individual page to a single screen height.** Embracing this constraint encourages each page to serve a clear and distinct purpose and results in a more glanceable design. Use variable-height pages judiciously and, if possible, only place them after fixed-height pages in your app design.

### Pickers
<sub>`pages/pickers.md`</sub>

Pickers display lists of items that people navigate using the Digital Crown, which helps people manage selections in a precise and engaging way.

A picker can display a list of items using the wheels style. watchOS can also display date and time pickers using the wheels style. For developer guidance, see [Picker](https://developer.apple.com/documentation/swiftui/picker) and [DatePicker](https://developer.apple.com/documentation/swiftui/datepicker).

![An illustration representing a screen containing a picker view on Apple Watch, showing three items in a list. The center item is highlighted.](/images/com.apple.HIG/pickers-wheel-watch@2x.png)

![An illustration representing a screen containing a date picker on Apple Watch, with the day highlighted.](/images/com.apple.HIG/pickers-date-watch@2x.png)

![An illustration representing a screen containing a time picker on Apple Watch, with the minutes highlighted.](/images/com.apple.HIG/pickers-time-watch@2x.png)

You can configure a picker to display an outline, caption, and scrolling indicator.

For longer lists, the navigation link displays the picker as a button. When someone taps the button, the system shows the list of options. The person can also scrub through the options using the Digital Crown without tapping the button. For developer guidance, see [navigationLink](https://developer.apple.com/documentation/swiftui/pickerstyle/navigationlink).

![An illustration representing a screen that contains a picker button on Apple Watch. The button’s text denotes that the second item is selected.](/images/com.apple.HIG/pickers-navigation-button-watch@2x.png)

![An illustration representing a screen showing a list of items on Apple Watch. The second item in the list is selected.](/images/com.apple.HIG/pickers-navigation-list-watch@2x.png)

### Playing audio
<sub>`pages/playing-audio.md`</sub>

In watchOS, the system manages audio playback. An app can play short audio clips while it’s active and running in the foreground, or it can play longer audio that continues even when people lower their wrist or switch to another app. For developer guidance, see [Playing Background Audio](https://developer.apple.com/documentation/watchkit/playing-background-audio).

**Use the recommended encoding values for media assets.** Specifically, use the 64 kbps HE-AAC (High-Efficiency Advanced Audio Coding) format to produce good-quality audio with lower data requirements.

**Consider** **presenting a Now Playing view so people can control current or recently played audio without leaving your app.** The system-provided Now Playing view also displays information about the current audio source — which might be another app on a person’s Apple Watch or iPhone — and automatically selects the current or most recently used source. For developer guidance, see [Adding a Now Playing View](https://developer.apple.com/documentation/watchkit/adding-a-now-playing-view).

### Playing haptics
<sub>`pages/playing-haptics.md`</sub>

Apple Watch Series 4 and later provides haptic feedback for the Digital Crown, which gives people a more tactile experience as they scroll through content. By default, the system provides linear haptic detents that people can feel as they rotate the Digital Crown. Some system controls, like table views, provide detents as new items scroll onto the screen. For developer guidance, see [WKHapticType](https://developer.apple.com/documentation/watchkit/wkhaptictype).

watchOS defines the following set of haptics, each of which conveys a specific meaning to people.

**Notification**

*(video: An animation that represents an arrangement of haptic pulses of various durations and strengths by showing a set of thin vertical lines that symbolize sound waves.)*

**Notification.** Tells the person that something significant or out of the ordinary has happened and requires their attention. The system plays this same haptic when a local or remote notification arrives.

**Up**

*(video: An animation that represents an arrangement of haptic pulses of various durations and strengths by showing a set of thin vertical lines that symbolize sound waves.)*

**Up.** Tells the person that an important value increased above a significant threshold.

**Down**

*(video: An animation that represents an arrangement of haptic pulses of various durations and strengths by showing a set of thin vertical lines that symbolize sound waves.)*

**Down.** Tells the person that an important value decreased below a significant threshold.

**Success**

*(video: An animation that represents an arrangement of haptic pulses of various durations and strengths by showing a set of thin vertical lines that symbolize sound waves.)*

**Success.** Tells the person that an action completed successfully.

**Failure**

*(video: An animation that represents an arrangement of haptic pulses of various durations and strengths by showing a set of thin vertical lines that symbolize sound waves.)*

**Failure.** Tells the person that an action failed.

**Retry**

*(video: An animation that represents an arrangement of haptic pulses of various durations and strengths by showing a set of thin vertical lines that symbolize sound waves.)*

**Retry.** Tells the person that an action failed but they can retry it.

**Start**

*(video: An animation that represents an arrangement of haptic pulses of various durations and strengths by showing a set of thin vertical lines that symbolize sound waves.)*

**Start.** Tells the person that an activity started. Use this haptic when starting a timer or any other activity that a person can explicitly start and stop. The stop haptic usually follows this haptic.

**Stop**

*(video: An animation that represents an arrangement of haptic pulses of various durations and strengths by showing a set of thin vertical lines that symbolize sound waves.)*

**Stop.** Tells the person that an activity stopped. Use this haptic when stopping a timer or other activity that the person previously started.

**Click**

*(video: An animation that represents an arrangement of haptic pulses of various durations and strengths by showing a set of thin vertical lines that symbolize sound waves.)*

**Click.** Provides the sensation of a dial clicking, helping you communicate progress at predefined increments or intervals. Overusing the click haptic tends to diminish its utility and can even be confusing when clicks overlap each other.

### Playing video
<sub>`pages/playing-video.md`</sub>

In watchOS, the system manages video playback. Apps can play short video clips while the app is active and running in the foreground. You can use a movie element to embed clips in your interface and play video inline, or you can play a clip in a separate interface. For developer guidance, see [VideoPlayer](https://developer.apple.com/documentation/avkit/videoplayer).

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

### Progress indicators
<sub>`pages/progress-indicators.md`</sub>

By default the system displays the progress indicators in white over the scene’s background color. You can change the color of the progress indicator by setting its tint color.

![An image of a progress bar filling from left to right in watchOS.](/images/com.apple.HIG/progress-bar-watch@2x.png)

![An image of a circular progress indicator filling clockwise in watchOS.](/images/com.apple.HIG/progress-ring-watch@2x.png)

![An image of a spinning activity indicator in watchOS.](/images/com.apple.HIG/activity-indicators-watch@2x.png)

### Scroll views
<sub>`pages/scroll-views.md`</sub>

**Prefer vertically scrolling content.** People are accustomed to using the Digital Crown to navigate to and within apps on Apple Watch. If your app contains a single list or content view, rotating the Digital Crown scrolls vertically when your app’s content is taller than the height of the display.

**Use tab views to provide page-by-page scrolling.** watchOS displays tab views as pages. If you place tab views in a vertical stack, people can rotate the Digital Crown to move vertically through full-screen pages of content. In this scenario, the system displays a page indicator next to the Digital Crown that shows people where they are in the content, both within the current page and within a set of pages. For guidance, see [Tab views](https://developer.apple.com/design/human-interface-guidelines/tab-views).

**When displaying paged content, consider limiting the content of an individual page to a single screen height.** Embracing this constraint clarifies the purpose of each page, helping you create a more glanceable design. However, if your app has long pages, people can still use the Digital Crown both to navigate between shorter pages and to scroll content in a longer page because the page indicator expands into a scroll indicator when necessary. Use variable-height pages judiciously and place them after fixed-height pages when possible.

### Search fields
<sub>`pages/search-fields.md`</sub>

When someone taps the search field, the system displays a text-input control that covers the entire screen. The app only returns to the search field after they tap the Cancel or Search button.

### Settings
<sub>`pages/settings.md`</sub>

In watchOS, apps and games don’t add custom settings to the system-provided Settings app. As an alternative, consider making a small number of essential options available at the bottom of the main view or letting people use a More menu to reconfigure objects.

### Sheets
<sub>`pages/sheets.md`</sub>

In watchOS, a sheet is a full-screen view that slides over your app’s current content. The sheet is semitransparent to help maintain the current context, but the system applies a material to the background that blurs and desaturates the covered content.

![A screenshot of a sheet with a primary Action button and a default cancel button on Apple Watch.](/images/com.apple.HIG/sheets-watch-overlay@2x.png)

**Use a sheet only when your modal task requires a custom title or custom content presentation.** If you need to give people important information or present a set of choices, consider using an [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) or [Action sheets](https://developer.apple.com/design/human-interface-guidelines/action-sheets).

**Keep sheet interactions brief and occasional.** Use a sheet only as a temporary interruption to the current workflow, and only to facilitate an important task. Avoid using a sheet to help people navigate your app’s content.

**If you change the default label, prefer using SF Symbols to represent the action.** Avoid using a label that might mislead people into thinking that the sheet is part of a hierarchical navigation interface. Also, if the text in the top-leading corner looks like a page or app title, people won’t know how to dismiss the sheet. For guidance, see [Standard icons](https://developer.apple.com/design/human-interface-guidelines/icons#Standard-icons).

![A screenshot that shows a top toolbar with a custom Back button at the top of the screen on Apple Watch.](/images/com.apple.HIG/modal-sheet-watchos-do-not-1@2x.png)

![An X in a circle to indicate incorrect usage.](/images/com.apple.HIG/crossout@2x.png)

![A screenshot that shows a top toolbar with a button with the words Page title at the top of the screen on Apple Watch.](/images/com.apple.HIG/modal-sheet-watchos-do-not-2@2x.png)

![An X in a circle to indicate incorrect usage.](/images/com.apple.HIG/crossout@2x.png)

![A screenshot that shows a top toolbar with the default Cancel button at the top of the screen on Apple Watch.](/images/com.apple.HIG/modal-sheet-watchos-do@2x.png)

![A checkmark in a circle to indicate correct usage.](/images/com.apple.HIG/checkmark@2x.png)

### Sliders
<sub>`pages/sliders.md`</sub>

A slider is a horizontal track — appearing as a set of discrete steps or as a continuous bar — that represents a finite range of values. People can tap buttons on the sides of the slider to increase or decrease its value by a predefined amount.

![An illustration of a watchOS volume slider with discrete steps. The first two of three steps are filled with a green highlight color, indicating the volume level.](/images/com.apple.HIG/sliders-watchos-discrete@2x.png)

![An illustration of a watchOS volume slider with a continuous bar. Two-thirds of the bar is filled with a green highlight color, indicating the volume level.](/images/com.apple.HIG/sliders-watchos-continuous@2x.png)

**If necessary, create custom glyphs to communicate what the slider does.** The system displays plus and minus signs by default.

### Split views
<sub>`pages/split-views.md`</sub>

In watchOS, the split view displays either the list view or a detail view as a full-screen view.

**Automatically display the most relevant detail view.** When your app launches, show people the most pertinent information. For example, display information relevant to their location, the time, or their recent actions.

**If your app displays multiple detail pages, place the detail views in a vertical [Tab views](https://developer.apple.com/design/human-interface-guidelines/tab-views).** People can then use the Digital Crown to scroll between the detail view’s tabs. watchOS also displays a page indicator next to the Digital Crown, indicating the number of tabs and the currently selected tab.

![A screenshot showing a detail view with a vertical tab on Apple Watch. The page indicator next to the Digital Crown shows that the fifth tab is currently selected.](/images/com.apple.HIG/split-view-watch-vertical-tab@2x.png)

### Tab views
<sub>`pages/tab-views.md`</sub>

watchOS displays tab views using [page controls](https://developer.apple.com/design/human-interface-guidelines/components/presentation/page-controls). For developer guidance, see [TabView](https://developer.apple.com/documentation/swiftui/tabview).

![An illustration showing the page control next to the Digital Crown on Apple Watch. The current dot is enlarged, indicating that people can scroll through the current content, as well as scroll between pages.](/images/com.apple.HIG/tab-view-watch-vertical@2x.png)

### Text fields
<sub>`pages/text-fields.md`</sub>

**Present a text field only when necessary.** Whenever possible, prefer displaying a list of options rather than requiring text entry.

### Toolbars
<sub>`pages/toolbars.md`</sub>

A toolbar button lets you offer important app functionality in a view that displays related content. You can place toolbar buttons in the top corners or along the bottom. If you place these buttons above scrolling content, the buttons always remain visible, as the content scrolls under them.

![A screenshot showing toolbar buttons in the top leading and trailing corners.](/images/com.apple.HIG/toolbars-watch-top-buttons@2x.png)

![A screenshot showing two toolbar buttons in the bottom leading and trailing corners.](/images/com.apple.HIG/toolbars-watch-bottom-buttons@2x.png)

For developer guidance, see [topBarLeading](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/topbarleading), [topBarTrailing](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/topbartrailing), or [bottomBar](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/bottombar).

You can also place a button in the scrolling view. By default, a scrolling toolbar button remains hidden until people reveal it by scrolling up. People frequently scroll to the top of a scrolling view, so discovering a toolbar button is automatic.

![A screenshot showing two toolbar buttons in the top leading and trailing corners. The toolbar also has a primary action button in the scroll view, but it's hidden.](/images/com.apple.HIG/toolbars-watch-primary-button-hidden@2x.png)

![A screenshot showing two toolbar buttons in the top leading and trailing corners. The toolbar also displays a primary action button in the scroll view.](/images/com.apple.HIG/toolbars-watch-primary-button-visible@2x.png)

For developer guidance, see [primaryAction](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/primaryaction).

**Use a scrolling toolbar button for an important action that isn’t a primary app function.** A toolbar button gives you the flexibility to offer important functionality in a view whose primary purpose is related to that functionality, but may not be the same. For example, Mail provides the essential New Message action in a toolbar button at the top of the Inbox view. The primary purpose of the Inbox is to display a scrollable list of email messages, so it makes sense to offer the closely related compose action in a toolbar button at the top of the view.

### Typography
<sub>`pages/typography.md`</sub>

SF Compact is the system font in watchOS, and apps can also use NY. In complications, watchOS uses SF Compact Rounded.

### Virtual keyboards
<sub>`pages/virtual-keyboards.md`</sub>

On Apple Watch, a text field can show a keyboard if the device screen is large enough. Otherwise, the system lets people use dictation or Scribble to enter information. You can’t change the keyboard type in watchOS, but you can set the content type of the text field. The system uses this information to make text entry easier, such as by offering suggestions. For developer guidance, see [textContentType(_:)](https://developer.apple.com/documentation/swiftui/view/textcontenttype(_:)) (SwiftUI).

People can also use a nearby paired iPhone to enter text on Apple Watch.

### Wallet
<sub>`pages/wallet.md`</sub>

On Apple Watch, Wallet displays passes in a scrolling carousel of cards. People can add your pass to their Apple Watch even if you don’t create a watch-specific app, so it’s important to understand how your pass can look on the device.

![A screenshot of a selected flight pass in a list of passes on Apple Watch. The pass includes information about a flight from SFO to LGA. The next pass in the list is a gym membership card with a barcode.](/images/com.apple.HIG/watch-card-and-details@2x.png)

People can tap a pass on their Apple Watch to reveal a details screen that displays additional information in a scroll view. In some cases, people can also tap a specific transaction to get more information.

![A screenshot of a flight pass on Apple Watch. The pass includes information about a flight from SFO to LGA, and appears above a QR code.](/images/com.apple.HIG/watch-pass-design-intro@2x.png)

Each pass style specifies the fields and images that can appear in the basic layout areas shown below:

![A diagram that shows the basic layout of a pass on Apple Watch. A top row contains a logo image and an essential field area. A second row contains a primary field area. A third row contains a secondary and auxiliary fields area.](/images/com.apple.HIG/watch-layout-diagram@2x.png)

If some information doesn’t fit within the layout areas, the system displays it in the scrolling details screen.

> **Important:** In every style, watchOS crops the strip image to fit the aspect ratio of the card interface and may crop white space from other images.

**Boarding**

![A diagram that shows the layout of a boarding pass on Apple Watch. The first row contains a logo image and departure or boarding time information. The second row contains origin and destination information. The third row contains the passenger name and seat.](/images/com.apple.HIG/watch-layout-boarding-pass@2x.png)

**Coupon**

![A diagram that shows the layout of a coupon pass on Apple Watch. The first row contains a logo image and expiration date. The second row contains a strip image. The third row is unused.](/images/com.apple.HIG/watch-layout-coupon@2x.png)

**Store**

![A diagram that shows the layout of a store card on Apple Watch. The top first row contains a logo image and an unused area. The second row contains a strip image. The third row contains a member name and number.](/images/com.apple.HIG/watch-layout-store-card@2x.png)

**Event**

![A diagram that shows the layout of an event ticket on Apple Watch. The first row contains a logo image and an event start date. The second row contains information about the event. The third row contains an attendee name and seat location.](/images/com.apple.HIG/watch-layout-event-ticket@2x.png)

**Generic**

![A diagram that shows the layout of a generic pass on Apple Watch. The first row contains a logo image and an expiration date. The second row contains a strip image. The third row contains a name and number.](/images/com.apple.HIG/watch-layout-generic-pass@2x.png)

### Widgets
<sub>`pages/widgets.md`</sub>

**Provide a colorful background that conveys meaning.** By default, widgets in the Smart Stack use a black background. Consider using a custom background color that provides additional meaning. For example, the Stocks app uses a red background for falling stock values and a green background if a stock’s value rises.

**Encourage the system to display or elevate the position of your watchOS widget in the Smart Stack.** Relevancy information helps the system show your widget when people need it most. Relevance can be location-based or specific to ongoing system actions, like a workout. For developer guidance, see [RelevanceKit](https://developer.apple.com/documentation/relevancekit).
