# visionOS-specific guidance, collected

Every place the HIG states a rule specific to visionOS, lifted from the page it lives on. Sections appear alphabetically by page.

A heading like `### visionOS, iPadOS` upstream means the rule is shared; it's reproduced here in full so you don't have to go looking. Each entry links to the complete page, which also carries the cross-platform guidance this file deliberately omits.

---

## Accessibility

Full page: `references/accessibility.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/accessibility

visionOS offers a variety of accessibility features people can use to interact with their surroundings in ways that are comfortable and work best for them, including head and hand Pointer Control, and a Zoom feature.

**Prioritize comfort.** The immersive nature of visionOS means that interfaces, animations, and interactions have a greater chance of causing motion sickness, and visual and ergonomic discomfort for people. To ensure the most comfortable experience, consider these tips:

- Keep interface elements within a person’s field of view. Prefer horizontal layouts to vertical ones that might cause neck strain, and avoid demanding the viewer’s attention in different locations in quick succession.
- Reduce the speed and intensity of animated objects, particularly in someone’s peripheral vision.
- Be gentle with camera and video motion, and avoid situations where someone may feel like the world around them is moving without their control.
- Avoid anchoring content to the wearer’s head, which may make them feel stuck and confined, and also prevent them from using assistive technologies like Pointer Control.
- Minimize the need for large and repetitive gestures, as these can become tiresome and may be difficult depending on a person’s surroundings.

For additional guidance, see [Create accessible spatial experiences](https://developer.apple.com/videos/play/wwdc2023/10034) and [Design considerations for vision and motion](https://developer.apple.com/videos/play/wwdc2023/10078).

---

## Alerts

Full page: `references/alerts.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/alerts

When your app is running in the Shared Space, visionOS displays an alert in front of the app’s window, slightly forward along the z-axis.

If someone moves a window without dismissing its alert, the alert remains anchored to the window. If your app is running in a Full Space, the system displays the alert centered in the wearer’s [Field of view](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Field-of-view).

If you need to display an accessory view in a visionOS alert, create a view that has a maximum height of 154 pt and a 16-pt corner radius.

---

## App icons

Full page: `references/app-icons.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/app-icons

**Avoid adding a shape that’s intended to look like a hole or concave area to the background layer.** The system-added shadow and specular highlights can make such a shape stand out instead of recede.

---

## Augmented reality

Full page: `references/augmented-reality.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/augmented-reality

With the wearer’s [visionOS](https://developer.apple.com/design/human-interface-guidelines/privacy#visionOS), you can use ARKit in your visionOS app to detect surfaces in a person’s surroundings, use a person’s hand and finger postions to inform your [Designing custom gestures in visionOS](https://developer.apple.com/design/human-interface-guidelines/gestures#Designing-custom-gestures-in-visionOS), support interactions that incorporate nearby physical objects into your [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences), and more. For developer guidance, see [ARKit](https://developer.apple.com/documentation/ARKit).

---

## Buttons

Full page: `references/buttons.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/buttons

A visionOS button typically includes a visible background that can help people see it, and the button plays sound to provide feedback when people interact with it.

There are three standard button shapes in visionOS. Typically, an icon-only button uses a [circle](https://developer.apple.com/documentation/SwiftUI/ButtonBorderShape/circle) shape, a text-only button uses a [roundedRectangle](https://developer.apple.com/documentation/SwiftUI/ButtonBorderShape/roundedRectangle) or [capsule](https://developer.apple.com/documentation/SwiftUI/ButtonBorderShape/capsule) shape, and a button that includes both an icon and text uses the capsule shape.

visionOS buttons use different visual styles to communicate four different interaction states.

![An image of a circular button that contains an icon of an outlined square with rounded corners. The button background is dark and the dashed outline is white.](https://docs-assets.developer.apple.com/published/aed0b1c313448f088dd1ee24663db11e/visionos-button-state-idle%402x.png)

![An image of a circular button that contains an icon of an outlined square with rounded corners. The button background is medium dark and the outline is white.](https://docs-assets.developer.apple.com/published/29d708fd7985184cbee9d90d7684da92/visionos-button-state-hover%402x.png)

![An image of a circular button that contains an icon of an outlined square with rounded corners. The button background is white and the outline is black.](https://docs-assets.developer.apple.com/published/0b94e710605235dfca19ef853499cf26/visionos-button-state-selected%402x.png)

![An image of a circular button that contains an icon of an outlined square with rounded corners. The button background is very dark and the outline is light.](https://docs-assets.developer.apple.com/published/737120252765e5427161af32bb17e7fb/visionos-button-state-unavailable%402x.png)

> **Note:** In visionOS, buttons don’t support custom hover effects.

In addition to the four states shown above, a button can also reveal a tooltip when people look at it for a brief time. In general, buttons that contain text don’t need to display a tooltip because the button’s descriptive label communicates what it does.

In visionOS, buttons can have the following sizes.

| Shape | Mini (28 pt) | Small (32 pt) | Regular (44 pt) | Large (52 pt) | Extra large (64 pt) |
| --- | --- | --- | --- | --- | --- |
| Circular | ![A checkmark denoting availability.](https://docs-assets.developer.apple.com/published/a98fac2c42999558da92de9e557ca89b/table-availability-checkmark%402x.png) | ![A checkmark denoting availability.](https://docs-assets.developer.apple.com/published/a98fac2c42999558da92de9e557ca89b/table-availability-checkmark%402x.png) | ![A checkmark denoting availability.](https://docs-assets.developer.apple.com/published/a98fac2c42999558da92de9e557ca89b/table-availability-checkmark%402x.png) | ![A checkmark denoting availability.](https://docs-assets.developer.apple.com/published/a98fac2c42999558da92de9e557ca89b/table-availability-checkmark%402x.png) | ![A checkmark denoting availability.](https://docs-assets.developer.apple.com/published/a98fac2c42999558da92de9e557ca89b/table-availability-checkmark%402x.png) |
| Capsule (text only) |  | ![A checkmark denoting availability.](https://docs-assets.developer.apple.com/published/a98fac2c42999558da92de9e557ca89b/table-availability-checkmark%402x.png) | ![A checkmark denoting availability.](https://docs-assets.developer.apple.com/published/a98fac2c42999558da92de9e557ca89b/table-availability-checkmark%402x.png) | ![A checkmark denoting availability.](https://docs-assets.developer.apple.com/published/a98fac2c42999558da92de9e557ca89b/table-availability-checkmark%402x.png) |  |
| Capsule (text and icon) |  |  | ![A checkmark denoting availability.](https://docs-assets.developer.apple.com/published/a98fac2c42999558da92de9e557ca89b/table-availability-checkmark%402x.png) | ![A checkmark denoting availability.](https://docs-assets.developer.apple.com/published/a98fac2c42999558da92de9e557ca89b/table-availability-checkmark%402x.png) |  |
| Rounded rectangle |  | ![A checkmark denoting availability.](https://docs-assets.developer.apple.com/published/a98fac2c42999558da92de9e557ca89b/table-availability-checkmark%402x.png) | ![A checkmark denoting availability.](https://docs-assets.developer.apple.com/published/a98fac2c42999558da92de9e557ca89b/table-availability-checkmark%402x.png) | ![A checkmark denoting availability.](https://docs-assets.developer.apple.com/published/a98fac2c42999558da92de9e557ca89b/table-availability-checkmark%402x.png) |  |

**Prefer buttons that have a discernible background shape and fill.** It tends to be easier for people to see a button when it’s enclosed in a shape that uses a contrasting background fill. The exception is a button in a toolbar, context menu, alert, or [Ornaments](https://developer.apple.com/design/human-interface-guidelines/ornaments) where the shape and material of the larger component make the button comfortably visible. The following guidelines can help you ensure that a button looks good in different contexts:

- When a button appears on top of a glass [visionOS](https://developer.apple.com/design/human-interface-guidelines/windows#visionOS), use the [thin](https://developer.apple.com/documentation/SwiftUI/Material/thin) material as the button’s background.
- When a button appears floating in space, use the [visionOS](https://developer.apple.com/design/human-interface-guidelines/materials#visionOS) for its background.

**Avoid creating a custom button that uses a white background fill and black text or icons.** The system reserves this visual style to convey the toggled state.

**In general, prefer circular or capsule-shape buttons.** People’s eyes tend to be drawn toward the corners in a shape, making it difficult to keep looking at the shape’s center. The more rounded a button’s shape, the easier it is for people to look steadily at it. When you need to display a button by itself, prefer a capsule-shape button.

**Provide enough space around a button to make it easy for people to look at it.** Aim to place buttons so their centers are always at least 60 pts apart. If your buttons measure 60 pts or larger, add 4 pts of padding around them to keep the hover effect from overlapping. Also, it’s usually best to avoid displaying small or mini buttons in a vertical stack or horizontal row.

**Choose the right shape if you need to display text-labeled buttons in a stack or row.** Specifically, prefer the rounded-rectangle shape in a vertical stack of buttons and prefer the capsule shape in a horizontal row of buttons.

**Use standard controls to take advantage of the audible feedback sounds people already know.** Audible feedback is especially important in visionOS, because the system doesn’t play haptics.

---

## Collaboration and sharing

Full page: `references/collaboration-and-sharing.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/collaboration-and-sharing

By default, the system supports screen sharing for an app running in the Shared Space by streaming the current window to other collaborators. If one person transitions the app to a Full Space while sharing is in progress, the system pauses the stream for other people until the app returns to the Shared Space. For guidance, see [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences).

---

## Color

Full page: `references/color.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/color

**Use color sparingly, especially on glass.** Standard visionOS windows typically use the system-defined glass [Materials](https://developer.apple.com/design/human-interface-guidelines/materials), which lets light and objects from people’s physical surroundings and their space show through. Because the colors in these physical and virtual objects are visible through the glass, they can affect the legibility of colorful app content in the window. Prefer using color in places where it can help call attention to important information or show the relationship between parts of the interface.

**Prefer using color in bold text and large areas.** Color in lightweight text or small areas can make them harder to see and understand.

**In a fully immersive experience, help people maintain visual comfort by keeping brightness levels balanced.** Although using high contrast can help direct people’s attention to important content, it can also cause visual discomfort if people’s eyes have adjusted to low light or darkness. Consider making content fully bright only when the rest of the visual context is also bright. For example, avoid displaying a bright object on a very dark or black background, especially if the object flashes or moves.

---

## Context menus

Full page: `references/context-menus.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/context-menus

**Consider using a context menu instead of a panel or inspector window to present frequently used functionality.** Minimizing the number of separate views or windows your app opens can help people keep their space uncluttered.

**In general, avoid letting a context menu’s height exceed the height of the window.** In visionOS, a window includes system-provided components above and below its top and bottom edges, such as window-management controls and the Share menu, so a context menu that’s too tall could obscure them. As you consider the number of items to include, be guided by the ways people are likely to use your app. For example, people who use an app to accomplish in-depth, specialist tasks often expect to spend time learning a large number of sophisticated commands and might appreciate contextual access to them. On the other hand, people who use an app to perform a few simple actions may appreciate short contextual menus that are quick to scan and use.

---

## Disclosure controls

Full page: `references/disclosure-controls.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/disclosure-controls

*(upstream heading: iOS, iPadOS, visionOS)*

Disclosure controls are available in iOS, iPadOS, and visionOS with the SwiftUI [DisclosureGroup](https://developer.apple.com/documentation/SwiftUI/DisclosureGroup) view.

---

## Drag and drop

Full page: `references/drag-and-drop.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/drag-and-drop

**When possible, launch your app to handle content that people drop into empty space.** When you associate a user activity with draggable app content, your app can open a window or scene that handles the content when people drop it. For example, when people drop a URL into empty space, it launches Safari; when people drop Quick Look–supported content, Quick Look launches to display it. For developer guidance, see [NSUserActivity](https://developer.apple.com/documentation/Foundation/NSUserActivity).

---

## Focus and selection

Full page: `references/focus-and-selection.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/focus-and-selection

visionOS supports the same focus system as in iPadOS and tvOS, letting people use a connected input device like a keyboard or game controller to interact with apps and the system.

> **Note:** When people look at a virtual object to identify it as the object they want to interact with, the system uses the *hover effect*, not a focus effect, to provide visual feedback (for guidance, see [Eyes](https://developer.apple.com/design/human-interface-guidelines/eyes)). The hover effect isn’t related to the focus system.

---

## Game controls

Full page: `references/game-controls.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/game-controls

**Match spatial game controller behavior to hand input.** In addition to supporting a wide array of wireless game controllers, your visionOS game can also support spatial game controllers such as PlayStation VR2 Sense controller. Allow players to interact with your game in a similar manner to how they interact using their hands. Specifically, support looking at an object and pressing the controller’s left or right trigger button to indirectly interact, or reaching out and pressing the left or right trigger button to directly interact. For more information, see [visionOS](https://developer.apple.com/design/human-interface-guidelines/gestures#visionOS).

---

## Gestures

Full page: `references/gestures.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/gestures

visionOS supports two categories of gestures: indirect and direct.

People use an *indirect* gesture by looking at an object to target it, and then manipulating that object from a distance — indirectly — with their hands. For example, a person can look at a button to focus it and select it by quickly tapping their finger and thumb together. Indirect gestures are comfortable to perform at any distance, and let people quickly change focus between different objects and select items with minimal movement.

People use a *direct* gesture to physically touch an interactive object. For example, people can directly type on the visionOS keyboard by tapping the virtual keys. Direct gestures work best when they are within reach. Because people may find it tiring to keep their arms raised for extended periods, direct gestures are best for infrequent use. visionOS also supports direct versions of all standard gestures, allowing people the choice to interact directly or indirectly with any standard component.

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

#### Designing custom gestures in visionOS

If you want to offer a specific interaction for your experience that people can’t perform using an existing system gesture, consider designing a custom gesture. To offer this type of interaction, your app needs to be running in a Full Space, and you must request people’s permission to access information about their hands. For developer guidance, see [Setting up access to ARKit data](https://developer.apple.com/documentation/visionOS/setting-up-access-to-arkit-data).

![A screenshot of a person's hands performing a custom gesture, placing the two hands together to form a heart, while playing a visionOS game.](https://docs-assets.developer.apple.com/published/363ecbc8eeb441809f62ae935e13fbdc/visionos-custom-spatial-gesture-happy-beam%402x.png)

**Prioritize comfort.** Continually test ergonomics of all interactions that require custom gestures. A custom interaction that requires people to keep their arms raised for even a little while can be physically tiring, and repeating very similar movements many times in succession can stress people’s muscles and joints.

**Carefully consider complex custom gestures that involve multiple fingers or both hands.** People may not always have both hands available when using your app or game. If you require a more complex gesture for your experience, consider also offering an alternative that requires less movement.

**Avoid custom gestures that require using a specific hand.** It can increase someone’s cognitive load if they need to remember which hand to use to trigger a custom gesture. It may also make your experience less welcoming to people with strong hand-dominance or limb differences.

#### Working with system overlays in visionOS

In visionOS 2 and later, people can look at the palm of one hand and use gestures to quickly access system overlays for Home and Control Center. These interactions are available systemwide, and are reserved solely for accessing system overlays.

> **Note:** The system overlay is the default method of accessing Control Center in visionOS 2 and later. The visionOS 1 behavior (looking upward) remains available as an accessibility setting.

When designing apps and games that use custom gestures or anchor content to a person’s hands, it’s important to take interactions with the system overlays into consideration.

**Reserve the area around a person’s hand for system overlays and their related gestures.** If possible, don’t anchor content to a person’s hands or wrists. If you’re designing a game that involves hand-anchored content, place it outside of the immediate area of someone’s hand to avoid colliding with the Home indicator.

![An illustration of a person's open hand with the palm facing upward. A dashed circular line above the hand indicates the area reserved for system overlays.](https://docs-assets.developer.apple.com/published/de8c04a523a3e225c723c5c09c458e1c/visionos-hand-area-of-focus%402x.png)

![An illustration of a person's open hand with the palm facing upward. A button with a circle icon representing the Home indicator appears above the palm.](https://docs-assets.developer.apple.com/published/961d33f07da24b20848f3502d2cea134/visionos-spatial-gesture-home-indicator%402x.png)

![An illustration of a person's open hand with the palm facing downward. An overlay with the status bar appears above the hand.](https://docs-assets.developer.apple.com/published/f1d5a8816f65f35853ccd513355272d8/visionos-spatial-gesture-control-center%402x.png)

**Consider deferring the system overlay behavior when designing an immersive app or game.** In certain circumstances, you may not want the Home indicator to appear when someone looks at the palm of their hand. For example, a game that uses virtual hands or gloves may want to keep someone within the world of the story, even if they happen to look at their hands from different angles. In such cases, when your app is running in a Full Space, you can choose to require a tap to reveal the Home indicator instead. For developer guidance, see [persistentSystemOverlays(_:)](https://developer.apple.com/documentation/SwiftUI/View/persistentSystemOverlays(_:)).

![An image of a person's open hand with the palm facing upward, shown from the person's perspective. A button with a circle icon representing the Home indicator appears above the palm. The image background shows the room that's the person's surroundings.](https://docs-assets.developer.apple.com/published/dc6b4a94633c063ddd432dcc8043cae3/gestures-default-home-indicator%402x.png)

![An image of a person's open hand with the palm facing upward, shown from the person's perspective. A button with a circle icon representing the Home indicator appears above the palm. The image background shows a forest in a fully immersive space.](https://docs-assets.developer.apple.com/published/96cb708d391f1ab78a77d23c7f2e0442/gestures-home-indicator-in-immersive-space%402x.png)

![An image of a person's open hand wearing a bulky space suit glove, shown from the person's perspective. The palm faces upward, and no button appears above it. The image background shows a starry sky in a fully immersive space.](https://docs-assets.developer.apple.com/published/b978fe99b00df892890e1d194f704a83/gestures-fully-immersive-game-with-glove%402x.png)

> **Note:** Apps and games that you built for visionOS 1 defer the system overlay behavior by default. When a person looks at their palm with your app running in a Full Space, the Home indicator won’t appear unless they tap first.

**Use caution when designing custom gestures that involve a rolling motion of the hand, wrist, and forearm.** This specific motion is reserved for revealing system overlays. Since system overlays always display on top of app content and your app isn’t aware of when they’re visible, it’s important to test any custom gestures or content that might conflict.

---

## Image views

Full page: `references/image-views.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/image-views

Windows in visionOS apps and games can use image views to display 2D and stereoscopic images, as well as spatial photos. If your app uses RealityKit, you can also display images of any type outside of image views next to 3D content, or generate a spatial scene from an existing 2D image. For design guidance, see [visionOS](https://developer.apple.com/design/human-interface-guidelines/images#visionOS); for developer guidance, see [ImagePresentationComponent](https://developer.apple.com/documentation/RealityKit/ImagePresentationComponent).

For guidance on presenting other 3D content in a window or volume, see [visionOS](https://developer.apple.com/design/human-interface-guidelines/windows#visionOS).

---

## Images

Full page: `references/images.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/images

In visionOS, people can view images at a much larger range of sizes than in any other platform, and the system dynamically scales the image resolution to match the current size. Because you can position images at specific angles within someone’s surroundings, image pixels may not line up 1:1 with screen pixels.

**Create a layered app icon.** App icons in visionOS are composed of two to three layers that provide the appearance of depth by moving at subtly different rates when the icon is in focus. For guidance, see [Layer design](https://developer.apple.com/design/human-interface-guidelines/app-icons#Layer-design).

**Prefer vector-based art for 2D images.** Avoid bitmap content because it might not look good when the system scales it up. If you use Core Animation layers, see [Drawing sharp layer-based content in visionOS](https://developer.apple.com/documentation/visionOS/drawing-sharp-layer-based-content) for developer guidance.

**If you need to use rasterized images, balance quality with performance as you choose a resolution.** Although a @2x image looks fine at common viewing distances, its fixed resolution means that the system doesn’t dynamically scale it and it might not look sharp from close up. To help a rasterized image look sharp when people view it from a wide range of distances, you can use a higher resolution, but each increase in resolution results in a larger file size and may impact your app’s runtime performance, especially for resolutions over @6x. If you use images that have resolutions higher than @2x, be sure to also apply high-quality image filtering to help balance quality and performance (for developer guidance, see [filters](https://developer.apple.com/documentation/QuartzCore/CALayer/filters)).

#### Spatial photos and spatial scenes

In addition to 2D and stereoscopic images, visionOS apps and games can use RealityKit to display spatial photos and spatial scenes. A *spatial photo* is a stereoscopic photo with additional spatial metadata, as captured on iPhone 15 Pro or later, Apple Vision Pro, or other compatible camera. A *spatial scene* is a 3D image generated from a 2D image to add a parallax effect that responds to head movement. For developer guidance, see [ImagePresentationComponent](https://developer.apple.com/documentation/RealityKit/ImagePresentationComponent).

**Make sure spatial photos render correctly in your app.** Use the stereo High-Efficiency Image Codec (HEIC) format to display a spatial photo in your app. When you add spatial metadata to a stereo HEIC, visionOS recognizes the photo as spatial and includes visual treatments that help minimize common causes of stereo-viewing discomfort.

**Prefer the feathered glass background effect to display text over spatial photos.** If you need to place text over a spatial photo in your app or game, use the feathered glass background effect. The effect adds contrast to make the text readable, and it blurs out detail to help reduce visual discomfort when people view text over spatial photos. For developer guidance, see [GlassBackgroundEffect](https://developer.apple.com/documentation/SwiftUI/GlassBackgroundEffect).

**Take visual comfort into consideration when you make spatial photos from existing 2D content.** When adjusting the spatial metadata of a photo for your app or game, consider how you want people to view your content. Metadata like disparity adjustment can alter how people perceive the 3D scene, and can cause visual discomfort from certain viewing positions. For developer guidance, see [Creating spatial photos and videos with spatial metadata](https://developer.apple.com/documentation/ImageIO/Creating-spatial-photos-and-videos-with-spatial-metadata).

**Display spatial photos and spatial scenes in standalone views.** Avoid displaying spatial photos inline with other content, as this can cause visual discomfort. Instead, showcase spatial photos or spatial scenes in a separate view, like a sheet or window. If you must display stereoscopic images inline, provide generous spacing between the image and any inline content to help people’s eyes adjust to the depth changes.

**Use spatial scenes in your app for specific moments.** Each spatial scene can take up to several seconds to generate from an existing image. Design experiences with this limitation in mind. For instance, the Photos app offers an explicit action to create a spatial scene while immersed in a single photo. Avoid displaying too many spatial scenes at once. Instead, use scroll views, pagination, or explicit actions to move to new photos and keep the visual information hierarchy simple.

**When displaying immersively, prefer minimal UI.** For example, the Spatial Gallery app displays a single piece of content with a small caption and a single Back button, relying on swipe gestures to navigate between items.

**Prefer displaying larger spatial scenes that you center in someone’s field of view.** When people view a spatial scene, they may move their head laterally to view the parallax effect. Smaller spatial scenes provide less of a parallax effect and may not be as impactful to viewers.

---

## Keyboards

Full page: `references/keyboards.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/keyboards

In visionOS, an app’s keyboard shortcuts appear in the shortcut interface that displays when people hold the Command key on a connected keyboard. Similar in organization to an app’s [The menu bar](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar) on iPad or Mac, the shortcut interface on Apple Vision Pro displays app commands in familiar system-defined menu categories such as File, Edit, and View. Unlike menu bar menus, the shortcut interface displays all relevant categories in one view, listing within each category only available commands that also have shortcuts.

**Write descriptive shortcut titles.** Because the shortcut interface displays a flat list of all items in each category, submenu titles aren’t available to provide context for their child items. Make sure each shortcut title is descriptive enough to convey its action without the additional context a submenu title might provide. For developer guidance, see [discoverabilityTitle](https://developer.apple.com/documentation/UIKit/UIKeyCommand/discoverabilityTitle).

**Recognize that people see an overlay when they use a physical keyboard with your visionOS app or game.** When people connect a physical keyboard while using your visionOS app or game, the system displays a virtual keyboard overlay that provides typing completion and other controls.

---

## Launching

Full page: `references/launching.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/launching

**Consider launching in the Shared Space even if your app is fully immersive.** Opening a window in the Shared Space lets you provide more context about your app or game while giving it time to load, and it also lets you present a control that people can use to open your fully immersive experience. In general, people appreciate being able to choose when to transition to a Full Space, especially if they’re currently running other apps in the Shared Space. For guidance, see [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences).

---

## Layout

Full page: `references/layout.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/layout

The guidance below can help you lay out content within the windows of your visionOS app or game, making it feel familiar and easy to use. For guidance on displaying windows in space and best practices for using depth, scale, and field of view in your visionOS app, see [Spatial layout](https://developer.apple.com/design/human-interface-guidelines/spatial-layout). To learn more about visionOS window components, see [visionOS](https://developer.apple.com/design/human-interface-guidelines/windows#visionOS).

> **Note:** When you add depth to content in a standard window, the content extends beyond the window’s bounds along the z-axis. If content extends too far along the z-axis, the system clips it.

**Consider centering the most important content and controls in your app or game.** Often, people can more easily discover and interact with content when it’s near the middle of a window, especially when the window is large.

**Keep a window’s content within its bounds.** In visionOS, the system displays window controls just outside a window’s bounds in the XY plane. For example, the Share menu appears above the window and the controls for resizing, moving, and closing the window appear below it. Letting 2D or 3D content encroach on these areas can make the system-provided controls, especially those below the window, difficult for people to use.

**If you need to display additional controls that don’t belong within a window, use an ornament.** An ornament lets you offer app controls that remain visually associated with a window without interfering with the system-provided controls. For example, a window’s toolbar and tab bar appear as ornaments. For guidance, see [Ornaments](https://developer.apple.com/design/human-interface-guidelines/ornaments).

**Make a window’s interactive components easy for people to look at.** You need to include enough space around an interactive component so that visually identifying it is easy and comfortable, and to prevent the system-provided hover effect from obscuring other content. For example, place buttons so their centers are at least 60 points apart. For guidance, see [Eyes](https://developer.apple.com/design/human-interface-guidelines/eyes), [Spatial layout](https://developer.apple.com/design/human-interface-guidelines/spatial-layout), and [visionOS](https://developer.apple.com/design/human-interface-guidelines/buttons#visionOS).

---

## Lists and tables

Full page: `references/lists-and-tables.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/lists-and-tables

*(upstream heading: iOS, iPadOS, visionOS)*

**Use an info button only to reveal more information about a row’s content.** An info button — called a *detail disclosure button* when it appears in a list row — doesn’t support navigation through a hierarchical table or list. If you need to let people drill into a list or table row’s subviews, use a disclosure indicator accessory control. For developer guidance, see [UITableViewCell.AccessoryType.disclosureIndicator](https://developer.apple.com/documentation/UIKit/UITableViewCell/AccessoryType-swift.enum/disclosureIndicator).

![An illustration of a grouped list of rows. Each list item includes an info button at the trailing end of the row.](https://docs-assets.developer.apple.com/published/fd301d26835e0341b95eaa2027f200f2/info-button-in-list%402x.png)

![An illustration of a grouped list of rows. Each list item includes a right-pointing chevron at the trailing end of the row.](https://docs-assets.developer.apple.com/published/dcb3678fe458846713b03756ab5e1a28/disclosure-indicator-in-list%402x.png)

**Avoid adding an index to a table that displays controls — like disclosure indicators — in the trailing ends of its rows.** An *index* typically consists of the letters in an alphabet, displayed vertically at the trailing side of a list. People can jump to a specific section in the list by choosing the index letter that maps to it. Because both the index and elements like disclosure indicators appear on the trailing side of a list, it can be difficult for people to use one element without activating the other.

---

## Live Photos

Full page: `references/live-photos.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/live-photos

In visionOS, people can view a Live Photo, but they can’t capture one.

---

## Materials

Full page: `references/materials.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/materials

In visionOS, windows generally use an unmodifiable system-defined material called *glass* that helps people stay grounded by letting light, the current Environment, virtual content, and objects in people’s surroundings show through. Glass is an adaptive material that limits the range of background color information so a window can continue to provide contrast for app content while becoming brighter or darker depending on people’s physical surroundings and other virtual content.

> **Note:** visionOS doesn’t have a distinct Dark Mode setting. Instead, glass automatically adapts to the luminance of the objects and colors behind it.

**Prefer translucency to opaque colors in windows.** Areas of opacity can block people’s view, making them feel constricted and reducing their awareness of the virtual and physical objects around them.

![An illustration of a field of view in visionOS with a window in the center. The window has an opaque background that obstructs its surroundings.](https://docs-assets.developer.apple.com/published/dafc40e7902535eecb404a446aa26199/materials-visionos-opaque-window-incorrect%402x.png)

![An X in a circle to indicate incorrect usage](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

![An illustration of a field of view in visionOS with a window in the center. The window has a translucent material background that allows its surroundings to pass through.](https://docs-assets.developer.apple.com/published/f9fc72228240c9b44f3c4b78204fdf52/materials-visionos-glass-window%402x.png)

![A checkmark in a circle to indicate correct usage](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

**If necessary, choose materials that help you create visual separations or indicate interactivity in your app.** If you need to create a custom component, you may need to specify a system material for it. Use the following examples for guidance.

- The [thin](https://developer.apple.com/documentation/SwiftUI/Material/thin) material brings attention to interactive elements like buttons and selected items.
- The [regular](https://developer.apple.com/documentation/SwiftUI/Material/regular) material can help you visually separate sections of your app, like a sidebar or a grouped table view.
- The [thick](https://developer.apple.com/documentation/SwiftUI/Material/thick) material lets you create a dark element that remains visually distinct when it’s on top of an area that uses a `regular` background.

![An illustration of a field of view in visionOS with a window in the center. The window is composed of a sidebar on the left and a content area on the right, with a text field at the top and a button in the lower-right corner. The sidebar uses regular material, while the text field uses thick material and the button uses thin material.](https://docs-assets.developer.apple.com/published/fb018620e0723711478c370be3155db0/visionos-materials-window-example%402x.png)

To ensure foreground content remains legible when it displays on top of a material, visionOS applies vibrancy to text, symbols, and fills. Vibrancy enhances the sense of depth by pulling light and color forward from both virtual and physical surroundings.

visionOS defines three vibrancy values that help you communicate a hierarchy of text, symbols, and fills.

- Use [UIVibrancyEffectStyle.label](https://developer.apple.com/documentation/UIKit/UIVibrancyEffectStyle/label) for standard text.
- Use [UIVibrancyEffectStyle.secondaryLabel](https://developer.apple.com/documentation/UIKit/UIVibrancyEffectStyle/secondaryLabel) for descriptive text like footnotes and subtitles.
- Use [UIVibrancyEffectStyle.tertiaryLabel](https://developer.apple.com/documentation/UIKit/UIVibrancyEffectStyle/tertiaryLabel) for inactive elements, and only when text doesn’t need high legibility.

![An illustration of a Share button with a translucent background material and a symbol. The symbol uses the default vibrant label color and has very high contrast against the background material.](https://docs-assets.developer.apple.com/published/3bb528e0723e62cc01d4c4f0da86397a/materials-visionos-label-vibrant-primary%402x.png)

![An illustration of a Share button with a translucent background material and a symbol. The symbol uses the secondary vibrant label color and has high contrast against the background material.](https://docs-assets.developer.apple.com/published/251390eaada0013960348d8620552946/materials-visionos-label-vibrant-secondary%402x.png)

![An illustration of a Share button with a translucent background material and a symbol. The symbol uses the tertiary vibrant label color and has muted contrast against the background material.](https://docs-assets.developer.apple.com/published/dcced2657d03292209f6ab7e928b85f6/materials-visionos-label-vibrant-tertiary%402x.png)

---

## Menus

Full page: `references/menus.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/menus

In visionOS, a menu can display items using the small or large layout styles that iOS and iPadOS define (for guidance, see [iOS, iPadOS](https://developer.apple.com/design/human-interface-guidelines/menus#iOS-iPadOS)). You can present a menu in your app or game from 3D content using a SwiftUI view. To ensure that your menu is always visible to people, even when other content occludes it, you can apply a [breakthrough effect](https://developer.apple.com/documentation/swiftui/view/presentationbreakthrougheffect(_:)). As in macOS, an open menu in a visionOS window can appear outside of the window’s boundaries.

**Prefer displaying a menu near the content it controls.** Because people need to look at a menu item before tapping it, they might miss the item’s effect if the content it controls is too far away.

![A partial screenshot showing an app window in visionOS. The window contains several buttons, including a 'More' button, which is selected. A menu containing a list of actions is displayed beneath the button.](https://docs-assets.developer.apple.com/published/ebdeac86703b1a5e8b3da0f2d91fa702/visionos-notes-menu-popover-style%402x.png)

**Prefer the subtle breakthrough effect in most cases.** This effect blends the presentation with its surrounding content, to maintain legibility and usability while preserving the depth and context of the scene. When you select [automatic](https://developer.apple.com/documentation/SwiftUI/BreakthroughEffect/automatic) for the breakthrough effect of a menu that overlaps with 3D content, the system applies [subtle](https://developer.apple.com/documentation/SwiftUI/BreakthroughEffect/subtle) by default. You can use [prominent](https://developer.apple.com/documentation/SwiftUI/BreakthroughEffect/prominent) if it’s important to display a menu prominently over the entire scene in your app or game, but this can disrupt the experience for people and potentially cause discomfort. Alternatively, you can use [none](https://developer.apple.com/documentation/SwiftUI/BreakthroughEffect/none) to fully occlude your menu behind other 3D content — for example, in a puzzle game that requires people to navigate around barriers — but this may make it difficult for people to see and access the menu.

---

## Motion

Full page: `references/motion.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/motion

In addition to subtly communicating context, drawing attention to information, and enriching immersive experiences, motion in visionOS can combine with [Depth](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Depth) to provide essential feedback when people look at interactive elements. Because motion is likely to be a large part of your visionOS experience, it’s crucial to avoid causing distraction, confusion, or discomfort.

**As much as possible, avoid displaying motion at the edges of a person’s field of view.** People can be particularly sensitive to motion that occurs in their peripheral vision: in addition to being distracting, such motion can even cause discomfort because it can make people feel like they or their surroundings are moving. If you need to show an object moving in the periphery during an immersive experience, make sure the object’s brightness level is similar to the rest of the visible content.

**Help people remain comfortable when showing the movement of large virtual objects.** If an object is large enough to fill a lot of the [Field of view](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Field-of-view), occluding most or all of [Immersion and passthrough](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences#Immersion-and-passthrough), people can naturally perceive it as being part of their surroundings. To help people perceive the object’s movement without making them think that they or their surroundings are moving, you can increase the object’s translucency, helping people see through it, or lower its contrast to make its motion less noticeable.

> **Note:** People can experience discomfort even when they’re the ones moving a large virtual object, such as a window. Although adjusting translucency and contrast can help in this scenario, consider also keeping a window’s size fairly small.

**Consider using fades when you need to relocate an object.** When an object moves from one location to another, people naturally watch the movement. If such movement doesn’t communicate anything useful to people, you can fade the object out before moving it and fade it back in after it’s in the new location.

**In general, avoid letting people rotate a virtual world.** When a virtual world rotates, the experience typically upsets people’s sense of stability, even when they control the rotation and the movement is subtle. Instead, consider using instantaneous directional changes during a quick fade-out.

**Consider giving people a stationary frame of reference.** It can be easier for people to handle visual movement when it’s contained within an area that doesn’t move. In contrast, if the entire surrounding area appears to move — for example, in a game that automatically moves a player through space — people can feel unwell.

**Avoid showing objects that oscillate in a sustained way.** In particular, you want to avoid showing an oscillation that has a frequency of around 0.2 Hz because people can be very sensitive to this frequency. If you need to show objects oscillating, aim to keep the amplitude low and consider making the content translucent.

---

## Multitasking

Full page: `references/multitasking.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/multitasking

On Apple Vision Pro, people can run multiple apps at the same time in the Shared Space, viewing and switching between windows and volumes throughout the space.

Only one window is active at a time in the Shared Space. When people look from one window to another, the window they’re currently looking at becomes active while the previous window becomes more translucent and appears to recede along the z-axis. Closing an app window in the Shared Space transitions the app to the background without quitting it.

> **Note:** When an app is the Now Playing app, closing its window automatically pauses audio playback; if people want to resume playback, they can do so in Control Center without opening the window.

**Avoid interfering with the system-provided multitasking behavior.** When people look from one window to another, visionOS applies a feathered mask to the window they look away from to clarify its changed state. To avoid interfering with this visual feedback, don’t change the appearance of a window’s edges.

**Don’t pause a window’s video playback when people look away from it.** In visionOS, as in macOS, people expect the playback they start in one window to continue while they view or perform a task in another window.

**Be prepared for situations where your audio can duck.** Unless an app is currently the Now Playing app, its audio can duck when people look away from it to another app.

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

## Page controls

Full page: `references/page-controls.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/page-controls

In visionOS, page controls represent available pages and indicate the current page, but people don’t interact with them.

---

## Playing audio

Full page: `references/playing-audio.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/playing-audio

Subtle, expressive sounds are everywhere in visionOS, enhancing experiences and providing essential feedback when people look at a virtual object and use gestures to interact with it. The system combines audio algorithms with information about a person’s physical surroundings to produce *Spatial Audio*, which is sound that people can perceive as coming from specific locations in space, not just from speakers.

> **Important:** In visionOS, as in every platform, avoid communicating important information using only sound. Always provide additional ways to help people understand your app. For guidance, see [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility).

In visionOS, audio playback from the Now Playing app pauses automatically when people close the app’s window, and audio from an app that isn’t the Now Playing app can duck when people look away from it to different app.

**Prefer playing sound.** People generally choose to keep sounds audible while they’re wearing the device, so an app that doesn’t play sound — especially in an immersive moment — can feel lifeless and may even seem broken. Throughout the design process, look for opportunities to create meaningful sounds that aid navigation and help people understand the spatial qualities of your app.

**Design custom sounds for custom UI elements.** In general, a system-provided element plays sound to help people locate it and receive feedback when they interact with it. To help people interact with your custom elements, design sounds that provide feedback and enhance the spatial experience of your app.

**Use Spatial Audio to create an intuitive, engaging experience.** Because people can perceive Spatial Audio as coming from anywhere around them, it works especially well in a fully immersive context as a way to help an experience feel lifelike. *Ambient audio* provides pervasive sounds that can help anchor people in a virtual world and an *audio source* can sound like it comes from a specific object. As you build the soundscape for your app, consider using both types of audio.

**Consider defining a range of places from which your app sounds can originate.** Spatial Audio helps people locate the object that’s making sound, whether it’s stationary or moving in space. For example, when people move an app window that’s playing audio, the sound continues to come directly from the window, wherever people move it.

**Consider varying sounds that people could perceive as repetitive over time.** For example, the system subtly varies the pitch and volume of the virtual keyboard’s sounds, suggesting the different sounds a physical keyboard can make as people naturally vary the speed and forcefulness of their typing. An efficient way to achieve a pleasing variation in sound is to randomize a sound file’s pitch and volume during playback, instead of creating different files.

**Decide whether you need to play sound that’s fixed to the wearer or tracked by the wearer.** People perceive *fixed* sound as if it’s pointed at them, regardless of the direction they look or the virtual objects they move. In contrast, people tend to perceive *tracked* sound as coming from a particular object, so moving the object closer or farther away changes what they hear. In general, you want to use tracked sound to enhance the realism of your experience, but there could be cases where fixed sound is a good choice. For example, Mindfulness uses fixed sound to envelop the wearer in an engaging, peaceful setting.

---

## Playing video

Full page: `references/playing-video.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/playing-video

**Help people stay comfortable when playing video in your app.** Often, an app doesn’t control the content in the videos it plays, but you can help people stay comfortable by:

- Letting them choose when to start playing a video
- Using a small window for playback, letting people resize it if they want
- Making sure people can see their surroundings during playback

**In a fully immersive experience, avoid letting virtual content obscure playback or transport controls.** In a fully immersive context, the system automatically places the video player at a predictable location that provides an optimal viewing experience. Use this location to help make sure that no virtual content occludes the default playback or transport controls in the ornament near the bottom of the player.

**Avoid automatically starting a fully immersive video playback experience.** People need control over their experience and they’re unlikely to appreciate being launched into a fully immersive video without warning.

**Create a thumbnail track if you want to support scrubbing.** The system displays thumbnails as people scrub to different times in the video, helping them choose the section they want. To improve performance, supply a set of thumbnails that each measure 160 px in width. For developer guidance, see [HTTP Live Streaming (HLS) Authoring Specification for Apple Devices > Trick Play](https://developer.apple.com/documentation/http-live-streaming/hls-authoring-specification-for-apple-devices#Trick-Play).

**Avoid expanding an inline video player to fill a window.** When you display the system-provided player view in a window, playback controls appear in the same plane as the player view and not in an ornament that floats above the window. Inline video needs to be 2D and you want to make sure that window content remains visible around the player so people don’t expect a more immersive playback experience. For developer guidance, see [AVPlayerViewController](https://developer.apple.com/documentation/AVKit/AVPlayerViewController).

**Use a RealityKit video player if you need to play video in a view like a splash screen or a transitional view.** In situations like these, people generally expect the video to lead into the next experience, so they don’t need playback controls or system-provided integration, like dimming and view anchoring. The RealityKit video player automatically uses the correct aspect ratio for both 2D and 3D video and supports closed captions. RealityKit can also help you play video as a special effect on the surface of a custom view or object. For developer guidance, see [RealityKit](https://developer.apple.com/documentation/RealityKit).

---

## Pointing devices

Full page: `references/pointing-devices.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/pointing-devices

In visionOS, people can attach an external pointing device or keyboard, and use both devices while they continue to use their eyes and hands. If people look at an element and then move the pointer, the system brings focus to the element under the pointer. Your app doesn’t have to do anything to support this behavior.

When a pointing device is attached, the area people are looking at determines the pointer’s context. For example, when people shift their eyes from one window to another, the pointer’s context seamlessly transitions to the new window.

When people use an attached pointing device that supports gestures, like a trackpad or mouse, the pointer hides while people are gesturing, minimizing visual distraction. In this scenario, the pointer remains hidden until people move it, when it reappears in the location they’re looking at.

---

## Privacy

Full page: `references/privacy.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/privacy

By default, visionOS uses ARKit algorithms to handle features like persistence, world mapping, segmentation, matting, and environment lighting. These algorithms are always running, allowing apps and games to automatically benefit from ARKit while in the Shared Space.

ARKit doesn’t send data to apps in the Shared Space; to access ARKit APIs, your app must open a Full Space. Additionally, features like Plane Estimation, Scene Reconstruction, Image Anchoring, and Hand Tracking require people’s permission to access any information. For developer guidance, see [Setting up access to ARKit data](https://developer.apple.com/documentation/visionOS/setting-up-access-to-arkit-data).

In visionOS, user input is private by design. The system automatically displays hover effects when people look at interactive components you create using SwiftUI or RealityKit, giving people the visual feedback they need without exposing where they’re looking before they tap. For guidance, see [Eyes](https://developer.apple.com/design/human-interface-guidelines/eyes) and [visionOS](https://developer.apple.com/design/human-interface-guidelines/gestures#visionOS).

Developer access to device cameras works differently in visionOS than it does in other platforms. Specifically, the back camera provides blank input and is only available as a compatibility convenience; the front camera provides input for [visionOS](https://developer.apple.com/design/human-interface-guidelines/shareplay#visionOS), but only after people grant their permission. If the iOS or iPadOS app you’re bringing to visionOS includes a feature that needs camera access, remove it or replace it with an option for people to import content instead. For developer guidance, see [Making your existing app compatible with visionOS](https://developer.apple.com/documentation/visionOS/making-your-app-compatible-with-visionos).

---

## Scroll views

Full page: `references/scroll-views.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/scroll-views

In visionOS, the scroll indicator has a small, fixed size to help communicate that people can scroll efficiently without making large movements. To make it easy to find, the scroll indicator always appears in a predictable location with respect to the window: vertically centered at the trailing edge during vertical scrolling and horizontally centered at the window’s bottom edge during horizontal scrolling.

When people begin swiping content in the direction they want it to scroll, the scroll indicator appears at the window’s edge, visually reinforcing the effect of their gesture and providing feedback about the content’s current position and overall length. When people look at the scroll indicator and begin a drag gesture, the indicator enables a jog bar experience that lets people manipulate the scrolling speed instead of the content’s position. In this experience, the scroll indicator reveals tick marks that speed up or slow down as people make small adjustments to their gesture, providing visual feedback that helps people precisely control scrolling acceleration.

**If necessary, account for the size of the scroll indicator.** Although the indicator’s overall size is small, it’s a little thicker than the same component in iOS. If your content uses tight margins, consider increasing them to prevent the scroll indicator from overlapping the content.

#### Look to Scroll

In views that support Look to Scroll, people can scroll using only their eyes. Scrolling starts when people look near the boundary of the scroll view — along the top and bottom for vertical scroll views, or along the sides for horizontal scroll views. For example, a person can look at the bottom edge of a Safari window to scroll the page down, or look at an album on the trailing edge in the Music app to scroll it horizontally toward the center of the page. Look to Scroll works in conjunction with existing behavior, so someone can choose whether to use a gesture or their eyes to scroll. For developer guidance, see [look](https://developer.apple.com/documentation/SwiftUI/ScrollInputKind/look).

**Support Look to Scroll for reading or browsing views.** Because Look to Scroll doesn’t work by default, you need to add support for it to each individual scroll view. If your app contains reading or browsing views, add support for Look to Scroll to provide a comfortable and hands-free experience. For developer guidance, see [ScrollInputKind](https://developer.apple.com/documentation/SwiftUI/ScrollInputKind).

**Avoid using Look to Scroll for secondary content.** In general, support standard gestures — but not Look to Scroll — in views that contain UI controls or dense information that requires quick, precise scrolling. For example, the Notes app offers Look to Scroll within the main view to let people easily read their content, but doesn’t support it for the list of notes.

**Maintain consistency across content.** If you support Look to Scroll for one view in your app, make sure to support it for all similar views. For example, if you offer several collection views of videos throughout your app, support Look to Scroll for each of these views so people know what to expect.

**Define clear scroll areas within your app.** In views that support Look to Scroll, prefer making the view the full width or full height of the window. This gives people generous space to scroll and provides clear edges. If you inset a scroll view from a window, like in the Notes app, provide clear boundaries so people know where to look.

**If your app uses custom scroll effects or animations, remove them before supporting Look to Scroll.** Custom effects that use scroll position to change content, such as parallax effects and animations, can cause Look to Scroll to behave unexpectedly.

---

## Segmented controls

Full page: `references/segmented-controls.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/segmented-controls

When people look at a segmented control that uses icons, the system displays a tooltip that contains the descriptive text you supply.

---

## SharePlay

Full page: `references/shareplay.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/shareplay

People expect most visionOS apps to support SharePlay. While wearing Apple Vision Pro, people choose the Spatial option in FaceTime to share content and activities with others.

In a shared activity, FaceTime can show representations of other participants — called spatial Personas — within each wearer’s space, making everyone feel like they’re sharing the same experience in the same place. During a shared experience in FaceTime, people can interact with each other in natural ways through their spatial Personas. For example, people can speak or gesture directly to others, tell when someone is paying attention to them, and know which person is using a shared tool or resource.

visionOS uses the concept of *shared context* to describe the characteristics of a shared activity that help people feel physically present with others while connecting over the same content. A shared context helps give people confidence that they’re experiencing the same thing as everyone else.

When people feel that they’re truly sharing an experience, social dynamics can encourage authentic, intuitive interactions. For example, people can communicate verbally and nonverbally to make plans, take turns, and share resources.

> **Note:** During a shared activity, the system helps preserve people’s privacy by obscuring some visual details about wearers. In addition, a person can adjust their spatial Persona if they want. Although the system can place spatial Personas shoulder to shoulder and it supports shared gestures like a handshake or “high five,” spatial Personas remain apart.

**Choose the spatial Persona template that suits your shared activity.** When you design a shared activity, you can use a spatial Persona template to specify a layout for arranging spatial Personas in the shared activity space. The system provides three spatial Persona templates: side-by-side, surround, and conversational.

The side-by-side template places participants next to each other along a curved line segment, all facing the shared content. The side-by-side template gives everyone a great view of the content, making it a good choice for helping people watch media together. Because people aren’t facing each other in this arrangement, the side-by-side template can encourage less nonverbal interaction than other spatial Persona templates.

![An illustration representing a side-by-side shared activity in visionOS. Participants are positioned next to one another and facing a shared screen.](https://docs-assets.developer.apple.com/published/165cd2e63eb739bc3209ac651d63b0d7/visionos-shareplay-side-by-side%402x.png)

The system-applied surround template arranges participants all the way around the shared content in the center. This spatial Persona template works especially well when the content is 3D, because each participant views it from a different angle. In the surround template, participants face each other as if they were grouped around a table, promoting both verbal and nonverbal interactions.

![An illustration representing a surround shared activity in visionOS. Participants are gathered in a circle around shared content.](https://docs-assets.developer.apple.com/published/a3653114364ca9d18cbaaec62c6d1cba/visionos-shareplay-surround%402x.png)

The conversational template also groups participants around a center point, but places your content along the circle, not at its center. Because of this position, not everyone has the same view of your content, and it might not be convenient for everyone to interact with it. Consider using the conversational arrangement if your experience is more about people being together while your app performs a task in the background like playing music.

![An illustration representing a conversational shared activity in visionOS. Participants are positioned in a semi-circle formation around shared content.](https://docs-assets.developer.apple.com/published/6606d08491fb7172de59f9f745c32b8f/visionos-shareplay-conversational%402x.png)

For developer guidance, see [SystemCoordinator](https://developer.apple.com/documentation/GroupActivities/SystemCoordinator) and [SpatialTemplatePreference](https://developer.apple.com/documentation/GroupActivities/SpatialTemplatePreference).

**Be prepared to launch directly into your shared activity.** When one person shares your activity with others on a FaceTime call, the system minimizes friction by automatically launching your app for everyone. In this scenario, you want to avoid displaying any windows that aren’t related to the shared activity. For example, if people need to sign in before joining the activity, be sure to present this task in an autodismissible window that disappears as soon as people finish providing the required input.

**Help people enter a shared activity together, but don’t force them.** When one participant changes their level of immersion, the system tells you so you can synchronize the experience for everyone. Before synchronizing, check whether changing a person’s level of immersion would disrupt their current task; if it would, offer them the choice to join the updated experience. For example, if someone is editing content in an unshared window, you might present an alert that lets them choose to transition. For guidance, see [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences).

**Smoothly update a shared activity when new participants join.** When someone joins an in-progress activity, you need to integrate them without disrupting the experience for everyone else. For example, it’s important to update shared immersive content to keep all participants synchronized. Also, consider designing ways to accommodate up to five participants in your arrangement, updating their positions as necessary.

#### Maintaining a shared context

When your shared activity runs in a Full Space, the system helps your app maintain a shared context by using a single coordinate system to arrange your content and all participants, automatically synchronizing the size, position, and orientation of your app for each person. You’re responsible for displaying objects, playing sounds, and supporting interactions in ways that enhance the feeling of sharing the experience.

**Make sure everyone views the same state of your app.** If your app has more than one state — such as a media app that provides both minimal and theater-like viewing modes — you need to avoid letting different participants view different states, because doing so can diminish people’s sense of being together in a shared space. The exception to this is when someone needs to temporarily exit a shared activity; for guidance, see [Adjusting a shared context](https://developer.apple.com/design/human-interface-guidelines/shareplay#Adjusting-a-shared-context).

**Use Spatial Audio to enrich your shared activity.** Playing Spatial Audio can help you strengthen the realism of the shared experience. For guidance, see [Playing audio](https://developer.apple.com/design/human-interface-guidelines/playing-audio).

**When possible, let people discover natural, social solutions to confusions or conflicts that might arise during a shared experience.** For example, if only one participant at a time can use a virtual tool, avoid displaying UI, like tool-use controls or notifications, and instead let people speak or gesture to the group when they want to use the tool. If conflicts can arise during your shared activity — for example, if multiple people try to change the same content at the same time — consider implementing a simple rule, like last change wins, and letting people use the rule to define behavior that’s acceptable to the group.

**Help people keep their private and shared content separate.** By default, the system clearly differentiates a shared window from windows that aren’t shared. For example, when people use Music to listen together, the shared Music window appears as a new window for everyone, while any individual’s open library window remains separate and unshared. If your app can open multiple windows, help people share the one they want and make it easy for them to distinguish shared from unshared windows. If possible, also let people drag content they want to share from a private window to a shared one.

#### Adjusting a shared context

Sometimes, it makes sense to adjust the shared context of a shared activity so each participant can customize their experience, such as for comfort or accessibility. In other situations, strictly maintaining a shared context might decrease people’s enjoyment of the experience. For example, when content has only one ideal viewing angle, each participant might need their own.

**Let people personalize their experience without changing the experience for others.** For example, people might need to adjust various settings, like volume or subtitles, to make views and interactions accessible or make themselves more comfortable.

![An image of a TV window in visionOS. The image is split down the center to contrast the personalized experiences of two people: Person 1 has subtitles turned on, while Person 2 has subtitles turned off.](https://docs-assets.developer.apple.com/published/d219149ff83746d8e664c078b451f098/visionos-shareplay-subtitles-personalization%402x.png)

**Consider when to give each participant a unique view of the shared content.** Some content looks best when people view it from a specific perspective. For example, people can share a Spatial Capture in a standard window with other people’s spatial Personas visible around it. However, to perceive the depth in a Spatial Capture, each person needs to view it from the right angle. In this scenario, a person could temporarily transition to a Full Space that hides other participants and ensures the right viewing angle for them, even while everyone else continues to view the standard window and each other. If it makes sense to provide per-person versions of your shared content, be sure to continue synchronizing people’s positions and your app context to maintain the shared experience.

**Make it easy for people to exit and rejoin a shared activity.** Sometimes, people need to perform an unrelated task in your app or a different one, or engage with their physical  surroundings. When this happens, you need to present a control or other component that lets people quickly rejoin the shared activity. In addition, you might want to continue displaying the shared content so people can stay informed about the ongoing shared experience while they’re hiding their spatial Persona.

---

## Sheets

Full page: `references/sheets.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/sheets

While a sheet is visible in a visionOS app, it floats in front of its parent window, dimming it, and becoming the target of people’s interactions with the app.

**Avoid displaying a sheet that emerges from the bottom edge of a window.** To help people view the sheet, prefer centering it in their [Field of view](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Field-of-view).

**Present a sheet in a default size that helps people retain their context.** Avoid displaying a sheet that covers most or all of its window, but consider letting people resize the sheet if they want.

---

## Sidebars

Full page: `references/sidebars.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/sidebars

**If your app’s hierarchy is deep, consider using a sidebar within a tab in a tab bar.** In this situation, a sidebar can support secondary navigation within the tab. If you do this, be sure to prevent selections in the sidebar from changing which tab is currently open.

![A partial screenshot of the Music app in visionOS. The app's window includes a sidebar for navigating the music library, and the secondary pane includes a grid of playlists.](https://docs-assets.developer.apple.com/published/4c166ae0e198642b7f73ee07fb579346/visionos-sidebar-music%402x.png)

---

## Sliders

Full page: `references/sliders.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/sliders

**Prefer horizontal sliders.** It’s generally easier for people to gesture from side to side than up and down.

---

## Split views

Full page: `references/split-views.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/split-views

**To display supplementary information, prefer a split view instead of a new window.** A split view gives people convenient access to more information without leaving the current context, whereas a new window may confuse people who are trying to navigate or reposition content. Opening more windows also requires you to carefully manage the relationship between views in your app or game. If you need to request a small amount of information or present a simple task that someone must complete before returning to their main task, use a [Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets).

---

## Tab bars

Full page: `references/tab-bars.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/tab-bars

In visionOS, a tab bar is always vertical, floating in a position that’s fixed relative to the window’s leading side. When people look at a tab bar, it automatically expands; to open a specific tab, people look at the tab and tap. While a tab bar is expanded, it can temporarily obscure the content behind it.

**Supply a symbol and a text label for each tab.** A tab’s symbol is always visible in the tab bar. When people look at the tab bar, the system reveals tab labels, too. Even though the tab bar expands, you need to keep tab labels short so people can read them at a glance.

![A screenshot showing a collapsed tab bar containing only symbols.](https://docs-assets.developer.apple.com/published/e3841d7f6231fc5a1fc03b88337cc83f/visionos-tab-bar-collapsed%402x.png)

![A screenshot showing an expanded tab bar containing both symbols and labels.](https://docs-assets.developer.apple.com/published/ae30c6b5bfaf91fc871e720bb236f543/visionos-tab-bar-expanded%402x.png)

**If it makes sense in your app, consider using a sidebar within a tab.** If your app’s hierarchy is deep, you might want to use a [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars) to support secondary navigation within a tab. If you do this, be sure to prevent selections in the sidebar from changing which tab is currently open.

---

## Toolbars

Full page: `references/toolbars.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/toolbars

In visionOS, the system-provided toolbar appears along the bottom edge of a window, above the window-management controls, and in a parallel plane that’s slightly in front of the window along the z-axis.

![A screenshot of a toolbar along the bottom of the Notes app window in visionOS.](https://docs-assets.developer.apple.com/published/320b52ef74d8c47456e7e5a092498a07/visionos-toolbar-notes-app%402x.png)

To maintain the legibility of toolbar items as content scrolls behind them, visionOS uses a variable blur in the bar background. The variable blur anchors the bar above the scrolling content while letting the view’s glass material remain uniform and undivided.

In visionOS, you can supply either a symbol or a text label for each toolbar item. When people look at a toolbar item that contains a symbol, visionOS reveals the text label, providing additional information.

**Prefer using a system-provided toolbar.** The standard toolbar has a consistent and familiar appearance and is optimized to work well with eye and hand input. In addition, the system automatically places a standard toolbar in the correct position in relation to its window.

![A screenshot of a toolbar in visionOS.](https://docs-assets.developer.apple.com/published/67993cb171c2a2a84d5cfa673ff696fe/visionos-toolbar-standard-layout%402x.png)

**Avoid creating a vertical toolbar.** In visionOS, [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) are vertical, so presenting a vertical toolbar could confuse people.

**Try to prevent windows from resizing below the width of the toolbar.** visionOS doesn’t include a menu bar where each app lists all its actions, so it’s important for the toolbar to provide reliable access to essential controls regardless of a window’s size.

**If your app can enter a modal state, consider offering contextually relevant toolbar controls.** For example, a photo-editing app might enter a modal state to help people perform a multistep editing task. In this scenario, the controls in the modal editing view are different from the controls in the main window. Be sure to reinstate the window’s standard toolbar controls when the app exits the modal state.

**Avoid using a pull-down menu in a toolbar.** A pull-down menu lets you offer additional actions related to a toolbar item, but can be difficult for people to discover and may clutter your interface. Because a toolbar is located at the bottom edge of a window in visionOS, a pull-down menu might obscure the standard window controls that appear below the bottom edge. For guidance, see [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons).

---

## Typography

Full page: `references/typography.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/typography

SF Pro is the system font in visionOS. If you use NY, you need to specify the type styles you want.

visionOS uses bolder versions of the Dynamic Type body and title styles and it introduces Extra Large Title 1 and Extra Large Title 2 for wide, editorial-style layouts. For guidance using vibrancy to indicate hierarchy in text and symbols, see [visionOS](https://developer.apple.com/design/human-interface-guidelines/materials#visionOS).

**In general, prefer 2D text.** The more visual depth text characters have, the more difficult they can be to read. Although a small amount of 3D text can provide a fun visual element that draws people’s attention, if you’re going to display content that people need to read and understand, prefer using text that has little or no visual depth.

![A screenshot that shows the correct placement of 2D text on a window in visionOS.](https://docs-assets.developer.apple.com/published/b7eca42cb50603b5ae1630781ce6d4c7/visionos-typography-2d-text-correct%402x.png)

![A checkmark in a circle to indicate correct usage.](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)

![A screenshot that shows the incorrect placement of 3D text on a window in visionOS.](https://docs-assets.developer.apple.com/published/8568cd71b363e427fb91a874b8c30aa8/visionos-typography-3d-text-incorrect%402x.png)

![An X in a circle to indicate incorrect usage.](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)

**Make sure text looks good and remains legible when people scale it.** Use a text style that makes the text look good at full scale, then test it for legibility at different scales.

**Maximize the contrast between text and the background of its container.** By default, the system displays text in white, because this color tends to provide a strong contrast with the default system background material, making text easier to read. If you want to use a different text color, be sure to test it in a variety of contexts.

**If you need to display text that’s not on a background, consider making it bold to improve legibility.** In this situation, you generally want to avoid adding shadows to increase text contrast. The current space might not include a visual surface on which to cast an accurate shadow, and you can’t predict the size and density of shadow that would work well with a person’s current Environment.

**Keep text facing people as much as possible.** If you display text that’s associated with a point in space, such as a label for a 3D object, you generally want to use *billboarding* — that is, you want the text to face the wearer regardless of how they or the object move. If you don’t rotate text to remain facing the wearer, the text can become impossible to read because people may view it from the side or a highly oblique angle. For example, imagine a virtual lamp that appears to be on a physical desk with a label anchored directly above it. For the text to remain readable, the label needs to rotate around the y-axis as people move around the desk; in other words, the baseline of the text needs to remain perpendicular to the person’s line of sight.

---

## Virtual keyboards

Full page: `references/virtual-keyboards.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/virtual-keyboards

In visionOS, the system-provided virtual keyboard supports both direct and indirect gestures and appears in a separate window that people can move where they want. You don’t need to account for the location of the keyboard in your layouts.

---

## VoiceOver

Full page: `references/voiceover.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/voiceover

**Be mindful that custom gestures aren’t always accessible.** When VoiceOver is turned on in visionOS, apps and games that define custom gestures don’t receive hand input by default. This ensures people can explore the interface using their voice, without an app responding to hand input at the same time. A person can opt out of this behavior by enabling Direct Gesture mode, which disables standard VoiceOver gestures and lets apps process hand input directly. For developer guidance, see [Improving accessibility support in your visionOS app](https://developer.apple.com/documentation/visionOS/improving-accessibility-support-in-your-app).

---

## Widgets

Full page: `references/widgets.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/widgets

Widgets in visionOS are 3D objects that people place on a horizontal or vertical surface. When a person places a widget on a surface, the widget persists in that location even when the person turns Apple Vision Pro off and back on. Widgets have a consistent, real-world scale. Their size, *mounting style*, and *treatment style* impact how a person perceives them.

visionOS widgets appear in full-color by default, but they appear in the accented rendering mode when people personalize them with tint colors using a range of system-provided color palettes. Additionally, people can customize the frame width of widgets that use the elevated mounting style, and custom options that are unique to the widget. For example, visionOS doesn’t provide systemwide light or dark appearances. However, the Music poster widget offers its own customization option that lets people choose between a light and a dark theme that the app generates from the displayed album art.

For developer guidance, see [Updating your widgets for visionOS](https://developer.apple.com/documentation/WidgetKit/Updating-your-widgets-for-visionOS).

**Adapt your design and content for the spatial experience Apple Vision Pro provides.** In visionOS, widgets don’t float in isolation but are part of living rooms, kitchens, offices, and more. Consider this context early and think of widgets as part of someone’s surroundings when you bring your existing widgets to visionOS or design them from scratch. For example, the Music widget adapts to a poster-like appearance that’s glanceable across the room with large typography and a high-resolution image, and a productivity app might offer a small widget that easily fits on a desk.

**Test your widgets across the full range of system color palettes and in different lighting conditions.** Make sure your widget’s tone, contrast, and legibility remain consistent and intentional. If you choose to exclude UI elements from tinting, test your widget in every provided tint color palette to make sure the untinted elements remain legible when a person customizes their widgets with tint colors.

#### Thresholds and sizes

Widgets on Apple Vision Pro can adapt based on a person’s proximity, and visionOS provides widgets with two key thresholds to design for: the [simplified](https://developer.apple.com/documentation/WidgetKit/LevelOfDetail/simplified) threshold for when a person views a widget at a distance, and the [default](https://developer.apple.com/documentation/WidgetKit/LevelOfDetail/default) threshold when a person views it nearby.

![A placeholder image showing a widget viewed from a distance in visionOS.](https://docs-assets.developer.apple.com/published/5df163628788eedfcfe4e486c8a1cfa1/widgets-extra-large-portrait-far-proximity%402x.png)

![A placeholder image showing a widget viewed from nearby in visionOS.](https://docs-assets.developer.apple.com/published/25e218680c0e089f0288b61f4910928a/widgets-extra-large-portrait-close-proximity%402x.png)

Because widgets can appear throughout a person’s environment, it’s also important to match a widget’s size to the type of content it contains, and to be aware of how it appears at a variety of distances.

**Design a responsive layout that shows the right level of detail for each of the two thresholds.** When a person views the widget at a distance, display a simplified version of your widget that shows fewer details and has a larger type size, and remove interactive elements like buttons or toggles. When a person views the widget from nearby, show more details and use a smaller type size. To create a smooth and consistent experience and help your layout feel continuous, maintain shared elements across both distance thresholds.

**Offer widget family sizes that fit a person’s surroundings well.** Widgets map to real-world dimensions and have a permanent presence in a person’s spatial environment. Think about where people might place your widget — mounted to a wall, placed on a sideboard, or sitting next to a workplace — and choose a widget family size that’s right for that context. For example, offer a small system widget with content that people might place on a desk or an extra large widget to let people decorate their surroundings with something visually rich, like artwork or photography.

**Display content in a way that remains legible from a range of distances.** To make a widget feel intentional and proportionate to where they place it, people can scale a widget from 75 to 125 percent in size. Use print design principles like clear hierarchy, strong typography, and scale to make sure your content remains glanceable. Include high-resolution assets that look good scaled up to every size.

#### Mounting styles

The way a widget appears on a surface plays a big role in how a person perceives it. To make it feel intentional and integrated into their surroundings, people place a widget on surfaces in distinct mounting styles.

- **[elevated](https://developer.apple.com/documentation/WidgetKit/WidgetMountingStyle/elevated) style**.  On horizontal surfaces — for example, on a desk — the widget always appears elevated and gently tilts backward, providing a subtle angle that improves readability, and casts a soft shadow that helps it feel grounded on the surface. On vertical surfaces — for example, on a wall — the widget either appears elevated, sitting flush on the surface and similar to how you mount a picture frame.
- **[recessed](https://developer.apple.com/documentation/WidgetKit/WidgetMountingStyle/recessed) style**. On vertical surfaces — for example, on a wall — the widget can appear recessed, with content set back into the surface, creating a depth effect that gives the illusion of a cutout in the surface. Horizontal surfaces don’t use the recessed mounting style.

By default, widgets use the elevated mounting style, because it works for horizontal and vertical surfaces.

**Choose the mounting style that fits your content and the experience you want to create.** By default, visionOS widgets use the elevated mounting style, which is ideal for content that you want to stand out and feel present, like reminders, media, or glanceable data. Recessed widgets are ideal for immersive or ambient content, like weather or editorial content, and people can only place them on a vertical surface. If a style doesn’t suit your widget, you can opt out of it for each widget. If you choose to only support the recessed mounting style, people can’t place the widget on a horizontal surface. For example, a weather app might only support the recessed mounting style to give the illusion of looking out of a window for its large and extra-large system family widgets, and only support the elevated style for its small system family widget.

> **Note:** Use the [supportedMountingStyles(_:)](https://developer.apple.com/documentation/SwiftUI/WidgetConfiguration/supportedMountingStyles(_:)) property of your [WidgetConfiguration](https://developer.apple.com/documentation/SwiftUI/WidgetConfiguration) to  declare supported mounting styles — elevated, recessed, or both — for all widgets included in the configuration. To offer a widget that only supports one mounting style and other widgets that support both mounting styles, create separate widget configurations. For example, create one widget configuration for the widget that only supports the recessed mounting style, and a second configuration for the widgets that support both mounting styles.

**Test your elevated widget designs with each system-provided frame width.** People can choose from different system-defined frame widths for widgets that use the elevated mounting style. You can’t change your layout based on the frame width a person chooses, so make sure your widget layout stays visually balanced for each frame width.

#### Treatment styles

In addition to size and mounting style, the system applies one of two treatment styles to visionOS widgets. Choosing the right treatment for your widget helps reinforce the experience you want to create.

- The [paper](https://developer.apple.com/documentation/WidgetKit/WidgetTexture/paper) style creates a more grounded, print-like style that feels solid and makes the widget feel like part of its surroundings. When lighting conditions change, widgets in the paper style become darker or lighter in response.
- The [glass](https://developer.apple.com/documentation/WidgetKit/WidgetTexture/glass) style creates a lighter, layered look that adds depth and visual separation between foreground and background elements to emphasize clarity and contrast. The foreground elements always stay bright and legible, and don’t dim or brighten, even as ambient light changes.

**Choose the paper style for a print-like look that feels more like a real object in the room.** The entire widget responds to the ambient lighting and blends naturally into its surroundings. For example, the Music poster widget uses the paper style to display albums and playlists like framed artwork on a wall.

**Choose the glass style for information-rich widgets.** Glass visually separates foreground and background elements, allowing you to decide which parts of your interface adapt to the surroundings and which stay visually consistent. Foreground elements appear in full color, unaffected by ambient lighting, to make sure important content stays sharp and legible. For example, a News widget appears with editorial images in the background with a soft, print-like look. Its headlines stay in the foreground, crisp and easy to read.

---

## Windows

Full page: `references/windows.md` in the `apple-hig` skill — https://developer.apple.com/design/human-interface-guidelines/windows

visionOS defines two main window styles: default and volumetric. Both a default window (called a *window*) and a volumetric window (called a *volume*) can display 2D and 3D content, and people can view multiple windows and volumes at the same time in both the Shared Space and a Full Space.

![An illustration representing a window in visionOS. The illustration consists of two parallel rounded rectangles, slightly separated and displayed on an angle, positioned above a window bar.](https://docs-assets.developer.apple.com/published/e8dc51484c2e5f3289a5f6a878f4c47d/visionos-window-style-2d-window%402x.png)

![An illustration representing a volume in visionOS. The illustration consists of a translucent cube. The base of the cube is darker than the other sides. The front of the cube is positioned above a window bar.](https://docs-assets.developer.apple.com/published/92d953d099f72f9909c47bad408f4c9b/visionos-window-style-3d-volume%402x.png)

> **Note:** visionOS also defines the *plain* window style, which is similar to the default style, except that the upright plane doesn’t use the glass background. For developer guidance, see [PlainWindowStyle](https://developer.apple.com/documentation/SwiftUI/PlainWindowStyle).

The system defines the initial position of the first window or volume people open in your app or game. In both the Shared Space and a Full Space, people can move windows and volumes to new locations.

#### visionOS windows

The default window style consists of an upright plane that uses an unmodifiable background [Materials](https://developer.apple.com/design/human-interface-guidelines/materials) called *glass* and includes a close button, window bar, and resize controls that let people close, move, and resize the window. A window can also include a Share button, [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars), [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars), and one or more [Ornaments](https://developer.apple.com/design/human-interface-guidelines/ornaments). By default, visionOS uses dynamic [Scale](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Scale) to help a window’s size appear to remain consistent regardless of its proximity to the viewer. For developer guidance, see [DefaultWindowStyle](https://developer.apple.com/documentation/SwiftUI/DefaultWindowStyle).

![A screenshot of a window for an app named 'Hello World' in visionOS. The window includes text and buttons for entering different experiences.](https://docs-assets.developer.apple.com/published/95650cb19e1930e6b08ca5aa3b5b06a0/visionos-window-2d%402x.png)

**Prefer using a window to present a familiar interface and to support familiar tasks.** Help people feel at home in your app by displaying an interface they’re already comfortable with, reserving more [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences) for the meaningful content and activities you offer. If you want to showcase bounded 3D content like a game board, consider using a [visionOS volumes](https://developer.apple.com/design/human-interface-guidelines/windows#visionOS-volumes).

**Retain the window’s glass background.** The default glass background helps your content feel like part of people’s surroundings while adapting dynamically to lighting and using specular reflections and shadows to communicate the window’s scale and position. Removing the glass material tends to cause UI elements and text to become less legible and to no longer appear related to each other; using an opaque background obscures people’s surroundings and can make a window feel constricting and heavy.

**Choose an initial window size that minimizes empty areas within it.** By default, a window measures 1280x720 pt. When a window first opens, the system places it about two meters in front of the wearer, giving it an apparent width of about three meters. Too much empty space inside a window can make it look unnecessarily large while also obscuring other content in people’s space.

**Aim for an initial shape that suits a window’s content.** For example, a default Keynote window is wide because slides are wide, whereas a default Safari window is tall because most webpages are much longer than they are wide. For games, a tower-building game is likely to open in a taller window than a driving game.

**Choose a minimum and maximum size for each window to help keep your content looking great.** People appreciate being able to resize windows as they customize their space, but you need to make sure your layout adjusts well across all sizes. If you don’t set a minimum and maximum size for a window, people could make it so small that UI elements overlap or so large that your app or game becomes unusable. For developer guidance, see [Positioning and sizing windows](https://developer.apple.com/documentation/visionOS/positioning-and-sizing-windows).

![A screenshot of a window for an app in visionOS. The window includes text that discusses objects in orbit, and it includes buttons for viewing a satellite, the moon, and a telescope. The satellite button is selected and a 3D satellite is displayed.](https://docs-assets.developer.apple.com/published/db1e41fe4000281898003f792ff037c8/visionos-window-2d-with-volume%402x.png)

**Minimize the depth of 3D content you display in a window.** The system adds highlights and shadows to the views and controls within a window, giving them the appearance of [Depth](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Depth) and helping them feel more substantial, especially when people view the window from an angle. Although you can display 3D content in a window, the system clips it if the content extends too far from the window’s surface. To display 3D content that has greater depth, use a volume.

#### visionOS volumes

You can use a volume to display 2D or 3D content that people can view from any angle. A volume includes window-management controls just like a window, but unlike in a window, a volume’s close button and window bar shift position to face the viewer as they move around the volume. For developer guidance, see [VolumetricWindowStyle](https://developer.apple.com/documentation/SwiftUI/VolumetricWindowStyle).

![A screenshot of a volume containing a 3D globe in visionOS, beside a window.](https://docs-assets.developer.apple.com/published/99098a290c36254e48329511216e1d5a/visionos-window-3d%402x.png)

**Prefer using a volume to display rich, 3D content.** In contrast, if you want to present a familiar, UI-centric interface, it generally works best to use a [visionOS windows](https://developer.apple.com/design/human-interface-guidelines/windows#visionOS-windows).

**Place 2D content so it looks good from multiple angles.** Because a person’s perspective changes as they move around a volume, the location of 2D content within it might appear to change in ways that don’t make sense. To pin 2D content to specific areas of 3D content inside a volume, you can use an attachment.

**In general, use dynamic scaling.** Dynamic scaling helps a volume’s content remain comfortably legible and easy to interact with, even when it’s far away from the viewer. On the other hand, if you want a volume’s content to represent a real-world object, like a product in a retail app, you can use fixed scaling (this is the default).

**Take advantage of the default baseplate appearance to help people discern the edges of a volume.** In visionOS 2 and later, the system automatically makes a volume’s horizontal “floor,” or *baseplate*, visible by displaying a gentle glow around its border when people look at it. If your content doesn’t fill the volume, the system-provided glow can help people become aware of the volume’s edges, which can be particularly useful in keeping the resize control easy to find. On the other hand, if your content is full bleed or fills the volume’s bounds — or if you display a custom baseplate appearance — you may not want the default glow.

**Consider offering high-value content in an ornament.** In visionOS 2 and later, a volume can include an ornament in addition to a toolbar and tab bar. You can use an ornament to reduce clutter in a volume and elevate important views or controls. When you use an attachment anchor to specify the ornament’s location, such as `topBack` or `bottomFront`, the ornament remains in the same position, relative to the viewer’s perspective, as they move around the volume. Be sure to avoid placing an ornament on the same edge as a toolbar or tab bar, and prefer creating only one additional ornament to avoid overshadowing the important content in your volume. For developer guidance, see [ornament(visibility:attachmentAnchor:contentAlignment:ornament:)](https://developer.apple.com/documentation/SwiftUI/View/ornament(visibility:attachmentAnchor:contentAlignment:ornament:)).

**Choose an alignment that supports the way people interact with your volume.** As people move a volume, the baseplate can remain parallel to the floor of a person’s surroundings, or it can tilt to match the angle at which a person is looking. In general, a volume that remains parallel to the floor works well for content that people don’t interact with much, whereas a volume that tilts to match where a person is looking can keep content comfortably usable, even when the viewer is reclining.

---
