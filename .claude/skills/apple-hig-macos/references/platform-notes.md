# macOS-specific guidance, collected

Every place the HIG states a rule specific to macOS, lifted from the page it lives on. Sections appear alphabetically by page.

A heading like `### macOS, iPadOS` upstream means the rule is shared; it's reproduced here in full so you don't have to go looking. Each entry links to the complete page, which also carries the cross-platform guidance this file deliberately omits.

---

## Alerts

Full page: `references/alerts.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/alerts

macOS automatically displays your app icon in an alert, but you can supply an alternative icon or symbol. In addition, macOS lets you:

- Configure repeating alerts to let people suppress subsequent occurrences of the same alert.
- Append a custom view if it’s necessary to provide additional information (for developer guidance, see [accessoryView](https://developer.apple.com/documentation/AppKit/NSAlert/accessoryView)).
- Include a Help button that opens your help documentation (see [Help buttons](https://developer.apple.com/design/human-interface-guidelines/buttons#Help-buttons)).

**Use a caution symbol sparingly.** Using a caution symbol like `exclamationmark.triangle` too frequently in your alerts diminishes its significance. Use the symbol only when extra attention is really needed, as when confirming an action that might result in unexpected loss of data. Don’t use the symbol for tasks whose only purpose is to overwrite or remove data, such as a save or empty trash.

---

## App Shortcuts

Full page: `references/app-shortcuts.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/app-shortcuts

App Shortcuts aren’t supported in macOS. However, actions you create for your app using App Intents are supported, and people can build custom shortcuts using them with the Shortcuts app on Mac.

---

## Boxes

Full page: `references/boxes.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/boxes

By default, macOS displays a box’s title above it.

---

## Buttons

Full page: `references/buttons.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/buttons

Several specific button types are unique to macOS.

#### Push buttons

The standard button type in macOS is known as a *push button*. You can configure a push button to display text, a symbol, an icon, or an image, or a combination of text and image content. Push buttons can act as the default button in a view and you can tint them.

**Use a flexible-height push button only when you need to display tall or variable height content.** Flexible-height buttons support the same configurations as regular push buttons — and they use the same corner radius and content padding — so they look consistent with other buttons in your interface. If you need to present a button that contains two lines of text or a tall icon, use a flexible-height button; otherwise, use a standard push button. For developer guidance, see [NSButton.BezelStyle.flexiblePush](https://developer.apple.com/documentation/AppKit/NSButton/BezelStyle-swift.enum/flexiblePush).

**Append a trailing ellipsis to the title when a push button opens another window, view, or app.** Throughout the system, an ellipsis in a control title signals that people can provide additional input. For example, the Edit buttons in the AutoFill pane of Safari Settings include ellipses because they open other views that let people modify autofill values.

**Consider supporting spring loading.** On systems with a Magic Trackpad, *spring loading* lets people activate a button by dragging selected items over it and force clicking — that is, pressing harder — without dropping the selected items. After force clicking, people can continue dragging the items, possibly to perform additional actions.

#### Square buttons

A *square button* (also known as a *gradient button*) initiates an action related to a view, like adding or removing rows in a table.

Square buttons contain symbols or icons — not text — and you can configure them to behave like push buttons, toggles, or pop-up buttons. The buttons appear in close proximity to their associated view — usually within or beneath it — so people know which view the buttons affect.

**Use square buttons in a view, not in the window frame.** Square buttons aren’t intended for use in toolbars or status bars. If you need a button in a [toolbar](https://developer.apple.com/design/human-interface-guidelines/toolbars), use a toolbar item.

**Prefer using a symbol in a square button.** [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) provides a wide range of symbols that automatically receive appropriate coloring in their default state and in response to user interaction.

**Avoid using labels to introduce square buttons.** Because square buttons are closely connected with a specific view, their purpose is generally clear without the need for descriptive text.

For developer guidance, see [NSButton.BezelStyle.smallSquare](https://developer.apple.com/documentation/AppKit/NSButton/BezelStyle-swift.enum/smallSquare).

#### Help buttons

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

#### Image buttons

An *image button* appears in a view and displays an image, symbol, or icon. You can configure an image button to behave like a push button, toggle, or pop-up button.

**Use an image button in a view, not in the window frame.** For example, avoid placing an image button in a toolbar or status bar. If you need to use an image as a button in a toolbar, use a toolbar item. See [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars).

**Include about 10 pixels of padding between the edges of the image and the button edges.** An image button’s edges define its clickable area even when they aren’t visible. Including padding ensures that a click registers correctly even if it’s not precisely within the image. In general, avoid including a system-provided border in an image button; for developer guidance, see [isBordered](https://developer.apple.com/documentation/AppKit/NSButton/isBordered).

**If you need to include a label, position it below the image button.** For related guidance, see [Labels](https://developer.apple.com/design/human-interface-guidelines/labels).

---

## Color

Full page: `references/color.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/color

macOS defines the following dynamic system colors (you can also view them in the Developer palette of the standard Color panel):

| Color | Use for… | AppKit API |
| --- | --- | --- |
| Alternate selected control text color | The text on a selected surface in a list or table. | [alternateSelectedControlTextColor](https://developer.apple.com/documentation/AppKit/NSColor/alternateSelectedControlTextColor) |
| Alternating content background colors | The backgrounds of alternating rows or columns in a list, table, or collection view. | [alternatingContentBackgroundColors](https://developer.apple.com/documentation/AppKit/NSColor/alternatingContentBackgroundColors) |
| Control accent | The accent color people select in System Settings. | [controlAccentColor](https://developer.apple.com/documentation/AppKit/NSColor/controlAccentColor) |
| Control background color | The background of a large interface element, such as a browser or table. | [controlBackgroundColor](https://developer.apple.com/documentation/AppKit/NSColor/controlBackgroundColor) |
| Control color | The surface of a control. | [controlColor](https://developer.apple.com/documentation/AppKit/NSColor/controlColor) |
| Control text color | The text of a control that is available. | [controlTextColor](https://developer.apple.com/documentation/AppKit/NSColor/controlTextColor) |
| Current control tint | The system-defined control tint. | [currentControlTint](https://developer.apple.com/documentation/AppKit/NSColor/currentControlTint) |
| Unavailable control text color | The text of a control that’s unavailable. | [disabledControlTextColor](https://developer.apple.com/documentation/AppKit/NSColor/disabledControlTextColor) |
| Find highlight color | The color of a find indicator. | [findHighlightColor](https://developer.apple.com/documentation/AppKit/NSColor/findHighlightColor) |
| Grid color | The gridlines of an interface element, such as a table. | [gridColor](https://developer.apple.com/documentation/AppKit/NSColor/gridColor) |
| Header text color | The text of a header cell in a table. | [headerTextColor](https://developer.apple.com/documentation/AppKit/NSColor/headerTextColor) |
| Highlight color | The virtual light source onscreen. | [highlightColor](https://developer.apple.com/documentation/AppKit/NSColor/highlightColor) |
| Keyboard focus indicator color | The ring that appears around the currently focused control when using the keyboard for interface navigation. | [keyboardFocusIndicatorColor](https://developer.apple.com/documentation/AppKit/NSColor/keyboardFocusIndicatorColor) |
| Label color | The text of a label containing primary content. | [labelColor](https://developer.apple.com/documentation/AppKit/NSColor/labelColor) |
| Link color | A link to other content. | [linkColor](https://developer.apple.com/documentation/AppKit/NSColor/linkColor) |
| Placeholder text color | A placeholder string in a control or text view. | [placeholderTextColor](https://developer.apple.com/documentation/AppKit/NSColor/placeholderTextColor) |
| Quaternary label color | The text of a label of lesser importance than a tertiary label, such as watermark text. | [quaternaryLabelColor](https://developer.apple.com/documentation/AppKit/NSColor/quaternaryLabelColor) |
| Secondary label color | The text of a label of lesser importance than a primary label, such as a label used to represent a subheading or additional information. | [secondaryLabelColor](https://developer.apple.com/documentation/AppKit/NSColor/secondaryLabelColor) |
| Selected content background color | The background for selected content in a key window or view. | [selectedContentBackgroundColor](https://developer.apple.com/documentation/AppKit/NSColor/selectedContentBackgroundColor) |
| Selected control color | The surface of a selected control. | [selectedControlColor](https://developer.apple.com/documentation/AppKit/NSColor/selectedControlColor) |
| Selected control text color | The text of a selected control. | [selectedControlTextColor](https://developer.apple.com/documentation/AppKit/NSColor/selectedControlTextColor) |
| Selected menu item text color | The text of a selected menu. | [selectedMenuItemTextColor](https://developer.apple.com/documentation/AppKit/NSColor/selectedMenuItemTextColor) |
| Selected text background color | The background of selected text. | [selectedTextBackgroundColor](https://developer.apple.com/documentation/AppKit/NSColor/selectedTextBackgroundColor) |
| Selected text color | The color for selected text. | [selectedTextColor](https://developer.apple.com/documentation/AppKit/NSColor/selectedTextColor) |
| Separator color | A separator between different sections of content. | [separatorColor](https://developer.apple.com/documentation/AppKit/NSColor/separatorColor) |
| Shadow color | The virtual shadow cast by a raised object onscreen. | [shadowColor](https://developer.apple.com/documentation/AppKit/NSColor/shadowColor) |
| Tertiary label color | The text of a label of lesser importance than a secondary label. | [tertiaryLabelColor](https://developer.apple.com/documentation/AppKit/NSColor/tertiaryLabelColor) |
| Text background color | The background color behind text. | [textBackgroundColor](https://developer.apple.com/documentation/AppKit/NSColor/textBackgroundColor) |
| Text color | The text in a document. | [textColor](https://developer.apple.com/documentation/AppKit/NSColor/textColor) |
| Under page background color | The background behind a document’s content. | [underPageBackgroundColor](https://developer.apple.com/documentation/AppKit/NSColor/underPageBackgroundColor) |
| Unemphasized selected content background color | The selected content in a non-key window or view. | [unemphasizedSelectedContentBackgroundColor](https://developer.apple.com/documentation/AppKit/NSColor/unemphasizedSelectedContentBackgroundColor) |
| Unemphasized selected text background color | A background for selected text in a non-key window or view. | [unemphasizedSelectedTextBackgroundColor](https://developer.apple.com/documentation/AppKit/NSColor/unemphasizedSelectedTextBackgroundColor) |
| Unemphasized selected text color | Selected text in a non-key window or view. | [unemphasizedSelectedTextColor](https://developer.apple.com/documentation/AppKit/NSColor/unemphasizedSelectedTextColor) |
| Window background color | The background of a window. | [windowBackgroundColor](https://developer.apple.com/documentation/AppKit/NSColor/windowBackgroundColor) |
| Window frame text color | The text in the window’s title bar area. | [windowFrameTextColor](https://developer.apple.com/documentation/AppKit/NSColor/windowFrameTextColor) |

#### App accent colors

Beginning in macOS 11, you can specify an *accent color* to customize the appearance of your app’s buttons, selection highlighting, and sidebar icons. The system applies your accent color when the current value in General > Accent color settings is *multicolor*.

![A screenshot of the accent color picker in the System Settings app.](https://docs-assets.developer.apple.com/published/93ebe4b08af4e94a5c4479459fc7905b/colors-accent-colors-picker-multicolor%402x.png)

If people set their accent color setting to a value other than multicolor, the system applies their chosen color to the relevant items throughout your app, replacing your accent color. The exception is a sidebar icon that uses a fixed color you specify. Because a fixed-color sidebar icon uses a specific color to provide meaning, the system doesn’t override its color when people change the value of accent color settings. For guidance, see [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars).

---

## Color wells

Full page: `references/color-wells.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/color-wells

When people click a color well, it receives a highlight to provide visual confirmation that it’s active. It then opens a color picker so people can choose a color. After they make a selection, the color well updates to show the new color.

Color wells also support drag and drop, so people can drag colors from one color well to another, and from the color picker to a color well.

---

## Context menus

Full page: `references/context-menus.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/context-menus

On a Mac, a context menu is sometimes called a *contextual* menu.

---

## Dark Mode

Full page: `references/dark-mode.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/dark-mode

When people choose the graphite accent color in General settings, macOS causes window backgrounds to pick up color from the current desktop picture. The result — called *desktop tinting* — is a subtle effect that helps windows blend more harmoniously with their surrounding content.

**Include some transparency in custom component backgrounds when appropriate.** Transparency lets your components pick up color from the window background when desktop tinting is active, creating a visual harmony that can persist even when the desktop picture changes. To help achieve this harmony, add transparency only to a custom component that has a visible background or bezel, and only when the component is in a neutral state, such as state that doesn’t use color. You don’t want to add transparency when the component is in a state that uses color, because doing so can cause the component’s color to fluctuate when the window background adjusts to a different location on the desktop or when the desktop picture changes.

---

## Drag and drop

Full page: `references/drag-and-drop.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/drag-and-drop

**Consider letting people drag content from your app into the Finder.** When you support this, be sure to present the content in a format your app can open later. For example, Calendar lets people drag an event to the Finder as a `.ics` file. People can share this file with others or drag it back to Calendar to open it. When necessary, you can output dragged content in a *clipping*, which is a temporary container for storing dragged content. For example, most system apps let people drag text to the Finder, where it appears as a clipping. Later, people can drag the clipping into a text field or other location that accepts text. Note that a drag-and-drop clipping isn’t related to the Clipboard.

**Let people drag selected content from an inactive window without first making the window active.** Selected content in an inactive window is known as a *background selection* and has a different appearance from selected content in the active window. In general, people expect to drag a background selection to the active window without bringing the inactive window forward.

**When possible, let people drag individual items from an inactive window without affecting an existing background selection.** For example, people can drag an unselected file from an inactive Finder window without deselecting any of the window’s selected files.

**Consider displaying a badge during multi-item drag operations.** A badge is a small filled oval containing a number you can use to indicate the number of items people are dragging. If a destination can accept only a subset of dragged items, update the badge to show the new number.

**Consider changing the pointer appearance to indicate what will happen when people drop content.** In addition to using the *copy* pointer, you might want to use the *drag link*, *disappearing item*, and *operation not allowed* pointers, depending on the situation. For guidance, see [Pointers](https://developer.apple.com/design/human-interface-guidelines/pointing-devices#Pointers).

**As much as possible, let people select and drag content with a single motion.** Unless people are selecting multiple items, they appreciate it when they don’t have to pause between making a selection and starting the drag operation.

---

## Edit menus

Full page: `references/edit-menus.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/edit-menus

To learn about the order of items in a macOS app’s Edit menu, see [Edit menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Edit-menu).

---

## Entering data

Full page: `references/entering-data.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/entering-data

**Consider using an expansion tooltip to show the full version of clipped or truncated text in a field.** An *expansion tooltip* behaves like a regular tooltip, appearing when the pointer rests on top of a field. Apps running in macOS — including iOS and iPadOS apps running on a Mac — can use an expansion tooltip to help people view the complete data they entered when a text field is too small to display it. For guidance, see [Offering help > macOS, visionOS](https://developer.apple.com/design/human-interface-guidelines/offering-help#macOS-visionOS).

---

## File management

Full page: `references/file-management.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/file-management

#### Custom file management

People have strong associations with the familiar file browsing experience of the Finder and most document-based apps. Use the default file browser unless you have an important reason to create a custom one.

**Make your custom file-opening interface convenient.** For example, people might appreciate an “open recent” action in addition to the simple “open” action. You might also want to let people choose criteria on which to filter the file-browsing experience, or select multiple documents to open at once. In a macOS open panel, you can customize the title of the Open button to reflect the task — for example, if your app lets people insert a file’s contents into the current document, you might change the title to Insert.

**Provide a save interface to let people change a file’s name, format, or location.** By default, a new document’s title is “Untitled” until people choose a custom name. As with a document-opening interface, a save view can also provide a browsing experience that defaults to a logical location to help people place the saved document where they want. If you support saving content in different formats, also give people a way to choose a specific file format.

**Consider extending the functionality of the Save dialog.** If it makes sense in your app, you can add a custom accessory view containing useful settings or options to the Save dialog. For example, the dialog for saving Mail messages as files contains an option to include attachments.

#### Finder Sync extensions

If your app syncs local and remote files, you can create a Finder Sync app extension to express file synchronization status and control within the Finder. For developer guidance, see [Finder Sync](https://developer.apple.com/documentation/FinderSync).

For example, you can use a Finder Sync extension to:

- Display badges in the Finder to indicate the sync status of items
- Provide custom contextual menu items that perform file and folder management tasks, like favoriting and adding password-protection
- Provide custom toolbar buttons that perform global actions, like initiating a sync operation

**Help people avoid losing work if they turn off autosaving.** People can turn off autosaving by selecting the “Ask to keep changes when closing documents” toggle in Desktop & Dock settings. In this scenario, show that a document has unsaved changes and present a save dialog when people choose to close the document, quit your app, log out, or restart.

**When autosaving is off, make sure people know when a document has unsaved changes.** To show that there are unsaved changes, display a dot on the document window’s close button and next to the document’s name in your app’s Window menu. When autosaving is on, showing a dot in these locations is confusing, because it implies that people need to take action to avoid losing their work. Regardless of autosave status, you can append “Edited” to the document’s title in the title bar, but be sure to remove this suffix as soon as autosave occurs or when people explicitly save their work.

---

## Gauges

Full page: `references/gauges.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/gauges

In addition to supporting gauges, macOS also defines a level indicator that displays a specific numerical value within a range. You can configure a level indicator to convey capacity, rating, or — rarely — relevance.

The capacity style can depict discrete or continuous values.

![An image of a continuous capacity indicator that uses the default green fill to indicate an amount of about two-thirds of the total capacity.](https://docs-assets.developer.apple.com/published/8d1f4b040b7736a1ba832b93a7dc3bfb/indicators-continuous%402x.png)

**Continuous.** A horizontal translucent track that fills with a solid bar to indicate the current value.

![An image of a discrete capacity indicator that uses the default green fill to indicate an amount of three-quarters of the total capacity.](https://docs-assets.developer.apple.com/published/f148e7934177391449aa61cc97ffea49/indicators-discrete%402x.png)

**Discrete.** A horizontal row of separate, equally sized, rectangular segments. The number of segments matches the total capacity, and the segments fill completely — never partially — with color to indicate the current value.

**Consider using the continuous style for large ranges.** A large value range can make the segments of a discrete capacity indicator too small to be useful.

**Consider changing the fill color to inform people about significant parts of the range.** By default, the fill color for both capacity indicator styles is green. If it makes sense in your app, you can change the fill color when the current value reaches certain levels, such as very low, very high, or just past the middle. You can change the fill color of the entire indicator or you can use the tiered state to show a sequence of several colors in one indicator, as shown below.

![An image of a continuous capacity indicator in which the leftmost one-eigth is red, the next three-eighths are yellow, the next one-fourth is green, and the last one-fourth is unfilled.](https://docs-assets.developer.apple.com/published/6d84b116ed12ffcabc2a36fb8f63e31e/indicators-continuous-tiered%402x.png)

For guidance using the rating style to help people rank something, see [Rating indicators](https://developer.apple.com/design/human-interface-guidelines/rating-indicators).

Although rarely used, the relevance style can communicate relevancy using a shaded horizontal bar. For example, a relevance indicator might appear in a list of search results, helping people visualize the relevancy of the results when sorting or comparing multiple items.

---

## Gestures

Full page: `references/gestures.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/gestures

People primarily interact with macOS using a [Keyboards](https://developer.apple.com/design/human-interface-guidelines/keyboards) and mouse. In addition, they can make [Standard gestures](https://developer.apple.com/design/human-interface-guidelines/gestures#Standard-gestures) on a Magic Trackpad, Magic Mouse, or a [Game controls](https://developer.apple.com/design/human-interface-guidelines/game-controls) that includes a touch surface.

---

## Going full screen

Full page: `references/going-full-screen.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/going-full-screen

**Use the system-provided full-screen experience.** Using the system’s full-screen support ensures that your full-screen window works well in all contexts. For example, some Mac models include a camera housing that occupies an area at the top-center of the screen. Using the system’s full-screen support automatically accommodates this area. For developer guidance, see [toggleFullScreen(_:)](https://developer.apple.com/documentation/AppKit/NSWindow/toggleFullScreen(_:)).

**In a game, don’t change the display mode when players go full screen.** People expect to be in control of their display mode, and changing it automatically doesn’t improve performance.

For additional developer guidance, see [Managing your game window for Metal in macOS](https://developer.apple.com/documentation/Metal/managing-your-game-window-for-metal-in-macos).

**Always let people choose when to enter full-screen mode.** Prefer letting people use your window’s Enter Full Screen button, View menu item, or the Control-Command-F keyboard shortcut. Avoid offering a custom menu of window modes. In a game, you might also provide a custom [toggle](https://developer.apple.com/design/human-interface-guidelines/toggles) that turns full-screen mode on and off.

---

## Icons

Full page: `references/icons.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/icons

#### Document icons

If your macOS app can use a custom document type, you can create a document icon to represent it. Traditionally, a document icon looks like a piece of paper with its top-right corner folded down. This distinctive appearance helps people distinguish documents from apps and other content, even when icon sizes are small.

If you don’t supply a document icon for a file type you support, macOS creates one for you by compositing your app icon and the file’s extension onto the canvas. For example, Preview uses a system-generated document icon to represent JPG files.

![An image of the Preview document icon for a JPG file.](https://docs-assets.developer.apple.com/published/b290daefbf64098b16ded1f6542fc0b9/doc-icon-generated%402x.png)

In some cases, it can make sense to create a set of document icons to represent a range of file types your app handles. For example, Xcode uses custom document icons to help people distinguish projects, AR objects, and Swift code files.

![Image of an Xcode project document icon.](https://docs-assets.developer.apple.com/published/13dfa9f3cb0738af049255b084cd4ba4/doc-icon-custom-1%402x.png)

![Image of a document icon for an AR object.](https://docs-assets.developer.apple.com/published/856cab730b694bb196bada2588842ab8/doc-icon-custom-2%402x.png)

![Image of a document icon for a Swift file.](https://docs-assets.developer.apple.com/published/3994c93c362ba70063c98f5aea90ffda/doc-icon-custom-3%402x.png)

To create a custom document icon, you can supply any combination of background fill, center image, and text. The system layers, positions, and masks these elements as needed and composites them onto the familiar folded-corner icon shape.

![A square canvas that contains a grid of pink lines and a jagged white EKG line that runs horizontally across the middle. The pink grid gets lighter in color toward the bottom edge.](https://docs-assets.developer.apple.com/published/2aed446834a2dc6e8275b6bd7a797ca9/doc-icon-parts-background-fill%402x.png)

![A solid pink heart.](https://docs-assets.developer.apple.com/published/b59c836903d1b409ab9e21f81762df3e/doc-icon-parts-center-image%402x.png)

![The word heart in all caps.](https://docs-assets.developer.apple.com/published/0e1dd539ad0328be72dc1b9719842d84/doc-icon-parts-text%402x.png)

![A custom document icon that displays the pink heart and the word heart on top of the pink grid and white EKG line.](https://docs-assets.developer.apple.com/published/e6e553f1633a6b373bff40e615ba229e/doc-icon-parts%402x.png)

[Apple Design Resources](https://developer.apple.com/design/resources/#macos-apps) provides a template you can use to create a custom background fill and center image for a document icon. As you use this template, follow the guidelines below.

**Design simple images that clearly communicate the document type.** Whether you use a background fill, a center image, or both, prefer uncomplicated shapes and a reduced palette of distinct colors. Your document icon can display as small as 16x16 px, so you want to create designs that remain recognizable at every size.

**Designing a single, expressive image for the background fill can be a great way to help people understand and recognize a document type.** For example, Xcode and TextEdit both use rich background images that don’t include a center image.

![Image of an Xcode project document icon.](https://docs-assets.developer.apple.com/published/13dfa9f3cb0738af049255b084cd4ba4/doc-icon-custom-1%402x.png)

![Image of a TextEdit rich text document icon.](https://docs-assets.developer.apple.com/published/6b12fe092fe0e9f81377c30b896a3933/doc-icon-fill-only%402x.png)

**Consider reducing complexity in the small versions of your document icon.** Icon details that are clear in large versions can look blurry and be hard to recognize in small versions. For example, to ensure that the grid lines in the custom heart document icon remain clear in intermediate sizes, you might use fewer lines and thicken them by aligning them to the reduced pixel grid. In the 16x16 px size, you might remove the lines altogether.

![Pixelated image of the heart document icon. The grid, the EKG line, the heart shape, and the word heart are visible but blurry.](https://docs-assets.developer.apple.com/published/1f8bc7946a75363224f373924b557a3a/doc-icon-fewer-details-1%402x.png)

![Pixelated image of the heart document icon, in which only the blurry heart shape and EKG line are visible.](https://docs-assets.developer.apple.com/published/e46ac887801d9a16393948c3f2098715/doc-icon-fewer-details-2%402x.png)

![Pixelated image of the heart document icon, in which only the blurry heart shape is visible.](https://docs-assets.developer.apple.com/published/fd0d2afcd76a9b25c1217ef2ffb1ad0e/doc-icon-fewer-details-3%402x.png)

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

![Diagram of the solid pink heart shape within blue margins that measure 10 percent of the canvas width.](https://docs-assets.developer.apple.com/published/948d6a9f01550fa7701023a69c016049/doc-icon-parts-margins%402x.png)

**Specify a succinct term if it helps people understand your document type.** By default, the system displays a document’s extension at the bottom edge of the document icon, but if the extension is unfamiliar you can supply a more descriptive term. For example, the document icon for a SceneKit scene file uses the term *scene* instead of the file extension *scn*. The system automatically scales the extension text to fit in the document icon, so be sure to use a term that’s short enough to be legible at small sizes. By default, the system capitalizes every letter in the text.

![Image of a SceneKit scene document icon.](https://docs-assets.developer.apple.com/published/bec2eab10b4adb39f67071411e446d29/doc-icon-custom-extension%402x.png)

---

## Image views

Full page: `references/image-views.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/image-views

**If your app needs an editable image view, use an image well.** An [image well](https://developer.apple.com/design/human-interface-guidelines/image-wells) is an image view that supports copying, pasting, dragging, and using the Delete key to clear its content.

**Use an image button instead of an image view to make a clickable image.** An [image button](https://developer.apple.com/design/human-interface-guidelines/buttons#Image-buttons) contains an image or icon, appears in a view, and initiates an instantaneous app-specific action.

---

## Labels

Full page: `references/labels.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/labels

> **Note:** To display uneditable text in a label, use the [isEditable](https://developer.apple.com/documentation/AppKit/NSTextField/isEditable) property of [NSTextField](https://developer.apple.com/documentation/AppKit/NSTextField).

---

## Layout

Full page: `references/layout.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/layout

**Avoid placing controls or critical information at the bottom of a window.** People often move windows so that the bottom edge is below the bottom of the screen.

**Avoid displaying content within the camera housing at the top edge of the window.** For developer guidance, see [NSPrefersDisplaySafeAreaCompatibilityMode](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSPrefersDisplaySafeAreaCompatibilityMode).

---

## Lists and tables

Full page: `references/lists-and-tables.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/lists-and-tables

**When it provides value, let people click a column heading to sort a table view based on that column**. If people click the heading of a column that’s already sorted, re-sort the data in the opposite direction.

**Let people resize columns.** Data displayed in a table view often varies in width. People appreciate resizing columns to help them concentrate on different areas or reveal clipped data.

**Consider using alternating row colors in a multicolumn table.** Alternating colors can help people track row values across columns, especially in a wide table.

**Use an outline view instead of a table view to present hierarchical data.** An [outline view](https://developer.apple.com/design/human-interface-guidelines/outline-views) looks like a table view, but includes disclosure triangles for exposing nested levels of data. For example, an outline view might display folders and the items they contain.

---

## Live Activities

Full page: `references/live-activities.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/live-activities

Active Live Activities automatically appear in the Menu bar of a paired Mac using the compact, minimal, and expanded presentations. Clicking the Live Activity launches iPhone Mirroring to display your app.

---

## Materials

Full page: `references/materials.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/materials

macOS provides several standard materials with designated purposes, and vibrant versions of all [Specifications](https://developer.apple.com/design/human-interface-guidelines/color#Specifications). For developer guidance, see [NSVisualEffectView.Material](https://developer.apple.com/documentation/AppKit/NSVisualEffectView/Material-swift.enum).

**Choose when to allow vibrancy in custom views and controls.** Depending on configuration and system settings, system views and controls use vibrancy to make foreground content stand out against any background. Test your interface in a variety of contexts to discover when vibrancy enhances the appearance and improves communication.

**Choose a background blending mode that complements your interface design.** macOS defines two modes that blend background content: behind window and within window. For developer guidance, see [NSVisualEffectView.BlendingMode](https://developer.apple.com/documentation/AppKit/NSVisualEffectView/BlendingMode-swift.enum).

---

## Multitasking

Full page: `references/multitasking.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/multitasking

On Mac, multitasking is the default experience because people typically run more than one app at a time, switching between windows and tasks as they work. When multiple app windows are open, macOS applies drop shadows that make the windows appear layered on the desktop, and applies other visual effects to help people distinguish different window states; for guidance, see [macOS window states](https://developer.apple.com/design/human-interface-guidelines/windows#macOS-window-states).

---

## Offering help

Full page: `references/offering-help.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/offering-help

*(upstream heading: macOS, visionOS)*

A *tooltip* (called a *help tag* in user documentation) displays a small, transient view that briefly describes how to use a component in the interface. In apps that run on a Mac — including iPhone and iPad apps — tooltips can appear when a person holds the pointer over an element; in visionOS apps, a tooltip can appear when a person looks at an element or holds the pointer over it. For developer guidance, see [help(_:)](https://developer.apple.com/documentation/SwiftUI/View/help(_:)-6oiyb).

![An illustration of a toolbar in macOS Finder with the pointer over the Back button. A tooltip with the title See folders you viewed previously appears beneath the pointer.](https://docs-assets.developer.apple.com/published/73b93ef4399648628ff79fab1ea92208/offering-help-macos-tooltip-help-tag%402x.png)

**Describe only the control that people indicate interest in.** When people want to know how to use a specific control, they don’t want to learn how to use nearby controls or how to perform a larger task.

**Explain the action or task the control initiates.** It often works well to begin the description with a verb — for example, “Restore default settings” or “Add or remove a language from the list.”

**In general, avoid repeating a control’s name in its tooltip.** Repeating the name takes up space in the tooltip and rarely adds value to the description.

**Be brief.** As much as possible, limit tooltip content to a maximum of 60 to 75 characters (note that localization often changes the length of text). To make a description brief and direct, consider using a sentence fragment and omitting articles. If you need a lot of text to describe a control, consider simplifying your interface design.

**Use sentence case.** Sentence case tends to appear more casual and approachable. If you write complete sentences, omit ending punctuation unless it’s required to be consistent with your app’s style.

**Consider offering context-sensitive tooltips.** For example, you could provide different text for a control’s different states.

---

## Pickers

Full page: `references/pickers.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/pickers

**Choose a date picker style that suits your app.** There are two styles of date pickers in macOS: textual and graphical. The textual style is useful when you’re working with limited space and you expect people to make specific date and time selections. The graphical style is useful when you want to give people the option of browsing through days in a calendar or selecting a range of dates, or when the look of a clock face is appropriate for your app.

For developer guidance, see [NSDatePicker](https://developer.apple.com/documentation/AppKit/NSDatePicker).

---

## Playing audio

Full page: `references/playing-audio.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/playing-audio

In macOS, notification sounds mix with other audio by default.

---

## Playing haptics

Full page: `references/playing-haptics.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/playing-haptics

When a Magic Trackpad is available, your app can provide one of the three following haptic patterns in response to a drag operation or force click.

| Haptic feedback pattern | Description |
| --- | --- |
| Alignment | Indicates the alignment of a dragged item. For example, this pattern could be used in a drawing app when the people drag a shape into alignment with another shape. Other scenarios where this type of feedback could be used might include scaling an object to fit within specific dimensions, positioning an object at a preferred location, or reaching the beginning/end or minimum/maximum of something like a scrubber in a video app. |
| Level change | Indicates movement between discrete levels of pressure. For example, as people press a fast-forward button on a video player, playback could increase or decrease and haptic feedback could be provided as different levels of pressure are reached. |
| Generic | Intended for providing general feedback when the other patterns don’t apply. |

For developer guidance, see [NSHapticFeedbackPerformer](https://developer.apple.com/documentation/AppKit/NSHapticFeedbackPerformer).

---

## Pointing devices

Full page: `references/pointing-devices.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/pointing-devices

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

#### Pointers

macOS offers a variety of standard pointer styles, which your app can use to communicate the interactive state of an interface element or the result of a drag operation.

| Pointer | Name | Meaning | AppKit API |
| --- | --- | --- | --- |
| ![A pointer that resembles a diagonal arrow pointing up and to the left.](https://docs-assets.developer.apple.com/published/5be2c381c17d5d868866b3a5de1013f8/pointers-arrow%402x.png) | Arrow | Standard pointer for selecting and interacting with content and interface elements. | [arrow](https://developer.apple.com/documentation/AppKit/NSCursor/arrow) |
| ![A closed, gloved hand.](https://docs-assets.developer.apple.com/published/6680cdb870edf5364f84a483fd2bead9/pointers-closed-hand%402x.png) | Closed hand | Dragging to reposition the display of content within a view—for example, dragging a map around in Maps. | [closedHand](https://developer.apple.com/documentation/AppKit/NSCursor/closedHand) |
| ![A pointer arrow with a small menu-like square to the right of the arrow.](https://docs-assets.developer.apple.com/published/0cb033cee3b55bd4be661b28b928fdc1/pointers-contextual-menu%402x.png) | Contextual menu | A contextual menu is available for the content below the pointer. This pointer is generally shown only when the Control key is pressed. | [contextualMenu](https://developer.apple.com/documentation/AppKit/NSCursor/contextualMenu) |
| ![A plus symbol.](https://docs-assets.developer.apple.com/published/d55eabe14365af873000aa389e5fad6c/pointers-crosshair%402x.png) | Crosshair | Precise rectangular selection is possible, such as when viewing an image in Preview. | [crosshair](https://developer.apple.com/documentation/AppKit/NSCursor/crosshair) |
| ![A small pointer arrowhead with a circle underneath; the circle contains an Ex.](https://docs-assets.developer.apple.com/published/528819d511869de26beb1fd5008ac773/pointers-disappearing-item%402x.png) | Disappearing item | A dragged item will disappear when dropped. If the item references an original item, the original is unaffected. For example, when dragging a mailbox out of the favorites bar in Mail, the original mailbox isn’t removed. | [disappearingItem](https://developer.apple.com/documentation/AppKit/NSCursor/disappearingItem) |
| ![A small pointer arrowhead with a circle underneath; the circle contains a plus symbol.](https://docs-assets.developer.apple.com/published/ccc7052f9bc6fb302d913633c648adcd/pointers-drag-copy%402x.png) | Drag copy | Duplicates a dragged—not moved—item when dropped into the destination. Appears when pressing the Option key during a drag operation. | [dragCopy](https://developer.apple.com/documentation/AppKit/NSCursor/dragCopy) |
| ![A curved arrow, pointing up and to the right.](https://docs-assets.developer.apple.com/published/47dfbfd5f1bf3141dbf875f47446d1fd/pointers-drag-link%402x.png) | Drag link | During a drag and drop operation, creates an alias of the selected file when dropped. The alias points to the original file, which remains unmoved. Appears when pressing the Option and Command keys during a drag operation. | [dragLink](https://developer.apple.com/documentation/AppKit/NSCursor/dragLink) |
| ![Opposing veritcal braces, used to form an insertion marker.](https://docs-assets.developer.apple.com/published/060f443dee8d260a1a1191d7831e36b7/pointers-horizontal-beam%402x.png) | Horizontal I beam | Selection and insertion of text is possible in a horizontal layout, such as a TextEdit or Pages document. | [iBeam](https://developer.apple.com/documentation/AppKit/NSCursor/iBeam) |
| ![An open, gloved hand.](https://docs-assets.developer.apple.com/published/a5daee642ccc8fb3ac550d176b2d1932/pointers-open-hand%402x.png) | Open hand | Dragging to reposition content within a view is possible. | [openHand](https://developer.apple.com/documentation/AppKit/NSCursor/openHand) |
| ![A small pointer arrowhead with a do not enter symbol underneath.](https://docs-assets.developer.apple.com/published/2daaf47bef26569f92f30a9016095dde/pointers-operation-not-allowed%402x.png) | Operation not allowed | A dragged item can’t be dropped in the current location. | [operationNotAllowed](https://developer.apple.com/documentation/AppKit/NSCursor/operationNotAllowed) |
| ![A gloved hand, with the index finger extended.](https://docs-assets.developer.apple.com/published/25193808b5e72d5983ff26764889718a/pointers-pointing-hand%402x.png) | Pointing hand | The content beneath the pointer is a URL link to a webpage, document, or other item. | [pointingHand](https://developer.apple.com/documentation/AppKit/NSCursor/pointingHand) |
| ![A horizontal bar with a downward-pointing arrow at its midpoint.](https://docs-assets.developer.apple.com/published/328443ed3b5dd85c84de91a60ed30b43/pointers-resize-down%402x.png) | Resize down | Resize or move a window, view, or element downward. | [resizeDown](https://developer.apple.com/documentation/AppKit/NSCursor/resizeDown) |
| ![A vertical bar with a left-pointing arrow at its midpoint.](https://docs-assets.developer.apple.com/published/34113d73f24c003f4b3715e0cef8fbf6/pointers-resize-left%402x.png) | Resize left | Resize or move a window, view, or element to the left. | [resizeLeft](https://developer.apple.com/documentation/AppKit/NSCursor/resizeLeft) |
| ![A vertical bar with left- and right-pointing arrows extending from its midpoint.](https://docs-assets.developer.apple.com/published/478726bb1a630013de1f77b3bccde9e0/pointers-resize-left-right%402x.png) | Resize left/right | Resize or move a window, view, or element to the left or right. | [resizeLeftRight](https://developer.apple.com/documentation/AppKit/NSCursor/resizeLeftRight) |
| ![A vertical bar with a right-pointing arrow at its midpoint.](https://docs-assets.developer.apple.com/published/6045fce093cc242bf438393155b77992/pointers-resize-right%402x.png) | Resize right | Resize or move a window, view, or element to the right. | [resizeRight](https://developer.apple.com/documentation/AppKit/NSCursor/resizeRight) |
| ![A horizontal bar with an up-pointing arrow at its midpoint.](https://docs-assets.developer.apple.com/published/34576a4ab42dea114abf11b3ee57a4f8/pointers-resize-up%402x.png) | Resize up | Resize or move a window, view, or element upward. | [resizeUp](https://developer.apple.com/documentation/AppKit/NSCursor/resizeUp) |
| ![A horizontal bar with up- and down-pointing arrows extending from its midpoint.](https://docs-assets.developer.apple.com/published/d55d0d01c955105a957231266affb447/pointers-resize-up-down%402x.png) | Resize up/down | Resize or move a window, view, or element upward or downward. | [resizeUpDown](https://developer.apple.com/documentation/AppKit/NSCursor/resizeUpDown) |
| ![Opposing horizontal braces, used to form an insertion marker.](https://docs-assets.developer.apple.com/published/15923a8cac833b5bb1fd69b4a395c4a9/pointers-vertical-beam%402x.png) | Vertical I beam | Selection and insertion of text is possible in a vertical layout. | [iBeamCursorForVerticalLayout](https://developer.apple.com/documentation/AppKit/NSCursor/iBeamCursorForVerticalLayout) |

---

## Popovers

Full page: `references/popovers.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/popovers

You can make a popover detachable in macOS, which becomes a separate panel when people drag it. The panel remains visible onscreen while people interact with other content.

**Consider letting people detach a popover.** People might appreciate being able to convert a popover into a panel if they want to view other information while the popover remains visible.

**Make minimal appearance changes to a detached popover.** A panel that looks similar to the original popover helps people maintain context.

---

## Printing

Full page: `references/printing.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/printing

**If your macOS app offers app-specific print options that the system doesn’t offer, consider creating a custom category for the print panel.** By default, the print panel offers several categories of settings, such as Layout, Paper Handling, and Media & Quality. Give your custom category a unique name, such as your app name, and include options that help people have a great print experience in your app. For example, Keynote offers presentation-specific options, like the ability to print presenter notes, slide backgrounds, and skipped slides.

**If your app supports document-specific page settings, consider presenting a page setup dialog.** A *page setup dialog* includes rarely changed settings for page size, orientation, and scaling that apply to printing a particular document. If this makes sense in your app, avoid implementing features the system already provides. For example, you don’t need to include options like changing the page orientation or printing in reverse order because the system implements these options.

**Make sure interdependencies between options are clear.** For example, if double-sided printing is available, an option to print on transparencies becomes unavailable.

**Separate advanced features from frequently used features.** Consider using a disclosure control to hide advanced options until they’re needed. Label advanced options as *Advanced Options*.

**Consider letting people preview the effect of a setting.** For example, you could update a thumbnail image to show the effect of changing a tone control.

**Consider storing modified settings with the document.** At minimum, it makes sense to store print settings until the document is closed in case people want to print it again.

---

## Privacy

Full page: `references/privacy.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/privacy

**Sign your app with a valid Developer ID.** If you choose to distribute your app outside the store, signing your app with Developer ID identifies you as an Apple developer and confirms that your app is safe to use. For developer guidance, see [Xcode Help](https://developer.apple.com/go/?id=ios-app-distribution-guide).

**Protect people’s data with app sandboxing.** Sandboxing provides your app with access to system resources and user data while protecting it from malware. All apps submitted to the Mac App Store require sandboxing. For developer guidance, see [Configuring the macOS App Sandbox](https://developer.apple.com/documentation/Xcode/configuring-the-macos-app-sandbox).

**Avoid making assumptions about who is signed in.** Because of fast user switching, multiple people may be active on the same system.

---

## Progress indicators

Full page: `references/progress-indicators.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/progress-indicators

In macOS, an indeterminate progress indicator can have a bar or circular appearance. Both versions use an animated image to indicate that the app is performing a task.

![An image of a completely filled horizontal progress bar in macOS. The fill is animated to cycle through various shade changes as progress continues.](https://docs-assets.developer.apple.com/published/7507cf2f58cb8aa230b7d2f5f8edb6d9/progress-indicator-intermediate-bar%402x.png)

![An image of a spinning, circular activity indicator in macOS.](https://docs-assets.developer.apple.com/published/6c1e23fcc6e04603423dacd5df6c48a3/progress-indicator-intermediate-spinner%402x.png)

**Prefer an activity indicator (spinner) to communicate the status of a background operation or when space is constrained.** Spinners are small and unobtrusive, so they’re useful for asynchronous background tasks, like retrieving messages from a server. Spinners are also good for communicating progress within a small area, such as within a text field or next to a specific control, such as a button.

**Avoid labeling a spinning progress indicator.** Because a spinner typically appears when people initiate a process, a label is usually unnecessary.

---

## Scroll views

Full page: `references/scroll-views.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/scroll-views

In macOS, a *scroll indicator* is commonly called a *scroll bar*.

**If necessary, use small or mini scroll bars in a panel.** When space is tight, you can use smaller scroll bars in panels that need to coexist with other windows. Be sure to use the same size for all controls in such a panel.

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

**Consider using introductory text to clarify the purpose of a segmented control.** When the control uses symbols or interface icons, you could also add a label below each segment to clarify its meaning. If your app includes tooltips, provide one for each segment in a segmented control.

**Use a tab view in the main window area — instead of a segmented control — for view switching.** A [Tab views](https://developer.apple.com/design/human-interface-guidelines/tab-views) supports efficient view switching and is similar in appearance to a [Boxes](https://developer.apple.com/design/human-interface-guidelines/boxes) combined with a segmented control. Consider using a segmented control to help people switch views in a toolbar or inspector pane.

![A screenshot of the macOS Calendar app. The main window area shows a tab view that contains four tabs: Day, Week, Month, and Year. The sidebar shows a segmented control that contains two segments: New and Replied.](https://docs-assets.developer.apple.com/published/45678627e5bb166ff19d3992605c0900/macos-calendar-tab-view-segmented-control-comparison%402x.png)

**Consider supporting spring loading.** On a Mac equipped with a Magic Trackpad, spring loading lets people activate a segment by dragging selected items over it and force clicking without dropping the selected items. People can also continue dragging the items after a segment activates.

---

## Settings

Full page: `references/settings.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/settings

When people choose the Settings item in your app’s or game’s App menu, your custom settings window opens. Typically, a custom settings window contains a toolbar that includes buttons for switching between views — called *panes* — that each contain a group of related settings.

**Include a settings item in the [App menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#App-menu).** Avoid adding settings buttons to a window’s toolbar, because doing so decreases the space available for essential commands that people use frequently. If you provide document-level options, add this item to your app’s [File menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#File-menu).

**Dim a settings window’s minimize and maximize buttons.** It’s quick to open a custom settings window using the standard Command–Comma (,) keyboard command, so there’s no need to keep the window in the Dock, and because a settings window accommodates the size of the current pane, people don’t need to expand the window to see more.

**In your settings window, use a noncustomizable toolbar that remains visible and always indicates the active toolbar button.** A settings window’s toolbar identifies the areas people can customize and helps people navigate among those areas. People rely on a stable settings interface to help them find what they need.

**Update the window’s title to reflect the currently visible pane.** If your settings window doesn’t have multiple panes, use the title *App Name* Settings.

**Restore the most recently viewed pane.** People often adjust related settings more than once, so it can be convenient when a settings window opens to the last pane people used.

---

## Sheets

Full page: `references/sheets.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/sheets

In macOS, a sheet is a cardlike view with rounded corners that floats on top of its parent window. The parent window is dimmed while the sheet is onscreen, signaling that people can’t interact with it until they dismiss the sheet. However, people expect to interact with other app windows before dismissing a sheet.

![A screenshot of the Notes app, with the What's New in Notes sheet centered on top of a dimmed Notes document in the background.](https://docs-assets.developer.apple.com/published/6e8c0d63600e92eee0a77c840a10c4c9/sheets-macos-notes%402x.png)

**Present a sheet in a reasonable default size.** People don’t generally expect to resize sheets, so it’s important to use a size that’s appropriate for the content you display. In some cases, however, people appreciate a resizable sheet — such as when they need to expand the contents for a clearer view — so it’s a good idea to support resizing.

**Let people interact with other app windows without first dismissing a sheet.** When a sheet opens, you bring its parent window to the front — if the parent window is a document window, you also bring forward its modeless document-related panels. When people want to interact with other windows in your app, make sure they can bring those windows forward even if they haven’t dismissed the sheet yet.

**Use a panel instead of a sheet if people need to repeatedly provide input and observe results.** A find and replace panel, for example, might let people initiate replacements individually, so they can observe the result of each search for correctness. For guidance, see [Panels](https://developer.apple.com/design/human-interface-guidelines/panels).

---

## Sidebars

Full page: `references/sidebars.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/sidebars

A sidebar’s row height, text, and glyph size depend on its overall size, which can be small, medium, or large. You can set the size programmatically, but people can also change it by selecting a different sidebar icon size in General settings.

**Consider automatically hiding and revealing a sidebar when its container window resizes.** For example, reducing the size of a Mail viewer window can automatically collapse its sidebar, making more room for message content.

**Avoid putting critical information or actions at the bottom of a sidebar.** People often relocate a window in a way that hides its bottom edge.

---

## Sliders

Full page: `references/sliders.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/sliders

Sliders in macOS can also include tick marks, making it easier for people to pinpoint a specific value within the range.

In a linear slider either with or without tick marks, the thumb is a narrow lozenge shape, and the portion of track between the minimum value and the thumb is filled with color. A linear slider often includes supplementary icons that illustrate the meaning of the minimum and maximum values.

In a circular slider, the thumb appears as a small circle. Tick marks, when present, appear as evenly spaced dots around the circumference of the slider.

![An illustration of a horizontal slider with the thumb in the middle. The leading portion of the track up to the thumb is filled with a blue highlight color.](https://docs-assets.developer.apple.com/published/92445cf683c4dc1b179fb5359a0bdb28/sliders-no-tick-marks%402x.png)

![An illustration of a horizontal slider with the thumb between two tick marks in the middle of the slider. The leading portion of the track up to the thumb is filled with a blue highlight color.](https://docs-assets.developer.apple.com/published/e31ef9e35e8675bd62f695ba6a988a51/sliders-tick-marks%402x.png)

![An illustration of a circular slider with the thumb at the 12 o'clock position.](https://docs-assets.developer.apple.com/published/3f253ed199e7e92b6124e6161dd79152/sliders-circular%402x.png)

**Consider giving live feedback as the value of a slider changes.** Live feedback shows people results in real time. For example, your Dock icons are dynamically scaled when adjusting the Size slider in Dock settings.

**Choose a slider style that matches peoples’ expectations.** A horizontal slider is ideal when moving between a fixed starting and ending point. For example, a graphics app might offer a horizontal slider for setting the opacity level of an object between 0 and 100 percent. Use circular sliders when values repeat or continue indefinitely. For example, a graphics app might use a circular slider to adjust the rotation of an object between 0 and 360 degrees. An animation app might use a circular slider to adjust how many times an object spins when animated — four complete rotations equals four spins, or 1440 degrees of rotation.

**Consider using a label to introduce a slider.** Labels generally use [sentence-style capitalization](https://help.apple.com/applestyleguide/#/apsgb744e4a3?sub=apdca93e113f1d64) and end with a colon. For guidance, see [Labels](https://developer.apple.com/design/human-interface-guidelines/labels).

**Use tick marks to increase clarity and accuracy.** Tick marks help people understand the scale of measurements and make it easier to locate specific values.

![A partial screenshot of the Energy Saver settings pane in macOS, cropped to show the slider that controls how long the display remains on after inactivity.](https://docs-assets.developer.apple.com/published/90d44ac8355f4a4e672e5e81633814e6/sliders-labels%402x.png)

**Consider adding labels to tick marks for even greater clarity.** Labels can be numbers or words, depending on the slider’s values. It’s unnecessary to label every tick mark unless doing so is needed to reduce confusion. In many cases, labeling only the minimum and maximum values is sufficient. When the values of the slider are nonlinear, like in the Energy Saver settings pane, periodic labels provide context. It’s also a good idea to provide a [tooltip](https://developer.apple.com/design/human-interface-guidelines/offering-help#macOS-visionOS) that displays the value of the thumb when people hold their pointer over it.

---

## Split views

Full page: `references/split-views.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/split-views

In macOS, you can arrange the panes of a split view vertically, horizontally, or both. A split view includes dividers between panes that can support dragging to resize them. For developer guidance, see [VSplitView](https://developer.apple.com/documentation/SwiftUI/VSplitView) and [HSplitView](https://developer.apple.com/documentation/SwiftUI/HSplitView).

**Set reasonable defaults for minimum and maximum pane sizes.** If people can resize the panes in your app’s split view, make sure to use sizes that keep the divider visible. If a pane gets too small, the divider can seem to disappear, becoming difficult to use.

**Consider letting people hide a pane when it makes sense.** If your app includes an editing area, for example, consider letting people hide other panes to reduce distractions or allow more room for editing — in Keynote, people can hide the navigator and presenter notes panes when they want to edit slide content.

**Provide multiple ways to reveal hidden panes.** For example, you might provide a toolbar button or a menu command — including a keyboard shortcut — that people can use to restore a hidden pane.

**Prefer the thin divider style.** The thin divider measures one point in width, giving you maximum space for content while remaining easy for people to use. Avoid using thicker divider styles unless you have a specific need. For example, if both sides of a divider present table rows that use strong linear elements that might make a thin divider hard to distinguish, it might work to use a thicker divider. For developer guidance, see [NSSplitView.DividerStyle](https://developer.apple.com/documentation/AppKit/NSSplitView/DividerStyle-swift.enum).

---

## Steppers

Full page: `references/steppers.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/steppers

**For large value ranges, consider supporting Shift-click to change the value quickly.** If your app benefits from larger changes in a stepper’s value, it can be useful to let people Shift-click the stepper to change the value by more than the default increment (by 10 times the default, for example).

---

## Text fields

Full page: `references/text-fields.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/text-fields

**Consider using a combo box if you need to pair text input with a list of choices.** For related guidance, see [Combo boxes](https://developer.apple.com/design/human-interface-guidelines/combo-boxes).

---

## The menu bar

Full page: `references/the-menu-bar.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/the-menu-bar

The menu bar in macOS includes the Apple menu, which is always the first item on the leading side of the menu bar. The Apple menu includes system-defined menu items that are always available, and you can’t modify or remove it. Space permitting, the system can also display menu bar extras in the trailing end of the menu bar. For guidance, see [Menu bar extras](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Menu-bar-extras).

When menu bar space is constrained, the system prioritizes the display of menus and essential menu bar extras. To ensure that menus remain readable, the system may decrease the space between the titles, truncating them if necessary.

When people enter full-screen mode, the menu bar typically hides until they reveal it by moving the pointer to the top of the screen. For guidance, see [Going full screen](https://developer.apple.com/design/human-interface-guidelines/going-full-screen).

#### Menu bar extras

A menu bar extra exposes app-specific functionality using an icon that appears in the menu bar when your app is running, even when it’s not the frontmost app. Menu bar extras are on the opposite side of the menu bar from your app’s menus. For developer guidance, see [MenuBarExtra](https://developer.apple.com/documentation/SwiftUI/MenuBarExtra).

When necessary, the system hides menu bar extras to make room for app menus. Similarly, if there are too many menu bar extras, the system may hide some to avoid crowding app menus.

![A screenshot of the Input menu bar extra and its menu.](https://docs-assets.developer.apple.com/published/cda99c09f1c6c7c3e9bae02cbca79b8d/menu-bar-extras%402x.png)

**Consider using a symbol to represent your menu bar extra.** You can create an [Icons](https://developer.apple.com/design/human-interface-guidelines/icons) or you can choose one of the [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols), using it as-is or customizing it to suit your needs. Both interface icons and symbols use black and clear colors to define their shapes; the system can apply other colors to the black areas in each image so it looks good on both dark and light menu bars, and when your menu bar extra is selected. The menu bar’s height is 24 pt.

**Display a menu — not a popover — when people click your menu bar extra.** Unless the app functionality you want to expose is too complex for a menu, avoid presenting it in a [Popovers](https://developer.apple.com/design/human-interface-guidelines/popovers).

**Let people — not your app — decide whether to put your menu bar extra in the menu bar.** Typically, people add a menu bar extra to the menu bar by changing a setting in an app’s settings window. To ensure discoverability, however, consider giving people the option of doing so during setup.

**Avoid relying on the presence of menu bar extras.** The system hides and shows menu bar extras regularly, and you can’t be sure which other menu bar extras people have chosen to display or predict the location of your menu bar extra.

**Consider exposing app-specific functionality in other ways, too.** For example, you can provide a [Dock menu](https://developer.apple.com/design/human-interface-guidelines/dock-menus) that appears when people Control-click your app’s Dock icon. People can hide or choose not to use your menu bar extra, but a Dock menu is aways available when your app is running.

---

## Toggles

Full page: `references/toggles.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/toggles

In addition to the switch toggle style, macOS supports the checkbox style and also defines radio buttons that can provide similar behaviors.

**Use switches, checkboxes, and radio buttons in the window body, not the window frame.** In particular, avoid using these components in a toolbar or status bar.

#### Switches

**Prefer a switch for settings that you want to emphasize.** A switch has more visual weight than a checkbox, so it looks better when it controls more functionality than a checkbox typically does. For example, you might use a switch to let people turn on or off a group of settings, instead of just one setting. For developer guidance, see [switch](https://developer.apple.com/documentation/SwiftUI/ToggleStyle/switch).

**Within a grouped form, consider using a mini switch to control the setting in a single row.** The height of a mini switch is similar to the height of buttons and other controls, resulting in rows that have a consistent height. If you need to present a hierarchy of settings within a grouped form, you can use a regular switch for the primary setting and mini switches for the subordinate settings. For developer guidance, see [GroupedFormStyle](https://developer.apple.com/documentation/SwiftUI/GroupedFormStyle) and [ControlSize](https://developer.apple.com/documentation/SwiftUI/ControlSize).

**In general, don’t replace a checkbox with a switch.** If you’re already using a checkbox in your interface, it’s probably best to keep using it.

#### Checkboxes

A checkbox is a small, square button that’s empty when the button is off, contains a checkmark when the button is on, and can contain a dash when the button’s state is mixed. Typically, a checkbox includes a title on its trailing side. In an editable checklist, a checkbox can appear without a title or any additional content.

**Use a checkbox instead of a switch if you need to present a hierarchy of settings.** The visual style of checkboxes helps them align well and communicate grouping. By using alignment — generally along the leading edge of the checkboxes — and indentation, you can show dependencies, such as when the state of a checkbox governs the state of subordinate checkboxes.

![An illustration showing a layout that includes two levels of checkboxes.](https://docs-assets.developer.apple.com/published/6e1459c0a6b3369a3990649bfd1da1bf/checkbox-alignment%402x.png)

**Consider using radio buttons if you need to present a set of more than two mutually exclusive options.** When people need to choose from options in addition to just “on” or “off,” using multiple radio buttons can help you clarify each option with a unique label.

**Consider using a label to introduce a group of checkboxes if their relationship isn’t clear.** Describe the set of options, and align the label’s baseline with the first checkbox in the group.

**Accurately reflect a checkbox’s state in its appearance.** A checkbox’s state can be on, off, or mixed. If you use a checkbox to globally turn on and off multiple subordinate checkboxes, show a mixed state when the subordinate checkboxes have different states. For example, you might need to present a text-style setting that turns all styles on or off, but also lets people choose a subset of individual style settings like bold, italic, or underline. For developer guidance, see [allowsMixedState](https://developer.apple.com/documentation/AppKit/NSButton/allowsMixedState).

![An illustration that shows a checkbox with the on state, which looks like a small rounded square with blue fill and a white checkmark.](https://docs-assets.developer.apple.com/published/2a49bf0361aee44a80f14ab2e19cd749/checkbox-selected%402x.png)

![An illustration that shows a checkbox with the off state, which looks like a small rounded square with no fill.](https://docs-assets.developer.apple.com/published/d1c2d6d3748b184a8a83620278290253/checkbox-deselected%402x.png)

![An illustration that shows a checkbox with the mixed state, which looks like a small rounded square with blue fill and a white hyphen.](https://docs-assets.developer.apple.com/published/e42e170d0099e9f244122cd44ffd3fad/checkbox-mixed%402x.png)

#### Radio buttons

A radio button is a small, circular button followed by a label. Typically displayed in groups of two to five, radio buttons present a set of mutually exclusive choices.

![An illustration that shows five items in a column, each with a radio button preceding the text Radio Button Label. The radio button for the third item is filled, indicating that it's selected.](https://docs-assets.developer.apple.com/published/45bd61e0318028eb08d68a59cabcffe5/radio-button-example%402x.png)

A radio button’s state is either selected (a filled circle) or deselected (an empty circle). Although a radio button can also display a mixed state (indicated by a dash), this state is rarely useful because you can communicate multiple states by using additional radio buttons. If you need to show that a setting or item has a mixed state, consider using a checkbox instead.

![An illustration that shows a selected radio button, which looks like a white dot centered in a small circle with a dark fill.](https://docs-assets.developer.apple.com/published/91c45b3934ecd18b42b2bb72e64ca702/radio-button-selected%402x.png)

![An illustration that shows a deselected radio button, which looks like a small, empty circle.](https://docs-assets.developer.apple.com/published/1bec25f63381d81a41f885e1338eb571/radio-button-deselected%402x.png)

**Prefer a set of radio buttons to present mutually exclusive options.** If you need to let people choose multiple options in a set, use checkboxes instead.

**Avoid listing too many radio buttons in a set.** A long list of radio buttons takes up a lot of space in the interface and can be overwhelming. If you need to present more than about five options, consider using a component like a [Pop-up buttons](https://developer.apple.com/design/human-interface-guidelines/pop-up-buttons) instead.

**To present a single setting that can be on or off, prefer a checkbox.** Although a single radio button can also turn something on or off, the presence or absence of the checkmark in a checkbox can make the current state easier to understand at a glance. In rare cases where a single checkbox doesn’t clearly communicate the opposing states, you can use a pair of radio buttons, each with a label that specifies the state it controls.

**Use consistent spacing when you display radio buttons horizontally.** Measure the space needed to accommodate the longest button label, and use that measurement consistently.

![An illustration that shows three items in a row, with a radio button preceding each item. The first and third items have long text labels, while the second has a short label. The horizontal space each item occupies is equal. A filled radio button precedes the second item, indicating that it's selected.](https://docs-assets.developer.apple.com/published/95fc61aefa156d2d78d9eb6589a47f6e/radio-button-equal-spacing%402x.png)

---

## Toolbars

Full page: `references/toolbars.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/toolbars

In a macOS app, the toolbar resides in the frame at the top of a window, either below or integrated with the title bar. Note that window titles can display inline with controls, and toolbar items don’t include a bezel.

![A diagram of a Finder window in macOS with callouts showing the location of the toolbar and the window frame.](https://docs-assets.developer.apple.com/published/e33da55f917f535c6d31b4ecf86b1e98/toolbars-mac-window-anatomy%402x.png)

**Make every toolbar item available as a command in the menu bar.** Because people can customize the toolbar or hide it, it can’t be the only place that presents a command. In contrast, it doesn’t make sense to provide a toolbar item for every menu item, because not all menu commands are important enough or used often enough to warrant space in the toolbar.

---

## Typography

Full page: `references/typography.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/typography

SF Pro is the system font in macOS. NY is available for Mac apps built with Mac Catalyst. macOS doesn’t support Dynamic Type.

**When necessary, use dynamic system font variants to match the text in standard controls.** Dynamic system font variants give your text the same look and feel of the text that appears in system-provided controls. Use the variants listed below to achieve a look that’s consistent with other apps on the platform.

| Dynamic font variant | API |
| --- | --- |
| Control content | [controlContentFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/controlContentFont(ofSize:)) |
| Label | [labelFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/labelFont(ofSize:)) |
| Menu | [menuFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/menuFont(ofSize:)) |
| Menu bar | [menuBarFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/menuBarFont(ofSize:)) |
| Message | [messageFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/messageFont(ofSize:)) |
| Palette | [paletteFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/paletteFont(ofSize:)) |
| Title | [titleBarFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/titleBarFont(ofSize:)) |
| Tool tips | [toolTipsFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/toolTipsFont(ofSize:)) |
| Document text (user) | [userFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/userFont(ofSize:)) |
| Monospaced document text (user fixed pitch) | [userFixedPitchFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/userFixedPitchFont(ofSize:)) |
| Bold system font | [boldSystemFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/boldSystemFont(ofSize:)) |
| System font | [systemFont(ofSize:)](https://developer.apple.com/documentation/AppKit/NSFont/systemFont(ofSize:)) |

---

## Undo and redo

Full page: `references/undo-and-redo.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/undo-and-redo

**Place undo and redo commands in the Edit menu and support the standard keyboard shortcuts.** Mac users expect to find undo and redo at the top of the Edit menu; they also expect to use Command–Z and Shift–Command–Z to perform undo and redo, respectively.

---

## Windows

Full page: `references/windows.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/windows

In macOS, people typically run several apps at the same time, often viewing windows from multiple apps on one desktop and switching frequently between different windows — moving, resizing, minimizing, and revealing the windows to suit their work style.

To learn about setting up a window to display your game in macOS, see [Managing your game window for Metal in macOS](https://developer.apple.com/documentation/Metal/managing-your-game-window-for-metal-in-macos).

#### macOS window anatomy

A macOS window consists of a frame and a body area. People can move a window by dragging the frame and can often resize the window by dragging its edges.

The *frame* of a window appears above the body area and can include window controls and a  [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars). In rare cases, a window can also display a bottom bar, which is a part of the frame that appears below body content.

#### macOS window states

A macOS window can have one of three states:

- **Main.** The frontmost window that people view is an app’s main window. There can be only one main window per app.
- **Key.** Also called the *active window*, the key window accepts people’s input. There can be only one key window onscreen at a time. Although the front app’s main window is usually the key window, another window — such as a panel floating above the main window — might be key instead. People typically click a window to make it key; when people click an app’s Dock icon to bring all of that app’s windows forward, only the most recently accessed window becomes key.
- **Inactive.** A window that’s not in the foreground is an inactive window.

The system gives main, key, and inactive windows different appearances to help people visually identify them. For example, the key window uses color in the title bar options for closing, minimizing, and zooming; inactive windows and main windows that aren’t key use gray in these options. Also, inactive windows don’t use [Materials](https://developer.apple.com/design/human-interface-guidelines/materials) (an effect that can pull color into a window from the content underneath it), which makes them appear subdued and seem visually farther away than the main and key windows.

![An illustration of a stack of three windows, as follows: An inactive window in the background, an app’s main window in the middle, and a key window appearing above the other two windows.](https://docs-assets.developer.apple.com/published/00151f56a691d0c6a3854113f6232437/window-states%402x.png)

> **Note:** Some windows — typically, panels like Colors or Fonts — become the key window only when people click the window’s title bar or a component that requires keyboard input, such as a text field.

**Make sure custom windows use the system-defined appearances.** People rely on the visual differences between windows to help them identify the foreground window and know which window will accept their input. When you use system-provided components, a window’s background and button appearances update automatically when the window changes state; if you use custom implementations, you need to do this work yourself.

**Avoid putting critical information or actions in a bottom bar, because people often relocate a window in a way that hides its bottom edge.** If you must include one, use it only to display a small amount of information directly related to a window’s contents or to a selected item within it. For example, Finder uses a bottom bar (called the status bar) to display the total number of items in a window, the number of selected items, and how much space is available on the disk. A bottom bar is small, so if you have more information to display, consider using an inspector, which typically presents information on the trailing side of a split view.

---
