# tvOS-specific guidance, collected

Every place the HIG states a rule specific to tvOS, lifted from the page it lives on. Sections appear alphabetically by page.

A heading like `### tvOS, iPadOS` upstream means the rule is shared; it's reproduced here in full so you don't have to go looking. Each entry links to the complete page, which also carries the cross-platform guidance this file deliberately omits.

---

## App icons

Full page: `references/app-icons.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/app-icons

**Include a safe zone to ensure the system doesn’t crop your content.** When someone focuses your app icon, the system may crop content around the edges as the icon scales and moves. To ensure that your icon’s content is always visible, keep a safe zone around it. Be aware that the safe zone can vary, depending on the image size, layer depth, and motion, and the system crops foreground layers more than background layers.

![A diagram of the Settings icon in tvOS with a white dotted line inside the outer border, which indicates the safe zone.](https://docs-assets.developer.apple.com/published/bb9ddd2fe1f2ba4bad183b6d33f9d001/tvos-app-icon-safe-zone%402x.png)

---

## Color

Full page: `references/color.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/color

**Consider choosing a limited color palette that coordinates with your app logo.** Subtle use of color can help you communicate your brand while deferring to the content.

**Avoid using only color to indicate focus.** Subtle scaling and responsive animation are the primary ways to denote interactivity when an element is in focus.

---

## Focus and selection

Full page: `references/focus-and-selection.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/focus-and-selection

**In a full-screen experience, let people use gestures to interact with the content, not to move focus.** When an item displays in full screen, it doesn’t show focus, so people naturally assume that their gestures will affect the object, and not its focus state.

**Avoid displaying a pointer.** People expect to navigate a fixed number of items by changing focus, not by trying to drag a tiny pointer around a huge screen. While free-form movement might make sense during gameplay, such as when looking for a hidden object or flying a plane, use the focus model when people navigate menus and other interface elements. If your app requires a pointer, make sure it’s highly visible and feels integrated with your experience.

**Design your interface to accommodate components in various focus states.** In tvOS, focusable items can have up to five different states, each of which is visually distinct. Because focusing an item often increases its scale, you need to supply assets for the larger, focused size to ensure they always look sharp, and you need to make sure the larger item doesn’t crowd the surrounding interface.

| State | Description |
| --- | --- |
| ![An image of an unfocused button on top of a photograph. A small drop shadow makes it appear very close to the content behind it, with a translucent background infused by the colors of the content, and a high-contrast text color.](https://docs-assets.developer.apple.com/published/aa4269d4ccd0fa70d2b7dc2026e546ff/focus-and-selection-state-unfocused%402x.png) | The viewer hasn’t brought focus to the item. Unfocused items appear less prominent than focused items. |
| ![An image of a focused button on top of a photograph. It’s larger than an unfocused button, and a drop shadow makes it appear farther away from the content behind it, with an opaque white background and a black text label.](https://docs-assets.developer.apple.com/published/89603ce2379330efff3731122a9db0fb/focus-and-selection-state-focused%402x.png) | The viewer brings focus to the item. A focused item visually stands out from the other onscreen content through elevation to the foreground, illumination, and animation. |
| ![An image of a highlighted button on top of a photograph. It’s the same size as an unfocused button, and a drop shadow makes it appear a little farther away from the surface of the content behind it, with an opaque white background and a black text label.](https://docs-assets.developer.apple.com/published/e96afa3822e94ae8647dbe138347b5dd/focus-and-selection-state-highlighted%402x.png) | The viewer chooses the focused item. A focused item provides instant visual feedback when people choose it. For example, a button might briefly invert its colors and animate before it transitions to its selected appearance. |
| ![An image of a selected button on top of a photograph. It’s the same size as an unfocused button, and a small drop shadow makes it appear very close to the content behind it, with an opaque white background and a black text label.](https://docs-assets.developer.apple.com/published/2492d95b8d71bd7da61e5217eb539198/focus-and-selection-state-selected%402x.png) | The viewer has chosen or activated the item in some way. For example, a heart-shaped button that people can use to favorite a photo might appear filled in the selected state and empty in the deselected state. |
| ![An image of an unavailable button on top of a photograph. It’s the same size as an unfocused button. It lacks a drop shadow and appears to rest directly on the content behind it, with a translucent background tinted by the the colors of nearby content, and a low-contrast text color.](https://docs-assets.developer.apple.com/published/57d15e479c370a06e1b4fe46d9c867c4/focus-and-selection-state-unavailable%402x.png) | The viewer can’t bring focus to the item or choose it. An unavailable item appears inactive. |

For developer guidance, see [Adding user-focusable elements to a tvOS app](https://developer.apple.com/documentation/UIKit/adding-user-focusable-elements-to-a-tvos-app).

---

## Game Center

Full page: `references/game-center.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/game-center

**Display an optional image at the top of the dashboard.** In tvOS, you can add an additional piece of artwork to the dashboard to highlight your game’s aesthetic. Use a simple, easily recognizable image that looks great at a distance. Consider using your game’s logo or word mark; however, don’t use your app icon for this image. Use the following specifications to create a dashboard image.

![A diagram of the layout for a tvOS dashboard image, with a callout indicating the image size.](https://docs-assets.developer.apple.com/published/438f3caaa842926ba5a0f54470c64373/tvos-dashboard-image%402x.png)

| Attribute | Value |
| --- | --- |
| Image size | 600x180 pt (1200x360 px @2x) |
| Format | PNG, TIF, or JPG |
| Color space | sRGB or P3 |
| Resolution | 72 DPI (minimum) |

---

## Gestures

Full page: `references/gestures.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/gestures

People expect to use [Standard gestures](https://developer.apple.com/design/human-interface-guidelines/gestures#Standard-gestures) to navigate tvOS apps and games with a compatible remote, Siri Remote, or [Game controls](https://developer.apple.com/design/human-interface-guidelines/game-controls) that includes a touch surface. For guidance, see [Remotes](https://developer.apple.com/design/human-interface-guidelines/remotes).

---

## Image views

Full page: `references/image-views.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/image-views

Many tvOS images combine multiple layers with transparency to create a feeling of depth. For guidance, see [Layered images](https://developer.apple.com/design/human-interface-guidelines/images#Layered-images).

---

## Images

Full page: `references/images.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/images

Layered images are at the heart of the Apple TV user experience. The system combines layered images, transparency, scaling, and motion to produce a sense of realism and vigor that evokes a personal connection as people interact with onscreen content.

#### Parallax effect

*Parallax* is a subtle visual effect the system uses to convey depth and dynamism when an element is in focus. As an element comes into focus, the system elevates it to the foreground, gently swaying it while applying illumination that makes the element’s surface appear to shine. After a period of inactivity, out-of-focus content dims and the focused element expands.

Layered images are required to support the parallax effect.

#### Layered images

A *layered image* consists of two to five distinct layers that come together to form a single image. The separation between layers, along with use of transparency, creates a feeling of depth. As someone interacts with an image, layers closer to the surface elevate and scale, overlapping lower layers farther back and producing a 3D effect.

> **Important:** Your tvOS [tvOS](https://developer.apple.com/design/human-interface-guidelines/app-icons#tvOS) must use a layered image. For other focusable images in your app, including [Top Shelf](https://developer.apple.com/design/human-interface-guidelines/top-shelf) images, layered images are strongly encouraged, but optional.

You can embed layered images in your app or retrieve them from a content server at runtime. For guidance on adding layered images to your app, see the [Parallax Previewer User Guide](https://help.apple.com/itc/parallaxpreviewer/).

> **Note:** If your app retrieves layered images from a content server at runtime, you must provide runtime layered images (`.lcr`). You can generate them from LSR files or Photoshop files using the `layerutil` command-line tool that Xcode provides. Runtime layered images are intended to be downloaded — don’t embed them in your app.

**Use standard interface elements to display layered images.** If you use standard views and system-provided focus APIs — such as [FocusState](https://developer.apple.com/documentation/SwiftUI/FocusState) — layered images automatically get the parallax treatment when people bring them into focus.

**Identify logical foreground, middle, and background elements.** In foreground layers, display prominent elements like a character in a game, or text on an album cover or movie poster. Middle layers are perfect for secondary content and effects like shadows. Background layers are opaque backdrops that showcase the foreground and middle layers without upstaging them.

**Generally, keep text in the foreground.** Unless you want to obscure text, bring it to the foreground layer for clarity.

**Keep the background layer opaque.** Using varying levels of opacity to let content shine through higher layers is fine, but your background layer must be opaque — you’ll get an error if it’s not. An opaque background layer ensures your artwork looks great with parallax, drop shadows, and system backgrounds.

**Keep layering simple and subtle.** Parallax is designed to be almost unnoticeable. Excessive 3D effects can appear unrealistic and jarring. Keep depth simple to bring your content to life and add delight.

**Leave a safe zone around the foreground layers of your image.** When focused, content on some layers may be cropped as the layered image scales and moves. To ensure that essential content is always visible, keep it within a safe zone. For guidance, see [App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons).

**Always preview layered images.** To ensure your layered images look great on Apple TV, preview them throughout your design process using Xcode, the Parallax Previewer app for macOS, or the Parallax Exporter plug-in for Adobe Photoshop. Pay special attention as scaling and clipping occur, and readjust your images as needed to keep important content safe. After your layered images are final, preview them on an actual TV for the most accurate representation of what people will see. To download Parallax Previewer and Parallax Exporter, see [Resources](https://developer.apple.com/design/resources/#parallax-previewer).

---

## Launching

Full page: `references/launching.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/launching

> **Note:** Unlike the [Layered images](https://developer.apple.com/design/human-interface-guidelines/images#Layered-images) throughout much of a tvOS app, the launch screen is static.

**In a live-viewing app, consider automatically starting playback soon after people start the app.** People come to your app to watch TV, so you might want to start playing new or recently viewed live content after a few seconds of inactivity. For guidance, see [Live-viewing apps](https://developer.apple.com/design/human-interface-guidelines/live-viewing-apps).

---

## Layout

Full page: `references/layout.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/layout

**Be prepared for a wide range of TV sizes.** On Apple TV, layouts don’t automatically adapt to the size of the screen like they do on iPhone or iPad. Instead, apps and games show the same interface on every display. Take extra care in designing your layout so that it looks great in a variety of screen sizes.

**Adhere to the screen’s safe area.** Inset primary content 60 points from the top and bottom of the screen, and 80 points from the sides. It can be difficult for people to see content that close to the edges, and unintended cropping can occur due to overscanning on older TVs. Allow only partially displayed offscreen content and elements that deliberately flow offscreen to appear outside this zone.

![An illustration of a TV with a safe zone border on all sides. In width, the top and bottom borders measure 60 points, and the side borders both measure 80 points.](https://docs-assets.developer.apple.com/published/1be425edd08beb67cba3c1000983581f/visual-design-safe-zone%402x.png)

**Include appropriate padding between focusable elements.** When you use UIKit and the focus APIs, an element gets bigger when it comes into focus. Consider how elements look when they’re focused, and make sure you don’t let them overlap important information. For developer guidance, see [About focus interactions for Apple TV](https://developer.apple.com/documentation/UIKit/about-focus-interactions-for-apple-tv).

![An illustration that uses vertical shaded rectangles to show padding between focusable items.](https://docs-assets.developer.apple.com/published/1cfcdddb80150197945945a6884a9ade/visual-design-padding%402x.png)

#### Grids

The following grid layouts provide an optimal viewing experience. Be sure to use appropriate spacing between unfocused rows and columns to prevent overlap when an item comes into focus.

If you use the UIKit collection view flow element, the number of columns in a grid is automatically determined based on the width and spacing of your content. For developer guidance, see [UICollectionViewFlowLayout](https://developer.apple.com/documentation/UIKit/UICollectionViewFlowLayout).

**Include additional vertical spacing for titled rows.** If a row has a title, provide enough spacing between the bottom of the previous unfocused row and the center of the title to avoid crowding. Also provide spacing between the bottom of the title and the top of the unfocused items in the row.

**Use consistent spacing.** When content isn’t consistently spaced, it no longer looks like a grid and it’s harder for people to scan.

**Make partially hidden content look symmetrical.** To help direct attention to the fully visible content, keep partially hidden offscreen content the same width on each side of the screen.

---

## Lists and tables

Full page: `references/lists-and-tables.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/lists-and-tables

**Confirm that images near a table still look good as each row highlights and slightly increases in size when it becomes focused.** A focused row’s corners can also become rounded, which may affect the appearance of images on either side of it. Account for this effect as you prepare images, and don’t add your own masks to round the corners.

---

## Managing accounts

Full page: `references/managing-accounts.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/managing-accounts

Most people interact with Apple TV using a remote, not a keyboard, so ask for the minimum amount of information necessary.

**Prefer letting people use another device to sign up or authenticate.** When you configure your app’s associated domains, Apple TV can work with other devices to safely suggest sign-in credentials, including [Sign in with Apple](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple). For developer guidance, see [Configuring an associated domain](https://developer.apple.com/documentation/Xcode/configuring-an-associated-domain).

**When people are signed in to a shared account, avoid asking them to choose their profile every time they become the current user.** In tvOS 16 and later, your app can share its credentials with all users while storing each individual’s profile and user data separately. When you support this type of sharing, your app can automatically use the current user’s profile without asking each person to sign in separately to a shared account. For developer guidance, see [kSecUseUserIndependentKeychain](https://developer.apple.com/documentation/Security/kSecUseUserIndependentKeychain) and [User Management Entitlement](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.user-management).

**Minimize data entry.** If you need to gather more than a small amount of information, ask people to visit a website from another device. If you need an email address, show the email keyboard screen, which includes a list of recently entered addresses.

---

## Materials

Full page: `references/materials.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/materials

In tvOS, Liquid Glass appears throughout navigation elements and system experiences such as Top Shelf and Control Center. Certain interface elements, like image views and buttons, adopt Liquid Glass when they gain focus.

![A screenshot of the Destination Video app running in tvOS. The app shows a screen with details about a video called A BOT-anist Adventure. The background is a colorful image of the main character in a scene from the video. The interface elements floating above the background adopt a Liquid Glass appearance to allow background color to show through and create a more immersive media experience.](https://docs-assets.developer.apple.com/published/d92912242c5166aa658abd2328301131/materials-tvos-media-player%402x.png)

In addition to Liquid Glass, tvOS continues to provide standard materials, which you can use to help define structure in the content layer. The thickness of a standard material affects how prominently the underlying content shows through. For example, consider using standard materials in the following ways:

| Material | Recommended for |
| --- | --- |
| [ultraThin](https://developer.apple.com/documentation/SwiftUI/Material/ultraThin) | Full-screen views that require a light color scheme |
| [thin](https://developer.apple.com/documentation/SwiftUI/Material/thin) | Overlay views that partially obscure onscreen content and require a light color scheme |
| [regular](https://developer.apple.com/documentation/SwiftUI/Material/regular) | Overlay views that partially obscure onscreen content |
| [thick](https://developer.apple.com/documentation/SwiftUI/Material/thick) | Overlay views that partially obscure onscreen content and require a dark color scheme |

---

## Multitasking

Full page: `references/multitasking.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/multitasking

On Apple TV, people can play or browse content while also playing movies or TV shows in Picture in Picture (where supported).

---

## Page controls

Full page: `references/page-controls.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/page-controls

**Use page controls on collections of full-screen pages.** A page control is designed to operate in a full-screen environment where multiple content-rich pages are peers in the page hierarchy. Inclusion of additional controls makes it difficult to maintain focus while moving between pages.

---

## Pickers

Full page: `references/pickers.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/pickers

Pickers are available in tvOS with SwiftUI. For developer guidance, see [Picker](https://developer.apple.com/documentation/SwiftUI/Picker).

---

## Playing audio

Full page: `references/playing-audio.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/playing-audio

In tvOS, the system plays audio only when people initiate it, through interactions within apps and games or when performing device calibrations. For example, tvOS doesn’t play sounds to accompany components like alerts or notifications.

---

## Playing video

Full page: `references/playing-video.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/playing-video

**Defer to content when displaying logos or noninteractive overlays above video.** A small, unobtrusive logo or countdown timer may be appropriate for your video, but avoid large, distracting overlays that don’t enhance the viewing experience. Also, be aware that some devices are prone to image retention, so it’s generally better to keep overlays short and to prefer translucent graphics in Standard Dynamic Range (SDR) to bright, opaque content.

**Show interactive overlays gracefully.** Some videos display interactive overlays, such as quizzes, surveys, and progress check-ins. For the best user experience, implement a minimum delay of 0.5 seconds to pause playing media, and display an interactive overlay. Give people a clear way to dismiss the overlay and resume media playback after they finish interacting.

---

## Scroll views

Full page: `references/scroll-views.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/scroll-views

Views in tvOS can scroll, but they aren’t treated as distinct objects with scroll indicators. Instead, when content exceeds the size of the screen, the system automatically scrolls the interface to keep focused items visible.

---

## Search fields

Full page: `references/search-fields.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/search-fields

A search screen is a specialized keyboard screen that helps people enter search text, displaying search results beneath the keyboard in a fully customizable view. For developer guidance, see [UISearchController](https://developer.apple.com/documentation/UIKit/UISearchController).

![An illustration of a search screen in tvOS. The screen includes a field with a keyboard input area at the top, a scope bar, and a grid of top results at the bottom.](https://docs-assets.developer.apple.com/published/494283107367d7c6b1a652b047ab9431/search-fields-tvos-search%402x.png)

**Provide suggestions to make searching easier.** People typically don’t want to do a lot of typing in tvOS. To improve the search experience, provide popular and context-specific search suggestions, including recent searches when available. For developer guidance, see [Using suggested searches with a search controller](https://developer.apple.com/documentation/UIKit/using-suggested-searches-with-a-search-controller).

---

## Segmented controls

Full page: `references/segmented-controls.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/segmented-controls

**Consider using a split view instead of a segmented control on screens that perform content filtering.** People generally find it easy to navigate back and forth between content and filtering options using a split view. Depending on its placement, a segmented control may not be as easy to access.

**Avoid putting other focusable elements close to segmented controls.** Segments become selected when focus moves to them, not when people click them. Carefully consider where you position a segmented control relative to other interface elements. If other focusable elements are too close, people might accidentally focus on them when attempting to switch between segments.

---

## Split views

Full page: `references/split-views.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/split-views

In tvOS, a split view can work well to help people filter content. When people choose a filter category in the primary pane, your app can display the results in the secondary pane.

**Choose a split view layout that keeps the panes looking balanced.** By default, a split view devotes a third of the screen width to the primary pane and two-thirds to the secondary pane, but you can also specify a half-and-half layout.

**Display a single title above a split view, helping people understand the content as a whole.** People already know how to use a split view to navigate and filter content; they don’t need titles that describe what each pane contains.

**Choose the title’s alignment based on the type of content the secondary pane contains.** Specifically, when the secondary pane contains a content collection, consider centering the title in the window. In contrast, if the secondary pane contains a single main view of important content, consider placing the title above the primary view to give the content more room.

---

## Tab bars

Full page: `references/tab-bars.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/tab-bars

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

---

## Text views

Full page: `references/text-views.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/text-views

You can display text in tvOS using a text view. Because text input in tvOS is minimal by design, tvOS uses [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields) for editable text instead.

---

## Typography

Full page: `references/typography.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/typography

SF Pro is the system font in tvOS, and apps can also use NY.

---

## Virtual keyboards

Full page: `references/virtual-keyboards.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards

tvOS displays a linear virtual keyboard when people select a text field using the Siri Remote.

> **Note:** A grid keyboard screen appears when people use devices other than the Siri Remote, and the layout of content automatically adapts to the keyboard.

When people activate a digit entry view, tvOS displays a digit-specific keyboard. For guidance, see [Digit entry views](https://developer.apple.com/design/human-interface-guidelines/digit-entry-views).

---
