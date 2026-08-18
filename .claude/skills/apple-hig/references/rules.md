# Every HIG rule, as a checklist

2326 guidelines, one line each, grouped by topic. Apple states each as a bolded imperative followed by its reasoning; the imperative is the rule, the rest is why.

`[iOS]`-style tags mark rules that apply only to those platforms. An untagged rule applies everywhere.

Grep this file to review something against the guidelines without reading 178 pages — `grep -A1 -i 'button' rules.md` gets you every button rule. Open `pages/<slug>.md` when a rule's rationale matters.

---

## Accessibility
<sub>`pages/accessibility.md`</sub>

- **Support larger text sizes.**
  Make sure people can adjust the size of your text or icons to make them more legible, visible, and comfortable to read. Ideally, give people the option to enlarge text by at least 200 percent (or 140 percent in watchOS apps). Your...
- **Use recommended defaults for custom type sizes.**
  Each platform has different default and minimum sizes for system-defined type styles to promote readability. If you’re using custom type styles, follow the recommended defaults.
- **Bear in mind that font weight can also impact how easy text is to read.**
  If you’re using a custom font with a thin weight, aim for larger than the recommended sizes to increase legibility. For more guidance, see [Typography](https://developer.apple.com/design/human-interface-guidelines/typography).
- **Strive to meet color contrast minimum standards.**
  To ensure all information in your app is legible, it’s important that there’s enough contrast between foreground text and icons and background colors. Two popular standards of measure for color contrast are the [Web Content...
- **Prefer system-defined colors.**
  These colors have their own accessible variants that automatically adapt when people adjust their color preferences, such as enabling Increase Contrast or toggling between the light and dark appearances. For guidance, see...
- **Convey information with more than color alone.**
  Some people have trouble differentiating between certain colors and shades. For example, people who are color blind may have particular difficulty with pairings such as red-green and blue-orange. Offer visual indicators, like distinct...
- **Describe your app’s interface and content for VoiceOver.**
  VoiceOver is a screen reader that lets people experience your app’s interface without needing to see the screen. For more guidance, see [VoiceOver](https://developer.apple.com/design/human-interface-guidelines/voiceover).
- **Support text-based ways to enjoy audio and video.**
  It’s important that dialogue and crucial information about your app or game isn’t communicated through audio alone. Depending on the context, give people different text-based ways to experience their media, and allow people to customize...
- **Use haptics in addition to audio cues.**
  If your interface conveys information through audio cues — such as a success chime, error sound, or game feedback — consider pairing that sound with matching haptics for people who can’t perceive the audio or have their audio turned...
- **Augment audio cues with visual cues.**
  This is especially important for games and spatial apps where important content might be taking place off screen. When using audio to guide people towards a specific action, also add in visual indicators that point to where you want...
- **Offer sufficiently sized controls.**
  Controls that are too small are hard for many people to interact with and select. Strive to meet the recommended minimum control size for each platform to ensure controls and menus are comfortable for all when tapping and clicking.
- **Consider spacing between controls as important as size.**
  Include enough padding between elements to reduce the chance that someone taps the wrong control. In general, it works well to add about 12 points of padding around elements that include a bezel. For elements without a bezel, about 24...
- **Support simple gestures for common interactions.**
  For many people, with or without disabilities, complex gestures can be challenging. For interactions people do frequently in your app or game, use the simplest gesture possible — avoid custom multifinger and multihand gestures — so...
- **Offer alternatives to gestures.**
  Make sure your UI’s core functionality is accessible through more than one type of physical interaction. Gestures can be less comfortable for people who have limited dexterity, so offer onscreen ways to achieve the same outcome. For...
- **Let people use Voice Control to give guidance and enter information verbally.**
  With Voice Control, people can interact with their devices entirely by speaking commands. They can perform gestures, interact with screen elements, dictate and edit text, and more. To ensure a smooth experience, label interface elements...
- **Integrate with Siri and Shortcuts to let people perform tasks using voice alone.**
  When your app supports Siri and Shortcuts, people can automate the important and repetitive tasks they perform regularly. They can initiate these tasks from Siri, the Action button on their iPhone or Apple Watch, and shortcuts on their...
- **Support mobility-related assistive technologies.**
  Features like [VoiceOver](https://developer.apple.com/design/human-interface-guidelines/voiceover), AssistiveTouch, Full Keyboard Access, Pointer Control, and [Switch...
- **Let people use the keyboard alone to navigate and interact with your app.**
  People can turn on Full Keyboard Access to navigate apps using their physical keyboard. The system also defines accessibility keyboard shortcuts and a wide range of other [keyboard shortcuts](https://support.apple.com/en-us/102650) that...
- **Support Switch Control.**
  Switch Control is an assistive technology that lets people control their devices through separate hardware, game controllers, or sounds such as a click or a pop. People can perform actions like selecting, tapping, typing, and drawing...
- **Keep actions simple and intuitive.**
  Ensure that people can navigate your interface using easy-to-remember and consistent interactions. Prefer system gestures and behaviors people are already familiar with over creating custom gestures people must learn and retain.
- **Minimize use of time-boxed interface elements.**
  Views and controls that auto-dismiss on a timer can be problematic for people who need longer to process information, and for people who use assistive technologies that require more time to traverse the interface. Prefer dismissing...
- **Consider offering difficulty accommodations in games.**
  Everyone has their own way of playing and enjoying games. To support a variety of cognitive abilities, consider adding the ability to customize the difficulty level of your game, such as offering options for people to reduce the...
- **Let people control audio and video playback.**
  Avoid autoplaying audio and video content without also providing controls to start and stop it. Make sure these controls are discoverable and easy to act upon, and consider global settings that let people opt out of auto-playing all...
- **Allow people to opt out of flashing lights in video playback.**
  People might want to avoid bright, frequent flashes of light in the media they consume. A Dim Flashing Lights setting allows the system to calculate, mitigate, and inform people about flashing lights in a piece of media. If your app...
- **Be cautious with fast-moving and blinking animations.**
  When you use these effects in excess, it can be distracting, cause dizziness, and in some cases even result in epileptic episodes. People who are prone to these effects can turn on the Reduce Motion accessibility setting. When this...
- **Optimize your app’s UI for Assistive Access.**
  Assistive Access is an accessibility feature in iOS and iPadOS that allows people with cognitive disabilities to use a streamlined version of your app. Assistive Access sets a default layout and control presentation for apps that...
- **Pointer Control (hand)** `[visionOS]`
- **Pointer Control (head)** `[visionOS]`
- **Prioritize comfort.** `[visionOS]`
  The immersive nature of visionOS means that interfaces, animations, and interactions have a greater chance of causing motion sickness, and visual and ergonomic discomfort for people. To ensure the most comfortable experience, consider...

## Action button
<sub>`pages/action-button.md`</sub>

- **Support the Action button with a set of your app’s essential functions.**
  For example, if your cooking app includes an egg timer, a “Start Egg Timer” action might be one that people want to initiate when they press the Action button. You don’t need to offer an App Shortcut that opens your app, because the...
- **For each action you support, write a short label that succinctly describes it.**
  People see your labels when they visit Settings to configure the Action button’s behavior. Create labels that use [title-style capitalization](https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web#apdca93e113f1d64), begin...
- **Prefer letting the system show people how to use the Action button with your app.**
  When you support the Action button, the system automatically helps people configure it to initiate one of your app’s functions. Avoid creating content that repeats the guidance offered in Settings for the Action button, or other usage...
- **Let people use your actions without leaving their current context.** `[iOS]`
  When possible, make use of lightweight multitasking capabilities like [Live Activities](https://developer.apple.com/design/human-interface-guidelines/live-activities) and custom snippets to provide functionality without opening your...
- **Consider offering a secondary function that supports or advances the primary action people choose.** `[watchOS]`
  People often use the Action button without looking at the screen, so a subsequent button press needs to flow logically from the first press, while also making sense in the current context. If your app supports workout or dive actions,...
- **Prefer using subsequent button presses to support additional functionality rather than to stop or conclude a function.** `[watchOS]`
  If you need to let people stop their main task — as opposed to pausing the current function — offer this option within your interface instead.
- **Pause the current function when people press the Action button and side button together.** `[watchOS]`
  The exception is in a diving app where pausing a dive may be dangerous to the diver, causing them to lose track of their depth or not understand how long they’ve been underwater. Unless pausing the current function results in a negative...

## Action sheets
<sub>`pages/action-sheets.md`</sub>

- **Use an action sheet — not an alert — to offer choices related to an intentional action.**
  For example, when people cancel the message they’re editing in Mail on iPhone, an action sheet provides two choices: delete the draft, or save the draft. Although an alert can also help people confirm or cancel an action that has...
- **Use action sheets sparingly.**
  Action sheets give people important information and choices, but they interrupt the current task to do so. To encourage people to pay attention to action sheets, avoid using them more than necessary.
- **Aim to keep titles short enough to display on a single line.**
  A long title is difficult to read quickly and might get truncated or require people to scroll.
- **Provide a message only if necessary.**
  In general, the title — combined with the context of the current action — provides enough information to help people understand their choices.
- **If necessary, provide a Cancel button that lets people reject an action that might destroy data.**
  Place the Cancel button at the bottom of the action sheet (or in the upper-left corner of the sheet in watchOS). A SwiftUI confirmation dialog includes a Cancel button by default.
- **Make destructive choices visually prominent.**
  Use the destructive style for buttons that perform destructive actions, and place these buttons at the top of the action sheet where they tend to be most noticeable. For developer guidance, see...
- **Use an action sheet — not a menu — to provide choices related to an action.** `[iOS, iPadOS]`
  People are accustomed to having an action sheet appear when they perform an action that might require clarifying choices. In contrast, people expect a menu to appear when they choose to reveal it.
- **Avoid letting an action sheet scroll.** `[iOS, iPadOS]`
  The more buttons an action sheet has, the more time and effort it takes for people to make a choice. Also, scrolling an action sheet can be hard to do without inadvertently tapping a button.
- **Avoid displaying more than four buttons in an action sheet, including the Cancel button.** `[watchOS]`
  When there are fewer buttons onscreen, it’s easier for people to view all their options at once. Because the Cancel button is required, aim to provide no more than three additional choices.

## Activity rings
<sub>`pages/activity-rings.md`</sub>

- **Display Activity rings when they’re relevant to the purpose of your app.**
  If your app is related to health or fitness, and especially if it contributes information to HealthKit, people generally expect to find Activity rings in your interface. For example, if you structure a workout or health session around...
- **Use Activity rings only to show Move, Exercise, and Stand information.**
  Activity rings are designed to consistently represent progress in these specific areas. Don’t replicate or modify Activity rings for other purposes. Never use Activity rings to display other types of data. Never show Move, Exercise, and...
- **Use Activity rings to show progress for a single person.**
  Never use Activity rings to represent data for more than one person, and make sure it’s obvious whose progress you’re showing by using a label, a photo, or an avatar.
- **Always keep the visual appearance of Activity rings the same, regardless of where you display them.**
  Follow these guidelines to provide a consistent experience:
- **To display a label or value that’s directly associated with an Activity ring, use the colors that match it.**
  To display the ring-specific labels *Move*, *Exercise*, and *Stand*, or to display a person’s current and goal values for each ring, use the following colors, specified as RGB values.
- **Maintain Activity ring margins.**
  An Activity ring element must include a minimum outer margin of no less than the distance between rings. Never allow other elements to crop, obstruct, or encroach upon this margin or the rings themselves.
- **Differentiate other ring-like elements from Activity rings.**
  Mixing different ring styles can lead to a visually confusing interface. If you must include other rings, use padding, lines, or labels to separate them from Activity rings. Color and scale can also help provide visual separation.
- **Don’t send notifications that repeat the same information the Activity app sends.**
  The system already delivers Move, Exercise, and Stand progress updates, so it’s confusing for people to receive redundant information from your app. Also, don’t show an Activity ring element in your app’s notifications. It’s fine to...
- **Don’t use Activity rings for decoration.**
  Activity rings provide information to people; they don’t just embellish your app’s design. Never display Activity rings in labels or background graphics.
- **Don’t use Activity rings for branding.**
  Use Activity rings strictly to display Activity progress in your app. Never use Activity rings in your app’s icon or marketing materials.

## Activity views
<sub>`pages/activity-views.md`</sub>

- **Avoid creating duplicate versions of common actions that are already available in the activity view.**
  For example, providing a duplicate Print action is unnecessary and confusing because people wouldn’t know how to distinguish your action from the system-provided one. If you need to provide app-specific functionality that’s similar to...
- **Consider using a symbol to represent your custom activity.**
  [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) provides a comprehensive set of configurable symbols you can use to communicate items and concepts in an activity view. If you need to create a...
- **Write a succinct, descriptive title for each custom action you provide.**
  If a title is too long, the system wraps it and may truncate it. Prefer a single verb or a brief verb phrase that clearly communicates what the action does. Avoid including your company or product name in an action title. In contrast,...
- **Make sure activities are appropriate for the current context.**
  Although you can’t reorder system-provided tasks in an activity view, you can exclude tasks that aren’t applicable to your app. For example, if it doesn’t make sense to print from within your app, you can exclude the Print activity. You...
- **Use the Share button to display an activity view.**
  People are accustomed to accessing system-provided activities when they choose the Share button. Avoid confusing people by providing an alternative way to do the same thing.
- **If necessary, create a custom interface that feels familiar to people.**
  For a share extension, prefer the system-provided composition view because it provides a consistent sharing experience that people already know. For an action extension, include your app name. If you need to present an interface,...
- **Streamline and limit interaction.**
  People appreciate extensions that let them perform a task in just a few steps. For example, a share extension might immediately post an image to a social media account with a single tap or click.
- **Avoid placing a modal view above your extension.**
  By default, the system displays an extension within a modal view. While it might be necessary to display an alert above an extension, avoid displaying additional modal views.
- **If necessary, provide an image that communicates the purpose of your extension.**
  A share extension automatically uses your app icon, helping give people confidence that your app provided the extension. For an action extension, prefer using a...
- **Use your main app to denote the progress of a lengthy operation.**
  An activity view dismisses immediately after people complete the task in your share or action extension. If a task is time-consuming, continue it in the background, and give people a way to check the status in your main app. Although...

## AirPlay
<sub>`pages/airplay.md`</sub>

- **Prefer the system-provided media player.**
  The built-in media player offers a standard set of controls and supports features like chapter navigation, subtitles, closed captioning, and AirPlay streaming. It’s also easy to implement, provides a consistent and familiar playback...
- **Provide content in the highest possible resolution.**
  Your [HTTP Live Streaming](https://developer.apple.com/documentation/http-live-streaming) (HLS) playlist needs to include the full range of available resolutions so that people can experience your content in the resolution that’s...
- **Stream only the content people expect.**
  Avoid streaming content like background loops and short video experiences that make sense only within the context of the app itself. For developer guidance, see...
- **Support both AirPlay streaming and mirroring.**
  Supporting both features gives people the most flexibility.
- **Support remote control events.**
  When you do, people can choose actions like play, pause, and fast forward on the lock screen, and through interaction with Siri or HomePod. For developer guidance, see [Remote command center...
- **Don’t stop playback when your app enters the background or when the device locks.**
  For example, people expect the TV show they started streaming from your app to continue while they check their mail or put their device to sleep. In this type of scenario, it’s also crucial to avoid automatic mirroring because people...
- **Don’t interrupt another app’s playback unless your app is starting to play immersive content.**
  For example, if your app plays a video when it launches or auto-plays inline videos, play this content on only the local device, while allowing current playback to continue. For developer guidance, see...
- **Let people use other parts of your app during playback.**
  When AirPlay is active, your app needs to remain functional. If people navigate away from the playback screen, make sure other in-app videos don’t begin playing and interrupt the streaming content.
- **If necessary, provide a custom interface for controlling media playback.**
  If you can’t use the system-provided media player, you can create a custom media player that gives people an intuitive way to enter AirPlay. If you need to do this, be sure to provide custom buttons that match the appearance and...
- **Position the AirPlay icon consistently with other technology icons.**
  If you display other technology icons within shapes, you can display the AirPlay icon in the same manner.
- **Don’t use the AirPlay icon or name in custom buttons or interactive elements.**
  Use the icon and the name *AirPlay* only in noninteractive ways.
- **Pair the icon with the name *AirPlay* correctly.**
  You can show the name below or beside the icon if you also reference other technologies in this way. Use the same font you use in the rest of your layout. Avoid using the AirPlay icon within text or as a replacement for the name *AirPlay*.
- **Emphasize your app over AirPlay.**
  Make references to AirPlay less prominent than your app name or main identity.
- **Use correct capitalization when using the term *AirPlay*.**
  *AirPlay* is one word, with an uppercase *A* and uppercase *P*, each followed by lowercase letters. If your layout displays only all-uppercase designations, you can typeset *AirPlay* in all uppercase to match the style of the rest of...
- **Always use *AirPlay* as a noun.**
- **Use terms like *works with*, *use*, *supports*, and *compatible*.**
- **Use the name *Apple* with the name *AirPlay* if desired.**
- **Refer to AirPlay if appropriate and to add clarity.**
  If your content is specific to AirPlay, you can use Airplay to make that clear. You can also refer to AirPlay in technical specifications.

## Alerts
<sub>`pages/alerts.md`</sub>

- **Use alerts sparingly.**
  Alerts give people important information, but they interrupt the current task to do so. Encourage people to pay attention to your alerts by making certain that each one offers only essential information and useful actions.
- **Avoid using an alert merely to provide information.**
  People don’t appreciate an interruption from an alert that’s informative, but not actionable. If you need to provide only information, prefer finding an alternative way to communicate it within the relevant context. For example, when a...
- **Avoid displaying alerts for common, undoable actions, even when they’re destructive.**
  For example, you don’t need to alert people about data loss every time they delete an email or file because they do so with the intention of discarding data, and they can undo the action. In comparison, when people take an uncommon...
- **Avoid showing an alert when your app starts.**
  If you need to inform people about new or important information the moment they open your app, design a way to make the information easily discoverable. If your app detects a problem at startup, like no network connection, consider...
- **In all alert copy, be direct, and use a neutral, approachable tone.**
  Alerts often describe problems and serious situations, so avoid being oblique or accusatory, or masking the severity of the issue.
- **Write a title that clearly and succinctly describes the situation.**
  You need to help people quickly understand the situation, so be complete and specific, without being verbose. As much as possible, describe what happened, the context in which it happened, and why. Avoid writing a title that doesn’t...
- **Include informative text only if it adds value.**
  If you need to add an informative message, keep it as short as possible, using complete sentences, sentence-style capitalization, and appropriate punctuation.
- **Avoid explaining alert buttons.**
  If your alert text and button titles are clear, you don’t need to explain what the buttons do. In rare cases where you need to provide guidance on choosing a button, use a term like *choose* to account for people’s current device and...
- **If supported, include a text field only if you need people’s input to resolve the situation.**
  For example, you might need to present a secure text field to receive a password.
- **Create succinct, logical button titles.**
  Aim for a one- or two-word title that describes the result of selecting the button. Prefer verbs and verb phrases that relate directly to the alert text — for example, “View All,” “Reply,” or “Ignore.” In informational alerts only, you...
- **Avoid using OK as the default button title unless the alert is purely informational.**
  The meaning of “OK” can be unclear even in alerts that ask people to confirm that they want to do something. For example, does “OK” mean “OK, I want to complete the action” or “OK, I now understand the negative results my action would...
- **Place buttons where people expect.**
  In general, place the button people are most likely to choose on the trailing side in a row of buttons or at the top in a stack of buttons. Always place the default button on the trailing side of a row or at the top of a stack. Cancel...
- **Use the destructive style to identify a button that performs a destructive action people didn’t deliberately choose.**
  For example, when people deliberately choose a destructive action — such as Empty Trash — the resulting alert doesn’t apply the destructive style to the Empty Trash button because the button performs the person’s original intent. In...
- **If there’s a destructive action, include a Cancel button to give people a clear, safe way to avoid the action.**
  Always use the title “Cancel” for a button that cancels an alert’s action. Note that you don’t want to make a Cancel button the default button. If you want to encourage people to read an alert and not just automatically press Return to...
- **Provide alternative ways to cancel an alert when it makes sense.**
  In addition to choosing a Cancel button, people appreciate using keyboard shortcuts or other quick ways to cancel an onscreen alert. For example:
- **Use an action sheet — not an alert — to offer choices related to an intentional action.** `[iOS, iPadOS]`
  For example, when people cancel the Mail message they’re editing, an action sheet provides three choices: delete the edits (or the entire draft), save the draft, or return to editing. Although an alert can also help people confirm or...
- **When possible, avoid displaying an alert that scrolls.** `[iOS, iPadOS]`
  Although an alert might scroll if the text size is large enough, be sure to minimize the potential for scrolling by keeping alert titles short and including a brief message only when necessary.
- **Use a caution symbol sparingly.** `[macOS]`
  Using a caution symbol like `exclamationmark.triangle` too frequently in your alerts diminishes its significance. Use the symbol only when extra attention is really needed, as when confirming an action that might result in unexpected...

## Always On
<sub>`pages/always-on.md`</sub>

- **Hide sensitive information.**
  It’s crucial to redact personal information that people wouldn’t want casual observers to view, like bank balances or health data. You also need to hide personal information that might be visible in a notification; for guidance, see...
- **Keep other types of personal information glanceable when it makes sense.**
  On Apple Watch, for example, people typically appreciate getting pace and heart rate updates while they’re working out; on iPhone, people appreciate getting a glanceable update on a flight arrival or a notification when a ride-sharing...
- **Keep important content legible and dim nonessential content.**
  You can increase dimming on secondary text, images, and color fills to give more prominence to the information that’s important to people. For example, a to-do list app might remove row backgrounds and dim each item’s additional details...
- **Maintain a consistent layout.**
  Avoid making distracting interface changes when Always On begins or ends and throughout the Always On experience. For example, when Always On begins, prefer transitioning an interactive component to an unavailable appearance — don’t...
- **Gracefully transition motion to a resting state; don’t stop it instantly.**
  Smoothly finishing the current motion helps communicate the transition and avoids making people think that something went wrong.

## App Clips
<sub>`pages/app-clips.md`</sub>

- **Allow people to complete a task or a demo in your App Clip.**
  Don’t require people to install the full app to experience the entire demo, to complete a task, or to finish a level in a game.
- **Focus on essential features.**
  Interactions with App Clips are quick and focused. Limit features to what’s necessary to accomplish the task at hand. Reserve advanced or complex features for the app. If you offer a demo version of your full app, focus on essential...
- **Don’t use App Clips solely for marketing purposes.**
  App Clips need to provide real value and help people accomplish tasks. Don’t use them as a means to advertise services or products, and don’t display ads in your App Clip.
- **Avoid using web views in your App Clip.**
  App Clips use native components and frameworks to offer an app-quality experience. If only web components are available to you, offer a quick link to your website instead of an App Clip.
- **Design a linear, easy-to-use, and focused user interface.**
  App Clips don’t need tab bars, complex navigation, or settings. Keep the number of screens and entry forms to a minimum. Remove extraneous information and reduce complexity in the user interface wherever possible.
- **On launch, show the most relevant part of your App Clip.**
  Skip unnecessary steps and take people immediately to the part of the App Clip that best fits their context.
- **Ensure people can use your App Clip immediately.**
  App Clips need to include all required assets, omit splash screens, and never make people wait on launch.
- **Ensure your App Clip is small.**
  The smaller your App Clip, the faster it will launch on a person’s device. Keeping your App Clip small is especially important when bandwidth is limited. As much as possible, reduce unnecessary code and remove unused assets. Avoid...
- **Make the App Clip shareable.**
  When someone shares a link to an App Clip in the Messages app, recipients can launch the App Clip from within the Messages app. Offer the ability to share links to specific points in your App Clip, and encourage people to share the App...
- **Make it easy to pay for a service or product.**
  Entering payment information can be a long and error-prone task. Consider supporting [Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay) to offer express checkout and let people enter shipping...
- **Avoid requiring people to create an account before they can benefit from your App Clip.**
  Creating an account is a complex task that takes time and effort. Consider not requiring an account, or think about asking people to create an account after they finish a task. If your App Clip requires an account to provide value,...
- **Provide a familiar, focused experience in your app.**
  When people install the full app, it replaces the App Clip on their device. From this moment, invocations that would have launched the App Clip launch the full app instead. Ensure your app provides a focused, familiar experience to...
- **Limit the amount of data you store and handle yourself.**
  If you need to store people’s data — for example, login information — store it securely. In addition, don’t rely on the availability of data you previously stored on the device — the system may have removed the App Clip from the device...
- **Consider offering Sign in with Apple.**
  Sign in with Apple securely retains login information off people’s devices and preserves their privacy. For guidance, see [Sign in with Apple](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple).
- **Offer a secure way to pay for services or goods that also respects people’s privacy.**
  For example, consider offering [Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay).
- **Don’t compromise the user experience by asking people to install the full app.**
  If your App Clip offers an on-the-go experience, consider whether the App Clip card and the system-provided app banner provide enough incentive for people to download the full app. If your App Clip offers a demo experience, let people...
- **Pick the right time to recommend your app.**
  When someone completes a task or reaches a natural pause, display an [SKOverlay](https://developer.apple.com/documentation/storekit/skoverlay) that allows people to initiate a download of your full app or game from the context of the...
- **Recommend your app in a nonintrusive, polite way.**
  Don’t ask people to install the full app repeatedly or interrupt them during a task. Push notifications aren’t a good way to ask people to install the app either. Clearly communicate your app’s additional features.
- **Only ask for permission to use notifications for an extended period of time if it’s really needed.**
  If your App Clip’s functionality spans more than a day, explicitly request permission to schedule and receive notifications. For example, a car rental company’s App Clip can ask for permission to send a notification that reminds people...
- **Keep notifications focused.**
  Don’t send purely promotional notifications, and only use notifications in response to an explicit user action. If a person completes their task without leaving the App Clip, you might not need to send any notifications at all.
- **Use notifications to help people complete a task.**
  Notifications for an App Clip relate directly to the task the App Clip helps to accomplish. For example, an App Clip that helps people order food could send notifications related to a scheduled delivery.
- **Use consistent branding.**
  When people see the App Clip card for a business, the brand for that business is front and center. Tone down your own branding and make sure the branding for the business is clearly visible to avoid confusing people when they enter the...
- **Consider multiple businesses.**
  An App Clip may power many different businesses or a business that has multiple locations. In both scenarios, people may end up using the App Clip for more than one business or location at a time. The App Clip must handle this use case...
- **Be informative.**
  Make sure the image on the App Clip card clearly communicates the features offered by your App Clip, supported tasks, or content.
- **Prefer photography and graphics.**
  Avoid using a screenshot of your app’s user interface because it’s unlikely to communicate the purpose of your App Clip. Instead, use an image that helps people understand the App Clip’s value, or a photo of the location of its...
- **Avoid using text.**
  Text in the header image isn’t localizable, can be difficult to read, and can make a card image less aesthetically pleasing.
- **Adhere to image requirements.**
  Use a 1800x1200 px PNG or JPEG image without transparency.
- **Use concise copy.**
  An App Clip card requires both a title and a subtitle. Clearly express the purpose of your App Clip within the available space so people can read and understand it at a glance. Create a title that has no more than 30 characters and a...
- **Pick a verb for the action button that best fits your App Clip.**
  Possible verbs are *View*, *Play*, or *Open*. Pick *View* for media, or if your App Clip provides informational or educational content. Pick *Play* for games. Choose *Open* for all other App Clips.
- **Include the App Clip logo when space allows.**
  The logo helps make it clear that the code launches an App Clip; however, if you can’t meet the clear space requirements, use the App Clip Code design without the App Clip logo. Also, use the design without the App Clip logo if you...
- **Place your App Clip Code on a flat or cylindrical surface only.**
  If you place your App Clip Code on a cylindrical surface — for example, on a scooter’s handlebar — make sure the width of the App Clip Code doesn’t exceed one-sixth of the cylinder’s circumference.
- **Help your App Clip Code remain as flat as possible so it’s easy for people to scan.**
  To provide the best scanning experience, avoid displaying App Clip Codes on deformable materials that readily fold or crumple, such as paper, plastic, or fabric. If you need to make your App Clip Code available on a bag, flexible box,...
- **Place your App Clip Code in a location that helps ensure reliable scanning.**
  For example, place a scan-only App Clip Code in a location that offers enough light to ensure reliable scanning, and don’t require people to scan from a wide angle.
- **Make sure the App Clip Code is unobstructed.**
  Don’t overlay the App Clip Code with text, logos, or images. Never animate the App Clip Code or dim it.
- **Display the App Clip Code in an upright position.**
  Don’t rotate the generated App Clip Code or display the center glyph at an angle.
- **Don’t create App Clip Codes that are too small.**
  App Clip Codes must adhere to the following specifications.
- **Provide enough space between an App Clip Code and adjacent App Clip Codes, graphics, or materials.**
  The minimum clear space around an App Clip Code is equal to the space between the center glyph and the circular code. If you place your App Clip Code next to another App Clip Code or other machine-readable code, leave enough clear space...
- **Adhere to [Guidelines for Using Apple Trademarks](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html) when referring to your App Clip and App Clip Codes.**
  For example, Apple trademarks can’t appear in your app name or images, always use title case when using the terms App Clips or App Clip Code, and so on. For additional information, see [Legal...
- **Always use the generated App Clip Code.**
  Don’t create your own App Clip Code design or modify a generated App Clip Code in any way. Don’t apply filters, augment its colors, or add glows, shadows, gradients, or reflections. They negatively impact people’s scanning experience....
- **Choose colors with enough contrast that ensure accurate scanning.**
  Each App Clip Code uses three colors: a foreground color, a background color, and a third color that’s generated for you based on the foreground and background colors. Both [App Store Connect](https://appstoreconnect.apple.com) and the...
- **Use high-quality, non-textured print materials.**
  Print App Clip Codes on matte finishes. Avoid shine, gloss, reflective or holographic overlays, as well as thin laminate finishes or materials. In case you need to laminate print material with an App Clip Code on it, use a matte...
- **Use high-resolution images and printer settings.**
  When rasterizing the SVG file, set the image resolution to at least 600 ppi, and print your App Clip Codes with a minimum resolution of 300 dpi. Consider leveling and calibrating your printer before printing to ensure a high print...
- **Use correct color settings when you convert the generated SVG file to a CMYK image.**
  Both the [App Clip Code Generator](https://developer.apple.com/app-clips/resources/) command-line tool and [App Store Connect](https://appstoreconnect.apple.com) generate App Clip Codes as SVG files in the sRGB color space. To print...
- **If you’re using a printer that only prints in grayscale, only generate grayscale App Clip Codes.**
  Codes generated in color and then printed in grayscale may work less reliably.
- **For NFC-integrated App Clip Codes, choose Type 5 NFC tags.**
  The embedded NFC tag needs to be at least 35 mm in diameter or of equivalent size.
- **If you create large batches of App Clip Codes, thoroughly test your printing workflow, and verify printed App Clip Codes.**
  For example, conduct small, inexpensive print runs using a subset of codes. Print your App Clip Codes on print templates with additional padded regions that allow you to display the encoded invocation URL and the SVG filename alongside...
- **Verify print quality of your chosen color pair with the printer calibration test sheet that shows text boxes for each default color pair.**
  Follow the instructions on the sheet to print it at the right scale and to verify that your printer can create high-quality App Clip Codes.
- **Verify your printer’s grayscale settings by printing the printer calibration test sheet that shows two grayscale bars.**
  If any of the specific gray colors are light or entirely missing, the printer may need calibration or may not be suitable for printing an App Clip Code that allows for reliable scanning.

## App Shortcuts
<sub>`pages/app-shortcuts.md`</sub>

- **To surface common types of app functionality throughout the system, consider adopting app schemas instead.**
  Apps in common domain areas can adopt [App schema domains](https://developer.apple.com/documentation/appintents/app-schema-domains) to make their actions and content available to Apple Intelligence. On supported devices, this lets Siri...
- **Offer App Shortcuts for your app’s most common and important tasks.**
  Straightforward tasks that people can complete without leaving their current context work best, but you can also open your app if it helps people complete multistep tasks more easily.
- **Add flexibility by letting people choose from a set of options.**
  An App Shortcut can include a single optional value, or parameter, if it makes sense. For example, a meditation app could offer an App Shortcut that lets someone begin a specific type of meditation: “Start [morning, daily, sleep]...
- **Ask for clarification in response to a request that’s missing optional information.**
  For example, someone might say “Start meditation” without specifying the type (morning, daily, or sleep); you could follow up by suggesting the one they used most recently, or one based on the current time of day. If one option is most...
- **Keep voice interactions simple.**
  If your phrase feels too complicated when you say it aloud, it’s probably too difficult to remember or say correctly. For example, “Start [sleep] meditation with nature sounds” appears to have two possible parameters: the meditation...
- **Make App Shortcuts discoverable in your app.**
  People are most likely to remember and use App Shortcuts for tasks they do often, once they know the shortcut is available. Consider showing occasional tips in your app when people perform common actions to let them know an App Shortcut...
- **Provide enough detail for interaction on audio-only devices.**
  People can receive responses on audio-only devices such as AirPods and HomePod too, and may not always be able to see content onscreen. Include all critical information in the full dialogue text of your App Shortcuts. For developer...
- **Provide brief, memorable activation phrases and natural variants.**
  Because an App Shortcut phrase (or a variant you define) is what people say to run an App Shortcut with Siri, it’s important to keep it brief to make it easier to remember. You have to include your app name, but you can be creative with...
- **When referring to App Shortcuts or the Shortcuts app, always use title case and make sure that *Shortcuts* is plural.**
  For example, *MyApp integrates with Shortcuts to provide a quick way to get things done with just a tap or by asking Siri, and offers App Shortcuts you can place on the Action button.*
- **When referring to individual shortcuts (not App Shortcuts or the Shortcuts app), use lowercase.**
  For example, *Run a shortcut by asking Siri or tapping a suggestion on the Lock Screen.*
- **Order shortcuts based on importance.** `[iOS, iPadOS]`
  The order you choose determines how App Shortcuts initially appear in both Spotlight and the Shortcuts app, so it’s helpful to include the most generally useful ones first. Once people start using your App Shortcuts, the system updates...

## App icons
<sub>`pages/app-icons.md`</sub>

- **Prefer clearly defined edges in foreground layers.**
  To ensure system-drawn highlights and shadows look best, avoid soft and feathered edges on foreground layer shapes.
- **Vary opacity in foreground layers to increase the sense of depth and liveliness.**
  For example, the Photos icon separates its centerpiece into multiple layers that contain translucent pieces, bringing greater dynamism to the design. Importing fully opaque layers and adjusting transparency in Icon Composer lets you...
- **Design a background that both stands out and emphasizes foreground content.**
  If you choose a gradient for your background layer, ensure that it responds well to system lighting effects. Icon Composer supports solid colors and gradients for background layers, making it unnecessary to import custom background...
- **Prefer vector graphics when bringing layers into Icon Composer.**
  Unlike raster images, vector graphics (such as SVG or PDF) scale gracefully and appear crisp at any size. Outline artwork and convert text to outline in your design. For mesh gradients and raster artwork, prefer PNG format because it’s...
- **iOS, iPadOS, macOS**
- **visionOS, watchOS**
- **Produce appropriately shaped, unmasked layers.**
  The system masks all layer edges to produce an icon’s final shape. For iOS, iPadOS, and macOS icons, provide square layers so the system can apply rounded corners. For visionOS and watchOS, provide square layers so the system can create...
- **Keep primary content centered to avoid truncation when the system adjusts corners or applies masking.**
  Pay particular attention to centering content in visionOS and watchOS icons. To help with icon placement, use the grids in the app icon production templates, which you can find in [Apple Design...
- **Provide a visually consistent icon design across all the platforms your app supports.**
  A consistent design helps people quickly find your app wherever it appears and prevents people from mistaking your app for multiple apps.
- **Consider basing your icon design around filled, overlapping shapes.**
  Overlapping solid shapes in the foreground, particularly when paired with transparency and blurring, can give an icon a sense of depth.
- **Include text only when it’s essential to your experience or brand.**
  Text in icons doesn’t support accessibility or localization, is often too small to read easily, and can make an icon appear cluttered. In some contexts, your app name already appears nearby, making it redundant to display the name...
- **Prefer illustrations to photos and avoid replicating UI components.**
  Photos are full of details that don’t work well when displayed in different appearances, viewed at small sizes, or split into layers. Instead of using photos, create a graphic representation of the content that emphasizes the features...
- **Don’t use replicas of Apple hardware products.**
  Apple products are copyrighted and can’t be reproduced in your app icons.
- **Let the system handle blurring and other visual effects.**
  The system dynamically applies visual effects to your app icon layers, so there’s no need to include specular highlights, drop shadows between layers, beveled edges, blurs, glows, and other effects. In addition to interfering with...
- **Create layer groupings to apply effects to multiple layers at once.**
  System effects typically occur on individual layers. If it makes sense for your design, however, you can group several layers together in Icon Composer or your design tool so effects occur at the group level. For a group, Icon Composer...
- **Keep your icon’s features consistent across appearances.**
  To create a seamless experience, keep your icon’s core visual features the same in the default, dark, clear, and tinted appearances. Avoid creating custom icon variants that swap elements in and out with each variant, which may make it...
- **Design dark and tinted icons that feel at home beside system app icons and widgets.**
  You can preserve the color palette of your default icon, but be mindful that dark icons are more subdued, and clear and tinted icons are even more so. A great app icon is visible, legible, and recognizable, regardless of its appearance...
- **Use your light app icon as the basis for your dark icon.**
  Choose complementary colors that reflect the default design, and avoid excessively bright images. Color backgrounds generally offer the greatest contrast in dark icons. For guidance, see [Dark...
- **Consider offering alternate app icons.**
  In iOS, iPadOS, tvOS, and compatible apps running in visionOS, it’s possible to let people visit your app’s settings to choose an alternate version of your app icon. For example, a sports app might offer icons for different teams,...
- **Include a safe zone to ensure the system doesn’t crop your content.** `[tvOS]`
  When someone focuses your app icon, the system may crop content around the edges as the icon scales and moves. To ensure that your icon’s content is always visible, keep a safe zone around it. Be aware that the safe zone can vary,...
- **Avoid adding a shape that’s intended to look like a hole or concave area to the background layer.** `[visionOS]`
  The system-added shadow and specular highlights can make such a shape stand out instead of recede.
- **Avoid using black for your icon’s background.** `[watchOS]`
  Lighten a black background so the icon doesn’t blend into the display background.

## Apple Pay
<sub>`pages/apple-pay.md`</sub>

- **Offer Apple Pay on all devices and browsers that support it.**
  If the device doesn’t support Apple Pay, don’t present Apple Pay as a payment option. For developer guidance, see [PKPaymentAuthorizationController](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller)...
- **Make Apple Pay the primary payment option when credentials are available.**
  If you use Apple Pay APIs to find out whether someone has an active card in Wallet, you must make Apple Pay the primary — but not necessarily sole — payment option everywhere you use the APIs. Don’t separate Apple Pay into a different...
- **Use Apple Pay buttons only to initiate payment or, when appropriate, the Apple Pay setup process.**
  When people choose an Apple Pay button to make a purchase, but their device doesn’t have Apple Pay set up, they’re given the opportunity to set up Apple Pay. Don’t use Apple Pay buttons in any other way.
- **If you use a custom button to start the Apple Pay payment process, make sure your custom button doesn’t display “Apple Pay” or the Apple Pay logo.**
  In this scenario, you must let people know that you accept Apple Pay by displaying the [Apple Pay mark](https://developer.apple.com/design/human-interface-guidelines/apple-pay#Apple-Pay-mark) graphic or referencing Apple Pay in text on...
- **Use the Apple Pay mark graphic only to communicate that you accept Apple Pay.**
  The Apple Pay mark doesn’t facilitate payment. Never use it as a payment button or position it as a button. When using the Apple Pay mark to indicate Apple Pay as the selected payment method, you can create a separate custom button that...
- **Don’t hide an Apple Pay button or make it appear unavailable.**
  If an Apple Pay button can’t be used yet, such as when a product size or color hasn’t been selected, gracefully point out the problem after someone taps or clicks the button.
- **Inform search engines that Apple Pay is accepted on your website.**
  If your website uses semantic markup to provide product details to search engines, list Apple Pay as a payment option.
- **Provide a cohesive checkout experience.**
  It’s best when the entire checkout flow feels tightly integrated with your app or website. Use your branding throughout the checkout experience and avoid opening different pages or windows. For website checkout flows in particular,...
- **If Apple Pay is available, assume people want to use it.**
  Consider presenting the Apple Pay button as the first payment option, displaying it larger than other options, or using a line to visually separate it from other choices.
- **Accelerate single-item purchases with Apple Pay buttons on product detail pages.**
  In addition to a shopping cart, consider offering Apple Pay buttons on product detail pages so people can purchase an individual item quickly. Purchases initiated in this way need to be for an individual item only, excluding any items...
- **Accelerate multi-item purchases with express checkout.**
  An express checkout feature immediately shows the payment sheet and lets someone purchase everything in their cart quickly using a single shipping method and destination.
- **Support coupons and promotional codes in the payment sheet.**
  If you offer a coupon or promotional code, let people enter it directly on the payment sheet rather than requiring a separate step. This is especially important for express checkout flows, where people bypass the standard checkout...
- **Collect necessary information, like color and size options, before people reach the Apple Pay button.**
  When information is missing at checkout time — perhaps because someone forgot to choose an option — gracefully point out the problem and help them correct it. Use highlighting or warning text to identify missing information, and...
- **Collect optional information before checkout begins.**
  There’s no way to input optional data — like gift messages or delivery instructions — on the payment sheet, so collect this information ahead of time or even after the purchase is complete.
- **Gather multiple shipping methods and destinations before showing the payment sheet.**
  The payment sheet lets people select a single shipping method and destination for an entire order. If people can choose different shipping methods and destinations for individual items in an order, collect those details before Apple Pay...
- **For in-store pickup, help people choose a pickup location before displaying the payment sheet.**
  After someone chooses a pickup location, show the location’s address on the payment sheet. For developer guidance, see [Displaying a Read-Only Pickup...
- **Prefer checkout information from Apple Pay.**
  Assume that Apple Pay information is complete and up to date. Even if your app or website has existing contact, shipping, and payment information, consider fetching the latest from Apple Pay during checkout to reduce potential corrections.
- **Avoid requiring account creation before purchase.**
  If you want people to register for an account, ask them to do so on the order confirmation page. Prepopulate as many registration fields as possible using information provided during checkout.
- **Report transaction results in the payment sheet.**
  In failure cases, such as a bad address, provide error messages so people can take steps to fix the problem.
- **Display an order confirmation or thank-you page.**
  After the payment sheet shows the result of the transaction, display an order confirmation page to thank people for their purchase, provide details about when the order will ship, and indicate how to check its status. Listing Apple Pay...
- **Only present and request essential information.**
  People may get confused or have privacy concerns if the payment sheet includes extraneous information. For example, it makes sense to see a contact email address but not a shipping address if the purchase is a gift card that’s delivered...
- **Display the active coupon or promotional code, or let people enter one.**
  If people can enter a code before the payment sheet appears, show it on the sheet to reassure them that you applied the code. Consider allowing code entry on the payment sheet as well, particularly in an express checkout flow.
- **Let people choose the shipping method in the payment sheet.**
  To the extent space permits, show a clear description, a cost, and, optionally, an estimated delivery or pickup date — or range of dates — for each available option. Leverage the shipping method’s calendar and time-zone support to...
- **For in-store pickup, consider letting people choose a pickup window that works for them.**
  You can use the shipping method to supply a range of dates and times from which people can choose.
- **Use line items to explain additional charges, discounts, pending costs, add-on donations, recurring payments, and future payments.**
  A line item includes a label and cost; a line item for a recurring payment can also include a frequency. Don’t use line items to show an itemized list of products that make up the purchase. For developer guidance, see...
- **Keep line items short.**
  Make line items specific and easily understandable at a glance. Whenever possible, fit line items on a single line.
- **Provide a business name after the word *Pay* on the same line as the total.**
  Use the same business name people will see when they look for the charge on their bank or credit card statement. This provides reassurance that payment is going to the right place. For example, Pay [*Business_Name*].
- **If you’re not the end merchant, identify both businesses in the payment sheet.**
  When your app, App Clip, or website acts as an intermediary, such as a marketplace where people buy from third-party sellers, people may not realize two businesses are involved. Clearly describe the relationship in the Pay line using...
- **Clearly disclose when people may incur additional costs after payment authorization.**
  In some cases, you may not know the total cost at checkout time. For example, the price of a car ride based on distance or time might change after checkout. Or, someone might want to add a tip after they receive their delivery. In...
- **Handle data entry and payment errors gracefully.**
  If an error occurs during checkout, help people resolve it quickly so they can complete their transaction. For related guidance, see [Data validation...
- **Defer to the payment sheet for progress information during payment.**
  The payment sheet already presents loading states and progress clearly. Additional spinners or progress indicators can create confusion about the state of the transaction.
- **Avoid forcing compliance with your business logic.**
  Design a data validation process that’s intelligent enough to ignore irrelevant data and infer missing data whenever possible. For example, if your app requires a five-digit zip code but someone enters a Zip+4 code, ignore the...
- **Accurately report problems to the system.**
  When a problem occurs, provide a custom error message and the correct status code so the system can show the most relevant error on the payment sheet. For developer guidance, see...
- **Explain the problem clearly and succinctly when data is invalid or incorrectly formatted.**
  Reference the relevant field and indicate exactly what’s expected. For example, if people enter an invalid zip code, instead of showing “Address is invalid,” show a specific message like “Zip code doesn’t match city.” If the shipping...
- **Handle interruptions correctly.**
  An event like a cancellation or timeout might interrupt the payment flow, causing the payment sheet to dismiss. When such an event occurs, you must cancel any in-progress payment. After the payment sheet dismisses, people can restart...
- **Clarify subscription details before showing the payment sheet.**
  Before asking people to authorize a recurring payment, make sure they fully understand the billing frequency and any other terms of service. You can show the billing frequency on the payment sheet.
- **Include line items that reiterate billing frequency, discounts, and additional upfront fees.**
  Use these line items to remind people what they’re authorizing. If no payment is required at authorization time, clearly disclose when billing will occur.
- **Clearly communicate trial period terms.**
  For subscriptions with a trial period, use line items to display the trial amount (including $0 if free), the regular amount after the trial, and the date regular billing begins.
- **Clarify the current payment amount in the total line.**
  Make sure people know the amount they’re being billed at the time of authorization.
- **Only show the payment sheet when a subscription change results in additional fees.**
  When someone changes a subscription, authorization isn’t necessary if the cost decreases or remains the same.
- **Use a line item to identify a donation.**
  Display a line item on the payment sheet that reminds people they’re authorizing a donation; for example, display *Donation $50.00*.
- **Streamline checkout by offering predefined donation amounts.**
  You can reduce steps in the donation process by offering recommended donations, like $25, $50, $100. Include an Other Amount option too, so people can customize the donation if they prefer.
- **Always use the Apple-provided API to display Apple Pay buttons.**
  Unlike button graphics, API-generated buttons always have the correct appearance and are localized automatically. Don’t create custom Apple Pay button designs or try to replicate the Apple-provided ones. For developer guidance, see...
- **Prominently display the Apple Pay button.**
  Make the Apple Pay button no smaller than other payment buttons, and avoid making people scroll to see it.
- **Position the Apple Pay button correctly in relation to an Add to Cart button.**
  In a side-by-side layout, place the Apple Pay button to the right of an Add to Cart button.
- **Adjust the corner radius to match the appearance of other buttons.**
  By default, an Apple Pay button has rounded corners. You can change the corner radius to produce a button with square corners or a capsule-shape button. For developer guidance, see...
- **Maintain the minimum button size and margins around the button.**
  Be mindful that the button title may vary in length depending on the locale.
- **Use only the artwork provided by Apple, with no alterations other than height.**
  You can specify a height for the Apple Pay mark, but make sure that the height you use is equal to or larger than other payment brand marks in your payment flow. Don’t adjust the width, corner radius, or aspect ratio of the artwork;...
- **Maintain a minimum clear space around the mark of 1/10 of its height.**
  Don’t let the Apple Pay mark share its surrounding border with another graphic or button.
- **Capitalize Apple Pay in text as it appears in the Apple Trademark List.**
  Use two words with an uppercase *A*, an uppercase *P*, and lowercase for all other letters. Display Apple Pay entirely in uppercase only when doing so is necessary for conforming to an established typographic style that capitalizes all...
- **Never use the Apple logo to represent the name *Apple* in text.**
  In the United States, use the registered trademark symbol (®) the first time Apple Pay appears in body text. Don’t include a registered trademark symbol when Apple Pay appears as a selection option during checkout.
- **Coordinate the font face and size with your app or website.**
  Don’t mimic Apple typography. Instead, use text attributes that are consistent with the rest of your app or website.
- **Don’t translate *Apple Pay* or any other Apple trademark.**
  Always use Apple trademarks in English, even when they appear within non-English text.
- **In a payment selection context, you can display a text-only description of Apple Pay only when all payment options have text-only descriptions.**
  If any other payment option description includes an icon or logo, you must use the Apple Pay mark graphic as described in [Offering Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay#Offering-Apple-Pay).
- **When promoting Apple Pay in an app, follow App Store guidelines.**
  For specific guidance, see the [App Store marketing guidelines](https://developer.apple.com/app-store/marketing/guidelines/).

## Apple Pencil and Scribble
<sub>`pages/apple-pencil-and-scribble.md`</sub>

- **Support behaviors people intuitively expect when using a marking instrument.**
  Most people have a lot of experience with real-world marking tools, and this knowledge informs their expectations when they use Apple Pencil with your app. To provide a delightful experience, think about the ways people interact with...
- **Let people choose when to switch between Apple Pencil and finger input.**
  For example, if your app supports Apple Pencil for marking, also ensure that your app’s controls respond to Apple Pencil so people don’t have to switch to using their finger to activate them. In this scenario, a control that doesn’t...
- **Let people make a mark the moment Apple Pencil touches the screen**
  . You want the experience of putting Apple Pencil to screen to mirror the experience of putting a classic pencil to paper, so it’s essential to avoid requiring people to tap a button or enter a special mode before they can make a mark.
- **Help people express themselves by responding to the way they use Apple Pencil.**
  Apple Pencil may sense tilt (altitude), force (pressure), orientation (azimuth), and [Barrel roll](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble#Barrel-roll). Use this information to affect the...
- **Provide visual feedback to indicate a direct connection with content.**
  Make sure Apple Pencil appears to directly and immediately manipulate content it touches onscreen. Avoid letting Apple Pencil appear to initiate seemingly disconnected actions, or affect content on other parts of the screen.
- **Design a great left- and right-handed experience.**
  Avoid placing controls in locations that may be obscured by either hand. If there’s a chance controls may become obscured, consider letting people reposition them.
- **Use hover to help people predict what will happen when Apple Pencil touches the screen.**
  For example, as people hold Apple Pencil above the screen, a hover preview can show the dimensions and color of the mark that the current tool can make. As much as possible, avoid continuously modifying the preview as people move Apple...
- **Avoid using hover to initiate an action.**
  Unlike tapping a button or marking the screen, hovering is a relatively imprecise motion that doesn’t require people to think about the actual distance between Apple Pencil and the display. You don’t want people to inadvertently perform...
- **Prefer showing a preview value that’s near the middle in a range of dynamic values.**
  Dynamic properties like opacity or flow can be difficult to depict at the highest or lowest ends of the spectrum. For example, previewing the appearance of a brush mark made with the maximum pressure could occlude the area in which...
- **Consider using hover to support relevant interactions close to where people are marking.**
  For example, you might respond to hover by displaying a contextual menu of tool sizes when people perform a gesture like [Squeeze](https://developer.apple.com/design/human-interface-guidelines/apple-pencil-and-scribble#Squeeze) or press...
- **Prefer showing hover previews for Apple Pencil, not for a pointing device.**
  Although a pointing device can also respond to hover gestures, it might be confusing to provide the same visual feedback for both devices. If it makes sense in your app, you can restrict your hover preview to Apple Pencil only. For...
- **Respect people’s settings for the double-tap gesture when they make sense in your app.**
  By default, models of Apple Pencil that support the double-tap gesture respond by toggling between the current tool and the eraser, but people can set the gesture to toggle between the current and previous tool, show and hide the color...
- **Give people a way to specify custom double-tap behavior if necessary.**
  If you offer custom double-tap behavior in addition to some or all of the default behaviors, provide a control that lets people choose the custom behavior mode. People need to know which mode they’re in; otherwise, they may get confused...
- **Avoid using the double-tap gesture to perform an action that modifies content.**
  In rare cases, it’s possible for people to double-tap accidentally, which means that they may not even be aware that your app has performed the action. Prefer using double tap to perform actions that are easy for people to undo. In...
- **Treat squeeze as a single, quick gesture that performs a discrete — not continuous — action.**
  People sometimes squeeze with a lot of force, so holding a squeeze or squeezing several times quickly can be tiring. Help people remain comfortable by responding to a single squeeze and promptly displaying the result.
- **If you use squeeze to reveal app UI, like a contextual menu, display it close to Apple Pencil Pro.**
  Displaying the result of a squeeze near the tip of Apple Pencil Pro strengthens the connection between the device and the gesture, and can help people stay engaged with their task.
- **Define squeeze actions that are nondestructive and easy to undo.**
  As with the double-tap gesture, people can make the squeeze gesture without meaning to, so it’s essential to avoid using squeeze to perform an action that could result in data loss.
- **Use barrel roll only to modify marking behavior, not to enable navigation or display other controls.**
  In contrast to double tap and squeeze, barrel roll is naturally related to marking and doesn’t make sense for performing an interface action.
- **Make text entry feel fluid and effortless.**
  By default, Scribble works in all standard text components — such as text fields, text views, search fields, and editable fields in web content — except password fields. If you use a custom text field in your app, avoid making people...
- **Make Scribble available everywhere people might want to enter text.**
  Unlike using the keyboard, using Apple Pencil encourages people to treat the screen the way they treat a sheet of paper. Help strengthen this perception in your app by making Scribble consistently available in places where text entry...
- **Avoid distracting people while they write.**
  Some text field behaviors work well for keyboard input, but can disrupt the natural writing experience that Apple Pencil provides. For example, it’s best to avoid displaying autocompletion text as people write in a text field because...
- **While people are writing in a text field, make sure it remains stationary.**
  In some cases, it can make sense to move a text field when it becomes focused: for example, a search field might move to make more room to display results. Such a movement is fine when people are using the keyboard, but when they’re...
- **Prevent autoscrolling text while people are writing and editing in a text field.**
  When transcribed text autoscrolls, people might try to avoid writing on top of it. Worse, if text scrolls while people are using Apple Pencil to select it, they might select a different range of text than they want.
- **Give people enough space to write.**
  A small text field can feel uncomfortable to write in. When you know that Apple Pencil input is likely, improve the writing experience in your app by increasing the size of the text field before people begin to write in it or when they...
- **Help people draw on top of existing content.**
  By default, the colors on your PencilKit canvas dynamically adjust to Dark Mode, so people can create content in either mode and the results will look great in both. However, when people draw on top of existing content like a PDF or a...
- **Consider displaying custom undo and redo buttons when your app runs in a compact environment.**
  In a regular environment, the tool picker includes undo and redo buttons, but in a compact environment it doesn’t. In a compact environment, you could display undo and redo buttons in a toolbar. You might also consider supporting the...

## Augmented reality
<sub>`pages/augmented-reality.md`</sub>

- **Offer AR features only on capable devices.**
  If your app’s primary purpose is AR, make your app available only to devices that support ARKit. If your app includes features that require specific AR capabilities, or if AR features are optional in your app, don’t show people an error...
- **Let people use the entire display.**
  Devote as much of the screen as possible to displaying the physical world and your app’s virtual objects. Avoid cluttering the screen with controls and information that diminish the immersive experience.
- **Strive for convincing illusions when placing realistic objects.**
  Design detailed 3D assets with lifelike textures to create objects that appear to inhabit the physical environment in which you place them. Using information from ARKit, you can scale objects properly and position them on detected...
- **Consider how virtual objects with reflective surfaces show the environment.**
  Reflections in ARKit are approximations based on the environment captured by the camera. To help maintain the illusion that an AR experience is real, prefer small or coarse reflective surfaces that downplay the effect of these...
- **Use audio and haptics to enhance the immersive experience.**
  A sound effect or bump sensation is a great way to confirm that a virtual object has made contact with a physical surface or other virtual object. Background music can also help envelop people in the virtual world. For guidance, see...
- **Minimize text in the environment.**
  Display only the information that people need for your app experience.
- **If additional information or controls are necessary, consider displaying them in screen space.**
  Content in *screen space* appears fixed to a consistent location either in the virtual world or, less commonly, on the device screen. It’s typically easy for people to find and view content in screen space because it remains stationary...
- **Consider using indirect controls when you need to provide persistent controls.**
  *Indirect controls* are not part of the virtual environment — instead, they are 2D controls displayed in screen space. If people need access to persistent controls in your app, consider placing the controls so that people don’t have to...
- **Anticipate that people will use your app in a wide variety of real-world environments.**
  People may open your app in a place where there isn’t much room to move around or there aren’t any large, flat surfaces. Clearly communicate your app’s requirements and expectations to people up front to help them understand how their...
- **Be mindful of people’s comfort.**
  Holding a device at a certain distance or angle for a prolonged period can be fatiguing. To help avoid causing fatigue, consider placing objects at a distance that reduces the need to move the device closer to the object; in a game,...
- **If your app encourages people to move, introduce motion gradually.**
  For example, you might not want to make people dodge a virtual projectile as soon as they enter your AR game. Give people time to adapt to the AR experience in your app and then progressively encourage movement.
- **Be mindful of people’s safety.**
  When people are immersed in an AR experience, they’re not necessarily aware of their physical surroundings, so making rapid, sweeping, or expansive motions might be dangerous. Consider ways of making your app safe to operate; for...
- **Hide unnecessary app UI while people are using a coaching view.**
  By default, the coaching view appears automatically when initialization or relocalization starts, so be prepared to hide unrelated UI to help people concentrate on the coaching view’s instructions.
- **If necessary, offer a custom coaching experience.**
  Although you can configure the system-provided coaching view to help people provide specific information — such as the detection of a horizontal or vertical plane — you might need additional information or want to use a different visual...
- **Show people when to locate a surface and place an object.**
  You can use the system-provided coaching view to help people find a horizontal or vertical flat surface on which to place an object. After ARKit detects a surface, your app can display a custom visual indicator to show when object...
- **When people place an object, immediately integrate that object into the AR environment.**
  Although surface detection quickly and progressively refines accuracy, it’s best to avoid waiting for more accurate data before placing an object. Use the information available to respond instantly when people place an object; then,...
- **Consider guiding people toward offscreen virtual objects.**
  Sometimes, it can be difficult for people to locate an object that’s positioned offscreen. When this is the case, you can help people find such objects by offering visual or audible cues. For example, if an object is offscreen to the...
- **Avoid trying to precisely align objects with the edges of detected surfaces.**
  In AR, surface boundaries are approximations that may change as people’s surroundings are further analyzed.
- **Incorporate plane classification information to inform object placement.**
  For example, only let people place a virtual piece of furniture on a plane that’s classified as “floor,” or require a plane to be classified as “table” in order to place a virtual game board.
- **Let people use direct manipulation to interact with objects when possible.**
  It’s more immersive and intuitive when people can interact with onscreen 3D objects by touching them directly, than by using indirect controls in screen space. However, in situations where people are moving around as they use your app,...
- **Let people directly interact with virtual objects using standard, familiar gestures.**
  For example, consider supporting a single-finger drag gesture for moving objects, and a two-finger rotation gesture for spinning objects. For guidance, see [Gestures](https://developer.apple.com/design/human-interface-guidelines/gestures).
- **In general, keep interactions simple.**
  Touch gestures are inherently two-dimensional, but an AR experience involves the three dimensions of the real world. Consider the following approaches to simplifying people’s interactions with virtual objects.
- **Respond to gestures within reasonable proximity of interactive virtual objects.**
  It can be difficult for people to be precise when aiming to touch specific points on objects that are small, thin, or placed at a distance. When your app detects a gesture near an interactive object, it’s usually best to assume that...
- **Let people initiate object scaling when it makes sense in your app.**
  For example, if your app lets people explore an imaginary environment, it probably makes sense to support object scaling because your app doesn’t need to represent the real world. On the other hand, if your app helps shoppers decide on...
- **Be wary of potentially conflicting gestures.**
  A two-finger pinch gesture, for example, is similar to a two-finger rotation gesture. If you implement two similar gestures like this, be sure to test your app and make sure they’re interpreted properly.
- **Strive for virtual object movement that’s consistent with the physics of your app’s AR environment.**
  People don’t necessarily expect an object to move smoothly over a rough or uneven surface, but they do expect objects to remain visible during movement. Aim to keep moving objects attached to real-world surfaces and avoid causing...
- **Explore even more engaging methods of interaction.**
  Gestures aren’t the only way for people to interact with virtual objects in AR. Your app can use other factors, like motion and proximity, to bring content to life. A game character, for example, could turn its head to look at a person...
- **Consider allowing people occlusion.**
  If your app supports placing virtual objects behind people who appear in the device’s camera feed, enhance the illusion of reality by letting the people occlude the objects. For developer guidance, see [Occluding virtual content with...
- **When possible, let new participants enter a multiuser AR experience.**
  Unless your app requires all participants to join before the experience begins, consider using implicit map merging to let new people quickly join an ongoing AR experience. For developer guidance, see...
- **When a detected image first disappears, consider delaying the removal of virtual objects that are attached to it.**
  ARKit doesn’t track changes to the position or orientation of each detected image. To help prevent virtual objects from flickering, consider waiting up to one second before fading them out or removing them.
- **Limit the number of reference images in use at one time.**
  Image detection performance works best when ARKit looks for 100 or fewer distinct images in the real-world environment. If you need more than 100 reference images, you can change the set of active reference images based on context. For...
- **Limit the number of reference images requiring an accurate position.**
  Updating the position of a reference image requires more resources. Use a tracked image when the image may move in the environment or when an attached animation or virtual object is small compared to the size of the image.
- **If you must display instructional text, use approachable terminology.**
  AR is an advanced concept that may be intimidating to some people. To help make it approachable, avoid using technical terms like ARKit, world detection, and tracking. Instead, use friendly, conversational terms that most people will...
- **In a three-dimensional context, prefer 3D hints.**
  For example, placing a 3D rotation indicator around an object is more intuitive than displaying text-based instructions in a 2D overlay. Avoid displaying textual overlay hints in a 3D context unless people aren’t responding to...
- **Make important text readable.**
  Use screen space to display text used for critical labels, annotations, and instructions. If you need to display text in 3D space, make sure the text faces people and that you use the same type size regardless of the distance between...
- **If necessary, provide a way to get more information.**
  Design a visual indicator that fits with your app experience to show people that they can tap for more information.
- **Consider using the system-provided coaching view to help people relocalize.**
  During relocalization, ARKit attempts to reconcile its previous state with new observations of the current environment. To make these observations more useful, you can use the coaching view to help people return the device to its...
- **Consider hiding previously placed virtual objects during relocalization.**
  To avoid flickering or other unpleasant visual effects during relocalization, it can be best to hide virtual objects and redisplay them in their new positions.
- **Minimize interruptions if your app supports both AR and non-AR experiences.**
  One way to avoid interruptions is by embedding a non-AR experience within an AR experience so that people can handle the task without exiting and re-entering AR. For example, if your app helps people decide on a piece of furniture to...
- **Allow people to cancel relocalization.**
  If people don’t position and orient their device near where it was before an interruption, relocalization continues indefinitely without success. If coaching people to resume their session isn’t successful, consider providing a reset...
- **Indicate when the front-facing camera is unable to track a face for more than about half a second.**
  Use a visual indicator to indicate that the camera can no longer track the person’s face. If you need to provide text instructions in this situation, keep them to a minimum.
- **Let people reset the experience if it doesn’t meet their expectations.**
  Don’t force people to wait for conditions to improve or struggle with object placement. Give them a way to start over again and see if they have better results.
- **Suggest possible fixes if problems occur.**
  Analysis of the real-world environment and surface detection can fail or take too long for a variety of reasons — insufficient light, an overly reflective surface, a surface without enough detail, or too much camera motion. If your app...
- **Use the AR glyph as intended.**
  The glyph is strictly for initiating an ARKit-based experience. Never alter the glyph (other than adjusting its size and color), use it for other purposes, or use it in conjunction with AR experiences not created using ARKit.
- **Maintain minimum clear space.**
  The minimum amount of clear space required around an AR glyph is 10% of the glyph’s height. Don’t let other elements infringe on this space or occlude the glyph in any way.
- **Use the AR badges as intended and don’t alter them.**
  You can download AR badges, available in collapsed and expanded form, in [Resources](https://developer.apple.com/design/resources/#ios-apps). Use these images exclusively to identify products or other objects that can be viewed in AR...
- **Prefer the AR badge to the glyph-only badge.**
  In general, use the glyph-only badge for constrained spaces that can’t accommodate the AR badge. Both badges work well at their default size.
- **Use badging only when your app contains a mixture of objects that can be viewed in AR and objects that cannot.**
  If all objects in your app can be viewed in AR, then badging is redundant.
- **Keep badge placement consistent and clear.**
  A badge looks best when displayed in one corner of an object’s photo. Always place it in the same corner and make sure it’s large enough to be seen clearly (but not so large that it occludes important detail in the photo).
- **Maintain minimum clear space.**
  The minimum amount of clear space required around an AR badge is 10% of the badge’s height. Don’t allow other elements to infringe on this space and occlude the badge in any way.

## Boxes
<sub>`pages/boxes.md`</sub>

- **Prefer keeping a box relatively small in comparison with its containing view.**
  As a box’s size gets close to the size of the containing window or screen, it becomes less effective at communicating the separation of grouped content, and it can crowd other content.
- **Consider using padding and alignment to communicate additional grouping within a box.**
  A box’s border is a distinct visual element — adding nested boxes to define subgroups can make your interface feel busy and constrained.
- **Provide a succinct introductory title if it helps clarify the box’s contents.**
  The appearance of a box helps people understand that its contents are related, but it might make sense to provide more detail about the relationship. Also, a title can help VoiceOver users predict the content they encounter within the box.
- **If you need a title, write a brief phrase that describes the contents.**
  Use sentence-style capitalization. Avoid ending punctuation unless you use a box in a settings pane, where you append a colon to the title.

## Branding
<sub>`pages/branding.md`</sub>

- **Use your brand’s unique voice and tone in all the written communication you display.**
  For example, your brand might convey feelings of encouragement and optimism by using plain words, occasional exclamation marks and emoji, and simple sentence structures.
- **Consider choosing an accent color.**
  On most platforms, you can specify a color that the system applies to app elements like interface icons, buttons, and text. In macOS, people can also choose their own accent color that the system can use in place of the color an app...
- **Consider using a custom font.**
  If your brand is strongly associated with a specific font, be sure that it’s legible at all sizes and supports accessibility features like bold text and larger type. It can work well to use a custom font for headlines and subheadings...
- **Ensure branding always defers to content.**
  Using screen space for an element that does nothing but display a brand asset can mean there’s less room for the content people care about. Aim to incorporate branding in refined, unobtrusive ways that don’t distract people from your...
- **Help people feel comfortable by using standard patterns consistently.**
  Even a highly stylized interface can be approachable if it maintains familiar behaviors. For example, place UI components in expected locations and use standard symbols to represent common actions.
- **Resist the temptation to display your logo throughout your app or game unless it’s essential for providing context.**
  People seldom need to be reminded which app they’re using, and it’s usually better to use the space to give people valuable information and controls.
- **Avoid using a launch screen as a branding opportunity.**
  Some platforms use a launch screen to minimize the startup experience, while simultaneously giving the app or game a little time to load resources (for guidance, see [Launch...
- **Follow Apple’s trademark guidelines.**
  Apple trademarks must not appear in your app name or images. See [Apple Trademark List](https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html) and [Guidelines for Using Apple...

## Buttons
<sub>`pages/buttons.md`</sub>

- **Make buttons easy for people to use.**
  It’s essential to include enough space around a button so that people can visually distinguish it from surrounding components and content. Giving a button enough space is also critical for helping people select or activate it,...
- **Always include a press state for a custom button.**
  Without a press state, a button can feel unresponsive, making people wonder if it’s accepting their input.
- **In general, use a button that has a prominent visual style for the most likely action in a view.**
  To draw people’s attention to a specific button, use a prominent button style so the system can apply an accent color to the button’s background. Buttons that use color tend to be the most visually distinctive, helping people quickly...
- **Use style — not size — to visually distinguish the preferred choice among multiple options.**
  When you use buttons of the same size to offer two or more options, you signal that the options form a coherent set of choices. By contrast, placing two buttons of different sizes near each other can make the interface look confusing...
- **Avoid applying a similar color to button labels and content layer backgrounds.**
  If your app already has bright, colorful content in the content layer, prefer using the default monochromatic appearance of button labels. For more guidance, see [Liquid Glass...
- **Ensure that each button clearly communicates its purpose.**
  Depending on the platform, a button can contain a symbol (or icon), a text label, or both to help people understand what it does.
- **Try to associate familiar actions with familiar icons.**
  For example, people can predict that a button containing the `square.and.arrow.up` symbol will help them perform share-related activities. If it makes sense to use an icon in your button, consider using an existing or customized [SF...
- **Consider using text when a short label communicates more clearly than an icon.**
  To use text, write a few words that succinctly describe what the button does. Using [title-style capitalization](https://help.apple.com/applestyleguide/#/apsgb744e4a3?sub=apdca93e113f1d64), consider starting the label with a verb to...
- **Assign the primary role to the button people are most likely to choose.**
  When a primary button responds to the Return key, it makes it easy for people to quickly confirm their choice. In addition, when the button is in a temporary view — like a...
- **Don’t assign the primary role to a button that performs a destructive action, even if that action is the most likely choice.**
  Because of its visual prominence, people sometimes choose a primary button without reading it first. Help people avoid losing content by assigning the primary role to nondestructive buttons.
- **Configure a button to display an activity indicator when you need to provide feedback about an action that doesn’t instantly complete.** `[iOS, iPadOS]`
  Displaying an activity indicator within a button can save space in your user interface while clearly communicating the reason for the delay. To help clarify what’s happening, you can also configure the button to display a different...
- **Use a flexible-height push button only when you need to display tall or variable height content.** `[macOS]`
  Flexible-height buttons support the same configurations as regular push buttons — and they use the same corner radius and content padding — so they look consistent with other buttons in your interface. If you need to present a button...
- **Append a trailing ellipsis to the title when a push button opens another window, view, or app.** `[macOS]`
  Throughout the system, an ellipsis in a control title signals that people can provide additional input. For example, the Edit buttons in the AutoFill pane of Safari Settings include ellipses because they open other views that let people...
- **Consider supporting spring loading.** `[macOS]`
  On systems with a Magic Trackpad, *spring loading* lets people activate a button by dragging selected items over it and force clicking — that is, pressing harder — without dropping the selected items. After force clicking, people can...
- **Use square buttons in a view, not in the window frame.** `[macOS]`
  Square buttons aren’t intended for use in toolbars or status bars. If you need a button in a [toolbar](https://developer.apple.com/design/human-interface-guidelines/toolbars), use a toolbar item.
- **Prefer using a symbol in a square button.** `[macOS]`
  [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) provides a wide range of symbols that automatically receive appropriate coloring in their default state and in response to user interaction.
- **Avoid using labels to introduce square buttons.** `[macOS]`
  Because square buttons are closely connected with a specific view, their purpose is generally clear without the need for descriptive text.
- **Use the system-provided help button to display your help documentation.** `[macOS]`
  People are familiar with the appearance of the standard help button and know that choosing it opens help content.
- **When possible, open the help topic that’s related to the current context.** `[macOS]`
  For example, the help button in the Rules pane of Mail settings opens the Mail User Guide to a help topic that explains how to change these settings. If no specific help topic applies directly to the current context, open the top level...
- **Include no more than one help button per window.** `[macOS]`
  Multiple help buttons in the same context make it hard for people to predict the result of clicking one.
- **Position help buttons where people expect to find them.** `[macOS]`
  Use the following locations for guidance.
- **Use a help button within a view, not in the window frame.** `[macOS]`
  For example, avoid placing a help button in a toolbar or status bar.
- **Avoid displaying text that introduces a help button.** `[macOS]`
  People know what a help button does, so they don’t need additional descriptive text.
- **Use an image button in a view, not in the window frame.** `[macOS]`
  For example, avoid placing an image button in a toolbar or status bar. If you need to use an image as a button in a toolbar, use a toolbar item. See [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars).
- **Include about 10 pixels of padding between the edges of the image and the button edges.** `[macOS]`
  An image button’s edges define its clickable area even when they aren’t visible. Including padding ensures that a click registers correctly even if it’s not precisely within the image. In general, avoid including a system-provided...
- **If you need to include a label, position it below the image button.** `[macOS]`
  For related guidance, see [Labels](https://developer.apple.com/design/human-interface-guidelines/labels).
- **Prefer buttons that have a discernible background shape and fill.** `[visionOS]`
  It tends to be easier for people to see a button when it’s enclosed in a shape that uses a contrasting background fill. The exception is a button in a toolbar, context menu, alert, or...
- **Avoid creating a custom button that uses a white background fill and black text or icons.** `[visionOS]`
  The system reserves this visual style to convey the toggled state.
- **In general, prefer circular or capsule-shape buttons.** `[visionOS]`
  People’s eyes tend to be drawn toward the corners in a shape, making it difficult to keep looking at the shape’s center. The more rounded a button’s shape, the easier it is for people to look steadily at it. When you need to display a...
- **Provide enough space around a button to make it easy for people to look at it.** `[visionOS]`
  Aim to place buttons so their centers are always at least 60 pts apart. If your buttons measure 60 pts or larger, add 4 pts of padding around them to keep the hover effect from overlapping. Also, it’s usually best to avoid displaying...
- **Choose the right shape if you need to display text-labeled buttons in a stack or row.** `[visionOS]`
  Specifically, prefer the rounded-rectangle shape in a vertical stack of buttons and prefer the capsule shape in a horizontal row of buttons.
- **Use standard controls to take advantage of the audible feedback sounds people already know.** `[visionOS]`
  Audible feedback is especially important in visionOS, because the system doesn’t play haptics.
- **Use a toolbar to place buttons in the corners.** `[watchOS]`
  The system automatically moves the time and title to accommodate toolbar buttons. The system also applies the [Liquid Glass](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass) appearance to toolbar...
- **Prefer buttons that span the width of the screen for primary actions in your app.** `[watchOS]`
  Full-width buttons look better and are easier for people to tap. If two buttons must share the same horizontal space, use the same height for both, and use images or short text titles for each button’s content.
- **Use toolbar buttons to provide either navigation to related areas or contextual actions for the view’s content.** `[watchOS]`
  These buttons provide access to additional information or secondary actions for the view’s content.
- **Use the same height for vertical stacks of one- and two-line text buttons.** `[watchOS]`
  As much as possible, use identical button heights for visual consistency.

## Camera Control
<sub>`pages/camera-control.md`</sub>

- **Use SF Symbols to represent control functionality.**
  The system doesn’t support custom symbols; instead, pick a symbol from SF Symbols that clearly denotes a control’s behavior. iOS offers thousands of symbols you can use to represent the controls your app shows in the overlay. Symbols...
- **Keep names of controls short.**
  Control labels adhere to Dynamic Type sizes, and longer names may obfuscate the camera’s viewfinder.
- **Include units or symbols with slider control values to provide context.**
  Providing descriptive information in the overlay, such as EV, %, or a custom string, helps people understand what the slider controls. For developer guidance, see...
- **Define prominent values for a slider control.**
  Prominent values are ones people choose most frequently, or values that are evenly spaced, like the major increments of zoom factor. When a person slides on the Camera Control to adjust a slider control, the system more easily lands on...
- **Make space for the overlay in the viewfinder.**
  The overlay and control labels occupy the screen area adjacent to the Camera Control in both portrait and landscape orientations. To avoid overlapping the interface elements of your camera capture experience, place your UI outside of...
- **Minimize distractions in the viewfinder.**
  When capturing a photo or video, people appreciate a large preview image with as few visual distractions as possible. Avoid duplicating controls, like sliders and toggles, in your UI and the overlay when the system displays the overlay.
- **Enable or disable controls depending on the camera mode.**
  For example, disable video controls when taking photos. The overlay supports multiple controls, but you can’t remove or add controls at runtime.
- **Consider how to arrange your controls.**
  Order commonly used controls toward the middle to allow quick access, and include lesser used controls on either side. When a person lightly presses the Camera Control to open the overlay again, the system remembers the last control...
- **Allow people to use the Camera Control to launch your experience from anywhere.**
  Create a locked camera capture extension that lets people configure the Camera Control to launch your app’s camera experience from their locked device, the Home Screen, or from within other apps. For guidance, see [Camera experiences on...

## CarPlay
<sub>`pages/carplay.md`</sub>

- **Eliminate app interactions on iPhone when CarPlay is active.**
  Interactions with your app need to occur using the car’s built-in controls and display. If your app requires setup on iPhone, make sure people perform it before the vehicle is in motion.
- **Never lock people out of CarPlay because the connected iPhone requires input.**
  Your app needs to function when iPhone is inaccessible — for example, when people put it in a bag or in the trunk while driving. If people must resolve a problem on the connected iPhone, let them do so after the vehicle stops.
- **Make sure your app works without requiring people to unlock iPhone.**
  Most people use CarPlay while their iPhone is locked, so ensure that the features you provide in your CarPlay app work as expected in this scenario.
- **Let people choose when to start playback.**
  In general, avoid beginning playback automatically unless your app’s purpose is to play a single source of audio, or your app is resuming previously interrupted audio. Also, avoid starting an audio session until you’re ready to actually...
- **Start playback as soon as audio has sufficiently loaded.**
  After people make a selection, it may take several seconds for audio to begin playing, depending on buffering and network conditions. The system keeps the selection highlighted and displays a spinning activity indicator until your app...
- **Display the Now Playing screen when audio is ready to play.**
  Don’t delay playback until descriptive information completes loading. If necessary, continue loading such information in the background, and show it when it’s available.
- **Resume audio playback after an interruption only when it’s appropriate.**
  For example, your app can resume audio after a temporary interruption like a phone call. Permanent interruptions, such as a music playlist initiated by Siri, are nonresumable. When a resumable interruption occurs, your app needs to...
- **When necessary, automatically adjust audio levels, but don’t change the overall volume.**
  Although your app can adjust relative, independent volume levels to achieve a great mix of audio, people need to control the final output volume.
- **Provide useful, high-value information in a clean layout that’s easy to scan from the driver’s seat.**
  Don’t clutter the screen with nonessential details and unnecessary visual embellishments.
- **Maintain an overall consistent appearance throughout your app.**
  In general, ensure that elements with similar functions look similar.
- **Ensure that primary content stands out and feels actionable.**
  Large items tend to appear more important than smaller ones and are easier for people to tap. In general, place the most important content and controls in the upper half of the screen.
- **In general, prefer a limited color palette that coordinates with your app logo.**
  Subtle use of color is a great way to communicate your brand.
- **Avoid using the same color for interactive and noninteractive elements.**
  If interactive and noninteractive elements have the same color, it’s hard for people to know where to tap.
- **Test your app’s color scheme under a variety of lighting conditions in an actual car.**
  Lighting varies significantly based on time of day, weather, window tinting, and more. Colors you see on your computer at design time won’t always look the same when your app is used in the real world. Consider how color brightness...
- **Ensure your app looks great in both dark and light environments.**
  CarPlay supports both light and dark appearances, and may automatically adjust the current appearance based on lighting conditions.
- **Choose colors that help you communicate effectively with everyone.**
  Different people see and interpret colors differently. For guidance on using colors in ways that people appreciate, see [Inclusive color](https://developer.apple.com/design/human-interface-guidelines/color#Inclusive-color).
- **Supply high-resolution images with scale factors of @2x and @3x for all CarPlay artwork in your app.**
  The system automatically shows the correct images and scales them appropriately, based on the resolution and size of the car’s display.
- **Mirror your iPhone app icon.**
  A well-designed app icon works well in CarPlay and on iPhone, without the need for a second design.
- **Don’t use black for your icon’s background.**
  Lighten a black background or add a border so the icon doesn’t blend into the display background.
- **Report errors in CarPlay, not on the connected iPhone.**
  If you must notify people of a problem, do so clearly in CarPlay. Never direct people to pick up their iPhone to read or resolve an error.

## CareKit
<sub>`pages/carekit.md`</sub>

- **Provide a coherent privacy policy.**
  During the app submission process, you must provide a URL to a clearly stated privacy policy, so that people can view the policy when they click the link in the App Store page for your app. For developer guidance, see [App information >...
- **Request access to health data only when you need it.**
  It makes sense to request access to weight information when people log their weight, for example, but not immediately after your app launches. When your request is clearly related to the current context, you help people understand your...
- **Clarify your app’s intent by adding descriptive messages to the standard permission screen.**
  People expect to see the system-provided permission screen when asked to approve access to health data. Write a few succinct sentences that explain why you need the information and how people can benefit from sharing it with your app....
- **Manage health data sharing solely through the system’s privacy settings.**
  People expect to globally manage access to their health information in Settings > Privacy. Don’t confuse people by building additional screens in your app that affect the flow of health data.
- **Use the simple style for a one-step task.**
  The default simple-style view consists of a header area that contains a title, subtitle, and button. You provide the title and subtitle, and you can provide a custom image to display in the button when the task is complete. If you don’t...
- **Use the instructions style when you need to add informative text to a simple task.**
  For example, if a single-step medication task needs to include additional information — such as “Take on an empty stomach” or “Take at bedtime” — you can use an instructions-style task to display it.
- **Use the log style to help people log events.**
  For example, you could use this task style to display a button people can tap whenever they feel nauseated. The log-style task can automatically display a timestamp every time the patient logs an event.
- **Use the checklist style to display a list of actions or steps in a multistep task.**
  For example, if people must take a medication three times per day, you could display the three scheduled times in a checklist. Each checklist item can include a text description and a button that people can tap to mark the item as done....
- **Use the grid style to display a grid of buttons in a multistep task.**
  Like the checklist style, the grid style also supports a multistep task, but it displays the steps in a more compact arrangement. You can supply a succinct title for each button (if you need to provide additional description for each...
- **Consider using color to reinforce the meaning of task items.**
  Color can be a good way to help people understand information at a glance. For example, you could use one color for medications and a different color for physical activities. Always avoid using color as the only way to convey...
- **Combine accuracy with simplicity when describing a task and its steps.**
  For example, use a medication’s marketing name instead of its chemical description. Also, when the context of a task helps to clarify meaning, minimize the number of words you use. For example, a daily medication task generally tells...
- **Consider supplementing multistep or complex tasks with videos or images.**
  Visually demonstrating how to perform a task can help people avoid mistakes.
- **Consider highlighting narratives and trends to illustrate progress.**
  For example, your app could display a bar chart that shows a correlation between the number of times people took medication and their level of pain. Displaying such data can encourage better adherence to a care plan.
- **Label chart elements clearly and succinctly.**
  Long, detailed labels can make a chart difficult to read and understand. Keep labels short and avoid repeating the same information. For example, a heart rate chart might use the term *BPM* in an axis label instead of using it in the...
- **Use distinct colors.**
  In general, avoid using different shades of the same color to mean different things. Also ensure that you use colors with sufficient contrast. For related guidance, see...
- **Consider providing a legend to add clarity.**
  If the colors you use to represent different types of data aren’t immediately clear, include a legend that clearly and succinctly describes them.
- **Clearly denote units of time.**
  People need to know whether time-based data is represented in seconds, minutes, hours, days, weeks, months, or years. If you don’t want to include this information in individual data value labels, include it in an axis label or...
- **Consolidate large data sets for greater readability.**
  A large amount of data can make a chart unreadable by reducing the size of individual data points and presenting too much visible information. Look for ways to group and organize data for clarity and simplicity.
- **If necessary, offset data to keep charts proportional.**
  It’s easy for very small data points to get lost or become unreadable in a chart that also contains very large data points. If the difference between data points is significant, find ways to offset or restructure the data so all data...
- **Consider using color to categorize care team members.**
  Color can help people identify care team members at a glance.
- **Minimize notifications.**
  Care plans vary from patient to patient. While one individual may have only a few daily tasks to complete, another may have a long list. Use notifications sparingly so people don’t feel overwhelmed. When possible, consider coalescing...
- **Consider providing a detail view.**
  In addition to providing more information, a notification detail view can help people take immediate action without leaving their current context to open your app. For example, you could use a notification detail view to display a list...
- **Design a relevant care symbol.**
  If you need to customize a symbol, be sure the design is closely related to your app or the general concept of health and wellness. Avoid creating a purely decorative symbol or using a corporate logo as a custom symbol.
- **Incorporate refined, unobtrusive branding.**
  People use CareKit apps to help them achieve their health and wellness goals; they don’t want to see advertising. To avoid distracting people from their care plan, subtly incorporate your brand through your app’s use of color and...

## Charting data
<sub>`pages/charting-data.md`</sub>

- **Use a chart when you want to highlight important information about a dataset.**
  Charts are visually prominent, so they tend to draw people’s attention. Take advantage of this prominence by clearly communicating what people can learn from the data they care about.
- **Keep a chart simple, letting people choose when they want additional details.**
  Resist the temptation to pack as much data as possible into a chart. Too much data can make a chart visually overwhelming and difficult to use, obscuring the relationships and other information you want to convey. If you have a lot of...
- **Make every chart in your app accessible.**
  A chart communicates visually through graphical representations of data and visual descriptions. In addition to the visual descriptions you display, it’s crucial to provide both accessibility labels that describe chart values and...
- **In general, prefer using common chart types.**
  People tend to be familiar with common chart types — such as bar charts and line charts — so using one of these types in your app can make it more likely that people will already know how to read your chart. For guidance, see...
- **If you need to create a chart that presents data in a novel way, help people learn how to interpret the chart.**
  For example, when a Watch pairs with iPhone, Activity introduces the Activity rings by animating them individually, showing people how each ring maps to the move, exercise, and stand metrics.
- **Examine the data from multiple levels or perspectives to find details you can display to enhance the chart.**
  For example, viewing the data from a macro level can help you determine high-level summaries that people might be interested in, like totals or averages. From a mid-level perspective, you might find ways to help people identify useful...
- **Aid comprehension by adding descriptive text to the chart.**
  Descriptive text titles, subtitles, and annotations help emphasize the most important information in a chart and can highlight actionable takeaways. You can also display brief descriptive text that serves as a headline or summary for a...
- **Match the size of a chart to its functionality, topic, and level of detail.**
  In general, a chart needs to be large enough to comfortably display the details you need to include and expansive enough for the interactivity you want to support. For example, you always want to make it easy for people to read a...
- **Prefer consistency across multiple charts, deviating only when you need to highlight differences.**
  If multiple charts in your app serve a similar purpose, you generally don’t want to imply that the charts are unrelated by using a different type or style for each one. Also, using a consistent visual approach for the charts in your app...
- **Maintain continuity among multiple charts that use the same data.**
  When you use multiple charts to help people explore one dataset from different perspectives, it’s important to use one chart type and consistent colors, annotations, layouts, and descriptive text to signal that the dataset remains the...

## Charts
<sub>`pages/charts.md`</sub>

- **Choose a mark type based on the information you want to communicate about the data.**
  Some of the most familiar mark types are bar, line, and point; for developer guidance on these and other mark types, see [Swift Charts](https://developer.apple.com/documentation/charts).
- **Consider combining mark types when it adds clarity to your chart.**
  For example, if you use a line chart to show a change over time, you might want to add point marks on top of the line to highlight individual data points. By combining points with a line, you can help people understand the overall trend...
- **Use a fixed or dynamic axis range depending on the meaning of your chart.**
  In a *fixed* range, the upper and lower bounds of the axis never change, whereas in a *dynamic* range, the upper and lower bounds can vary with the current data. Consider using a fixed range when specific minimum and maximum values are...
- **Define the value of the lower bound based on mark type and chart usage.**
  For example, bar charts can work well when you use zero for the lower bound of the Y axis, because doing so lets people visually compare the relative heights of individual bars to get a reasonable estimate of their values. In contrast,...
- **Prefer familiar sequences of values in the tick and grid-line labels for an axis.**
  For example, if you use a common number sequence like 0, 5, 10, etc., people are likely to know at a glance that each tick value equals the previous value plus five. Even though a sequence like 1, 6, 11, etc., follows the same rule,...
- **Tailor the appearance of grid lines and labels to a chart’s use cases.**
  Too many grid lines can be visually overwhelming, distracting people from the data; too few grid lines can make it difficult to estimate a mark’s value. To help you determine the appropriate density and visual weight of these elements,...
- **Write descriptions that help people understand what a chart does before they view it.**
  When you provide information-rich titles and labels that describe the purpose and functionality of a chart, you give people the context they need before they dive in and examine the details. Providing context in this way is especially...
- **Summarize the main message of your chart to help make it approachable and useful for everyone.**
  Although a primary reason to use a chart is to display the data that supports the main message, it’s essential to summarize key information so that people can grasp it quickly. For example, Weather provides a title and subtitle that...
- **Establish a consistent visual hierarchy that helps communicate the relative importance of various chart elements.**
  Typically, you want the data itself to be most prominent, while letting the descriptions and axes provide additional context without competing with the data.
- **In a compact environment, maximize the width of the plot area to give people enough space to comfortably examine a chart.**
  To help important data fit well in a given width, ensure that labels on a vertical axis are as short as possible without losing clarity. You might also consider describing units in other areas of the chart, such as in a title, and...
- **Make every chart in your app accessible.**
  Charts — like all infographics — need to be fully accessible to everyone, regardless of how they perceive content. For example, it’s essential to support VoiceOver, which describes onscreen content to help people get information and...
- **Let people interact with the data when it makes sense, but don’t require interaction to reveal critical information.**
  In Stocks, for example, people are often most interested in a stock’s performance over time, so the app displays a line graph that depicts performance during the time period people choose, such as one day, three months, or five years....
- **Make it easy for everyone to interact with a chart.**
  Sometimes, chart marks are too small to target with a finger or a pointer, making your chart hard to use for people with reduced motor control and uncomfortable for everyone. When this is the case, consider expanding the hit target to...
- **Make an interactive chart easy to navigate when using keyboard commands (including full keyboard access) or Switch Control.**
  By default, these input types tend to visit individual onscreen elements in a linear sequence, such as the sequence of values in a data file. If you want to provide a custom navigation experience in your chart, here are two main ways to...
- **Help people notice important changes in a chart.**
  For example, if people don’t notice when marks or axes change, they can misread a chart. Animating such changes can help people notice them, but you need to highlight the changes in other ways, too, to ensure that VoiceOver users and...
- **Align a chart with surrounding interface elements.**
  For example, it often works well to align the leading edge of a chart with the leading edge of other views in a screen. One way to maintain a clean leading edge in a chart is to display the label for each vertical grid line on its...
- **Avoid relying solely on color to differentiate between different pieces of data or communicate essential information in a chart.**
  Using meaningful color in a chart works well to highlight differences and elevate key details, but it’s crucial to include alternative ways to convey this information so that people can use your chart regardless of whether they can...
- **Aid comprehension by adding visual separation between contiguous areas of color.**
  For example, in a bar chart that stacks marks in a single row or column, it’s common to assign a different color to each mark. In this design, adding separators between the marks can help people distinguish individual ones.
- **Consider using Audio Graphs to give VoiceOver users more information about your chart.**
  You can customize the default Audio Graphs implementation that Swift Charts provides by supplying a chart title and descriptive summary that VoiceOver speaks to help people understand the purpose and main features of your chart. If you...
- **Write accessibility labels that support the purpose of your chart.**
  For example, Maps shows elevation for a cycling route using a chart that represents the change in elevation over the course of the route. The purpose of the chart is to give people a sense of the terrain for the entire route, not to...
- **Hide visible text labels for axes and ticks from assistive technologies.**
  Axis and tick labels help people visually assess trends in a chart and estimate mark values. VoiceOver users can get mark values and trend information through accessibility labels and Audio Graphs, so they don’t generally need the...
- **In general, avoid requiring complex chart interactions in your watchOS app.** `[watchOS]`
  As much as possible, prefer displaying useful information people can get at a glance and supporting simple interactions when they add value. If you also offer a version of your app in another platform, consider using it to display more...

## Collaboration and sharing
<sub>`pages/collaboration-and-sharing.md`</sub>

- **Place the Share button in a convenient location, like a toolbar, to make it easy for people to start sharing or collaborating.**
  In iOS 16, the system-provided share sheet includes ways to choose a file-sharing method and set permissions for a new collaboration; iPadOS 16 and macOS 13 introduce similar appearance and functionality in the sharing popover. In your...
- **If necessary, customize the share sheet or sharing popover to offer the types of file sharing your app supports.**
  If you use CloudKit, you can add support for sending a copy of a file by passing both the file and your collaboration object to the share sheet. Because the share sheet has built-in support for multiple items, it automatically detects...
- **Write succinct phrases that summarize the sharing permissions you support.**
  For example, you might write phrases like “Only invited people can edit” or “Everyone can make changes.” The system uses your permission summary in a button that reveals a set of sharing options that people use to define the collaboration.
- **Provide a set of simple sharing options that streamline collaboration setup.**
  You can customize the view that appears when people choose the permission summary button to provide choices that reflect your collaboration functionality. For example, you might offer options that let people specify who can access the...
- **Prominently display the Collaboration button as soon as collaboration starts.**
  The system-provided Collaboration button reminds people that the content is shared and identifies who’s sharing it. Because the Collaboration button typically appears after people interact with the share sheet or sharing popover, it...
- **Provide custom actions in the collaboration popover only if needed.**
  Choosing the Collaboration button in your app reveals a popover that consists of three sections. The top section lists collaborators and provides communication buttons that can open Messages or FaceTime, the middle section contains your...
- **If it makes sense in your app, customize the title of the modal view’s collaboration-management button.**
  People choose this button — titled “Manage Shared File” by default — to reveal the collaboration-management view where they can change settings and add or remove collaborators. If you use CloudKit sharing, the system provides a...
- **Consider posting collaboration event notifications in Messages.**
  Choose the type of event that occurred — such as a change in the content or the collaboration membership, or the mention of a participant — and include a universal link people can use to open the relevant view in your app. For developer...

## Collections
<sub>`pages/collections.md`</sub>

- **Use the standard row or grid layout whenever possible.**
  Collections display content by default in a horizontal row or a grid, which are simple, effective appearances that people expect. Avoid creating a custom layout that might confuse people or draw undue attention to itself.
- **Consider using a table instead of a collection for text.**
  It’s generally simpler and more efficient to view and digest textual information when it’s displayed in a scrollable list.
- **Make it easy to choose an item.**
  If it’s too difficult to get to an item in your collection, people will get frustrated and lose interest before reaching the content they want. Use adequate padding around images to keep focus or hover effects easy to see and prevent...
- **Add custom interactions when necessary.**
  By default, people can tap to select, touch and hold to edit, and swipe to scroll. If your app requires it, you can add more gestures for performing custom actions.
- **Consider using animations to provide feedback when people insert, delete, or reorder items.**
  Collections support standard animations for these actions, and you can also use custom animations.
- **Use caution when making dynamic layout changes.** `[iOS, iPadOS]`
  The layout of a collection can change dynamically. Be sure any changes make sense and are easy to track. If possible, try to avoid changing the layout while people are viewing and interacting with it, unless it’s in response to an...

## Color
<sub>`pages/color.md`</sub>

- **Avoid using the same color to mean different things.**
  Use color consistently throughout your interface, especially when you use it to help communicate information like status or interactivity. For example, if you use your brand color to indicate that a borderless button is interactive,...
- **Make sure all your app’s colors work well in light, dark, and increased contrast contexts.**
  iOS, iPadOS, macOS, and tvOS offer both light and [Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode) appearance settings. [System...
- **Test your app’s color scheme under a variety of lighting conditions.**
  Colors can look different when you view your app outside on a sunny day or in dim light. In bright surroundings, colors look darker and more muted. In dark environments, colors appear bright and saturated. In visionOS, colors can look...
- **Test your app on different devices.**
  For example, the True Tone display — available on certain iPhone, iPad, and Mac models — uses ambient light sensors to automatically adjust the white point of the display to adapt to the lighting conditions of the current environment....
- **Consider how artwork and translucency affect nearby colors.**
  Variations in artwork sometimes warrant changes to nearby colors to maintain visual continuity and prevent interface elements from becoming overpowering or underwhelming. Maps, for example, displays a light color scheme when in map mode...
- **If your app lets people choose colors, prefer system-provided color controls where available.**
  Using built-in color pickers provides a consistent user experience, in addition to letting people save a set of colors they can access from any app. For developer guidance, see...
- **Avoid relying solely on color to differentiate between objects, indicate interactivity, or communicate essential information.**
  When you use color to convey information, be sure to provide the same information in alternative ways so people with color blindness or other visual disabilities can understand it. For example, you can use text labels or glyph shapes to...
- **Avoid using colors that make it hard to perceive content in your app.**
  For example, insufficient contrast can cause icons and text to blend with the background and make content hard to read, and people who are color blind might not be able to distinguish some color combinations. For guidance, see...
- **Consider how the colors you use might be perceived in other countries and cultures.**
  For example, red communicates danger in some cultures, but has positive connotations in other cultures. Make sure the colors in your app send the message you intend.
- **Avoid hard-coding system color values in your app.**
  Documented color values are for your reference during the app design process. The actual color values may fluctuate from release to release, based on a variety of environmental variables. Use APIs like...
- **Avoid redefining the semantic meanings of dynamic system colors.**
  To ensure a consistent experience and ensure your interface looks great when the appearance of the platform changes, use dynamic system colors as intended. For example, don’t use the...
- **Apply color sparingly to the Liquid Glass material, and to symbols or text on the material.**
  If you apply color, reserve it for elements that truly benefit from emphasis, such as status indicators or primary actions. To emphasize primary actions, apply color to the background rather than to symbols or text. For example, the...
- **Avoid using similar colors in control labels if your app has a colorful background.**
  While color can make apps more visually appealing, playful, or reflective of your brand, too much color can be overwhelming and make control labels more difficult to read. If your app features colorful backgrounds or visually rich...
- **Be aware of the placement of color in the content layer.**
  Make sure your interface maintains sufficient contrast by avoiding overlap of similar colors in the content layer and controls when possible. Although colorful content might intermittently scroll underneath controls, make sure its...
- **Apply color profiles to your images.**
  Color profiles help ensure that your app’s colors appear as intended on different displays. The sRGB color space produces accurate colors on most displays.
- **Use wide color to enhance the visual experience on compatible displays.**
  Wide color displays support a P3 color space, which can produce richer, more saturated colors than sRGB. As a result, photos and videos that use wide color are more lifelike, and visual data and status indicators that use wide color can...
- **Provide color space–specific image and color variations if necessary.**
  In general, P3 colors and images appear fine on sRGB displays. Occasionally, it may be hard to distinguish two very similar P3 colors when viewing them on an sRGB display. Gradients that use P3 colors can also sometimes appear clipped...
- **Consider choosing a limited color palette that coordinates with your app logo.** `[tvOS]`
  Subtle use of color can help you communicate your brand while deferring to the content.
- **Avoid using only color to indicate focus.** `[tvOS]`
  Subtle scaling and responsive animation are the primary ways to denote interactivity when an element is in focus.
- **Use color sparingly, especially on glass.** `[visionOS]`
  Standard visionOS windows typically use the system-defined glass [Materials](https://developer.apple.com/design/human-interface-guidelines/materials), which lets light and objects from people’s physical surroundings and their space show...
- **Prefer using color in bold text and large areas.** `[visionOS]`
  Color in lightweight text or small areas can make them harder to see and understand.
- **In a fully immersive experience, help people maintain visual comfort by keeping brightness levels balanced.** `[visionOS]`
  Although using high contrast can help direct people’s attention to important content, it can also cause visual discomfort if people’s eyes have adjusted to low light or darkness. Consider making content fully bright only when the rest...
- **Use background color to support existing content or supply additional information.** `[watchOS]`
  Background color can establish a sense of place and help people recognize key content. For example, in Activity, each infographic view for the Move, Exercise, and Stand Activity rings has a background that matches the color of the ring....
- **Recognize that people might prefer graphic complications to use tinted mode instead of full color.** `[watchOS]`
  The system can use a single color that’s based on the wearer’s selected color in a graphic complication’s images, gauges, and text. For guidance, see...

## Color wells
<sub>`pages/color-wells.md`</sub>

- **Consider the system-provided color picker for a familiar experience.**
  Using the built-in color picker provides a consistent experience, in addition to letting people save a set of colors they can access from any app. The system-defined color picker can also help provide a familiar experience when...

## Column views
<sub>`pages/column-views.md`</sub>

- **Show the root level of your data hierarchy in the first column.**
  People know they can quickly scroll back to the first column to begin navigating the hierarchy from the top again.
- **Consider showing information about the selected item when there are no nested items to display.**
  The Finder, for example, shows a preview of the selected item and information like the creation date, modification date, file type, and size.
- **Let people resize columns.**
  This is especially important if the names of some data items are too long to fit within the default column width.

## Combo boxes
<sub>`pages/combo-boxes.md`</sub>

- **Populate the field with a meaningful default value from the list.**
  Although the field can be empty by default, it’s best when the default value refers to the hidden choices. The default value doesn’t have to be the first item in the list.
- **Use an introductory label to let people know what types of items to expect.**
  Generally, use title-style capitalization for labels and end them with a colon. For related guidance, see [Labels](https://developer.apple.com/design/human-interface-guidelines/labels).
- **Provide relevant choices.**
  People appreciate the ability to enter a custom value, as well as the convenience of choosing from a list of the most likely choices.
- **Make sure list items aren’t wider than the text field.**
  If an item is too wide, the text field might truncate it, which is hard for people to read.

## Complications
<sub>`pages/complications.md`</sub>

- **Identify essential, dynamic content that people want to view at a glance.**
  Although people can use a complication to quickly launch an app, the complication behavior they appreciate more is the display of relevant information that always feels up to date. A static complication that doesn’t display meaningful...
- **Support all complication families when possible.**
  Supporting more families means that your complications are available on more watch faces. If you can’t display useful information for a particular complication family, provide an image that represents your app — like your app icon —...
- **Consider creating multiple complications for each family.**
  Supporting multiple complications helps you take advantage of shareable watch faces and lets people configure a watch face that’s centered on an app they love. For example, an app that helps people train for triathlons could offer three...
- **Define a different deep link for each complication you support.**
  It works well when each complication opens your app to the most relevant area. If all the complications you support open the same area in your app, they can seem less useful.
- **Keep privacy in mind.**
  With the Always-On Retina display, information on the watch face might be visible to people other than the wearer. Make sure you help people prevent potentially sensitive information from being visible to others. For guidance, see...
- **Carefully consider when to update data.**
  You provide a complication’s data in the form of a timeline where each entry has a value that specifies the time at which to display your data on the watch face. Different data sets might require different time values. For example, a...
- **Choose a ring or gauge style based on the data you need to display.**
  Many families support a ring or gauge layout that provides consistent ways to represent numerical values that can change over time. For example:
- **Make sure images look good in tinted mode.**
  In tinted mode, the system applies a solid color to a complication’s text, gauges, and images, and desaturates full-color images unless you provide tinted versions of them. For developer guidance, see...
- **Recognize that people might prefer to use tinted mode for complications, instead of viewing them in full color.**
  When people choose tinted mode, the system automatically desaturates your complication, converting it to grayscale and tinting its images, gauges, and text using a single color that’s based on the wearer’s selected color.
- **When creating complication content, generally use line widths of two points or greater.**
  Thinner lines can be difficult to see at a glance, especially when the wearer is in motion. Use line weights that suit the size and complexity of the image.
- **Provide a set of static placeholder images for each complication you support.**
  The system uses placeholder images when there’s no other content to display for your complication’s data. For example, when people first install your app, the system can display a static placeholder while it checks to see if your app...

## Context menus
<sub>`pages/context-menus.md`</sub>

- **Prioritize relevancy when choosing items to include in a context menu.**
  A context menu isn’t for providing advanced or rarely used items; instead, it helps people quickly access the commands they’re most likely to need in their current context. For example, the context menu for a Mail message in the Inbox...
- **Aim for a small number of menu items.**
  A context menu that’s too long can be difficult to scan and scroll.
- **Support context menus consistently throughout your app.**
  If you provide context menus for items in some places but not in others, people won’t know where they can use the feature and may think there’s a problem.
- **Always make context menu items available in the main interface, too.**
  For example, in Mail in iOS and iPadOS, the context menu items that are available for a message in the Inbox are also available in the toolbar of the message view. In macOS, an app’s menu bar menus list all the app’s commands, including...
- **If you need to use submenus to manage a menu’s complexity, keep them to one level.**
  A submenu is a menu item that reveals a secondary menu of logically related commands. Although submenus can shorten a context menu and clarify its commands, more than one level of submenu complicates the experience and can be difficult...
- **Hide unavailable menu items, don’t dim them.**
  Unlike a regular menu, which helps people discover actions they can perform even when the action isn’t available, a context menu displays only the actions that are relevant to the currently selected view or content. In macOS, the...
- **Aim to place the most frequently used menu items where people are likely to encounter them first.**
  When a context menu opens, people often read it starting from the part that’s closest to where their finger or pointer revealed it. Depending on the location of the selected content, a context menu might open above or below it, so you...
- **Show keyboard shortcuts in your app’s main menus, not in context menus.**
  Context menus already provide a shortcut to task-specific commands, so it’s redundant to display keyboard shortcuts too.
- **Follow best practices for using separators.**
  As with other types of menus, you can use separators to group items in a context menu and help people scan the menu more quickly. In general, you don’t want more than about three groups in a context menu. For guidance, see...
- **In iOS, iPadOS, and visionOS, warn people about context menu items that can destroy data.**
  If you need to include potentially destructive items in your context menu — such as Delete or Remove — list them at the end of the menu and identify them as destructive (for developer guidance, see...
- **Include a title in a context menu only if doing so clarifies the menu’s effect.**
  For example, when people select multiple Mail messages and tap the Mark toolbar button in iOS and iPadOS, the resulting context menu displays a title that states the number of selected messages, reminding people that the command they...
- **Represent menu item actions with familiar icons.**
  Icons help people recognize common actions throughout your app. Use the same icons as the system to represent actions such as Copy, Share, and Delete, wherever they appear. For a list of icons that represent common actions, see...
- **Provide either a context menu or an edit menu for an item, but not both.** `[iOS, iPadOS]`
  If you provide both features for the same item, it can be confusing to people — and difficult for the system to detect their intent. See [Edit menus](https://developer.apple.com/design/human-interface-guidelines/edit-menus).
- **In iPadOS, consider using a context menu to let people create a new object in your app.** `[iOS, iPadOS]`
  iPadOS lets you reveal a context menu when people perform a long press on the touchscreen or use a secondary click with an attached trackpad or keyboard. For example, Files lets people create a new folder by revealing a context menu in...
- **Prefer a graphical preview that clarifies the target of a context menu’s commands.** `[iOS, iPadOS]`
  For example, when people reveal a context menu on a list item in Notes or Mail, the preview shows a condensed version of the actual content to help people confirm that they’re working with the item they intend.
- **Ensure that your preview looks good as it animates.** `[iOS, iPadOS]`
  As people reveal a context menu on an onscreen object, the system animates the preview image as it emerges from the content, dimming the screen behind the preview and the menu. It’s important to adjust the preview’s clipping path to...
- **Consider using a context menu instead of a panel or inspector window to present frequently used functionality.** `[visionOS]`
  Minimizing the number of separate views or windows your app opens can help people keep their space uncluttered.
- **In general, avoid letting a context menu’s height exceed the height of the window.** `[visionOS]`
  In visionOS, a window includes system-provided components above and below its top and bottom edges, such as window-management controls and the Share menu, so a context menu that’s too tall could obscure them. As you consider the number...

## Controls
<sub>`pages/controls.md`</sub>

- **Offer controls for actions that provide the most benefit without having to launch your app.**
  For example, launching a Live Activity from a control creates an easy and seamless experience that informs someone about progress without having to navigate to your app to stay up to date. For guidance, see [Live...
- **Update controls when someone interacts with them, when an action completes, or remotely with a push notification.**
  Update the contents of a control to accurately reflect the state and show if an action is still in progress.
- **Choose a descriptive symbol that suggests the behavior of the control.**
  Depending on where a person adds a control, it may not display the title and value, so the symbol needs to convey enough information about the control’s action. For control toggles, provide a symbol for both the on and off states. For...
- **Use symbol animations to highlight state changes.**
  For control toggles, animate the transition between both on and off states. For control buttons with actions that have a duration, animate indefinitely while the action performs and stop animating when the action is complete. For...
- **Select a tint color that works with your app’s brand.**
  The system applies this tint color to a control toggle’s symbol in its on state. When a person performs the action of a control from the Action button, the system also uses this tint color to display the value and symbol in the Dynamic...
- **Help people provide additional information the system needs to perform an action.**
  A person may need to configure a control to perform a desired action — for example, select a specific light in a house to turn on and off. If a control requires configuration, prompt people to complete this step when they first add it....
- **Provide hint text for the Action button.**
  When a person presses the Action button, the system displays hint text to help them understand what happens when they press and hold. When someone presses and holds the Action button, the system performs the action configured to it. Use...
- **If your control title or value can vary, include a placeholder.**
  Placeholder information tells people what your control does when the title and value are situational. The system displays this information when someone brings up the controls gallery in Control Center or the Lock Screen and chooses your...
- **Hide sensitive information when the device is locked.**
  When the device is locked, consider having the system redact the title and value to hide personal or security-related information. Specify if the system needs to redact the symbol state as well. If specified, the system redacts the...
- **Require authentication for actions that affect security.**
  For example, require people to unlock their device to access controls to lock or unlock the door to their house or start their car. For developer guidance, see...
- **Use the same camera UI in your app and your camera experience.**
  Sharing UI leverages people’s familiarity with the app. By using the same UI, the transition to the app is seamless when someone captures content and taps a button to perform additional tasks, such as posting to a social network or...
- **Provide instructions for adding the control.**
  Help people understand how to add the control that launches this camera experience.

## Dark Mode
<sub>`pages/dark-mode.md`</sub>

- **Avoid offering an app-specific appearance setting.**
  An app-specific appearance mode option creates more work for people because they have to adjust more than one setting to get the appearance they want. Worse, they may think your app is broken because it doesn’t respond to their...
- **Ensure that your app looks good in both appearance modes.**
  In addition to using one mode or the other, people can choose the Auto appearance setting, which switches between the light and dark appearances as conditions change throughout the day, potentially while your app is running.
- **Test your content to make sure that it remains comfortably legible in both appearance modes.**
  For example, in Dark Mode with Increase Contrast and Reduce Transparency turned on (both separately and together), you may find places where dark text is less legible when it’s on a dark background. You might also find that turning on...
- **In rare cases, consider using only a dark appearance in the interface.**
  For example, it can make sense for an app that supports immersive media viewing to use a permanently dark appearance that lets the UI recede and helps people focus on the media.
- **Embrace colors that adapt to the current appearance.**
  Semantic colors (like [labelColor](https://developer.apple.com/documentation/appkit/nscolor/labelcolor) and [controlColor](https://developer.apple.com/documentation/appkit/nscolor/controlcolor) in macOS or...
- **Aim for sufficient color contrast in all appearances.**
  Using system-defined colors can help you achieve a good contrast ratio between your foreground and background content. At a minimum, make sure the contrast ratio between colors is no lower than 4.5:1. For custom foreground and...
- **Soften the color of white backgrounds.**
  If you display a content image that includes a white background, consider slightly darkening the image to prevent the background from glowing in the surrounding Dark Mode context.
- **Use SF Symbols wherever possible.**
  Symbols work well in both appearance modes when you use dynamic colors to tint them or when you add vibrancy. For guidance, see [Color](https://developer.apple.com/design/human-interface-guidelines/color).
- **Design separate interface icons for the light and dark appearances if necessary.**
  For example, an icon that depicts a full moon might need a subtle dark outline to contrast well with a light background, but need no outline when it displays on a dark background. Similarly, an icon that represents a drop of oil might...
- **Make sure full-color images and icons look good in both appearances.**
  Use the same asset if it looks good in both the light and dark appearances. If an asset looks good in only one mode, modify the asset or create separate light and dark assets. Use asset catalogs to combine your assets into a single...
- **Use the system-provided label colors for labels.**
  The primary, secondary, tertiary, and quaternary label colors adapt automatically to the light and dark appearances.
- **Use system views to draw text fields and text views.**
  System views and controls make your app’s text look good on all backgrounds, adjusting automatically for the presence or absence of vibrancy. When possible, use a system-provided view to display text instead of drawing the text yourself.
- **Prefer the system background colors.** `[iOS, iPadOS]`
  Dark Mode is dynamic, which means that the background color automatically changes from base to elevated when an interface is in the foreground, such as a popover or modal sheet. The system also uses the elevated background color to...
- **Include some transparency in custom component backgrounds when appropriate.** `[macOS]`
  Transparency lets your components pick up color from the window background when desktop tinting is active, creating a visual harmony that can persist even when the desktop picture changes. To help achieve this harmony, add transparency...

## Design principles
<sub>`pages/design-principles.md`</sub>

- **Make something meaningful.**
- **Let people do things their own way.**
- **Act in people’s best interest.**
- **Build on what people know.**
- **Adapt to diverse contexts and needs.**
- **Be clear and direct.**
- **Care about every detail.**
- **Make it human.**
- **Create value.**
  The best designs reflect a constant orientation toward what makes a product genuinely useful. At every stage of development, ask what your product is for and whether the design serves that purpose.
- **Keep focused.**
  Prioritize your app’s most important features by aligning with how people want to use it, and focus on making those features truly great. A product with a clear use is more effective at helping people meet their goals.
- **Find new ways to solve the problem.**
  Investigate existing solutions, and avoid re-creating them. Define what sets your product apart, and ask how your design can reflect that.
- **Stay out of the way.**
  People use your product to get things done. Often the best way to help them do this is to get them directly to the task or content at hand. The best designs are unobtrusive and present when people need them.
- **Give people the freedom to explore.**
  Let them move through your interface and access features without being locked into specific flows or modes. When a guided flow is necessary, make it easy to skip or escape so people can get to the main experience quickly.
- **Help people recover from mistakes.**
  When people know they can reverse an action or return to a previous state, they feel free to explore, and that freedom makes your interface more inviting. Build forgiveness into your design, and make it easy. Recovering from the...
- **Be fully transparent about what your product does and why.**
  You have an opportunity to build a relationship with someone from their very first interaction. Make sure your app’s intentions are clear from the start. Provide a clear rationale when asking for permission, and when gathering data, be...
- **Keep people’s information safe.**
  People trust you to maintain the integrity of their data. Only collect what your product needs to function, and handle it with care. Anticipate ways it could be misused or cause harm, and put protections in place to prevent abuse and...
- **Use concepts that people know.**
  People bring knowledge of the real world and other software to every new experience. Draw on both to make your interface feel familiar and intuitive.
- **Keep visuals and interactions consistent**
  . Once you establish a behavior or appearance for an element, apply it throughout your design. Consistency helps people learn more quickly, and gives them confidence that new interactions will work the way they expect.
- **Provide clear feedback.**
  Give people clear signals about what’s happening as they use your app. Show when controls are available, indicate when content changes, and use system patterns to display alerts and offer choices. Consistent feedback helps keep people...
- **Design for everyone.**
  People are empowered by products designed with them in mind. Think about the diversity of people who may encounter your design, and take the range of their experiences, perspectives, and needs into account. Treat accessibility as a...
- **Preserve a person’s context.**
  Help people feel at home as your design adapts across platforms and configurations. Keep content and controls in consistent, predictable positions, and use natural animations to ease transitions.
- **Consider a variety of input methods.**
  People interact with their devices in different ways. Designing for as many inputs as possible — including voice, touch, keyboard, and more — means more people can use your product the way that works best for them.
- **Approach every platform with intention.**
  Your software should feel polished and at home wherever it runs. Give each platform you support the same level of care.
- **Include just what’s necessary.**
  Simplicity isn’t minimalism. Aim for a focused, useful experience that keeps the important things close by and lets the others fall away.
- **Establish hierarchy.**
  When form and function are readily apparent, people know how to reach a desired outcome. Prioritize recognizable controls and a consistent structure that helps people understand where they are and what comes next.
- **Quality sets the tone.**
  Every element of your design shows people how much you care. Be deliberate with each decision, and strive for stunning visuals, smooth animations, precise wording, and thoughtful audio.
- **Experiment and iterate.**
  Prototype early, try new approaches, and be willing to discard what doesn’t work. Set a high bar for every feature, refine it, and try again. Test your product in real-world settings to make sure it’s durable, reliable, and high-performing.
- **Maintain your craft.**
  Shipping isn’t the finish line. Keep your interface current with the latest platform capabilities and design patterns, and keep the quality bar high. Design is an ongoing commitment.
- **Identify the emotion you want to inspire.**
  Not all software feels the same to use. A fitness app might energize; a meditation app might calm; a game might thrill. Know the feeling you want to evoke, and let it shape your design.
- **Create defining moments.**
  Every interaction is a chance to show what your software stands for. From a simple button press to an error message, consider whether each moment is an opportunity to add a touch of character that reflects the spirit of your design.
- **Don’t mistake delight for decoration.**
  Keep in mind that people are trying to accomplish a task, so don’t let pursuit of delight for its own sake get in the way of your product’s core purpose. Think about your overall aesthetic: Some designs benefit from a carefully...
- **Consider the whole.**
  Delight emerges as the sum of the consideration that you put into your product. It’s the culmination of everything a person experiences as they use it: the freedom to act, the safety to explore, the comfort of familiar metaphors, and...

## Designing for games
<sub>`pages/designing-for-games.md`</sub>

- **Let people play as soon as installation completes.**
  You don’t want a player’s first experience with your game to be waiting for a lengthy download. Include as much playable content as you can in your game’s initial installation while keeping the download time to 30 minutes or less....
- **Provide great default settings.**
  People appreciate being able to start playing without first having to change a lot of settings. Use information about a player’s device to choose the best defaults for your game, such as the device resolution that makes your graphics...
- **Teach through play.**
  Players often learn better when they discover new information and mechanics in the context of your game’s world, so it can work well to integrate configuration and onboarding flows into a playable tutorial that engages people quickly...
- **Defer requests until the right time.**
  You don’t want to bombard people with too many requests before they start playing, but if your game uses certain sensors on an Apple device or personalizes gameplay by accessing data like hand-tracking, you must first get the player’s...
- **Make sure text is always legible.**
  When game text is hard to read, people can struggle to follow the narrative, understand important instructions and information, and stay engaged in the experience. To keep text comfortably legible on each device, ensure that it...
- **Make sure buttons are always easy to use.**
  Buttons that are too small or too close together can frustrate players and make gameplay less fun. Each platform defines a recommended minimum button size based on its default interaction method. For example, buttons in iOS must be at...
- **Prefer resolution-independent textures and graphics.**
  If creating resolution-independent assets isn’t possible, match the resolution of your game to the resolution of the device. In visionOS, prefer vector-based art that can continue to look good when the system dynamically scales it as...
- **Integrate device features into your layout.**
  For example, a device may have rounded corners or a camera housing that can affect parts of your interface. To help your game look at home on each device, accommodate such features during layout, relying on platform-provided safe areas...
- **Make sure in-game menus adapt to different aspect ratios.**
  Games need to look good and behave well at various aspect ratios, such as 16:10, 19.5:9, and 4:3. In particular, in-game menus need to remain legible and easy to use on every device — and, if you support them, in both orientations on...
- **Design for the full-screen experience.**
  People often enjoy playing a game in a distraction-free, full-screen context. In macOS, iOS, and iPadOS, full-screen mode lets people hide other apps and parts of the system UI; in visionOS, a game running in a Full Space can completely...
- **Support each platform’s default interaction method.**
  For example, people generally use touch to play games on iPhone; on a Mac, players tend to expect keyboard and mouse or trackpad support; and in a visionOS game, people expect to use their eyes and hands while making indirect and direct...
- **Support physical game controllers, while also giving people alternatives.**
  Every platform except watchOS supports physical game controllers. Although the presence of a game controller makes it straightforward to port controls from an existing game and handle complex control mappings, recognize that not every...
- **Offer touch-based game controls that embrace the touchscreen experience on iPhone and iPad.**
  In iOS and iPadOS, your game can allow players to interact directly with game elements, and to control the game using virtual controls that appear on top of your game content. For design guidance, see [Touch...
- **Prioritize perceivability.**
  Make sure people can perceive your game’s content whether they use sight, hearing, or touch. For example, avoid relying solely on color to convey an important detail, or providing a cutscene that doesn’t include descriptive subtitles or...
- **Help players personalize their experience.**
  Players have a variety of preferences and abilities that influence their interactions with your game. Because there’s no universal configuration that suits everyone, give players the ability to customize parameters like type size, game...
- **Give players the tools they need to represent themselves.**
  If your game encourages players to create avatars or supply names or descriptions, support the spectrum of self-identity and provide options that represent as many human characteristics as possible.
- **Avoid stereotypes in your stories and characters.**
  Ask yourself whether you’re depicting game characters and scenarios in a way that perpetuates real-life stereotypes. For example, does your game depict enemies as having a certain race, gender, or cultural heritage? Review your game to...
- **Integrate Game Center to help players discover your game across their devices and connect with their friends.**
  [Game Center](https://developer.apple.com/game-center/) is Apple’s social gaming network, available on all platforms. Game Center lets players keep track of their progress and achievements and allows you to set up leaderboards,...
- **Let players pick up their game on any of their devices.**
  People often have a single iCloud account that they use across multiple Apple devices. When you support [GameSave](https://developer.apple.com/documentation/gamesave), you can help people save their game state and start back up exactly...
- **Support haptics to help players feel the action.**
  When you adopt Core Haptics, you can compose and play custom haptic patterns, optionally combined with custom audio content. Core Haptics is available in iOS, iPadOS, tvOS, and visionOS, and supported on many game controllers. For...
- **Use Spatial Audio to immerse players in your game’s soundscape.**
  Providing multichannel audio can help your game’s audio adapt automatically to the current device, enabling an immersive Spatial Audio experience where supported. For guidance, see...
- **Take advantage of Apple technologies to enable unique gameplay mechanics.**
  For example, you can integrate technologies like augmented reality, machine learning, and [HealthKit](https://developer.apple.com/documentation/healthkit), and request access to location data and functionality like camera and...

## Designing for iOS
<sub>`pages/designing-for-ios.md`</sub>

- **App interactions.**
  Sometimes, people spend just a minute or two checking on event or social media updates, tracking data, or sending messages. At other times, people can spend an hour or more browsing the web, playing games, or enjoying media. People...
- **System features.**
  iOS provides several features that help people interact with the system and their apps in familiar, consistent ways.

## Designing for iPadOS
<sub>`pages/designing-for-ipados.md`</sub>

- **App interactions.**
  Sometimes, people perform a few quick actions on their iPad. At other times, they spend hours immersed in games, media, content creation, or productivity tasks. People frequently have multiple apps open at the same time, and they...
- **System features.**
  iPadOS provides several features that help people interact with the system and their apps in familiar, consistent ways.

## Designing for macOS
<sub>`pages/designing-for-macos.md`</sub>

- **App interactions.**
  Interactions can last anywhere from a few minutes of performing some quick tasks to several hours of deep concentration. People frequently have multiple apps open at the same time, and they expect smooth transitions between active and...
- **System features.**
  macOS provides several features that help people interact with the system and their apps in familiar, consistent ways.

## Designing for tvOS
<sub>`pages/designing-for-tvos.md`</sub>

- **App interactions.**
  People can get deeply immersed in a single experience — often lasting hours — but they also appreciate using a picture-in-picture view to simultaneously follow an alternative app or video.
- **System features.**
  Apple TV users expect their apps and games to integrate well with the following system experiences.

## Designing for visionOS
<sub>`pages/designing-for-visionos.md`</sub>

- **Passthrough.**
  [Immersion and passthrough](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences#Immersion-and-passthrough) provides live video from the device’s external cameras, and helps people interact with virtual...
- **Spatial Audio.**
  Apple Vision Pro combines acoustic and visual-sensing technologies to model the sonic characteristics of a person’s surroundings, automatically making audio sound natural in their space. When an app receives a person’s permission to...
- **Eyes and hands.**
  In general, people perform most actions by using their [Eyes](https://developer.apple.com/design/human-interface-guidelines/eyes) to look at a virtual object and making an *indirect*...
- **Accessibility.**
  Apple Vision Pro supports [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) technologies like VoiceOver, Switch Control, Dwell Control, Guided Access, Head Pointer, and many more, so people can...
- **Embrace the unique features of Apple Vision Pro.**
  Take advantage of space, Spatial Audio, and immersion to bring life to your experiences, while integrating passthrough and spatial input from eyes and hands in ways that feel at home on the device.
- **Consider different types of immersion as you design ways to present your app’s most distinctive moments.**
  You can present experiences in a windowed, UI-centric context, a fully immersive context, or something in between. For each key moment in your app, find the minimum level of immersion that suits it best — don’t assume that every moment...
- **Use windows for contained, UI-centric experiences.**
  To help people perform standard tasks, prefer standard [visionOS](https://developer.apple.com/design/human-interface-guidelines/windows#visionOS) that appear as planes in space and contain familiar controls. In visionOS, people can...
- **Prioritize comfort.**
  To help people stay comfortable and physically relaxed as they interact with your app or game, keep the following fundamentals in mind.
- **Help people share activities with others.**
  When you use [visionOS](https://developer.apple.com/design/human-interface-guidelines/shareplay#visionOS) to support shared activities, people can view the *spatial Personas* of other participants, making it feel like everyone is...

## Designing for watchOS
<sub>`pages/designing-for-watchos.md`</sub>

- **App interactions.**
  People glance at the Always On display many times throughout the day, performing concise app interactions that can last for less than a minute each. People frequently use a watchOS app’s related experiences — like complications,...
- **System features.**
  watchOS provides several features that help people interact with the system and their apps in familiar, consistent ways.

## Digit entry views
<sub>`pages/digit-entry-views.md`</sub>

- **Use secure digit fields.**
  Secure digit fields display asterisks instead of the entered digit onscreen. Always use a secure digit field when your app asks for sensitive data.
- **Clearly state the purpose of the digit entry view.**
  Use a title and prompt that explains why someone needs to enter digits.

## Digital Crown
<sub>`pages/digital-crown.md`</sub>

- **Anchor your app’s navigation to the Digital Crown.**
  Starting with watchOS 10, turning the Digital Crown is the main way people navigate within and between apps. List, tab, and scroll views are vertically oriented, allowing people to use the Digital Crown to easily move between the...
- **Consider using the Digital Crown to inspect data in contexts where navigation isn’t necessary.**
  In contexts where the Digital Crown doesn’t need to navigate through lists or between pages, it’s a great tool to inspect data in your app. For example, in World Clock, turning the Digital Crown advances the time of day at a selected...
- **Provide visual feedback in response to Digital Crown interactions.**
  For example, pickers change the currently displayed value as people use the Digital Crown. If you track turns directly, use this data to update your interface programmatically. If you don’t provide visual feedback, people are likely to...
- **Update your interface to match the speed with which people turn the Digital Crown.**
  People expect turning the Digital Crown to give them precise control over an interface, so it works well to use this speed to determine the speed at which you make changes. Avoid updating content at a rate that makes it difficult for...
- **Use the default haptic feedback when it makes sense in your app.**
  If haptic feedback doesn’t feel right in the context of your app — for example, if the default detents don’t match your app’s animation — turn off the detents. You can also adjust the haptic feedback behavior for tables, letting them...

## Disclosure controls
<sub>`pages/disclosure-controls.md`</sub>

- **Use a disclosure control to hide details until they’re relevant.**
  Place controls that people are most likely to use at the top of the disclosure hierarchy so they’re always visible, with more advanced functionality hidden by default. This organization helps people quickly find the most essential...
- **Provide a descriptive label when using a disclosure triangle.**
  Make sure your labels indicate what is disclosed or hidden, like “Advanced Options.”
- **Place a disclosure button near the content that it shows and hides.**
  Establish a clear relationship between the control and the expanded choices that appear when a person clicks or taps a button.
- **Use no more than one disclosure button in a single view.**
  Multiple disclosure buttons add complexity and can be confusing.

## Dock menus
<sub>`pages/dock-menus.md`</sub>

- **Make custom Dock menu items available in other places, too.**
  Not everyone uses a Dock menu, so it’s important to offer the same commands elsewhere, like in your menu bar menus or within your interface.
- **Prefer high-value custom items for your Dock menu.**
  For example, a Dock menu can list all currently or recently open windows, making it a convenient way to jump to the window people want. Also consider listing a few of the actions that are most likely to be useful when your app isn’t...

## Drag and drop
<sub>`pages/drag-and-drop.md`</sub>

- **As much as possible, support drag and drop throughout your app.**
  Most people are familiar with drag and drop and they often try it everywhere. When you use system-provided components — such as text fields and text views — you get built-in support for drag and drop.
- **Offer alternative ways to accomplish drag-and-drop actions.**
  Sometimes, drag-and-drop operations are inconvenient or impossible for people to perform, so it’s important to provide other ways to do the same things. For example, you can include menu commands that people can use to copy an item and...
- **Determine when dragging and dropping content within your app results in a move or a copy.**
  In general, a move makes sense when the source and destination containers are the same — such as dragging text from one location to another within a document — and a copy makes sense when they’re different, like dragging an image from...
- **Support multi-item drag and drop when it makes sense.**
  People appreciate the convenience of dragging a group of items to a destination, instead of dragging each item separately. In iOS, iPadOS, macOS, and visionOS, people can select multiple items and drag them as a group; macOS also lets...
- **Prefer letting people undo a drag-and-drop operation.**
  Sometimes, people inadvertently drop content in the wrong destination, so they appreciate being able to undo the action and return to their previous state. You might also be able to help people avoid mistakes by asking for confirmation...
- **Consider offering multiple versions of dragged content, ordered from highest to lowest fidelity.**
  By providing multiple alternatives, the destination can choose the highest quality version it can accept. For example, if people can drag a line drawing they created in your app, you could offer a PDF vector representation, a lossless...
- **Consider supporting spring loading.**
  Spring loading lets people activate certain controls, like buttons and segmented controls, by dragging selected content over them. For example, Calendar lets people drag a selected event over the day, week, month, or year segments in...
- **Display a drag image as soon as people drag a selection about three points.**
  It works well to create a translucent representation of the content people are dragging. Translucency helps distinguish the representation from the original content and lets people see destinations as they pass over them. Display the...
- **If it adds clarity, modify the drag image to help people predict the result of a drag-and-drop operation.**
  For example, when dragging a photo into a document, the drag image could expand to show the default size of the photo in the document. You can also use drag *flocking* to visually group multiple drag items — letting people confirm that...
- **Show people whether a destination can accept dragged content.**
  For example, you might display an insertion point or highlight a containing view only when the destination can accept a dragged item, and show no visual feedback — or an explicit “not allowed” image, like the `circle.slash` from SF...
- **When people drop an item on an invalid destination, or when dropping fails, provide visual feedback.**
  For example, the item can move back from its current location to its source (if the source is still visible) or it can scale up and fade out to give the impression of the item evaporating instead of landing successfully.
- **Scroll the contents of a destination when necessary.**
  When people drag an item within a scrolling container that has a lot of content, the content can automatically scroll as people move the item over it. This behavior makes it easy for people to find the right place to drop the item, but...
- **When there’s a choice, pick the richest version of dropped content your app can accept.**
  For example, if people drag a chart object from another app, the drag operation might offer both the rich, native chart object and a simple image of it. If your app supports charts, extract and display the native chart object; it it...
- **Extract only the relevant portion of dropped content if necessary.**
  For example, when people drag a contact to a recipient field in an email, Mail displays only the name and email address, not the contact’s address information.
- **When a physical keyboard is attached, check for the Option key at drop time.**
  When people hold the Option key while dragging, they can force a drag-and-drop operation within the same container to behave like a copy. If people stop holding Option before dropping content in the same container, the drag operation...
- **Provide feedback when dropped content needs time to transfer.**
  For example, you might display a progress indicator to help people estimate how long the transfer will take. In collections, lists, and tables, you might also display a placeholder at the drop location so people know where to find the...
- **Provide feedback when dropped content initiates a task or action.**
  If people drop content onto a control that initiates a task — such as printing — show people that the task has begun and keep them informed of its progress.
- **Apply appropriate styling to dropped text.**
  When the source and destination both support the same text styles, make sure dropped text maintains its original font, typeface, size, and other attributes. Otherwise, apply the destination’s style to dropped text.
- **After a drop, maintain the content’s selection state in the destination, updating it in the source as needed.**
  People expect the content they drop to remain selected so they can immediately act on it. When the source and destination are the same container, the content disappears from its original location when the drag operation performs a move....
- **Let people perform multiple simultaneous drag activities.** `[iOS, iPadOS]`
  In iPadOS, people can sequentially add items to an in-progress drag session, gathering as many items as their fingers can handle. For example, people can select an app icon on the Home Screen, start dragging it, and select additional...
- **Consider letting people drag content from your app into the Finder.** `[macOS]`
  When you support this, be sure to present the content in a format your app can open later. For example, Calendar lets people drag an event to the Finder as a `.ics` file. People can share this file with others or drag it back to...
- **Let people drag selected content from an inactive window without first making the window active.** `[macOS]`
  Selected content in an inactive window is known as a *background selection* and has a different appearance from selected content in the active window. In general, people expect to drag a background selection to the active window without...
- **When possible, let people drag individual items from an inactive window without affecting an existing background selection.** `[macOS]`
  For example, people can drag an unselected file from an inactive Finder window without deselecting any of the window’s selected files.
- **Consider displaying a badge during multi-item drag operations.** `[macOS]`
  A badge is a small filled oval containing a number you can use to indicate the number of items people are dragging. If a destination can accept only a subset of dragged items, update the badge to show the new number.
- **Consider changing the pointer appearance to indicate what will happen when people drop content.** `[macOS]`
  In addition to using the *copy* pointer, you might want to use the *drag link*, *disappearing item*, and *operation not allowed* pointers, depending on the situation. For guidance, see...
- **As much as possible, let people select and drag content with a single motion.** `[macOS]`
  Unless people are selecting multiple items, they appreciate it when they don’t have to pause between making a selection and starting the drag operation.
- **When possible, launch your app to handle content that people drop into empty space.** `[visionOS]`
  When you associate a user activity with draggable app content, your app can open a window or scene that handles the content when people drop it. For example, when people drop a URL into empty space, it launches Safari; when people drop...

## Edit menus
<sub>`pages/edit-menus.md`</sub>

- **Prefer the system-provided edit menu.**
  People are familiar with the contents and behavior of the system-provided component, so creating a custom menu that presents the same commands is redundant and likely to be confusing. For a list of standard edit menu commands, see...
- **Let people reveal an edit menu using the system-defined interactions they already know.**
  For example, people expect to touch and hold on a touchscreen, pinch and hold in visionOS, or use a secondary click with an attached trackpad or keyboard. Although the interactions to reveal an edit menu can differ based on platform,...
- **Offer commands that are relevant in the current context, removing or dimming commands that don’t apply.**
  For example, if nothing is selected, avoid showing options that require a selection, such as Copy or Cut. Similarly, avoid showing a Paste option when there’s nothing to paste.
- **List custom commands near relevant system-provided ones.**
  For example, if you offer custom formatting commands, you can help maintain the ordering people expect by listing them after the system-provided commands in the format section. Avoid overwhelming people with too many custom commands.
- **When it makes sense, let people select and copy noneditable text.**
  People appreciate being able to paste static content — such as an image caption or social media status — into a message, note, or web search. In general, let people copy content text, but not control labels.
- **Support undo and redo when possible.**
  Like all menus, an edit menu doesn’t require confirmation before performing its actions, so people can easily use undo and redo to recover a previous state. For guidance, see [Undo and...
- **In general, avoid implementing other controls that perform the same functions as edit menu items.**
  People typically expect to choose familiar edit commands in an edit menu, or use standard keyboard shortcuts. Offering redundant controls can crowd your interface, giving you less space for presenting actions that people might not...
- **Differentiate different types of deletion commands when necessary.**
  For example, a Delete menu item behaves the same as pressing a Delete key, but a Cut menu item copies the selected content to the system pasteboard before deleting it.
- **Create short labels for custom commands.**
  Use verbs or short verb phrases that succinctly describe the action your command performs. For guidance, see [Labels](https://developer.apple.com/design/human-interface-guidelines/labels).
- **Ensure your edit menu works well in both styles.** `[iOS, iPadOS]`
  The system displays the compact, horizontal style when people use Multi-Touch gestures to reveal the edit menu, and the vertical style when people use a keyboard or pointing device to reveal it. For guidance using the vertical menu...
- **Adjust an edit menu’s placement, if necessary.** `[iOS, iPadOS]`
  Depending on available space, the default menu position is above or below the insertion point or selection. The system also displays a visual indicator that points to the targeted content. Although you can’t change the shape of the menu...

## Entering data
<sub>`pages/entering-data.md`</sub>

- **Get information from the system whenever possible.**
  Don’t ask people to enter information that you can gather automatically — such as from settings — or by getting their permission, such as their location or calendar information.
- **Be clear about the data you need.**
  For example, you might display a prompt in a text field — like “username@company.com” — or provide an introductory label that describes the information, like “Email.” You can also prefill fields with reasonable default values, which can...
- **Use a secure text-entry field when appropriate.**
  If your app or game needs sensitive data, use a field that obscures people’s input as they enter it, typically by displaying a small filled circle symbol for each character. For developer guidance, see...
- **Never prepopulate a password field.**
  Always ask people to enter their password or use biometric or keychain authentication. For guidance, see [Managing accounts](https://developer.apple.com/design/human-interface-guidelines/managing-accounts).
- **When possible, offer choices instead of requiring text entry.**
  It’s usually easier and more efficient to choose from lists of options than to type information, even when a keyboard is conveniently available. When it makes sense, consider using a picker, menu, or other selection component to give...
- **As much as possible, let people provide data by dragging and dropping it or by pasting it.**
  Supporting these interactions can ease data entry and make your experience feel more integrated with the rest of the system.
- **Dynamically validate field values.**
  People can get frustrated when they have to go back and correct mistakes after filling out a lengthy form. When you verify values as soon as people enter them — and provide feedback as soon as you detect a problem — you give them the...
- **When data entry is necessary, make sure people understand that they must provide the required data before they can proceed.**
  For example, if you include a Next or Continue button after a set of text fields, make the button available only after people enter the data you require.
- **Consider using an expansion tooltip to show the full version of clipped or truncated text in a field.** `[macOS]`
  An *expansion tooltip* behaves like a regular tooltip, appearing when the pointer rests on top of a field. Apps running in macOS — including iOS and iPadOS apps running on a Mac — can use an expansion tooltip to help people view the...

## Eyes
<sub>`pages/eyes.md`</sub>

- **Always give people multiple ways to interact with your app.**
  Design your app to support the accessibility features people use to personalize the ways they interact with their devices. For guidance, see [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility).
- **Design for visual comfort.**
  Help people accomplish their primary task by making sure that the objects they need to use are within their [Field of view](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Field-of-view). When your app or...
- **Place content at a comfortable viewing distance.**
  For example, to help people remain comfortable while they read or engage with content over time, aim to place it at least one meter away. In general, you don’t want to place content very close to people unless they’ll view or interact...
- **Prefer using standard UI components.**
  System-provided components respond consistently when people look at them. If your custom components use different visual cues to provide visual feedback, it can be difficult for people to learn and remember how these components work.
- **Minimize visual distractions.**
  When there’s a lot of visual noise, it can be difficult for people to find the object they’re looking for. Visual movement can be even more distracting: When people sense movement — especially in their peripheral vision — they tend to...
- **Make it easy for people to look at an item by providing enough space around it.**
  Because eyes naturally tend to make small, quick adjustments in direction even while people are looking at one place, crowding UI objects together can make it difficult for people to look at one of them without jumping to another. You...
- **Avoid using a repeating pattern or texture that fills the field of view.**
  In some cases, people’s eyes can lock onto different elements in a pattern or texture, making the elements appear to have different depths. To avoid this effect, consider using the pattern in a smaller area.
- **Consider using subtle visual cues to encourage people to look at the item they’re most likely to want.**
  For example, it often works well to place the item near the center of the field of view or use techniques like gentle motion, increased contrast, or variations in color or scale to draw people’s attention. In general, prefer cues that...
- **In general, give an interactive item a rounded shape.**
  People’s eyes tend to be drawn toward the corners in a shape, making it difficult to keep looking at the shape’s center. The more rounded an item’s shape, the easier it is for people to use their eyes to target it.
- **If you create an interactive component that consists of more than one element, be sure to provide an overall containing shape that visionOS can highlight.**
  For example, if an image and a label below it combine to act as one interactive component, you need to define a custom region that encompasses both elements, allowing visionOS to highlight the entire region when people look at either...
- **Prefer using a custom hover effect to emphasize or enhance a special moment in your experience.**
  People are accustomed to the standard hover effects that provide visual feedback or, in the case of tab bars or tooltips, additional information, so a custom hover effect can be especially noticeable. Adding too many custom hover...
- **Choose the right delay.**
  An element’s custom hover effect can appear instantly, after a short delay, or after a slightly longer delay, depending on how you expect people to interact with the element.
- **Aim to keep one or more of the element’s primary views unchanged in both states of a custom hover effect.**
  When at least one primary view remains constant during a hover effect’s animation, it provides visual stability that can help people follow the element’s transition. If all of an element’s views move or change during a custom hover...
- **Thoroughly test custom hover effects.**
  Testing is the only way to determine whether a custom hover effect looks good, responds appropriately, and makes your experience feel alive without distracting people. Aim to test your custom hover effects while wearing Apple Vision Pro...

## Feedback
<sub>`pages/feedback.md`</sub>

- **Make sure all feedback is accessible.**
  When you use multiple ways to provide feedback, you reach more people and give them the opportunity to receive the feedback in ways that work for them. For example, when you provide feedback using color, text, sound, and haptics, people...
- **Consider integrating status feedback into your interface.**
  When status feedback is available near the items it describes, people get important information without having to take action or leave their current context. For example, Mail in iOS and iPadOS describes the most recent update and...
- **Use alerts to deliver critical — and ideally actionable — information.**
  By design, alerts disrupt the current context, so you need to match the importance of the information to the level of interruption. Alerts can lose their impact if you use them too often or to deliver unimportant information. For...
- **Warn people when they initiate a task that can cause data loss that’s unexpected and irreversible.**
  In contrast, don’t warn people when data loss is the expected result of their action. For example, the Finder doesn’t warn people every time they throw away a file because deleting the file is the expected result.
- **When it makes sense, confirm that a significant action or task has completed.**
  For example, people appreciate getting feedback that confirms a successful Apple Pay transaction. It’s generally best to reserve this type of confirmation for activities that are sufficiently important — because people typically expect...
- **Show people when a command can’t be carried out and help them understand why.**
  For example, if people request directions without specifying a destination, Maps tells them that it can’t provide directions to and from the same location.
- **Avoid displaying an indeterminate progress indicator — such as a loading indicator — in a watchOS app.** `[watchOS]`
  An animated indicator can make people think they need to continue paying attention to the display, which isn’t a good user experience. To provide a better experience, reassure people that they’ll receive a notification when the process...

## File management
<sub>`pages/file-management.md`</sub>

- **Use app menus and keyboard shortcuts to give people convenient ways to create and open documents.**
  In iPadOS and macOS, people expect to create new documents or open existing ones using familiar menu commands. When you provide commands like New or Open, iPadOS presents them in the shortcuts interface that displays when people hold...
- **If your app requires a custom file browser, support people’s understanding of the platform’s file system.**
  People who are familiar with the Finder and Files apps already understand the basic layout of their device’s file system. Although you might want to show the most relevant part of the file system when your custom file browser opens —...
- **Help people be confident that their work is always preserved unless they cancel or delete it.**
  In general, avoid making people take an explicit action to save their work. Instead, automatically perform periodic saves while they’re editing and when they close a file or switch to another app.
- **Hide file extensions by default, but let people view them if they choose.**
  Be sure to reflect the current choice in all the save or open interfaces you display.
- **Use a Quick Look viewer to let people preview a file even when your app can’t open it.**
  If your app lets people attach or otherwise interact with files that it doesn’t support, implementing a Quick Look viewer lets people preview those files without leaving your app.
- **Consider implementing a Quick Look generator if your app produces custom file types.**
  A Quick Look generator lets other apps — including the Finder, Files, and Spotlight — display previews of your documents, making it easier for people to find them.
- **Assign the title card’s buttons to your app’s most important functions.** `[iOS, iPadOS]`
  The primary button typically creates a new document, and the secondary button can provide additional options. For example, the primary button in Numbers is Start Writing and the secondary button is Choose a Template.
- **Provide a background that’s clearly distinct from the accessories and title card.** `[iOS, iPadOS]`
  You can use a solid color, a gradient, or a pattern. Avoid including complex images or patterns that might distract from foreground elements.
- **Be mindful of accessory placement.** `[iOS, iPadOS]`
  For example, you can place accessories both in front of and behind the title card to create the appearance of depth, but you need to make sure that your app name and both buttons remain clearly visible. Avoid cluttering the title card...
- **Use animation sparingly.** `[iOS, iPadOS]`
  Too much motion on the display can confuse or disorient people. If you want to animate your accessories, consider creating gentle, repeating animations that subtly highlight and enhance your app’s content. For example, you might create...
- **When someone uses your file provider extension to open or import documents, display only documents that are appropriate in the current context.** `[iOS, iPadOS]`
  For example, if a PDF-editing app loads your extension, only list PDF files for opening or import. You might also want to display additional information, such as modification dates, sizes, and whether documents are local or remote.
- **Let people select a destination when exporting and moving documents.** `[iOS, iPadOS]`
  Unless your app stores documents in a single directory, let people navigate to a specific destination in your directory hierarchy. You could also provide a way to add new subdirectories.
- **Avoid including a custom top toolbar.** `[iOS, iPadOS]`
  Your extension loads within a modal view that already includes a toolbar. Providing a second toolbar is confusing and takes space away from your content.
- **Make your custom file-opening interface convenient.** `[macOS]`
  For example, people might appreciate an “open recent” action in addition to the simple “open” action. You might also want to let people choose criteria on which to filter the file-browsing experience, or select multiple documents to...
- **Provide a save interface to let people change a file’s name, format, or location.** `[macOS]`
  By default, a new document’s title is “Untitled” until people choose a custom name. As with a document-opening interface, a save view can also provide a browsing experience that defaults to a logical location to help people place the...
- **Consider extending the functionality of the Save dialog.** `[macOS]`
  If it makes sense in your app, you can add a custom accessory view containing useful settings or options to the Save dialog. For example, the dialog for saving Mail messages as files contains an option to include attachments.
- **Help people avoid losing work if they turn off autosaving.** `[macOS]`
  People can turn off autosaving by selecting the “Ask to keep changes when closing documents” toggle in Desktop & Dock settings. In this scenario, show that a document has unsaved changes and present a save dialog when people choose to...
- **When autosaving is off, make sure people know when a document has unsaved changes.** `[macOS]`
  To show that there are unsaved changes, display a dot on the document window’s close button and next to the document’s name in your app’s Window menu. When autosaving is on, showing a dot in these locations is confusing, because it...

## Focus and selection
<sub>`pages/focus-and-selection.md`</sub>

- **Rely on system-provided focus effects.**
  System-defined focus effects are precisely tuned to complement interactions with Apple devices, providing experiences that feel responsive, fluid, and lifelike. Incorporating system-provided focus behaviors gives your app consistency...
- **Avoid changing focus without people’s interaction.**
  People rely on the focus system to help them know where they are in your app. If you change focus without their interaction, people have to spend time finding the newly focused item, delaying their current task. The exception is when...
- **Be consistent with the platform as you help people bring focus to items in your app.**
  For example, in iPadOS and macOS, a full keyboard access mode helps people use the keyboard to reach every control, so you only need to support focus for content elements like list items, text fields, and search fields, and not for...
- **Indicate focus using visual appearances that are consistent with the platform.**
  For example, consider a window that contains a list of items. In iPadOS and macOS, the system draws focused list items using white text and a background highlight that matches the app’s accent color, drawing unfocused items using the...
- **In general, use a focus ring for a text or search field, but use a highlight in a list or collection.**
  Although you can use a focus ring to draw attention to an item that fills a cell, like a photo, it’s usually easier for people to view lists and collections when an entire row is highlighted.
- **Customize the halo focus effect when necessary.** `[iPadOS]`
  By default, the system uses an item’s shape to infer the shape of its halo. If the system-provided halo doesn’t give you the appearance you want, you can refine it to match contours like rounded corners or shapes defined by Bézier...
- **Ensure that focus moves through your custom views in ways that make sense.** `[iPadOS]`
  As people continue pressing the Tab key, focus moves through focus groups in reading order: leading to trailing, and top to bottom. Although focus moves through system-provided views in ways that people expect, you might need to adjust...
- **Adjust the priority of an item to reflect its importance within a focus group.** `[iPadOS]`
  When a group receives focus, its *primary item* automatically receives focus too, making it easy for people to select the item they’re most likely to want. You can make an item primary by increasing its priority. For developer guidance,...
- **In a full-screen experience, let people use gestures to interact with the content, not to move focus.** `[tvOS]`
  When an item displays in full screen, it doesn’t show focus, so people naturally assume that their gestures will affect the object, and not its focus state.
- **Avoid displaying a pointer.** `[tvOS]`
  People expect to navigate a fixed number of items by changing focus, not by trying to drag a tiny pointer around a huge screen. While free-form movement might make sense during gameplay, such as when looking for a hidden object or...
- **Design your interface to accommodate components in various focus states.** `[tvOS]`
  In tvOS, focusable items can have up to five different states, each of which is visually distinct. Because focusing an item often increases its scale, you need to supply assets for the larger, focused size to ensure they always look...

## Game Center
<sub>`pages/game-center.md`</sub>

- **Display the access point in menu screens.**
  Consider adding the access point to the main menu or the settings area of your game. Avoid displaying the access point during active gameplay or in temporary splash screens, cinematic flows, or tutorials that might precede your game’s...
- **Avoid placing controls near the access point.**
  You can choose to present the access point at any of the four corners of the screen in a fixed position. Remember that the access point has both a collapsed and expanded version, so check whether the access point overlaps any important...
- **Consider pausing your game while the Game Overlay or dashboard is present.**
  Pausing your game can help players view their Game Center information without feeling like the game is continuing without them.
- **Use the artwork Game Center provides in custom links.**
  When referencing Game Center features in custom UI, use the official artwork from [Apple Design Resources](https://developer.apple.com/design/resources/#technologies). Preserve the appearance of this artwork and don’t adjust the...
- **Use the correct terminology in custom links.**
  The following table describes how to use Game Center terminology correctly so that you can avoid confusing players in custom UI.
- **Align with Game Center achievement states.**
  Game Center defines four achievement states: locked, in-progress, hidden, and completed. The system groups achievements by completion status, displaying completed achievements in the Completed group and all other achievements in the...
- **Determine a display order.**
  The order in which you upload achievements is the order in which they appear, so consider the order you want before uploading files. For example, you might want your achievements to appear in an order that corresponds to the most common...
- **Be succinct when describing achievements.**
  The achievement card limits the title and description to two lines each. If your title or description wraps beyond two lines, the card truncates the text. Use title-style capitalization for the achievement title and sentence-style...
- **Give players a sense of progress.**
  When you use progressive achievements, the system displays player progress and provides encouraging messages like “Youʼre more than halfway to completing Great Lakes Freighter in The Coast. Keep going!” to help motivate players to...
- **Design rich, high-quality images that help players feel rewarded.**
  Achievements are a prominent feature in Game Center UI, so it’s essential to design high-quality assets that catch the eye and encourage players to return to your game. Avoid reusing the same asset to represent more than one...
- **Create artwork in the appropriate size and format.**
  The system applies a circular mask to your achievement image, so be sure to keep content centered. Use the following specifications to create images.
- **iOS, iPadOS, macOS, visionOS**
- **Choose a leaderboard type.**
  Game Center supports two types of leaderboards: *classic* and *recurring*.
- **Take advantage of leaderboard sets for multiple leaderboards.**
  Leaderboard sets are an organization system that can make it easier for players to find the board they’re looking for. Consider grouping leaderboard sets by themes or gameplay experiences, such as:
- **Add leaderboard images.**
  Leaderboard artwork gives you another opportunity to reinforce your game’s visual aesthetic. Aim to create a unique image for each leaderboard in your game that reflects and showcases the gameplay involved in leaderboard ranking....
- **iOS, iPadOS, macOS**
- **Create engaging challenges.**
  Challenges are great for short, skill-based gameplay activities that have a clear way of gauging players’ accomplishments. Create challenges that take 1-5 minutes to play, with gameplay that players can complete individually. Examples...
- **Avoid creating challenges that track overall progress or personal best scores.**
  These can give regular players an unfair advantage. Instead, track players’ most recent score after each attempt at your challenge. This helps keep your challenge motivating by placing all players on a level playing field.
- **Make it easy to jump into your challenge.**
  Players can access challenges through invitation links, the Game Overlay, or in the Games app in iOS, iPadOS, and macOS. Always deep-link to the exact mode or level where your challenge begins, and help first-time players complete any...
- **Create high-quality artwork that encourages players to engage with your challenges.**
  The system shows your challenge’s artwork in the Game Overlay, Games app, and in the preview of an invitation link. Avoid placing the primary content of your artwork in an area where the challenge’s title and description might cover it....
- **Use party codes to invite players to multiplayer activities.**
  Game Center party codes are a great way to coordinate real-time multiplayer sessions whether you use Game Center matchmaking and networking facilities or provide your own. Game Center generates alpha-numeric party codes that are...
- **Support multiplayer activities through in-game UI.**
  The Game Overlay and Game Center dashboard help players find other people for a multiplayer match without leaving your game. Game Center’s default multiplayer interface lets a player invite nearby or recent players, Game Center friends,...
- **Provide engaging activity artwork.**
  Players see the preview image for a multiplayer activity throughout the system, such as in a party code, the Games app, or in-game UI. Use the following specifications to create your artwork.
- **Display an optional image at the top of the dashboard.** `[tvOS]`
  In tvOS, you can add an additional piece of artwork to the dashboard to highlight your game’s aesthetic. Use a simple, easily recognizable image that looks great at a distance. Consider using your game’s logo or word mark; however,...
- **Be aware of Game Center support on watchOS.** `[watchOS]`
  While GameKit features and API are available for watchOS games, keep in mind that there’s no system-supported Game Center UI that you can invoke on watchOS. Instead, Game Center content for watchOS games appears on a connected iPhone.

## Game controls
<sub>`pages/game-controls.md`</sub>

- **Determine whether it makes sense to display virtual controls on top of game content.**
  In general, virtual game controls benefit games that offer a large number of actions or require players to control movement. However, sometimes gameplay is more immersive and effective when players can interact directly with in-game...
- **Place virtual buttons where they’re easy to access.**
  Take into account the device’s boundaries and [Guides and safe areas](https://developer.apple.com/design/human-interface-guidelines/layout#Guides-and-safe-areas) as well as comfortable locations for controls. Make sure to position...
- **Make sure controls are large enough.**
  Make sure frequently used controls are a minimum size of 44x44 pt, and less important controls, such as menus, are a minimum size of 28x28 pt to accommodate people’s fingers.
- **Always include visible and tactile press states.**
  A virtual control feels unresponsive without a visual and physical press state. Help players understand when they successfully interact with a button by adding a visual press state effect, such as a glow, that they can see even when...
- **Use symbols that communicate the actions they perform.**
  Choose artwork that visually represents the action each button performs, such as a graphic of a weapon to represent an attack. Avoid using abstract shapes or controller-based naming like A, X, or R1 as artwork, which makes it harder for...
- **Show and hide virtual controls to reflect gameplay.**
  Take advantage of the dynamic nature of touch controls and adapt what controls players see onscreen depending on their context. You can hide controls when an action isn’t available or relevant, letting you reduce clutter and help...
- **Visible control**
- **Hidden control**
- **Combine functionality into a single control.**
  Consider redesigning game mechanics that require players to press multiple buttons at the same time or in a sequence. Leverage gestures such as double tap and touch and hold to provide different variations of the same action, such as...
- **Map movement and camera controls to predictable behavior.**
  Typically, players expect to control movement using the left side of their screen, and control camera direction using the right side of their screen. Maximize the amount of space that players can control both movement and the camera...
- **Support the platform’s default interaction method.**
  A game controller is an optional purchase, but every iPhone and iPad has a touchscreen, every Mac has a keyboard and a trackpad or mouse, every Apple TV has a remote, and every Apple Vision Pro responds to gestures people make with...
- **Tell people about game controller requirements.**
  In tvOS and visionOS, you can require the use of a physical game controller. The App Store displays a “Game Controller Required” badge to help people identify such apps. Remember that people can open your game at any time, even without...
- **Automatically detect whether a controller is paired.**
  Instead of having players manually set up a physical game controller, you can automatically detect whether a controller is paired and get its profile. For developer documentation, see [Game...
- **Customize onscreen content to match the connected game controller.**
  To simplify your game’s code, the Game Controller framework assigns standard names to controller elements based on their placement, but the colors and symbols on an actual game controller may differ. Be sure to use the connected...
- **Map controller buttons to expected UI behavior.**
  Outside of gameplay, players expect to navigate your game’s UI in a way that matches the familiar behavior of the platform they’re playing on. When not controlling gameplay, follow these conventions across all Apple platforms:
- **Support multiple connected controllers.**
  If there are multiple controllers connected, use labels and glyphs that match the one that the player is actively using. If your game supports multiplayer, use the appropriate labels and symbols when referring to a specific player’s...
- **Prefer using symbols, not text, to refer to game controller elements.**
  The Game Controller framework makes [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) available for most elements, including the buttons on various brands of game controllers. Using symbols instead...
- **Prioritize single-key commands.**
  Single-key commands are generally easier and faster for players to perform, especially while they’re simultaneously using a mouse or trackpad. For example, you might use the first letter of a menu item as a shortcut, such as I for...
- **Test key binding comfort game using an Apple keyboard.**
  For example, if a key binding uses the Control key (^) on a non-Apple keyboard, consider remapping it to the Command key (⌘) on an Apple keyboard. On Apple keyboards, the Command key is conveniently located next to the Space bar, making...
- **Take the proximity of keys into account.**
  For example, if players navigate using the W, A, S, and D keys, consider using nearby keys to define other high-value commands. Similarly, if there’s a group of closely related actions, it can work well to map their bindings to keys...
- **Let players customize key bindings.**
  Although players tend to expect a reasonable set of defaults, many people need to customize a game’s key bindings for personal comfort and play style.
- **Match spatial game controller behavior to hand input.** `[visionOS]`
  In addition to supporting a wide array of wireless game controllers, your visionOS game can also support spatial game controllers such as PlayStation VR2 Sense controller. Allow players to interact with your game in a similar manner to...

## Gauges
<sub>`pages/gauges.md`</sub>

- **Write succinct labels that describe the current value and both endpoints of the range.**
  Although not every gauge style displays all labels, VoiceOver reads the visible labels to help people understand the gauge without seeing the screen.
- **Consider filling the path with a gradient to help communicate the purpose of the gauge.**
  For example, a temperature gauge might use colors that range from red to blue to represent temperatures that range from hot to cold.
- **Consider using the continuous style for large ranges.** `[macOS]`
  A large value range can make the segments of a discrete capacity indicator too small to be useful.
- **Consider changing the fill color to inform people about significant parts of the range.** `[macOS]`
  By default, the fill color for both capacity indicator styles is green. If it makes sense in your app, you can change the fill color when the current value reaches certain levels, such as very low, very high, or just past the middle....

## Generative AI
<sub>`pages/generative-ai.md`</sub>

- **Design your experience responsibly.**
  Responsible AI is the intentional design and development of AI features that considers their direct and indirect impacts on people, systems, and society. With generative AI, it’s often easy to quickly prototype an exciting new feature...
- **Keep people in control.**
  While AI can manipulate and create content, respect people’s agency and ensure they remain in charge of decision making and the overall experience. Honor their requests when in scope and the expected output is clear, and handle...
- **Ensure an inclusive experience for all.**
  AI models learn from data and tend to favor the most common information. This may lead to harmful, unintended biases and stereotypes. Take extra care when designing your AI feature to consider how assumptions and personal attributes...
- **Design engaging and useful generative features.**
  Generative AI is a powerful tool, but it’s not the right solution for every situation. Offer generative features when and where they provide clear and specific value, like time savings, improved communication, or enhanced creativity.
- **Ensure a great experience even when generative features aren’t available or people opt not to use them.**
  In some cases, generative AI may be essential to an experience, and there’s no reasonable non-AI substitute. In other cases, AI may play a complementary role that enhances your app’s core functionality, but isn’t critical for people...
- **Communicate where your app uses AI.**
  Letting people know when and where your app uses AI sets expectations and gives people the opportunity to knowingly choose to use an AI-powered feature. Never trick someone into thinking they’re interacting with or viewing content...
- **Set clear expectations about what your AI-powered feature can and can’t do.**
  Clarifying your experience’s capabilities and limitations helps people establish a mental model of your feature. For example, when you introduce a feature, you might offer a brief tutorial. For open-ended features like a search bar or...
- **Choose a model type that fits your feature’s needs and protects people’s privacy.**
  On-device models keep people’s information on their device, respond quickly, and work offline. When a feature needs more processing power or a larger context size, server-based models are worth considering. Always weigh privacy...
- **Ask permission before using personal information and usage data.**
  Some interactions with an AI model may involve sensitive information, like personal details, messages, photos, and feature usage information. After obtaining permission, use the minimum data you need and always offer a clear way to opt...
- **Clearly disclose how your app and its model use and store personal information.**
  People are more likely to be comfortable sharing data when they understand how it’s used. Empower people to make an informed decision about what data they share with your AI model. When asking for permission to use someone’s...
- **Thoughtfully evaluate model capabilities.**
  There are different types of generative models, some of which possess general knowledge, while others are trained for specific tasks. It’s important to understand the capabilities of any model you consider. As early as you can, get a...
- **Be intentional when choosing or creating a dataset.**
  Whether you’re training a model from scratch or customizing an existing model, the data you choose greatly impacts the model’s behavior. When you teach and evaluate your AI model, choose datasets that include a diverse range of subject...
- **Guide people on how to use your generative feature.**
  Consider how to steer and educate people toward producing great results. One technique is to offer diverse, predefined example inputs that hint at what’s possible for a feature.
- **Raise awareness about and minimize the chance of hallucinations.**
  When a generative model is unsure how to respond to a request, it may produce content that seems plausible but is made up. These hallucinations can misinform people because the model may convincingly present the information as factual,...
- **Consider consequences and get permission before performing irreversible or potentially problematic tasks.**
  Before performing a task, consider whether a mistake or the inability to reverse the action might cause more work or stress for people. Avoid automating destructive actions, like deleting photos, and actions that are hard to undo, like...
- **Make it easy for people to refine or revert generated results, and acknowledge when their corrections take effect.**
  For example, surfacing controls like Edit, Undo, Retry, or Adjust near generated content preserves people’s agency while still letting them benefit from automation. When people adjust or personalize output, provide a clear signal that...
- **Help people improve requests when blocked or undesirable results occur.**
  Minimize scoped or blocked output by coaching people how to be more successful next time. For example, if prompted to generate harmful content, Image Playground says that it’s “Unable to use that description.” When possible, consider...
- **Reduce unexpected and harmful outcomes with thoughtful design and thorough testing.**
  People generally use apps with good intentions, but harmful outcomes can still arise from both accidental and purposeful misuse, and when responding to potentially sensitive topics. It may not be possible to mitigate every harmful...
- **Strive to avoid replicating copyrighted content.**
  Large AI models are trained using vast datasets from the internet and other sources. This means most generative models are familiar with and can unintentionally produce content similar to published work, including copyrighted content....
- **Factor processing time into your design.**
  *Latency* is how much time it takes for a model to produce an output. Non-generative models, such as [body position tracking in ARKit](https://developer.apple.com/documentation/arkit/capturing-body-motion-in-3d) and the...
- **Consider giving specific, reassuring feedback during generation.**
  Messages that describe what’s actually happening can be more helpful than a vague status message. For example, instead of “Processing…”, say “Finding substitutions for ingredients” or “Summarizing key themes from your notes.” Specific...
- **Consider offering alternate versions of results.**
  Depending on the design of your feature, it might work best to present a single result or multiple meaningfully different results from which people can choose. Offering people a choice can give them a greater sense of control and help...
- **Consider ways to improve your model over time.**
  You may want to update your model to adapt to people’s behavior, respond to feedback, include new data, and leverage enhanced capabilities. You can make some improvements, such as updating a list of blocked words, frequently and...
- **Let people share feedback on outputs.**
  Feedback can help you identify and respond to unexpected outcomes and new potential issues that arise despite thorough testing. Feedback also gives people a way to celebrate what they like best about your AI experience and report...
- **Design flexible, adaptable features.**
  Generative AI is a rapidly advancing technology, and models and their resource needs are constantly evolving. Consider ways your app or game can adapt as capabilities and models improve. For example, you may want to separate your model...

## Gestures
<sub>`pages/gestures.md`</sub>

- **Give people more than one way to interact with your app.**
  People commonly prefer or need to use other inputs — such as their voice, keyboard, or Switch Control — to interact with their devices. Don’t assume that people can use a specific gesture to perform a given task. For guidance, see...
- **In general, respond to gestures in ways that are consistent with people’s expectations.**
  People expect most gestures to work the same regardless of their current context. For example, people expect tap to activate or select an object. Avoid using a familiar gesture like tap or swipe to perform an action that’s unique to...
- **Handle gestures as responsively as possible.**
  Useful gestures enhance the experience of direct manipulation and provide immediate feedback. As people perform a gesture in your app, provide feedback that helps them predict its results and, if necessary, communicates the extent and...
- **Indicate when a gesture isn’t available.**
  If you don’t clearly communicate why a gesture doesn’t work, people might think your app has frozen or they aren’t performing the gesture correctly, leading to frustration. For example, if someone tries to drag a locked object, the UI...
- **Add custom gestures only when necessary.**
  Custom gestures work best when you design them for specialized tasks that people perform frequently and that aren’t covered by existing gestures, like in a game or drawing app. If you decide to implement a custom gesture, make sure it’s:
- **Make custom gestures easy to learn.**
  Offer moments in your app to help people quickly learn and perform custom gestures, and make sure to test your interactions in real use scenarios. If you’re finding it difficult to use simple language and graphics to describe a gesture,...
- **Use shortcut gestures to supplement standard gestures, not replace them.**
  While you may supply a custom gesture to quickly access parts of your app, people also need simple, familiar ways to navigate and perform actions, even if it means an extra tap or two. For example, in an app that supports navigation...
- **Avoid conflicting with gestures that access system UI.**
  Several platforms offer gestures for accessing system behaviors, like edge swiping in watchOS or rolling your hand over to access system overlays in visionOS. It’s important to avoid defining custom gestures that might conflict with...
- **Consider allowing simultaneous recognition of multiple gestures if it enhances the experience.** `[iOS, iPadOS]`
  Although simultaneous gestures are unlikely to be useful in nongame apps, a game might include multiple onscreen controls — such as a joystick and firing buttons — that people can operate at the same time. For guidance on integrating...
- **Support standard gestures everywhere you can.** `[visionOS]`
  For example, as soon as someone looks at an object in your app or game, tap is the first gesture they’re likely to make when they want to select or activate it. Even if you also support custom gestures, supporting standard gestures such...
- **Offer both indirect and direct interactions when possible.** `[visionOS]`
  Prefer indirect gestures for UI and common components like buttons. Reserve direct gestures and custom gestures for objects that invite close-up interaction or specific motions in a game or interactive experience.
- **Avoid requiring specific body movements or positions for input.** `[visionOS]`
  Not all people can perform specific body movements or position themselves in certain ways at all times, whether due to disability, spatial constraints, or other environmental factors. If your experience requires movement, consider...
- **Prioritize comfort.** `[visionOS]`
  Continually test ergonomics of all interactions that require custom gestures. A custom interaction that requires people to keep their arms raised for even a little while can be physically tiring, and repeating very similar movements...
- **Carefully consider complex custom gestures that involve multiple fingers or both hands.** `[visionOS]`
  People may not always have both hands available when using your app or game. If you require a more complex gesture for your experience, consider also offering an alternative that requires less movement.
- **Avoid custom gestures that require using a specific hand.** `[visionOS]`
  It can increase someone’s cognitive load if they need to remember which hand to use to trigger a custom gesture. It may also make your experience less welcoming to people with strong hand-dominance or limb differences.
- **Reserve the area around a person’s hand for system overlays and their related gestures.** `[visionOS]`
  If possible, don’t anchor content to a person’s hands or wrists. If you’re designing a game that involves hand-anchored content, place it outside of the immediate area of someone’s hand to avoid colliding with the Home indicator.
- **Consider deferring the system overlay behavior when designing an immersive app or game.** `[visionOS]`
  In certain circumstances, you may not want the Home indicator to appear when someone looks at the palm of their hand. For example, a game that uses virtual hands or gloves may want to keep someone within the world of the story, even if...
- **Use caution when designing custom gestures that involve a rolling motion of the hand, wrist, and forearm.** `[visionOS]`
  This specific motion is reserved for revealing system overlays. Since system overlays always display on top of app content and your app isn’t aware of when they’re visible, it’s important to test any custom gestures or content that...
- **Avoid setting a primary action in views with lists, scroll views, or vertical tabs.** `[watchOS]`
  This conflicts with the default navigation behaviors that people expect when they double-tap.
- **Choose the button that people use most commonly as the primary action in a view.** `[watchOS]`
  Double tap is helpful in a nonscrolling view when it performs the action that people use the most. For example, in a media controls view, you could assign the primary action to the play/pause button. For developer guidance, see...

## Going full screen
<sub>`pages/going-full-screen.md`</sub>

- **Support full-screen mode when it makes sense for your experience.**
  People appreciate full-screen mode when they want to concentrate on a task or be immersed in content. Consider offering a full-screen mode if your experience lets people play a game; view media like videos or photo slideshows; or...
- **If necessary, adjust your layout in full-screen mode, but don’t programmatically resize your window.**
  When a window is larger in full-screen mode than in non-full-screen mode, you want to keep essential content prominent while making good use of the extra space. For example, it might make sense to adjust the proportions of your...
- **Continue to provide access to essential features and controls so people can complete their task without exiting full-screen mode.**
  For example, a full-screen media experience needs to make playback controls persistently available or easy to reveal when people need them.
- **Except in games, let people reveal the Dock while your iPadOS or macOS app is in full-screen mode.**
  In iPadOS and macOS, it’s important to preserve access to the Dock so people can quickly open other apps and Dock items. To help prevent people from accidentally revealing the Dock while they’re playing your full-screen game, you can...
- **After people switch away from your full-screen experience, help them resume where they left off when they return.**
  For example, a game or a slideshow needs to pause automatically when people leave the experience so they don’t miss anything.
- **Let people choose when to exit full-screen mode.**
  People generally don’t expect full-screen mode to end automatically when they switch to a different experience or finish an absorbing activity, like playing a game or viewing a movie.
- **Prioritize content by temporarily hiding toolbars and navigation controls.**
  You can offer a distraction-free environment by hiding elements when content is the primary focus, such as when viewing full-screen photos or reading a document. If you implement such behavior, let people restore the hidden elements...
- **Consider deferring system gestures to prevent accidental exits in a full-screen app or game.** `[iOS, iPadOS]`
  By default, the Home Screen indicator automatically hides shortly after someone switches to your app or game. It reappears when someone interacts with the bottom portion of the screen, allowing them to swipe once to exit. Whenever...
- **Use the system-provided full-screen experience.** `[macOS]`
  Using the system’s full-screen support ensures that your full-screen window works well in all contexts. For example, some Mac models include a camera housing that occupies an area at the top-center of the screen. Using the system’s...
- **In a game, don’t change the display mode when players go full screen.** `[macOS]`
  People expect to be in control of their display mode, and changing it automatically doesn’t improve performance.
- **Always let people choose when to enter full-screen mode.** `[macOS]`
  Prefer letting people use your window’s Enter Full Screen button, View menu item, or the Control-Command-F keyboard shortcut. Avoid offering a custom menu of window modes. In a game, you might also provide a custom...

## Gyroscope and accelerometer
<sub>`pages/gyro-and-accelerometer.md`</sub>

- **Use motion data only to offer a tangible benefit to people.**
  For example, a fitness app might use the data to provide feedback about people’s activity and general health, and a game might use the data to enhance gameplay. Avoid gathering data simply to have the data.
- **Outside of active gameplay, avoid using accelerometers or gyroscopes for the direct manipulation of your interface.**
  Some motion-based gestures may be difficult to replicate precisely, may be physically challenging for some people to perform, and may affect battery usage.

## HealthKit
<sub>`pages/healthkit.md`</sub>

- **Provide a coherent privacy policy.**
  During the app submission process, you must provide a URL to a clearly stated privacy policy, so that people can view the policy when they click the link in the App Store page for your app. For developer guidance, see [App Information >...
- **Request access to health data only when you need it.**
  It makes sense to request access to weight information when people log their weight, for example, but not immediately after your app launches. When your request is clearly related to the current context, you help people understand your...
- **Clarify your app’s intent by adding descriptive messages to the standard permission screen.**
  People expect to see the system-provided permission screen when asked to approve access to health data. Write a few succinct sentences that explain why you need the information and how people can benefit from sharing it with your app....
- **Manage health data sharing solely through the system’s privacy settings.**
  People expect to globally manage access to their health information in Settings > Privacy. Don’t confuse people by building additional screens in your app that affect the flow of health data.
- **Use Activity rings for Move, Exercise, and Stand information only.**
  Activity rings consistently represent progress in these specific areas. Don’t attempt to replicate or modify Activity rings for other purposes or to display other types of data. Never show Move, Exercise, and Stand progress in another...
- **Use Activity rings to show progress for a single person.**
  Never use Activity rings to represent data for more than one person, and make sure it’s obvious whose progress is shown, such as by using a label, a photo, or an avatar.
- **Don’t use Activity rings for ornamentation.**
  Activity rings provide information to people; they don’t merely embellish your app’s design. Never display Activity rings in labels or background graphics.
- **Don’t use Activity rings for branding.**
  Use Activity rings strictly to display Activity progress in your app. Never use Activity rings in your app’s icon or marketing materials.
- **Maintain Activity ring and background colors.**
  For a consistent user experience, the visual appearance of Activity rings must always be the same, regardless of the context in which they appear. Never change the look of the rings or background by using filters, changing colors, or...
- **Maintain Activity ring margins.**
  An Activity ring element must include a minimum outer margin of no less than the distance between rings. Never allow other elements to crop, obstruct, or encroach upon this margin or the rings themselves. To display an Activity ring...
- **Differentiate other ring-like elements from Activity rings.**
  Mixing different ring styles can lead to a visually confusing interface. If you must include other rings, use padding, lines, or labels to separate them from Activity rings. Color and scale can also help provide visual separation.
- **Provide app-specific information only in Activity notifications.**
  The system already delivers Move, Exercise, and Stand progress updates. Don’t repeat this same information, and never show an Activity ring element in your app’s notifications. It’s fine to reference Activity progress in a notification,...
- **Use only the Apple-provided icon.**
  Don’t create your own Apple Health icon design or attempt to mimic any Apple-provided designs. Download the Apple Health app icon from [Apple Design Resources](https://developer.apple.com/design/resources/#technologies).
- **Display the name *Apple Health* close to the Apple Health icon.**
  Displaying both elements near each other reminds people that the icon represents the Health app.
- **Display the Apple Health icon consistently with other health-related app icons.**
  In a view that contains other app icons, make the Apple Health icon no smaller than other icons.
- **Don’t use the Apple Health icon as a button.**
  Use the icon only to indicate compatibility with the Health app.
- **Don’t alter the appearance of the Apple Health icon.**
  Don’t mask the icon to change its corner radius or present it in a circular shape. Don’t add embellishments like borders, color overlays, gradients, shadows, or other visual effects.
- **Maintain a minimum clear space around the Apple Health icon of 1/10 of its height.**
  Don’t composite the icon onto another graphic element.
- **Don’t use the Apple Health icon within text or as a replacement for the terms *Health*, *Apple Health*, or *HealthKit*.**
  See [Editorial guidelines](https://developer.apple.com/design/human-interface-guidelines/healthkit#Editorial-guidelines) to learn how to properly reference the Health app and HealthKit in text.
- **Don’t display Health app images or screenshots.**
  Like all Apple images, these designs are copyrighted and can’t appear in your app or marketing materials. You can include an Activity ring element in your app to display Move, Exercise, and Stand progress; for guidance, see [Activity...
- **Refer to the Health app as *Apple Health* or *the Apple Health app*.**
  In your app and marketing text, using *Apple Health* adds clarity.
- **Don’t use the term *HealthKit*.**
  *HealthKit* is a developer-facing term that names the framework your app uses to access health data. If you need to explain to people how your app works with their data, use the term *the Apple Health app*. For example, you might say...
- **Use correct capitalization when using the term *Apple Health*.**
  *Apple Health* is two words, with an uppercase A and uppercase H, followed by lowercase letters. You can display *Apple Health* entirely in uppercase only when you need to conform to an established typographic interface style, such as...
- **Use the system-provided translation of *Health* to avoid confusing people.**
  It’s best to refer to the Apple Health app using the translation that people view on their device.

## Home Screen quick actions
<sub>`pages/home-screen-quick-actions.md`</sub>

- **Create quick actions for compelling, high-value tasks.**
  For example, Maps lets people search near their current location or get directions home without first opening the Maps app. People tend to expect every app to provide at least one useful quick action; you can provide a total of four.
- **Avoid making unpredictable changes to quick actions.**
  Dynamic quick actions are a great way to keep actions relevant. For example, it may make sense to update quick actions based on the current location or recent activities in your app, time of day, or changes in settings. Make sure that...
- **For each quick action, provide a succinct title that instantly communicates the results of the action.**
  For example, titles like “Directions Home,” “Create New Contact,” and “New Message” can help people understand what happens when they choose the action. If you need to give more context, provide a subtitle too. Mail uses subtitles to...
- **Provide a familiar interface icon for each quick action.**
  Prefer using [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) to represent actions. For a list of icons that represent common actions, see [Standard...
- **Don’t use an emoji in place of a symbol or interface icon.**
  Emojis are full color, whereas quick action symbols are monochromatic and change appearance in Dark Mode to maintain contrast.

## HomeKit
<sub>`pages/homekit.md`</sub>

- **Acknowledge the hierarchical model that HomeKit uses.**
  Even if your app doesn’t organize accessories by rooms and zones in its UI, it’s useful to reference the HomeKit model when helping people set up or control their accessories. People need to know where accessories are located so they...
- **Make it easy for people to find an accessory’s related HomeKit details.**
  If your app’s organization is based on accessories, don’t hide other HomeKit information, such as an accessory’s zone or room, in a hard-to-discover settings screen. Instead, consider making the related HomeKit information easily...
- **Recognize that people can have more than one home.**
  Even if your app doesn’t support the concept of multiple homes per user, consider providing the relevant home information in an accessory detail view.
- **Don’t present duplicate home settings.**
  If your app has a different perspective on the organization of a home, don’t confuse people by asking them to set up all or parts of their homes again or by showing a duplicate settings view. Always defer to the settings people made in...
- **Use the system-provided setup flow to give people a familiar experience.**
  The HomeKit setup flow works more quickly than traditional setup flows because it lets people name accessories, join networks, pair with HomeKit, assign room and service categories, and designate favorites in just a few steps. Using the...
- **Provide context to explain why you need access to people’s Home data.**
  Create a purpose string with a phrase that describes why you’re asking for permission to access data, such as “Lets you control this accessory with the Apple Home app and Siri across your Apple devices.”
- **Don’t require people to create an account or supply personal information.**
  Instead, defer to HomeKit for any information you might need. If your app provides additional services that require an account, such as cloud services, make account setup optional and wait until after initial HomeKit setup to offer it.
- **Honor people’s setup choices.**
  When people choose to use HomeKit to set up your accessory, don’t force them to set up other platforms during the HomeKit setup flow. A cross-platform setup experience prevents people from using the accessory right away and can cause...
- **Carefully consider how and when to provide a custom accessory setup experience.**
  Always begin by presenting the system-provided setup flow. Then, after the accessory’s basic functionality is available, offer a custom post-setup experience that highlights the unique features of your accessory and helps people get the...
- **Suggest service names that suit your accessory.**
  If your app detects when someone creates a suboptimal name for Siri voice controls, recommend alternatives that you know will work well for most people. Never suggest company names or model numbers for use as service names.
- **Check that the names people provide follow HomeKit naming rules.**
  If your app lets people rename services, make sure that the new names follow the rules. (The system-provided setup flow automatically checks the original names.) If people enter a name that breaks one or more rules, briefly explain the...
- **Help people avoid creating names that include location information.**
  Although it’s natural for someone to use “kitchen light” to name a light in the kitchen, including the room name in the service name can lead to unpredictable results when controlling the accessory by voice. Your app can detect service...
- **Present example voice commands to demonstrate using Siri to control accessories during setup.**
  As soon as people complete the setup of a new accessory, consider using the service name they chose in a few example Siri phrases and encourage people to try them out.
- **After setup, consider teaching people about more complex Siri commands.**
  People might not be aware of the broad range of natural language phrases they can use with Siri and HomePod to control their accessories. After setup is complete, find useful places throughout your app to help people learn about these...
- **Recommend that people create zones and service groups, if they make sense for your accessory.**
  If people might benefit from using context-specific voice commands to control your accessory, suggest these types of interactions and help people set them up. For example, if you provide an accessory such as a light, switch, or...
- **Offer shortcuts only for accessory-specific functionality that HomeKit doesn’t support.**
  HomeKit lets people use ordinary (or natural) language to control accessories without requiring any additional configuration, so you avoid confusing people by offering shortcuts that duplicate HomeKit functionality. Instead, consider...
- **If your app supports both HomeKit and shortcuts, help people understand the difference between these types of voice control.**
  People can get confused if they’re presented with multiple methods of voice control. Be sure you clearly indicate what’s possible with shortcuts, and never encourage people to create a shortcut for a scene or action that HomeKit already...
- **Be clear about what people can do in your app and when they might want to use the Home app.**
  For example, if your app supports only lights, consider encouraging people to create a “Movie Time” scene that not only dims the lights, but also closes the shades, and turns on the TV to a specific input. To do this, first guide people...
- **Defer to HomeKit if your database differs from the HomeKit database.**
  Give people a seamless experience by automatically reflecting changes made in the Home app or in other third-party HomeKit apps. If you must ask people to manage conflicts in your app, present the conflict visually so that they have a...
- **Ask permission to update the HomeKit database when people make changes in your app.**
  You don’t want to surprise people by changing something in the Home app, so it’s essential to get permission or an indication of intent before you write to the database. In particular, never overwrite HomeKit database settings without a...
- **Don’t block camera images.**
  It’s fine to supplement the camera’s content with useful features, such as an alert calling attention to potentially interesting activity. However, avoid covering portions of the camera’s images with other content.
- **Show a microphone button only if the camera supports bidirectional audio.**
  A nonfunctioning microphone button takes up valuable display space in your app and risks confusing people.
- **Use only Apple-provided icons.**
  Don’t create your own HomeKit or Home app icon design or attempt to mimic the Apple-provided designs. Download HomeKit icons in [Resources](https://developer.apple.com/design/resources/).
- **Position the HomeKit icon consistently with other technology icons.**
  When other technology icons are contained within shapes, treat the HomeKit icon in the same manner.
- **Use the HomeKit icon noninteractively.**
  Don’t use the icon and the name *HomeKit* in custom interactive elements or buttons. You can use the Apple Home app icon to open the app’s product page in the App Store.
- **Don’t use the HomeKit icon within text or as a replacement for the word HomeKit.**
  See [Referring to HomeKit](https://developer.apple.com/design/human-interface-guidelines/homekit#Referring-to-HomeKit) to learn how to properly reference HomeKit in text.
- **Pair the icon with the name *HomeKit* correctly.**
  You can show the name below or beside the icon if other technologies are referenced in this way. Use the same font that’s used on the rest of your layout. For related guidance, see [Referring to...
- **Emphasize your app over HomeKit.**
  Make references to HomeKit or Apple Home less prominent than your app name or main identity.
- **Adhere to Apple’s trademark guidelines.**
  Apple trademarks can’t appear in your app name or images. In text, use Apple product names exactly as shown on the [Apple Trademark List](https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html).
- **Use correct capitalization when using the term *HomeKit*.**
  *HomeKit* is one word, with an uppercase *H* and uppercase *K*, followed by lowercase letters. *Apple Home* is two words, with an uppercase *A* and uppercase *H*, followed by lowercase letters. If your layout displays only all-uppercase...
- **Don’t use the name *HomeKit* as a descriptor.**
  Instead use terms like *works with*, *use*, *supports*, or *compatible*.
- **Don’t suggest that HomeKit is performing an action or function.**
- **Use the name *Apple* with the name *HomeKit*, if desired.**
- **Use the name *HomeKit* for setup, configuration, and instructions, if desired.**
- **Use the app name *Apple Home* whenever referring specifically to the app.**
  On the first mention of the app in body copy, use the complete name *Apple Home*. Subsequent mentions can refer to the Home app.

## ID Verifier
<sub>`pages/id-verifier.md`</sub>

- **Ask only for the data you need.**
  People may lose trust in the experience if you ask for more data than you need to complete the current verification. For example, if you need to ensure that a customer is at least a minimum age, use a request that specifies an age...
- **If your app qualifies for Apple Business Register, register for ID Verifier to ensure that people can view essential information about your organization when you make a request.**
  Registering for ID Verifier with Apple Business Register lets you provide your official organization name and logo for the system to display on customers’ devices as part of the ID verification UI. To learn if your app qualifies and how...
- **Provide a button that initiates the verification process.**
  Use a label like Verify Age in a button that performs a simple age check or Verify Identity for a more detailed identity data request. Avoid including a symbol that specifies a particular type of communication, like NFC or QR codes....
- **In a Display Only request, help the person using your app provide feedback on the visual confirmation they perform.**
  For example, when the reader displays the customer’s portrait, you might provide buttons labeled Matches Person and Doesn’t Match Person so your app can receive an approved or rejected value as part of the response.

## Icons
<sub>`pages/icons.md`</sub>

- **Create a recognizable, highly simplified design.**
  Too many details can make an interface icon confusing or unreadable. Strive for a simple, universal design that most people will recognize quickly. In general, icons work best when they use familiar visual metaphors that are directly...
- **Maintain visual consistency across all interface icons in your app.**
  Whether you use only custom icons or mix custom and system-provided ones, all interface icons in your app need to use a consistent size, level of detail, stroke thickness (or weight), and perspective. Depending on the visual weight of...
- **In general, match the weights of interface icons and adjacent text.**
  Unless you want to emphasize either the icons or the text, using the same weight for both gives your content a consistent appearance and level of emphasis.
- **If necessary, add padding to a custom interface icon to achieve optical alignment.**
  Some icons — especially asymmetric ones — can look unbalanced when you center them geometrically instead of optically. For example, the download icon shown below has more visual weight on the bottom than on the top, which can make it...
- **Provide a selected-state version of an interface icon only if necessary.**
  You don’t need to provide selected and unselected appearances for an icon that’s used in standard system components such as toolbars, tab bars, and buttons. The system updates the visual appearance of the selected state automatically.
- **Use inclusive images.**
  Consider how your icons can be understandable and welcoming to everyone. Prefer depicting gender-neutral human figures and avoid images that might be hard to recognize across different cultures or languages. For guidance, see...
- **Include text in your design only when it’s essential for conveying meaning.**
  For example, using a character in an interface icon that represents text formatting can be the most direct way to communicate the concept. If you need to display individual characters in your icon, be sure to localize them. If you need...
- **If you create a custom interface icon, use a vector format like PDF or SVG.**
  The system automatically scales a vector-based interface icon for high-resolution displays, so you don’t need to provide high-resolution versions of it. In contrast, PNG — used for app icons and other images that include effects like...
- **Provide alternative text labels for custom interface icons.**
  Alternative text labels — or accessibility descriptions — aren’t visible, but they let VoiceOver audibly describe what’s onscreen, simplifying navigation for people with visual disabilities. For guidance, see...
- **Avoid using replicas of Apple hardware products.**
  Hardware designs tend to change frequently and can make your interface icons and other content appear dated. If you must display Apple hardware, use only the images available in [Apple Design...
- **Design simple images that clearly communicate the document type.** `[macOS]`
  Whether you use a background fill, a center image, or both, prefer uncomplicated shapes and a reduced palette of distinct colors. Your document icon can display as small as 16x16 px, so you want to create designs that remain...
- **Designing a single, expressive image for the background fill can be a great way to help people understand and recognize a document type.** `[macOS]`
  For example, Xcode and TextEdit both use rich background images that don’t include a center image.
- **Consider reducing complexity in the small versions of your document icon.** `[macOS]`
  Icon details that are clear in large versions can look blurry and be hard to recognize in small versions. For example, to ensure that the grid lines in the custom heart document icon remain clear in intermediate sizes, you might use...
- **Avoid placing important content in the top-right corner of your background fill.** `[macOS]`
  The system automatically masks your image to fit the document icon shape and draws the white folded corner on top of the fill. Create a set of background images in the sizes listed below.
- **If a familiar object can convey a document’s type or its connection with your app, consider creating a center image that depicts it.** `[macOS]`
  Design a simple, unambiguous image that’s clear and recognizable at every size. The center image measures half the size of the overall document icon canvas. For example, to create a center image for a 32x32 px document icon, use an...
- **Define a margin that measures about 10% of the image canvas and keep most of the image within it.** `[macOS]`
  Although parts of the image can extend into this margin for optical alignment, it’s best when the image occupies about 80% of the image canvas. For example, most of the center image in a 256x256 px canvas would fit in an area that...
- **Specify a succinct term if it helps people understand your document type.** `[macOS]`
  By default, the system displays a document’s extension at the bottom edge of the document icon, but if the extension is unfamiliar you can supply a more descriptive term. For example, the document icon for a SceneKit scene file uses the...

## Image views
<sub>`pages/image-views.md`</sub>

- **Use an image view when the primary purpose of the view is simply to display an image.**
  In rare cases where you might want an image to be interactive, configure a system-provided [button](https://developer.apple.com/design/human-interface-guidelines/buttons) to display the image instead of adding button behaviors to an...
- **If you want to display an icon in your interface, consider using a symbol or interface icon instead of an image view.**
  [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) provides a large library of streamlined, vector-based images that you can render with various colors and opacities. An...
- **Take care when overlaying text on images.**
  Compositing text on top of images can decrease both the clarity of the image and the legibility of the text. To help improve the results, ensure the text contrasts well with the image, and consider ways to make the text object stand...
- **Aim to use a consistent size for all images in an animated sequence.**
  When you prescale images to fit the view, the system doesn’t have to perform any scaling. In cases where the system must do the scaling, performance is generally better when all images are the same size and shape.
- **If your app needs an editable image view, use an image well.** `[macOS]`
  An [image well](https://developer.apple.com/design/human-interface-guidelines/image-wells) is an image view that supports copying, pasting, dragging, and using the Delete key to clear its content.
- **Use an image button instead of an image view to make a clickable image.** `[macOS]`
  An [image button](https://developer.apple.com/design/human-interface-guidelines/buttons#Image-buttons) contains an image or icon, appears in a view, and initiates an instantaneous app-specific action.
- **Use SwiftUI to create animations when possible.** `[watchOS]`
  Alternatively, you can use WatchKit to animate a sequence of images within an image element if necessary. For developer guidance, see [WKImageAnimatable](https://developer.apple.com/documentation/watchkit/wkimageanimatable).

## Image wells
<sub>`pages/image-wells.md`</sub>

- **Revert to a default image when necessary.**
  If your image well requires an image, display the default image again if people clear the content of the image well.
- **If your image well supports copy and paste, make sure the standard copy and paste menu items are available.**
  People generally expect to choose these menu items — or use the standard keyboard shortcuts — to interact with an image well. For guidance, see [Edit...

## Images
<sub>`pages/images.md`</sub>

- **Provide high-resolution assets for all bitmap images in your app, for every device you support.**
  As you add each image to your project’s asset catalog, identify its scale factor by appending “@1x,” “@2x,” or “@3x” to its filename. Use the following values for guidance; for additional scale factors, see...
- **In general, design images at the lowest resolution and scale them up to create high-resolution assets.**
  When you use resizable vectorized shapes, you might want to position control points at whole values so that they’re cleanly aligned at 1x. This positioning allows the points to remain cleanly aligned to the raster grid at higher...
- **Include a color profile with each image.**
  Color profiles help ensure that your app’s colors appear as intended on different displays. For guidance, see [Color management](https://developer.apple.com/design/human-interface-guidelines/color#Color-management).
- **Always test images on a range of actual devices.**
  An image that looks great at design time may appear pixelated, stretched, or compressed when viewed on various devices.
- **Use standard interface elements to display layered images.** `[tvOS]`
  If you use standard views and system-provided focus APIs — such as [FocusState](https://developer.apple.com/documentation/swiftui/focusstate) — layered images automatically get the parallax treatment when people bring them into focus.
- **Identify logical foreground, middle, and background elements.** `[tvOS]`
  In foreground layers, display prominent elements like a character in a game, or text on an album cover or movie poster. Middle layers are perfect for secondary content and effects like shadows. Background layers are opaque backdrops...
- **Generally, keep text in the foreground.** `[tvOS]`
  Unless you want to obscure text, bring it to the foreground layer for clarity.
- **Keep the background layer opaque.** `[tvOS]`
  Using varying levels of opacity to let content shine through higher layers is fine, but your background layer must be opaque — you’ll get an error if it’s not. An opaque background layer ensures your artwork looks great with parallax,...
- **Keep layering simple and subtle.** `[tvOS]`
  Parallax is designed to be almost unnoticeable. Excessive 3D effects can appear unrealistic and jarring. Keep depth simple to bring your content to life and add delight.
- **Leave a safe zone around the foreground layers of your image.** `[tvOS]`
  When focused, content on some layers may be cropped as the layered image scales and moves. To ensure that essential content is always visible, keep it within a safe zone. For guidance, see [App...
- **Always preview layered images.** `[tvOS]`
  To ensure your layered images look great on Apple TV, preview them throughout your design process using Xcode, the Parallax Previewer app for macOS, or the Parallax Exporter plug-in for Adobe Photoshop. Pay special attention as scaling...
- **Create a layered app icon.** `[visionOS]`
  App icons in visionOS are composed of two to three layers that provide the appearance of depth by moving at subtly different rates when the icon is in focus. For guidance, see [Layer...
- **Prefer vector-based art for 2D images.** `[visionOS]`
  Avoid bitmap content because it might not look good when the system scales it up. If you use Core Animation layers, see [Drawing sharp layer-based content in...
- **If you need to use rasterized images, balance quality with performance as you choose a resolution.** `[visionOS]`
  Although a @2x image looks fine at common viewing distances, its fixed resolution means that the system doesn’t dynamically scale it and it might not look sharp from close up. To help a rasterized image look sharp when people view it...
- **Make sure spatial photos render correctly in your app.** `[visionOS]`
  Use the stereo High-Efficiency Image Codec (HEIC) format to display a spatial photo in your app. When you add spatial metadata to a stereo HEIC, visionOS recognizes the photo as spatial and includes visual treatments that help minimize...
- **Prefer the feathered glass background effect to display text over spatial photos.** `[visionOS]`
  If you need to place text over a spatial photo in your app or game, use the feathered glass background effect. The effect adds contrast to make the text readable, and it blurs out detail to help reduce visual discomfort when people view...
- **Take visual comfort into consideration when you make spatial photos from existing 2D content.** `[visionOS]`
  When adjusting the spatial metadata of a photo for your app or game, consider how you want people to view your content. Metadata like disparity adjustment can alter how people perceive the 3D scene, and can cause visual discomfort from...
- **Display spatial photos and spatial scenes in standalone views.** `[visionOS]`
  Avoid displaying spatial photos inline with other content, as this can cause visual discomfort. Instead, showcase spatial photos or spatial scenes in a separate view, like a sheet or window. If you must display stereoscopic images...
- **Use spatial scenes in your app for specific moments.** `[visionOS]`
  Each spatial scene can take up to several seconds to generate from an existing image. Design experiences with this limitation in mind. For instance, the Photos app offers an explicit action to create a spatial scene while immersed in a...
- **When displaying immersively, prefer minimal UI.** `[visionOS]`
  For example, the Spatial Gallery app displays a single piece of content with a small caption and a single Back button, relying on swipe gestures to navigate between items.
- **Prefer displaying larger spatial scenes that you center in someone’s field of view.** `[visionOS]`
  When people view a spatial scene, they may move their head laterally to view the parallax effect. Smaller spatial scenes provide less of a parallax effect and may not be as impactful to viewers.
- **In general, avoid transparency to keep image files small.** `[watchOS]`
  If you always composite an image on the same solid background color, it’s more efficient to include the background in the image. However, transparency is necessary in complication images, menu icons, and other interface icons that serve...
- **Use autoscaling PDFs to let you provide a single asset for all screen sizes.** `[watchOS]`
  Design your image for the 40mm and 42mm screens at 2x. When you load the PDF, WatchKit automatically scales the image based on the device’s screen size, using the values shown below:

## Immersive experiences
<sub>`pages/immersive-experiences.md`</sub>

- **Without dimmed passthrough**
- **With dimmed passthrough**
- **Full Space (Mixed)**
- **Full Space (Progressive)**
- **Full Space (Immersive)**
- **Offer multiple ways to use your app or game.**
  In addition to giving people the freedom to choose their experiences, it’s essential to design your software to support the accessibility features people use to personalize the ways they interact with their devices. For guidance, see...
- **Prefer launching your app or game in the Shared Space or using the `mixed` immersion style.**
  Launching in the Shared Space lets people reference your app or game while using other running software, and enables seamless switching between them. If your app or game provides a fully immersive or `progressive` style experience,...
- **Reserve immersion for meaningful moments and content.**
  Not every task benefits from immersion, and not every immersive task needs to be fully immersive. Although people sometimes want to enter a different world, they often want to stay grounded in their surroundings while they’re using your...
- **Help people engage with key moments in your app or game, regardless of the level of immersion.**
  Cues like dimming, tinting, [Motion](https://developer.apple.com/design/human-interface-guidelines/motion), [Scale](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Scale), and...
- **Prefer subtle tint colors for passthrough.**
  In visionOS 2 and later, you can tint passthrough to help a person’s surroundings visually coordinate with your content, while also making their hands look like they belong in your experience. Avoid bright or dramatic tints that can...
- **Be mindful of people’s visual comfort.**
  For example, although you can place 3D content anywhere while your app or game is running in a Full Space, prefer placing it within people’s [Field of...
- **Choose a style of immersion that supports the movements people might make while they’re in your app or game.**
  It’s essential to choose the right style for your immersive experience because it allows the system to respond appropriately when people move. Although people can make minor physical movements while in an immersive experience — such as...
- **Avoid encouraging people to move while they’re in a progressive or fully immersive experience.**
  Some people may not want to move, or are unable to move because of a disability or their physical surroundings. Design ways for people to interact with content without moving. For example, let people bring a virtual object closer to...
- **If you use the `mixed` immersion style, avoid obscuring passthrough too much.**
  People use passthrough to help them understand and navigate their physical surroundings, so it’s important to avoid displaying virtual objects that block too much of their view. If your app or game displays virtual objects that could...
- **Adopt ARKit if you want to blend custom content with someone’s surroundings.**
  For example, you might want to integrate virtual content into someone’s surroundings or use the wearer’s hand positions to inform your experience. If you need access to these types of sensitive data, you must request people’s...
- **Design smooth, predictable transitions when changing immersion.**
  Help people prepare for different experiences by providing gentle transitions that let people visually track changes. Avoid sudden, jarring transitions that might be disorienting or uncomfortable. For developer guidance, see...
- **Let people choose when to enter or exit a more immersive experience.**
  It can be disorienting for someone to suddenly enter a more immersive experience when they’re not expecting it. Instead, provide a clear action to enter or exit immersion so people can decide when to be more immersed in your content,...
- **Indicate the purpose of an exit control.**
  Make sure your button clarifies whether it returns people to a previous, less immersive context or quits an experience altogether. If exiting your immersive experience also quits your app or game, consider providing controls that let...
- **Prefer virtual hands that match familiar characteristics.**
  For example, match the positions and gestures of the viewer’s hands so they can continue to interact with your app or game in ways that feel natural. Hands that work in familiar ways help people stay immersed in the experience when in...
- **Use caution if you create virtual hands that are larger than the viewer’s hands.**
  Virtual hands that are significantly bigger than human hands can prevent people from seeing the content they’re interested in and can make interactions feel clumsy. Also, large virtual hands can seem out of proportion with the space,...
- **If there’s an interruption in hand-tracking data, fade out virtual hands and reveal the viewer’s own hands.**
  Don’t let the virtual hands become unresponsive and appear frozen. When hand-tracking data returns, fade the virtual hands back in.
- **Minimize distracting content.**
  To help immerse people in a primary task like watching a video, avoid displaying a lot of movement or high-contrast details in your environment. Alternatively, when you want to draw people’s attention to certain areas of your...
- **Help people distinguish interactive objects in your environment.**
  People often use an object’s proximity to help them decide if they can interact with it. For example, when you place a 3D object far away from people, they often don’t try to touch or move toward it, but when you place a 3D object close...
- **Keep animation subtle.**
  Small, gentle movements, like clouds drifting or transforming, can enrich your custom environment without distracting people or making them uncomfortable. Always avoid displaying too much movement near the edges of a person’s field of...
- **Create an expansive environment, regardless of the place it depicts.**
  A small, restrictive environment can make people feel uncomfortable and even claustrophobic.
- **Use Spatial Audio to create atmosphere.**
  In visionOS, you use Spatial Audio to play sound that people can perceive as coming from specific locations in space, not just from speakers (for guidance, see [Playing...
- **In general, avoid using a flat 360-degree image to create your environment.**
  A 360-degree image doesn’t tend to give people a sense of scale when they view it in an environment, so it can reduce the immersiveness of the experience. Prefer creating object meshes that include lighting, and use shaders to implement...
- **Help people feel grounded.**
  Always provide a ground plane mesh so people don’t feel like they’re floating. If you must use a flat 360-degree image in your environment, adding a ground plane mesh can help it feel more realistic.
- **Minimize asset redundancy.**
  Using the same assets or models too frequently tends to make an environment feel less realistic.

## In-app purchase
<sub>`pages/in-app-purchase.md`</sub>

- **Let people experience your app before making a purchase.**
  People may be more inclined to invest in paid items or features after they’ve enjoyed your app and discovered its value. If you offer auto-renewable subscriptions, consider supporting limited free access to your content; for guidance,...
- **Design an integrated shopping experience.**
  You don’t want people to think they’ve entered a different app when they browse and purchase your digital products. Present products and handle transactions in ways that mirror the style of your app.
- **Use simple, succinct product names and descriptions.**
  Titles that don’t truncate or wrap and plain, direct language can help people find products quickly.
- **Display the total billing price for each in-app purchase you offer, regardless of type.**
  People need to know the total billing amount for every purchase they consider.
- **Display your store only when people can make payments.**
  If someone canʼt make payments — for example, because of parental restrictions — consider hiding your store or displaying UI that explains why the store isnʼt available. For developer guidance, see...
- **Use the default confirmation sheet.**
  When someone initiates an in-app purchase, the system displays a confirmation sheet to help prevent accidental purchases. Don’t modify or replicate this sheet.
- **Prominently mention Family Sharing in places where people learn about the content you offer.**
  For example, including “Family” or “Shareable” in a subscription or item name and referring to Family Sharing in your sign-up screen can highlight the feature and help people make an informed choice.
- **Help people understand the benefits of Family Sharing and how to participate.**
  When you turn on Family Sharing, people can receive notifications about the change, depending on their current settings. For example, an existing subscriber whose sharing setting is turned off (the default) receives a notice from Apple...
- **Aim to customize your in-app messaging so that it makes sense to both purchasers and family members.**
  For example, when a family member views shared content for the first time, you might welcome them with wording like “Your family subscription includes…”.
- **Provide help that customers can view before they request a refund.**
  In addition to including a link to the system-provided refund flow, your custom purchase-help screen can provide assistance you tailor to your app. For example, your custom screen might help people resolve problems with missing...
- **Use a simple title for the refund action, like “Refund” or “Request a Refund”.**
  The system-provided refund flow makes it clear that people request a refund from Apple, so there’s no need to reiterate this information.
- **Help people find the problematic purchase.**
  For each recent purchase you display, include contextual information that helps people identify the one they want. For example, you might display an image of the product — along with its name and description — and list the original...
- **Consider offering alternative solutions.**
  For example, if the customer didn’t receive the item they purchased, you might offer immediate fulfillment or a conciliatory item. Regardless of the alternatives you offer, make it clear that people can still request a refund.
- **Make it easy for people to request a refund.**
  Although your purchase-help screen can offer useful information and alternative solutions, make sure this content doesn’t create a barrier to requesting a refund. For example, avoid making people scroll or open another screen to reveal...
- **Avoid characterizing or providing guidance on Apple’s refund policies.**
  For example, don’t speculate about whether customers will receive the refund they request. To help people understand the refund-request process, you can provide a link to [Request a refund for apps or content that you bought from...
- **Call attention to subscription benefits during onboarding.**
  By showing the value of your subscription when people first launch your app, you can educate them on how the app works and help them understand what they’ll gain by subscribing. Include a strong call to action and a clear summary of...
- **Offer a range of content choices, service levels, and durations.**
  People appreciate the flexibility to choose the subscription that best meets their needs.
- **Consider letting people try your content for free before signing up.**
  Limited free access gives people the opportunity to sample your content and encourages people who already engaged with your content to sign up. For example, you might offer a freemium app, a metered paywall, or a free trial.
- **Freemium app**
- **Metered paywall**
- **Prompt people to subscribe at relevant times, like when they near their monthly limit of free content.**
  Additionally, consider making it easy for people to subscribe at any time by including prompts at relevant points throughout your app.
- **Encourage a new subscription only when someone isn’t already a subscriber.**
  Otherwise, people may believe their existing subscription has lapsed when that’s not actually the case. If you offer the same subscription options in multiple apps or through your website, provide a sign-in option so people don’t think...
- **Provide clear, distinguishable subscription options.**
  Use short, self-explanatory names that differentiate subscription options from one another, and specify the price and duration for each option. If you offer an introductory price, be sure to list the introductory price, the duration of...
- **Simplify initial signup by asking only for necessary information.**
  A lengthy sign-up process may lower your subscription conversion rate. Defer asking for additional information until after people have signed up.
- **In your tvOS app, help people sign up or authenticate using another device.**
  Instead of asking people to input information in your tvOS app, send a code to another device where they can enter the information you need.
- **Give people more information in your app’s sign-up screen.**
  In addition to including links to your Terms of Service and Privacy Policy in your app and App Store metadata, the in-app sign-up screen needs to include:
- **Clearly describe how a free trial works.**
  It’s particularly important to make sure people know that when the free trial is over, a payment will be automatically initiated for the next subscription period. For example, the Ocean Journal sign-up screen explicitly states both the...
- **Include a sign-up opportunity in your app’s settings.**
  App and account settings are common places for people to look for a way to subscribe.
- **Clearly explain offer details.**
  To help people make an informed decision, provide a straightforward and succinct description of your offer in your marketing materials.
- **Follow guidelines for creating a custom code.**
  A custom code can contain only alphanumeric ASCII characters. Don’t use special characters, including Chinese and Arabic characters.
- **Tell people how to redeem a custom code.**
  Because people can’t redeem a custom code by entering it in their App Store account settings, it’s important to let them know that they can redeem it through a redemption URL or within your app.
- **Consider supporting offer redemption within your app.**
  The system automatically provides screens that present the offer-redemption flow, whether people redeem the offer in your app or in the App Store. When you use StoreKit API to let people redeem offer codes within your app, the only...
- **Supply an engaging and informative promotional image.**
  Creating this optional image can help people understand the value of your content. If you don’t supply a promotional image, the code redemption screens use your app icon by default. To learn more, see [Promoting your in-app...
- **Help people benefit from unlocked content as soon as they complete the redemption flow.**
  Think about ways to align the post-redemption experience in your app with the subscriber’s new status. For example, you might provide a welcome experience for new subscribers or a brief tour of new features for an existing subscriber...
- **Provide summaries of the customer’s subscriptions.**
  In particular, people appreciate viewing the upcoming renewal date without having to search for it. Consider displaying this information in a settings or account screen, near the subscription-management option. For developer guidance,...
- **Consider using the system-provided subscription-management UI.**
  Using StoreKit APIs lets you present a consistent experience that helps people manage or cancel their subscriptions without leaving your app. For developer guidance, see...
- **Consider ways to encourage a subscriber to keep their subscription or resubscribe later.**
  When you use StoreKit APIs, your app is notified when someone chooses to cancel their subscription. In this scenario, you might want to extend a personalized offer as an alternative to cancellation or invite people to describe their...
- **Always make it easy for customers to cancel an auto-renewable subscription.**
  If the manage subscription action is deep within an app — or hard to recognize — subscribers can feel they’re being discouraged or prevented from canceling.
- **Consider creating a branded, contextual experience to complement the system-provided management UI.**
  Within your custom UI, you might offer a popular premium tier or provide personalized suggestions for alternative plans based on what you know about the customer’s preferences or how they use your app. For example, you can create a...
- **Clearly describe the differences between versions of your app that run on different devices.** `[watchOS]`
  If your watchOS app supports different functionality or provides a subset of the content that’s available on other devices, be sure to clarify these differences in your description. Be straightforward about the advantages of accessing...
- **Consider using a modal sheet to display the required information.** `[watchOS]`
  After people respond to your call to action to learn more about your subscription offers, you can use a modal sheet to present all required items in a single view. Even though people must scroll the view to access all the information,...
- **Make subscription options easy to compare on a small screen.** `[watchOS]`
  People need to understand the terms of each subscription option before they can choose one. Aim to display the duration and discount information for each option in a compact way that’s easy to scan and compare. Here are two ways you...

## Inclusion
<sub>`pages/inclusion.md`</sub>

- **Consider the tone of your copy from different perspectives.**
  The style of your writing communicates almost as much as the words you use. Although different apps use different communication styles, make sure the tone you use doesn’t send messages you don’t intend. For example, an academic tone can...
- **Pay attention to how you refer to people.**
  It typically works well to use *you* and *your* to address people directly. Referring to people indirectly as *the user* or *the player* can make your experience feel distant and unwelcoming. Also, consider reserving words like *we* and...
- **Avoid using specialized or technical terms without defining them.**
  Using specialized or technical terms can make your writing more succinct, but doing so excludes people who don’t know what the terms mean. If you must use such terms, be sure to define them first and make the definitions easy for people...
- **Replace colloquial expressions with plain language.**
  Colloquial expressions are often culture-specific and can be difficult to translate. Worse, some colloquial phrases have exclusionary meanings you might not know. For example, the phrases *peanut gallery* and *grandfathered in* both...
- **Consider carefully before including humor.**
  Humor is highly subjective and — similar to colloquial expressions — difficult to translate from one culture to another. Including humor in your experience risks confusing people who donʼt understand it, irritating people who tire of...
- **Avoid images and language that exclude people with disabilities.**
  For example, include people with disabilities when you represent a variety of people, and avoid language that uses a disability to express a negative quality.
- **Take a people-first approach when writing about people with disabilities.**
  For example, you could describe an individual’s accomplishments and goals before mentioning a disability they may have. If you’re writing about a specific person or community, find out how they self-identify; for more guidance, see...
- **Prioritize simplicity and perceivability.**
  Prefer familiar, consistent interactions that make tasks simple to perform, and ensure that everyone can perceive your content, whether they use sight, hearing, or touch.

## Keyboards
<sub>`pages/keyboards.md`</sub>

- **Support Full Keyboard Access when possible.**
  Available in iOS, iPadOS, macOS, and visionOS, Full Keyboard Access lets people navigate and activate windows, menus, controls, and system features using only the keyboard. To test Full Keyboard Access in your app or game, turn it on in...
- **Respect standard keyboard shortcuts.**
  While using most apps, people generally expect to rely on the standard keyboard shortcuts that work in other apps and throughout the system. If your app offers a unique action that people perform frequently, prefer creating a [Custom...
- **In general, don’t repurpose standard keyboard shortcuts for custom actions.**
  People can get confused when the shortcuts they know work differently in your app or game. Only consider redefining a standard shortcut if its action doesn’t make sense in your experience. For example, if your app doesn’t support text...
- **Define custom keyboard shortcuts for only the most frequently used app-specific commands.**
  People appreciate using keyboard shortcuts for actions they perform frequently, but defining too many new shortcuts can make your app seem difficult to learn.
- **Use modifier keys in ways that people expect.**
  For example, pressing Command while dragging moves items as a group, and pressing Shift while drag-resizing constrains resizing to the item’s aspect ratio. In addition, holding an arrow key moves the selected item by the smallest...
- **List modifier keys in the correct order.**
  If you use more than one modifier key in a custom shortcut, always list them in this order: Control, Option, Shift, Command.
- **Avoid adding Shift to a shortcut that uses the upper character of a two-character key.**
  People already understand that they must hold the Shift key to type the upper character of a two-character key, so it’s clearer to simply list the upper character in the shortcut. For example, the keyboard shortcut for Hide Status Bar...
- **Let the system localize and mirror your keyboard shortcuts as needed.**
  The system automatically localizes a shortcut’s primary and modifier keys to support the currently connected keyboard; if your app or game switches to a right-to-left layout, the system automatically mirrors the shortcut. For guidance,...
- **Avoid creating a new shortcut by adding a modifier to an existing shortcut for an unrelated command.**
  For example, because people are accustomed to using Command-Z for undoing an action, it would be confusing to use Shift-Command-Z as the shortcut for a command that’s unrelated to undo and redo.
- **Write descriptive shortcut titles.** `[visionOS]`
  Because the shortcut interface displays a flat list of all items in each category, submenu titles aren’t available to provide context for their child items. Make sure each shortcut title is descriptive enough to convey its action...
- **Recognize that people see an overlay when they use a physical keyboard with your visionOS app or game.** `[visionOS]`
  When people connect a physical keyboard while using your visionOS app or game, the system displays a virtual keyboard overlay that provides typing completion and other controls.

## Labels
<sub>`pages/labels.md`</sub>

- **Use a label to display a small amount of text that people don’t need to edit.**
  If you need to let people edit a small amount of text, use a [text field](https://developer.apple.com/design/human-interface-guidelines/text-fields). If you need to display a large amount of text, and optionally let people edit it, use...
- **Prefer system fonts.**
  A label can display plain or styled text, and it supports Dynamic Type (where available) by default. If you adjust the style of a label or use custom fonts, make sure the text remains legible.
- **Use system-provided label colors to communicate relative importance.**
  The system defines four label colors that vary in appearance to help you give text different levels of visual importance. For additional guidance, see [Color](https://developer.apple.com/design/human-interface-guidelines/color).
- **Make useful label text selectable.**
  If a label contains useful information — like an error message, a location, or an IP address — consider letting people select and copy it for pasting elsewhere.

## Launching
<sub>`pages/launching.md`</sub>

- **Launch instantly.**
  People want to start interacting with your app or game right away, and sometimes they don’t want to wait more than a couple of seconds.
- **If the platform requires it, provide a launch screen.**
  In iOS, iPadOS, and tvOS, the system displays your launch screen the moment your app or game starts and quickly replaces it with your first screen, giving people the impression that your experience is fast and responsive. For guidance,...
- **If you need a splash screen, consider displaying it at the beginning of your onboarding flow.**
  A splash screen is a beautiful graphic that succinctly communicates branding and other information you need to provide. If you don’t provide an onboarding experience, you might display your splash screen as soon as launching completes.
- **Restore the previous state when your app restarts so people can continue where they left off.**
  Avoid making people retrace steps to reach their previous location in your app or game. Restore granular details of the previous state as much as possible. For example, scroll the view to people’s most recent position, and display...
- **Downplay the launch experience.**
  A launch screen isn’t part of an onboarding experience or a splash screen, and it isn’t an opportunity for artistic expression. A launch screen’s sole function is to enhance the perception of your experience as quick to launch and...
- **Design a launch screen that’s nearly identical to the first screen of your app or game.**
  If you include elements that look different when launching completes, people may experience an unpleasant flash between the launch screen and your first screen. If your app or game displays a solid color before transitioning to the...
- **Avoid including text on your launch screen, even if your first screen displays text.**
  Because the content in a launch screen doesn’t change, any text you display won’t be localized.
- **Don’t advertise.**
  The launch screen isn’t a branding opportunity. Avoid creating a screen that looks like a splash screen or an “About” window, and don’t include logos or other branding elements unless they’re a fixed part of your app’s first screen.
- **Launch in the appropriate orientation.** `[iOS, iPadOS]`
  If your app or game supports both portrait and landscape modes, launch using the device’s current orientation. If your interface only runs in one orientation, launch in that orientation and let people rotate the device if necessary....
- **In a live-viewing app, consider automatically starting playback soon after people start the app.** `[tvOS]`
  People come to your app to watch TV, so you might want to start playing new or recently viewed live content after a few seconds of inactivity. For guidance, see [Live-viewing...
- **Consider launching in the Shared Space even if your app is fully immersive.** `[visionOS]`
  Opening a window in the Shared Space lets you provide more context about your app or game while giving it time to load, and it also lets you present a control that people can use to open your fully immersive experience. In general,...

## Layout
<sub>`pages/layout.md`</sub>

- **Group related items to help people find the information they want.**
  For example, you might use negative space, background shapes, colors, materials, or separator lines to show when elements are related and to separate information into distinct areas. When you do so, ensure that content and controls...
- **Make essential information easy to find by giving it sufficient space.**
  People want to view the most important information right away, so don’t obscure it by crowding it with nonessential details. You can make secondary information available in other parts of the window, or include it in an additional view.
- **Extend content to fill the screen or window.**
  Make sure backgrounds and full-screen artwork extend to the edges of the display. Also ensure that scrollable layouts continue all the way to the bottom and the sides of the device screen. Controls and navigation components like...
- **Differentiate controls from content.**
  Take advantage of the Liquid Glass material to provide a distinct appearance for controls that’s consistent across iOS, iPadOS, and macOS. Instead of a background, use a scroll edge effect to provide a transition between content and the...
- **Place items to convey their relative importance.**
  People often start by viewing items in reading order — that is, from top to bottom and from the leading to trailing side — so it generally works well to place the most important items near the top and leading side of the window,...
- **Align components with one another to make them easier to scan and to communicate organization and hierarchy.**
  Alignment makes an app look neat and organized and can help people track content while scrolling or moving their eyes, making it easier to find information. Along with indentation, alignment can also help people understand an...
- **Take advantage of progressive disclosure to help people discover content that’s currently hidden.**
  For example, if you can’t display all the items in a large collection at once, you need to indicate that there are additional items that aren’t currently visible. Depending on the platform, you might use a [Disclosure...
- **Make controls easier to use by providing enough space around them and grouping them in logical sections.**
  If unrelated controls are too close together — or if other content crowds them — they can be difficult for people to tell apart or understand what they do, which can make your app or game hard to use. For guidance, see...
- **Design a layout that adapts gracefully to context changes while remaining recognizably consistent.**
  People expect your experience to work well and remain familiar when they rotate their device, resize a window, add another display, or switch to a different device. You can help ensure an adaptable interface by respecting system-defined...
- **Be prepared for text-size changes.**
  People appreciate apps and games that respond when they choose a different text size. When you support [Supporting Dynamic Type](https://developer.apple.com/design/human-interface-guidelines/typography#Supporting-Dynamic-Type) — a...
- **Preview your app on multiple devices, using different orientations, localizations, and text sizes.**
  You can streamline the testing process by first testing versions of your experience that use the largest and the smallest layouts. Although it’s generally best to preview features like wide-gamut color on actual devices, you can test on...
- **When necessary, scale artwork in response to display changes.**
  For example, viewing your app or game in a different context — such as on a screen with a different aspect ratio — might make your artwork appear cropped, letterboxed, or pillarboxed. If this happens, don’t change the aspect ratio of...
- **Respect key display and system features in each platform.**
  When an app or game doesn’t accommodate such features, it doesn’t feel at home in the platform and may be harder for people to use. In addition to helping you avoid display and system features, safe areas can also help you account for...
- **Aim to support both portrait and landscape orientations.** `[iOS]`
  People appreciate apps and games that work well in different device orientations, but sometimes your experience needs to run in only portrait or only landscape. When this is the case, you can rely on people trying both orientations...
- **Prefer a full-bleed interface for your game.** `[iOS]`
  Give players a beautiful interface that fills the screen while accommodating the corner radius, sensor housing, and features like Dynamic Island. If necessary, consider giving players the option to view your game using a letterboxed or...
- **Avoid full-width buttons.** `[iOS]`
  Buttons feel at home in iOS when they respect system-defined margins and are inset from the edges of the screen. If you need to include a full-width button, make sure it harmonizes with the curvature of the hardware and aligns with...
- **Hide the status bar only when it adds value or enhances your experience.** `[iOS]`
  The status bar displays information people find useful and it occupies an area of the screen most apps don’t fully use, so it’s generally a good idea to keep it visible. The exception is if you offer an in-depth experience like playing...
- **As someone resizes a window, defer switching to a compact view for as long as possible.** `[iPadOS]`
  Design for a full-screen view first, and only switch to a compact view when a version of the full layout no longer fits. This helps the UI feel more stable and familiar in as many situations as possible. For more complex layouts such as...
- **Test your layout at common system-provided sizes, and provide smooth transitions.** `[iPadOS]`
  Window controls provide the option to arrange windows to fill halves, thirds, and quadrants of the screen, so it’s important to check your layout at each of these sizes on a variety of devices. Be sure to minimize unexpected UI changes...
- **Consider a convertible tab bar for adaptive navigation.** `[iPadOS]`
  For many apps, you don’t need to choose between a tab bar or sidebar for navigation; instead, you can adopt a style of tab bar that provides both. The app first launches with your choice of a sidebar or a tab bar, and then people can...
- **Avoid placing controls or critical information at the bottom of a window.** `[macOS]`
  People often move windows so that the bottom edge is below the bottom of the screen.
- **Avoid displaying content within the camera housing at the top edge of the window.** `[macOS]`
  For developer guidance, see [NSPrefersDisplaySafeAreaCompatibilityMode](https://developer.apple.com/documentation/bundleresources/information-property-list/nsprefersdisplaysafeareacompatibilitymode).
- **Be prepared for a wide range of TV sizes.** `[tvOS]`
  On Apple TV, layouts don’t automatically adapt to the size of the screen like they do on iPhone or iPad. Instead, apps and games show the same interface on every display. Take extra care in designing your layout so that it looks great...
- **Adhere to the screen’s safe area.** `[tvOS]`
  Inset primary content 60 points from the top and bottom of the screen, and 80 points from the sides. It can be difficult for people to see content that close to the edges, and unintended cropping can occur due to overscanning on older...
- **Include appropriate padding between focusable elements.** `[tvOS]`
  When you use UIKit and the focus APIs, an element gets bigger when it comes into focus. Consider how elements look when they’re focused, and make sure you don’t let them overlap important information. For developer guidance, see [About...
- **Three-column** `[tvOS]`
- **Seven-column** `[tvOS]`
- **Eight-column** `[tvOS]`
- **Include additional vertical spacing for titled rows.** `[tvOS]`
  If a row has a title, provide enough spacing between the bottom of the previous unfocused row and the center of the title to avoid crowding. Also provide spacing between the bottom of the title and the top of the unfocused items in the row.
- **Use consistent spacing.** `[tvOS]`
  When content isn’t consistently spaced, it no longer looks like a grid and it’s harder for people to scan.
- **Make partially hidden content look symmetrical.** `[tvOS]`
  To help direct attention to the fully visible content, keep partially hidden offscreen content the same width on each side of the screen.
- **Consider centering the most important content and controls in your app or game.** `[visionOS]`
  Often, people can more easily discover and interact with content when it’s near the middle of a window, especially when the window is large.
- **Keep a window’s content within its bounds.** `[visionOS]`
  In visionOS, the system displays window controls just outside a window’s bounds in the XY plane. For example, the Share menu appears above the window and the controls for resizing, moving, and closing the window appear below it. Letting...
- **If you need to display additional controls that don’t belong within a window, use an ornament.** `[visionOS]`
  An ornament lets you offer app controls that remain visually associated with a window without interfering with the system-provided controls. For example, a window’s toolbar and tab bar appear as ornaments. For guidance, see...
- **Make a window’s interactive components easy for people to look at.** `[visionOS]`
  You need to include enough space around an interactive component so that visually identifying it is easy and comfortable, and to prevent the system-provided hover effect from obscuring other content. For example, place buttons so their...
- **Design your content to extend from one edge of the screen to the other.** `[watchOS]`
  The Apple Watch bezel provides a natural visual padding around your content. To avoid wasting valuable space, consider minimizing the padding between elements.
- **Avoid placing more than two or three controls side by side in your interface.** `[watchOS]`
  As a general rule, display no more than three buttons that contain glyphs — or two buttons that contain text — in a row. Although it’s usually better to let text buttons span the full width of the screen, two side-by-side buttons with...
- **Support autorotation in views people might want to show others.** `[watchOS]`
  When people flip their wrist away, apps typically respond to the motion by sleeping the display, but in some cases it makes sense to autorotate the content. For example, a wearer might want to show an image to a friend or display a QR...

## Lists and tables
<sub>`pages/lists-and-tables.md`</sub>

- **Prefer displaying text in a list or table.**
  A table can include any type of content, but the row-based format is especially well suited to making text easy to scan and read. If you have items that vary widely in size — or you need to display a large number of images — consider...
- **Let people edit a table when it makes sense.**
  People appreciate being able to reorder a list, even if they can’t add or remove items. In iOS and iPadOS, people must enter an edit mode before they can select table items.
- **Provide appropriate feedback when people select a list item.**
  The feedback can vary depending on whether selecting the item reveals a new view or toggles the item’s state. In general, a table that helps people navigate through a hierarchy persistently highlights the selected row to clarify the...
- **Keep item text succinct so row content is comfortable to read.**
  Short, succinct text can help minimize truncation and wrapping, making text easier to read and scan. If each item consists of a large amount of text, consider alternatives that help you avoid displaying over-large table rows. For...
- **Consider ways to preserve readability of text that might otherwise get clipped or truncated.**
  When a table is narrow — for example, if people can vary its width — you want content to remain recognizable and easy to read. Sometimes, an ellipsis in the middle of text can make an item easier to distinguish because it preserves both...
- **Use descriptive column headings in a multicolumn table.**
  Use nouns or short noun phrases with [title-style capitalization](https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web#apdca93e113f1d64), and don’t add ending punctuation. If you don’t include a column heading in a...
- **Choose a table or list style that coordinates with your data and platform.**
  Some styles use visual details to help communicate grouping and hierarchy or to provide specific experiences. In iOS and iPadOS, for example, the grouped style uses headers, footers, and additional space to separate groups of data; the...
- **Choose a row style that fits the information you need to display.**
  For example, you might need to display a small image in the leading end of a row, followed by a brief explanatory label. Some platforms provide built-in row styles you can use to arrange content in list rows, such as the...
- **Use an info button only to reveal more information about a row’s content.** `[iOS, iPadOS, visionOS]`
  An info button — called a *detail disclosure button* when it appears in a list row — doesn’t support navigation through a hierarchical table or list. If you need to let people drill into a list or table row’s subviews, use a disclosure...
- **Avoid adding an index to a table that displays controls — like disclosure indicators — in the trailing ends of its rows.** `[iOS, iPadOS, visionOS]`
  An *index* typically consists of the letters in an alphabet, displayed vertically at the trailing side of a list. People can jump to a specific section in the list by choosing the index letter that maps to it. Because both the index and...
- **When it provides value, let people click a column heading to sort a table view based on that column** `[macOS]`
  . If people click the heading of a column that’s already sorted, re-sort the data in the opposite direction.
- **Let people resize columns.** `[macOS]`
  Data displayed in a table view often varies in width. People appreciate resizing columns to help them concentrate on different areas or reveal clipped data.
- **Consider using alternating row colors in a multicolumn table.** `[macOS]`
  Alternating colors can help people track row values across columns, especially in a wide table.
- **Use an outline view instead of a table view to present hierarchical data.** `[macOS]`
  An [outline view](https://developer.apple.com/design/human-interface-guidelines/outline-views) looks like a table view, but includes disclosure triangles for exposing nested levels of data. For example, an outline view might display...
- **Confirm that images near a table still look good as each row highlights and slightly increases in size when it becomes focused.** `[tvOS]`
  A focused row’s corners can also become rounded, which may affect the appearance of images on either side of it. Account for this effect as you prepare images, and don’t add your own masks to round the corners.
- **When possible, limit the number of rows.** `[watchOS]`
  Short lists are easier for people to scan, but sometimes people expect a long list of items. For example, if people subscribe to a large number of podcasts, they might think something’s wrong if they can’t view all their items. You can...
- **Constrain the length of detail views if you want to support vertical page-based navigation.** `[watchOS]`
  People use vertical page-based navigation to swipe vertically among the detail items of different list rows. Navigating in this way saves time because people don’t need to return to the list to tap a new detail item, but it works only...

## Live Activities
<sub>`pages/live-activities.md`</sub>

- **Offer Live Activities for tasks and events that have a defined beginning and end.**
  Live Activities work best for tracking short to medium duration activities that don’t exceed eight hours.
- **Focus on important information that people need to see at a glance.**
  Your Live Activity doesn’t need to display everything. Think about what information people find most useful and prioritize sharing it in a concise way. When a person wants to learn more, they can tap your Live Activity to open your app...
- **Don’t use a Live Activity to display ads or promotions**
  . Live Activities help people stay informed about ongoing events and tasks, so it’s important to display only information that’s related to those events and tasks.
- **Avoid displaying sensitive information.**
  Live Activities are prominently visible and could be viewed by casual observers; for example, on the Lock Screen or in the Always-On display. For content people might consider sensitive or private, display an innocuous summary and let...
- **Create a Live Activity that matches your app’s visual aesthetic and personality in both dark and light appearances.**
  This makes it easier for people to recognize your Live Activity and creates a visual connection to your app.
- **If you include a logo mark, display it without a container.**
  This better integrates the logo mark with your Live Activity layout. Don’t use the entire app icon.
- **Don’t add elements to your app that draw attention to the Dynamic Island.**
  Your Live Activity appears in the Dynamic Island while your app isn’t in use, and other items can appear in the Dynamic Island when your app is open.
- **Ensure text is easy to read.**
  Use large, heavier-weight text — a medium weight or higher. Use small text sparingly and make sure key information is legible at a glance.
- **Adapt to different screen sizes and presentations.**
  Live Activities scale to fit various device screens. Create layouts and assets for various devices and scale factors, recognizing that the actual size on screen may vary or change. Ensure they look great everywhere by using the values...
- **Adjust element size and placement for efficient use of space.**
  Create a layout that only uses the space you need to clearly display its content. Adapt the size and placement of elements in your Live Activity so they fit well together.
- **Use familiar layouts for custom views and layouts.**
  Templates with default system margins and recommended text sizes are available in [Apple Design Resources](https://developer.apple.com/design/resources/). Using them helps your Live Activity remain legible at a glance and fit in with...
- **Use consistent margins and concentric placement.**
  Use even, matching margins between rounded shapes and the edges of the Live Activity, including corners, to ensure a harmonious fit. This prevents elements from poking into the rounded shape of the Live Activity and creating visual...
- **When separating a block of content, place it in an inset container shape or use a thick line.**
  Don’t draw content all the way to the edge of the Dynamic Island.
- **Dynamically change the height of your Live Activity on the Lock Screen or in the expanded presentation.**
  When there’s less information to show, reduce the height of the Live Activity to only use the space needed for the content. When more information becomes available, increase the height to display additional content. For example, a...
- **Carefully consider using a custom background color and opacity.**
  You can’t customize background colors for compact, minimal, and expanded presentations. However, you can use a custom background color for the Lock Screen presentation. If you set a custom background color or image for the Lock Screen...
- **Use color to express the character and identity of your app.**
  Live Activities in the Dynamic Island use a black opaque background. Consider using bold colors for text and objects to convey the personality and brand of your app. Bold colors make your Live Activity recognizable at a glance, stand...
- **Tint your Live Activity’s key line color so that it matches your content.**
  When the background is dark — for example, in Dark Mode — a key line appears around the Dynamic Island to distinguish it from other content. Choose a key line color that’s consistent with the color of other elements in your Live...
- **Use animations to reinforce the information you’re communicating and to bring attention to updates.**
  In addition to moving the position of elements, you can animate elements in and out with the default content-replace transition, or create custom transitions using scale, opacity, and movement. For example, a sports app might use...
- **Animate layout changes.**
  Content updates can require a change to your Live Activity layout — for example, when it expands to fill the screen in StandBy or when more information becomes available. During the transition to a new layout, preserve as much of the...
- **Try to avoid overlapping elements.**
  Sometimes, it’s best to animate out certain elements and then re-animate them in at a new position to avoid colliding with other parts of your transition. For example, when animating items in lists, only animate the element that moves...
- **Make sure tapping the Live Activity opens your app at the right location.**
  Take people directly to related details and actions — don’t make them navigate to find relevant information. For developer guidance on SwiftUI views that support deep linking to specific screens, see [Linking to specific app scenes from...
- **Focus on simple, direct actions.**
  Buttons or toggles take up space that might otherwise display useful information. Only include interactive elements for essential functionality that’s directly related to your Live Activity and that people activate once or temporarily...
- **Consider letting people respond to event or progress updates.**
  If an update to your Live Activity is something that a person could respond to, consider offering a button or toggle to let people take action. For example, the Live Activity of a rideshare app could include a button to contact the...
- **Start Live Activities at appropriate times, and make it easy for people to turn them off in your app.**
  People expect Live Activities to start and provide important updates for a task at hand or at specific times, even automatically. For example, they might expect a Live Activity to start after a food order, making a rideshare request, or...
- **Offer an App Shortcut that starts your Live Activity.**
  App Shortcuts expose functionality to the system, allowing access in various contexts. For example, create an App Shortcut that allows people to start your Live Activity using the Action button on iPhone. For more information, see [App...
- **Update a Live Activity only when new content is available.**
  If the underlying content or status remains the same, maintain the same display until the underlying content or status changes.
- **Alert people only for essential updates that require their attention.**
  Live Activity alerts light up the screen and by default play the notification sound to alert people about updates they shouldn’t miss. Alerts also show the expanded presentation in the Dynamic Island or a banner on devices that don’t...
- **Let people track multiple events efficiently with a single Live Activity.**
  Instead of creating separate Live Activities people need to jump between to track different events, prefer a single Live Activity that uses a dynamic layout and rotates through events. For example, a sports app could offer a single Live...
- **Always end a Live Activity immediately when the task or event ends, and consider setting a custom dismissal time.**
  When a Live Activity ends, the system immediately removes it from the Dynamic Island and in CarPlay. On the Lock Screen, in the Mac menu bar, and the watchOS Smart Stack, it remains for up to four hours. Depending on the Live Activity,...
- **Start with the iPhone design, then refine it for other contexts.**
  Create standard designs for each presentation first. Then, depending on the functionality that your Live Activity provides, design additional custom layouts for specific contexts like iPhone in StandBy, CarPlay, or Apple Watch. For more...
- **Focus on the most important information.**
  Use the compact presentation to show dynamic, up-to-date information that’s essential to the Live Activity and easy to understand. For example, a sports app could display two team logos and the score.
- **Ensure unified information and design of the compact presentations in the Dynamic Island.**
  Though the TrueDepth camera separates the leading and trailing elements, design them to read as a single piece of information, and use consistent color and typography to help create a connection between both elements.
- **Keep content as narrow as possible and ensure it’s snug against the TrueDepth camera.**
  Try not to obscure key information in the status bar, and don’t add padding between content and the TrueDepth camera. Maintain a balanced layout with similarly sized views for both leading and trailing elements; for example, use...
- **Link to relevant app content.**
  When people tap a compact Live Activity, open your app directly to the related details. Ensure both leading and trailing elements link to the same screen.
- **Ensure that your Live Activity is recognizable in the minimal presentation.**
  If possible, display updated information rather than just a logo, while ensuring people can quickly recognize your app. For example, the Timer app’s minimal Live Activity presentation displays the remaining time instead of a static icon.
- **Maintain the relative placement of elements to create a coherent layout between presentations.**
  The expanded presentation is an enlarged version of the compact or minimal presentation. Ensure information and layouts expand predictably when the Live Activity expands.
- **Wrap content tightly around the TrueDepth camera.**
  Arrange content close to the TrueDepth camera, and try to avoid leaving too much room around it to use space more efficiently and to help diminish the camera’s presence.
- **Don’t replicate notification layouts.**
  Create a unique layout that’s specific to the information that appears in the Live Activity.
- **Choose colors that work well on a personalized Lock Screen.**
  People customize their Lock Screen with wallpapers, custom tint colors, and widgets. To make a Live Activity fit a custom Lock Screen aesthetic while remaining legible, use custom background or tint colors and opacity sparingly.
- **Make sure your design, assets, and colors look great and offer enough contrast in Dark Mode and on an Always-On display.**
  By default, a Live Activity on the Lock Screen uses a light background color in the light appearance and a dark background color in the dark appearance. If you use a custom background color, choose a color that works well in both modes...
- **Verify the generated color of the dismiss button.**
  The system automatically generates a matching dismiss button based on the background and foreground colors of your Live Activity. Verify that the generated color matches your design and adjust it if needed using...
- **Use standard margins to align your design with notifications.**
  The standard layout margin for Live Activities on the Lock Screen is 14 points. While tighter margins may be appropriate for elements like graphics or buttons, avoid crowding the edges and creating a cluttered appearance. For developer...
- **Update your layout for StandBy.**
  Make sure assets look great at the larger scale, and consider creating a custom layout that makes use of the extra space. For developer guidance, see [Creating custom views for Live...
- **Consider using the default background color in StandBy.**
  The default background color seamlessly blends your Live Activity with the device bezel, achieves a softer look that integrates with a person’s surroundings, and allows the system to scale the Live Activity slightly larger because it...
- **Use standard margins and avoid extending graphic elements to the edge of the screen.**
  Without standard margins, content gets cut off as the Live Activity extends, making it feel broken.
- **Verify your design in Night Mode.**
  In Night Mode, the system applies a red tint to your Live Activity. Check that your Live Activity design uses colors that provide enough contrast in Night Mode.
- **Consider creating a custom layout if your Live Activity would benefit from larger text or additional information.**
  Instead of using the default appearance in CarPlay, declare support for a [ActivityFamily.small](https://developer.apple.com/documentation/widgetkit/activityfamily/small) supplemental activity family.
- **Carefully consider including buttons or toggles in your custom layout.**
  In CarPlay, the system deactivates interactive elements in your Live Activity. If people are likely to start or observe your Live Activity while driving, prefer displaying timely content rather than buttons and toggles.
- **Consider creating a custom watchOS layout.** `[watchOS]`
  While the system provides a default view automatically, a custom layout designed for Apple Watch can show more information and add interactive functionality like a button or toggle.
- **Carefully consider including buttons or toggles in your custom layout.** `[watchOS]`
  The custom watchOS layout also applies to your Live Activity in CarPlay where the system deactivates interactive elements. If people are likely to start or observe your Live Activity while driving, don’t include buttons or toggles in...
- **Focus on essential information and significant updates.** `[watchOS]`
  Use space in the Smart Stack as efficiently as possible and think of the most useful information that a Live Activity can convey:

## Live Photos
<sub>`pages/live-photos.md`</sub>

- **Apply adjustments to all frames.**
  If your app lets people apply effects or adjustments to a Live Photo, make sure those changes are applied to the entire photo. If you don’t support this, give people the option of converting it to a still photo.
- **Keep Live Photo content intact.**
  It’s important for people to experience Live Photos in a consistent way that uses the same visual treatment and interaction model across all apps. Don’t disassemble a Live Photo and present its frames or audio separately.
- **Implement a great photo sharing experience.**
  If your app supports photo sharing, let people preview the entire contents of Live Photos before deciding to share. Always offer the option to share Live Photos as traditional photos.
- **Clearly indicate when a Live Photo is downloading and when the photo is playable.**
  Show a progress indicator during the download process and provide some indication when the download is complete.
- **Display Live Photos as traditional photos in environments that don’t support Live Photos.**
  Don’t attempt to replicate the Live Photos experience provided in a supported environment. Instead, show a traditional, still representation of the photo.
- **Make Live Photos easily distinguishable from still photos.**
  The best way to identify a Live Photo is through a hint of movement. Because there are no built-in Live Photo motion effects, like the one that appears as you swipe through photos in the full-screen browser of Photos app, you need to...
- **Keep badge placement consistent.**
  If you show a badge, put it in the same location on every photo. Typically, a badge looks best in a corner of a photo.

## Live-viewing apps
<sub>`pages/live-viewing-apps.md`</sub>

- **Feature live content prominently and make it easy to access.**
  People come to your app to watch content, so you want to minimize the interval between starting your app and playing content. When live content is in the first tab, people don’t have to tap more than once to start viewing it.
- **Let people tap once — or not at all — to start playback.**
  For example, you might display a Watch Now button on top of featured or recently viewed live content. When people tap this button, it immediately disappears and playback begins, replacing your app’s UI with a full-screen, immersive...
- **Make sure live content looks live.**
  People need to be able to distinguish live content from VOD content. Although simply playing live content is the best way to make it feel live, you can also help people recognize live content by marking it in some way. For example, you...
- **Consider indicating the progress of currently playing live content.**
  People appreciate knowing where they’ll land when they jump into in-progress live content. You can use a progress bar or other indicator to show people how much content remains.
- **Give people additional actions and viewing alternatives.**
  In addition to playback, which always needs to be the primary action, make it easy for people to record, restart, download, and perform other actions that you support. Display these actions in the same order throughout your app — for...
- **Consider using a content footer for browsing channels during playback.**
  A content footer lets people browse without taking them out of the live playback experience. If you decide to use a content footer, be sure to:
- **Provide instant visual feedback when people change channels.**
  This is essential for two reasons: people need confirmation that they’ve arrived at the channel they want, and providing feedback can give the streaming content some time to load.
- **Match audio to the current context.**
  When people start playing live content, they expect the audio to match even if they switch to browsing while the content plays in the background. However, when people navigate away from the live tab in your app, they leave the...
- **Prominently display current information and make it easy to return to playback.**
  When people first open the EPG, the current program, channel, and time needs to be easy to spot so they can instantly return to the current channel.
- **Make browsing the EPG effortless.**
  A typical EPG contains a lot of information, so it’s important to help people page, scroll, or jump through it easily. Also consider providing a My Channels group or a Favorites group that gives people quick access to the content they...
- **Group content into familiar categories to help people find it more easily.**
  For example, you might use categories like Movies, TV Shows, Kids, Sports, and Popular. If your app includes a content footer, organize content thumbnails using the same categories as in the EPG.
- **Let people browse the EPG without leaving their current content.**
  For example, you can continue playing content in a picture-in-picture (PiP) mode or in the background while people browse the EPG.
- **Let people start and stop recording from the info panel.**
  While live-streaming, people want to reveal the info panel to start recording immediately.
- **Let people record a future program in a view that provides details about the content.**
  Also, give people the option to record only that program or all future episodes.
- **Help people adapt the recording experience to their needs.**
  Let people specify precisely what they want to record, such as only the current episode, only new episodes, or only games that involve specific teams.
- **Allow playback and other content-specific actions within your cloud DVR area.**
  When people open a view that displays content details in your cloud DVR section, let them play or delete content and, if applicable, adjust recording settings.
- **Consider offering a control that lets people manage cloud DVR settings.**
  For example, you might let people delete recordings they’ve already watched or content that’s older than a certain number of days. Ideally, help people avoid running out of space by letting them set up automatic storage management,...

## Loading
<sub>`pages/loading.md`</sub>

- **Show something as soon as possible.**
  If you make people wait for loading to complete before displaying anything, they can interpret the lack of content as a problem with your app or game. Instead, consider showing placeholder text, graphics, or animations as content loads,...
- **Let people do other things in your app or game while they wait for content to load.**
  Loading content in the background helps give people access to other actions. For example, a game could load content in the background while players learn about the next level or view an in-game menu. For developer guidance, see...
- **If loading takes an unavoidably long time, give people something interesting to view while they wait.**
  For example, you might provide gameplay hints, display tips, or introduce people to new features. Gauge the remaining loading time as accurately as possible to help you avoid giving people too little time to enjoy your placeholder...
- **Improve installation and launch time by downloading large assets in the background.**
  Consider using the [Background Assets](https://developer.apple.com/documentation/backgroundassets) framework to schedule asset downloads — like game level packs, 3D character models, and textures — to occur immediately after...
- **Clearly communicate that content is loading and how long it might take to complete.**
  Ideally, content displays instantly, but for situations where loading takes more than a moment or two, you can use system-provided components — called *progress indicators* — to show that loading is ongoing. In general, you use a...
- **For games, consider creating a custom loading view.**
  Standard progress indicators work well in most apps, but can sometimes feel out of place in a game. Consider designing a more engaging experience by using custom animations and elements that match the style of your game.
- **As much as possible, avoid showing a loading indicator in your watchOS experience.** `[watchOS]`
  People expect quick interactions with their Apple Watch, so aim to display content immediately. In situations where content needs a second or two to load, it’s better to display a loading indicator than a blank screen.

## Lockups
<sub>`pages/lockups.md`</sub>

- **Allow adequate space between lockups.**
  A focused lockup expands in size, so leave enough room between lockups to avoid overlapping or displacing other lockups. For guidance, see [Layout](https://developer.apple.com/design/human-interface-guidelines/layout).
- **Use consistent lockup sizes within a row or group.**
  A group of buttons or a row of content images is more visually appealing when the widths and heights of all elements match.
- **Prefer images over initials.**
  An image of a person creates a more intimate connection than text.

## Mac Catalyst
<sub>`pages/mac-catalyst.md`</sub>

- **Drag and drop.**
  When you support drag and drop in your iPad app, you also get support for drag and drop in the Mac version.
- **Keyboard navigation and shortcuts.**
  Even though a physical keyboard may not always be available on iPad, iPad users appreciate using the keyboard to navigate and keyboard shortcuts to streamline their interactions. On the Mac, people expect apps to offer both keyboard...
- **Multitasking.**
  Apps that do a good job scaling the interface to support Split View, Slide Over, and Picture in Picture lay the necessary groundwork to support the extensive window resizability that Mac users expect.
- **Multiple windows**
  . By supporting multiple scenes on iPad, you also get support for multiple windows in the macOS version of your app.
- **When you adopt the Mac idiom, thoroughly audit your app’s layout, and plan to make changes to it.**
  To help with this effort, consider using a separate asset catalog to contain your Mac app’s assets instead of reusing the asset catalog that contains your iPad app’s assets.
- **Adjust font sizes as needed.**
  With the Mac idiom, text renders at 100% of its configured size, which can appear too large without adjustment. When possible, use text styles and avoid fixed font sizes.
- **Make sure views and images look good in the Mac version of your app.**
  With the Mac idiom, iPadOS views render at 100% of their size, making them appear more detailed. To help you visualize the difference, consider the two depictions of an image asset shown below. One version illustrates how the asset...
- **Limit your appearance customizations to standard macOS appearance customizations that are the same or similar to those available in iPadOS.**
  Not all appearance customizations available to iPadOS controls are available to macOS controls.
- **Make sure people retain access to important tab-bar items in the Mac version of your app.**
  Regardless of whether you use a split view or a segmented control instead of a tab bar in your iPad app, be sure to give people quick access to top-level items by listing them in the macOS View menu.
- **Offer multiple ways to move between pages.**
  Mac users — especially those who interact using a pointing device or only the keyboard — appreciate Next and Previous buttons in addition to iPad or trackpad gestures that let them swipe between pages.
- **Create a macOS version of your app icon.**
  Great macOS app icons showcase the lifelike rendering style that people expect in macOS while maintaining a harmonious experience across all platforms.
- **Consider moving controls from the main UI of your iPad app to your Mac app’s toolbar.**
  Be sure to list the commands associated with these controls in the menus of your Mac app’s menu bar.
- **As much as possible, adopt a top-down flow.**
  Mac apps place the most important actions and content near the top of the window. If your iPad app provides controls in a toolbar, put these controls in the window toolbar of the macOS version of your app.
- **Relocate buttons from the side and bottom edges of the screen.**
  On iPad, placing buttons on these screen edges can help people reach them, but on a Mac, this ergonomic consideration doesn’t apply. You may want to relocate these controls to other areas or put them in the toolbar of your macOS window.

## Machine learning
<sub>`pages/machine-learning.md`</sub>

- **Request explicit feedback only when necessary.**
  People must take action to provide explicit feedback, so it’s best to avoid requesting it if possible. Instead, consider using implicit feedback to learn how people interact with your app without asking them to do extra work.
- **Always make providing explicit feedback a voluntary task.**
  You want to communicate that explicit feedback can help improve the experience without making people feel that providing it is mandatory.
- **Use simple, direct language to describe each explicit feedback option and its consequences.**
  Avoid using imprecise terms such as *dislike* because such terms don’t convey consequences and can be hard to translate. Instead, describe each option in a way that helps people understand what happens when they choose the option, such as:
- **Add icons to an option description if it helps people understand it.**
  [Icons](https://developer.apple.com/design/human-interface-guidelines/icons) can help clarify or emphasize part of an option description. Avoid using an icon by itself, because it might not be clear enough to communicate granularity or...
- **Consider offering multiple options when requesting explicit feedback.**
  Providing [multiple options](#Multiple-options) can give people a sense of control and help them identify unwanted suggestions and remove them from your app. To help people provide feedback, consider offering options that become...
- **Act immediately when you receive explicit feedback and persist the resulting changes.**
  For example, if people identify content they don’t want to see, hide it from their view and ensure it doesn’t appear elsewhere in your app. When you react immediately to feedback and show that your app remembers it, you build people’s...
- **Consider using explicit feedback to help improve when and where you show results.**
  For example, people might like a result, but they may not want to see it at certain times or in certain contexts. Explicit feedback on when and where to show results can help you fine-tune the experience people have in your app.
- **Always secure people’s information.**
  Implicit feedback can gather potentially sensitive user information, so you must be particularly careful to maintain strict controls on user privacy.
- **Help people control their information.**
  As an app developer, you know that the more you understand about the behavior of your users — both within your app and in other apps — the more you can improve the experience your app provides. Although most people understand the...
- **Don’t let implicit feedback decrease people’s opportunities to explore.**
  Implicit feedback tends to reinforce people’s behavior, which can improve the user experience in the short term, but may worsen it in the long term. For example, it might seem like a good idea to give people a set of suggestions that...
- **When possible, use multiple feedback signals to improve suggestions and mitigate mistakes.**
  Implicit feedback is indirect, so it can be difficult to discern a person’s actual intent in the information you gather. For example, if someone views a photo, shares it in a message, and adds it to a shared album, it doesn’t...
- **Consider withholding private or sensitive suggestions.**
  People often share their accounts and devices with others, or switch from using a personal device to a communal one. If your app receives implicit feedback related to private or sensitive topics, avoid offering recommendations based on...
- **Prioritize recent feedback.**
  People’s tastes can change frequently, so base your recommendations on recent implicit feedback. For example, Face ID prioritizes recent facial input because it’s most likely to represent what the person looks like now. If recent...
- **Use feedback to update predictions on a cadence that matches the person’s mental model of the feature.**
  For example, people expect typing suggestions to update immediately as they’re typing. On the other hand, giving people continuously updated song recommendations makes it hard to consider individual songs and could make them feel rushed...
- **Be prepared for changes in implicit feedback when you make changes to your app’s UI.**
  Even small UI changes can lead to noticeable changes in the amount and types of implicit feedback. For example, changing the location of a button can affect how people use it, even if there’s no change in the benefit they get from the...
- **Beware of confirmation bias.**
  Implicit feedback is constrained by what people can actually see and do in your app and other apps — it rarely gives you insight into new things they might like to do. Avoid relying solely on implicit feedback to inform your results.
- **Always secure people’s information.**
  During calibration, people may provide sensitive information and you must make sure it remains secure.
- **Be clear about why you need people’s information.**
  Typically, calibration is required before people can use a feature, so it’s essential that they understand the value of providing their information. As you briefly describe how people can benefit from your feature, emphasize what it...
- **Collect only the most essential information.**
  Designing a unique experience that requests a minimal amount of information can make people more comfortable participating in the process and increase their trust in your app.
- **Avoid asking people to participate in calibration more than once.**
  Also, it’s best when calibration occurs early in the user experience. As people continue using your app or feature, you can use implicit or explicit feedback to evolve your information about them without asking them to participate...
- **Make calibration quick and easy.**
  Even a brief calibration experience takes time and requires effort from people. An ideal calibration experience makes it easy for people to respond, without compromising the quality of the information they provide. The following...
- **Make sure people know how to perform calibration successfully.**
  After people decide to participate in calibration, give them an explicit goal and show their progress toward it. For example, Face ID calibration briefly describes what people need to do and changes the appearance of the tick marks...
- **Immediately provide assistance if progress stalls.**
  When progress stalls, people can feel stuck or powerless, and they may lose trust in your app. In this situation, it’s crucial to give people actionable recommendations that quickly get them back on track. As you provide this guidance,...
- **Confirm success.**
  The moment people successfully complete calibration, reward their time and effort by giving them a clear path toward using the feature. Providing an explicit completion to the calibration experience reinforces the unique nature of the...
- **Let people cancel calibration at any time.**
  Make sure you give people an easy way to cancel the experience at any point and avoid implying any judgment about their choice. There’s no need to provide any messaging that mentions the canceled calibration, because the next time...
- **Give people a way to update or remove information they provided during calibration.**
  Letting people edit their information gives them more control and can lead them to have greater trust in your app. Although the calibration experience can help people edit their responses, it’s a good idea to let people edit their...
- **Understand the significance of a mistake’s consequences.**
  For example, incorrect keyboard suggestions might annoy people, but suggesting a travel route that results in a missed flight is a serious inconvenience. Show empathy by providing corrective actions or tools that match the seriousness...
- **Make it easy for people to correct frequent or predictable mistakes.**
  If you don’t give people an easy way to correct mistakes, they can lose trust in your app.
- **Continuously update your feature to reflect people’s evolving interests and preferences and help avoid mistakes.**
  For example, you can use implicit feedback to discover changes in people’s tastes and habits. It’s also a good idea to update your feature with domain-specific information, such as current trends in popular entertainment. Ideally,...
- **When possible, address mistakes without complicating the UI.**
  Some patterns, such as corrections and limitations, tend to integrate seamlessly with an app’s UI, whereas others, like attributions, can be harder to integrate. Balance a pattern’s effect on the UI with its potential for compounding...
- **Be especially careful to avoid mistakes in proactive features.**
  A proactive feature — like a suggestion based on people’s behaviors — promises valuable results without asking people to do anything to get them. However, because people don’t request a proactive feature, they often have less patience...
- **As you work on reducing mistakes in one area, always consider the effect your work has on other areas and overall accuracy.**
  For example, optimizing an image-recognition app to improve how it recognizes dogs might result in a decreased ability to recognize cats. As your models evolve, be prepared for mistakes to evolve, too. Use what you know about people’s...
- **Give people familiar, easy ways to make corrections.**
  When your app makes a mistake, you don’t want people to be confused about how to correct it. You can avoid causing confusion by showing the steps your app takes as it performs the automated task. For example, Photos highlights the...
- **Provide immediate value when people make a correction.**
  Reward people’s effort by instantly displaying corrected content, especially when the feature is critical or you’re responding to direct user input. Also, be sure to persist the updates so people don’t have to make the same corrections...
- **Let people correct their corrections.**
  Sometimes, people make a correction without realizing that they’ve made a mistake. As you do with all corrections, respond immediately to an updated correction and persist the update.
- **Always balance the benefits of a feature with the effort required to make a correction.**
  People may not mind when a feature that automates a task makes a mistake, but they’re likely to stop using the feature if it seems easier to perform the task themselves.
- **Never rely on corrections to make up for low-quality results.**
  Although corrections can reduce the impact of a mistake, depending on them may erode people’s trust in your app and reduce the value of your feature.
- **Learn from corrections when it makes sense.**
  A correction is a type of [implicit](#Implicit-feedback) that can give you valuable information about ways your app doesn’t meet people’s expectations. Before you use a correction to update your models, make sure that the correction...
- **When possible, use guided corrections instead of freeform corrections.**
  Guided corrections suggest specific alternatives, so they require less user effort; freeform corrections don’t suggest specific alternatives, so they require more input from people. An example of guided correction is a speech-to-text...
- **Prefer diverse options.**
  When possible, balance the accuracy of a response with the diversity of multiple options. For example, Apple Maps generally suggests more than one route to a destination, such as a route without tolls, a scenic route, or a route that...
- **In general, avoid providing too many options.**
  People must evaluate each option before making a choice, so having more options increases cognitive load. When possible, list options on one screen so people don’t have to scroll to find the right one.
- **List the most likely option first.**
  When you know how your [confidence](#Confidence) values correlate with the quality of your results, you might use them to rank the options. You might also consider using contextual information, such as the time of day or the current...
- **Make options easy to distinguish and choose.**
  For example, in a routing app, people often need to make route choices quickly to avoid going the wrong way. When options look similar, help people distinguish between them by providing a brief description of each one and taking...
- **Learn from selections when it makes sense.**
  People give you [implicit](#Implicit-feedback) every time they make a selection. When it doesn’t adversely affect the user experience, use this feedback to refine the options you provide and increase the chance that you’ll present the...
- **Know what your confidence values mean before you decide how to present them.**
  For example, people may forgive low-quality results from [critical or complementary](#Critical-or-complementary) features — especially when results are accompanied by [attribution](#Attribution) or other contextual information — but...
- **In general, translate confidence values into concepts that people already understand.**
  Simply displaying a confidence value doesn’t necessarily help people understand how it relates to a result. For example, a feature that suggests new music based on a person’s listening habits might calculate that there’s a 97% match...
- **In situations where attributions aren’t helpful, consider ranking or ordering the results in a way that implies confidence levels.**
  If you must display confidence directly, consider expressing it in terms of semantic categories. For example, a feature that predicts travel prices might replace ranges of confidence numbers with categories like “high chance” and “low...
- **In scenarios where people expect statistical or numerical information, display confidence values that help them interpret the results.**
  For example, weather predictions, sports statistics, and polling numbers are often accompanied by specific values that express the accuracy of the data as an interval or a percentage.
- **Whenever possible, help people make decisions by conveying confidence in terms of actionable suggestions.**
  Understanding people’s goals is key to expressing confidence in ways that help them make decisions. For example, if your feature predicts when an item will be at its lowest price, you know that people want to optimize how they spend...
- **Consider changing how you present results based on different confidence thresholds.**
  If high or low levels of confidence have a meaningful impact on the ways people can experience the results, it’s a good idea to adapt your presentation accordingly. For example, when confidence is high, the face recognition feature in...
- **When you know that confidence values correspond to result quality, you generally want to avoid showing results when confidence is low.**
  Especially when a feature is proactive and can make unbidden suggestions, poor results can cause people to be annoyed and even lose trust in the feature. For suggestions and proactive features, it’s a good idea to set a confidence...
- **Consider using attributions to help people distinguish among results.**
  For example, if you present a set of results as [multiple options](#Multiple-options), including attributions can help people choose an option based on their understanding of the premise that led to it, such as “New books by authors...
- **Avoid being too specific or too general.**
  Overly specific attributions can make people feel like they have to do additional work to interpret the results, whereas overly general attributions typically don’t provide useful information. In apps that make content recommendations,...
- **Keep attributions factual and based on objective analysis.**
  To be useful, an attribution needs to help people reason about a result; you don’t want to provoke an emotional response. Don’t provide an attribution that implies understanding or judgment of people’s emotions, preferences, or beliefs....
- **In general, avoid technical or statistical jargon.**
  In most situations, using percentages, statistics, and other technical jargon doesn’t help people assess the results you provide. The exception to this is when the result itself is of a statistical or technical nature, such as...
- **Help people establish realistic expectations.**
  When a limitation may have a serious effect on user experience but happens rarely, consider making people aware of the limitation before they use your app or feature. You might describe the limitation in marketing materials or within...
- **Demonstrate how to get the best results.**
  If you don’t provide guidance for using a feature, people may assume it’ll do everything they want. When you proactively show people how to get good results, you help them benefit from the feature and establish a more accurate mental...
- **Explain how limitations can cause unsatisfactory results.**
  People can get frustrated when it seems that your feature works intermittently. Ideally, your feature can recognize and describe the reasons for poor results to make people aware of the limitations and help them to adjust their...
- **Consider telling people when limitations are resolved.**
  When people use a feature frequently, they learn to avoid the interactions that fail because of the feature’s limitations. When you update your app to remove a limitation, you might want to notify people so that they can adjust their...

## Managing accounts
<sub>`pages/managing-accounts.md`</sub>

- **Explain the benefits of creating an account and how to sign up.**
  If your app or game requires an account, write a brief, friendly description of the reasons for the requirement and its benefits. Display this message in your sign-in view.
- **Delay sign-in for as long as possible.**
  People often abandon apps when they’re forced to sign in before they can do anything useful. To help avoid this situation, give people a chance to get a sense of what your app or game does before asking them to make a commitment to it....
- **If you don’t use Sign in with Apple in your iOS, iPadOS, macOS, or visionOS app, prefer using a passkey.**
  Passkeys simplify account creation and authentication, eliminating the need for people to create or enter passwords. When an app supports passkeys, people simply provide their user name when creating a new account or signing in to an...
- **Always identify the authentication method you offer.**
  For example, if you display a button for signing in to your app with Face ID, title it using a phrase like “Sign In with Face ID” instead of a generic phrase like “Sign In.”
- **Refer only to authentication methods that are available in the current context.**
  For example, don’t reference Face ID on a device that doesn’t offer it. Check the device’s capabilities and use the appropriate terminology. For developer guidance, see...
- **In general, avoid offering an app-specific setting for opting in to biometric authentication.**
  People turn on biometric authentication at the system level, so presenting an in-app setting is redundant and could be confusing.
- **Avoid using the term *passcode* to refer to account authentication.**
  People create a passcode to unlock their device or authenticate for Apple services. If you use the term in your interface, people might think you’re asking them to reuse their passcode in your app or game.
- **Provide a clear way to initiate account deletion within your app or game.**
  If people can’t perform account deletion within your app, you must provide a direct link to the webpage on which people can do so. Make the link easy to discover — for example, don’t bury it in your Privacy Policy or Terms of Service pages.
- **Provide a consistent account-deletion experience whether people perform it within your app or game or on the website.**
  For example, avoid making one version of the deletion flow longer or more complicated than the other.
- **Consider letting people schedule account deletion to occur in the future.**
  People can appreciate the opportunity to use their remaining services or wait until their subscription auto-renews before deleting their account. If you offer a way to schedule account deletion, offer an option for immediate deletion as...
- **Tell people when account deletion will complete, and notify them when it’s finished.**
  Because it can sometimes take a while to fully delete an account, it’s essential to keep people informed about the status of the deletion process so they know what to expect.
- **If you support in-app purchases, help people understand how billing and cancellation work when they delete their account.**
  For example, you might need to help people understand the following scenarios:
- **Avoid displaying a sign-out option when people are signed in at the system level.**
  If your app must include a sign-out option, invoking it needs to prompt people to navigate to Settings > TV Provider to sign out of their account.
- **Never instruct people to sign out by adjusting privacy controls.**
  The TV provider controls in Settings > Privacy aren’t a sign-out mechanism. These settings help people manage the apps that can access their TV provider account.
- **Prefer letting people use another device to sign up or authenticate.** `[tvOS]`
  When you configure your app’s associated domains, Apple TV can work with other devices to safely suggest sign-in credentials, including [Sign in with...
- **When people are signed in to a shared account, avoid asking them to choose their profile every time they become the current user.** `[tvOS]`
  In tvOS 16 and later, your app can share its credentials with all users while storing each individual’s profile and user data separately. When you support this type of sharing, your app can automatically use the current user’s profile...
- **Minimize data entry.** `[tvOS]`
  If you need to gather more than a small amount of information, ask people to visit a website from another device. If you need an email address, show the email keyboard screen, which includes a list of recently entered addresses.

## Managing notifications
<sub>`pages/managing-notifications.md`</sub>

- **Build trust by accurately representing the urgency of each notification.**
  People have several ways to adjust how they receive your notifications — including turning off all notifications — so it’s essential to be as realistic as possible when assigning an interruption level. You don’t want people to feel that...
- **Use the Time Sensitive interruption level only for notifications that are relevant in the moment.**
  To help people understand the benefits of letting Time Sensitive notifications break through a Focus or scheduled delivery, make sure the notification is about an event that’s happening now or will happen within an hour. The first time...
- **Never use the Time Sensitive interruption level to send a marketing notification.**
  People may have agreed to receive marketing notifications from your app, but such a notification must never break through a Focus or scheduled delivery setting.
- **Get people’s permission if you want to send them promotional or marketing notifications.**
  Before you send these notifications to people, you must receive their explicit permission to do so. Create an alert, modal view, or other interface that describes the types of information you want to send and gives people a clear way to...
- **Make sure people can manage their notification settings within your app.**
  In addition to requesting permission to send informational or marketing notifications, you must also provide an in-app settings screen that lets people change their choice. For guidance, see...

## Maps
<sub>`pages/maps.md`</sub>

- **In general, make your map interactive.**
  People expect to be able to zoom, pan, and otherwise interact with maps in familiar ways. Noninteractive elements that obscure the map can interfere with people’s expectations for how maps behave.
- **Pick a map emphasis style that suits the needs of your app.**
  There are two emphasis styles to choose from:
- **Help people find places in your map.**
  Consider offering a search feature combined with a way to filter locations by category. The search field for a shopping mall map, for example, might include filters that make it easy to find common store types, like clothing,...
- **Clearly identify elements that people select.**
  When someone selects a specific area or other element on the map, use distinct styling like an outline and color variation to call attention to the selection.
- **Cluster overlapping points of interest to improve map legibility.**
  A *cluster* uses a single pin to represent multiple points of interest within close proximity. As people zoom in on a map, clusters expand to progressively reveal individual points of interest.
- **Help people see the Apple logo and legal link.**
  It’s fine when parts of your interface temporarily cover the logo and link, but don’t cover these elements all the time. Follow these guidelines to help keep the Apple logo and legal link visible:
- **Use annotations that match the visual style of your app.**
  Annotations identify custom points of interest on your map. The default annotation marker has a red tint and a white pin icon. You can change the tint to match the color scheme of your app. You can also change the icon to a string or...
- **If you want to display custom information that’s related to standard map features, consider making them independently selectable.**
  When you support selectable map features, the system treats Apple-provided features (including points of interest, territories, and physical features) independently from other annotations that you add. You can configure custom...
- **Use overlays to define map areas with a specific relationship to your content.**
- **Make sure there’s enough contrast between custom controls and the map.**
  Insufficient contrast makes controls hard to see and can cause them to blend in with the map. Consider using a thin stroke or light drop shadow to help a custom control stand out, or applying blend modes to the map area to increase its...
- **Full callout**
- **Compact callout**
- **Consider your map presentation when choosing a style.**
  The full callout style place card offers people the richest experience, presenting them with the most information about a place directly in your map. However, be sure to choose a place card style that fits in the context of your map....
- **Make sure your place card looks great on different devices and window sizes.**
  If you choose to specify a style, ensure that the content in your place card remains viewable on different devices and as window sizes change. For full callout style place cards, you can set a minimum width to prevent text from...
- **Avoid duplicating information.**
  Consider what information you already display in your app or website when you choose a place card style. For example, the full callout style place card might display information that your app already shows. In this case, the compact...
- **Keep the location on your map visible when displaying a place card.**
  This helps people maintain a sense of where the location is on your map while getting detailed place information. You can set an offset distance for your place card and point it to the selected location. For developer guidance, see...
- **Use location-related cues in surrounding content to help communicate that people can open a place card.**
  For example, you can display place names and addresses alongside a button for more details to help indicate that people can interact with it to get place information. For a space-efficient design, you can include a map pin icon with a...
- **Adjust map detail based on the zoom level.**
  Too much detail can cause a map to appear cluttered. Show large areas like rooms and buildings at all zoom levels. Then, progressively add more detailed features and labels as the map is zoomed in. An airport map might show only...
- **Use distinctive styling to differentiate the features of your map.**
  Using color along with icons can help distinguish different types of areas, stores, and services, and make it easy for people to quickly find what they’re looking for.
- **Offer a floor picker if your venue includes multiple levels.**
  A floor picker lets people quickly jump between floors. If you implement this feature, keep floor numbers concise for simplicity. In most cases, a list of floor numbers — rather than floor names — is sufficient.
- **Include surrounding areas to provide context.**
  Adjacent streets, playgrounds, and other nearby locations can all help orient people when they use your map. If these areas are noninteractive, use dimming and a distinct color to make them appear supplemental.
- **Consider supporting navigation between your venue and nearby transit points.**
  Make it easy to enter and exit your venue by offering routing to and from nearby bus stops, train stations, parking lots, garages, and other transit locations. You might also offer a way for people to quickly switch over to Apple Maps...
- **Limit scrolling outside of your venue.**
  This can help people avoid getting lost when they swipe too hard on your map. When possible, keep at least part of your indoor map visible onscreen at all times. To help people stay oriented, you may need to adjust the amount of...
- **Design an indoor map that feels like a natural extension of your app.**
  Don’t try to replicate the appearance of Apple Maps. Instead, make sure area overlays, icons, and text match the visual style of your app. For guidance, see [Indoor Mapping Data Format](https://register.apple.com/resources/imdf/).
- **Fit the map interface element to the screen.** `[watchOS]`
  The entire element needs to be visible on the Apple Watch display without requiring scrolling.
- **Show the smallest region that encompasses the points of interest.** `[watchOS]`
  The content within a map interface element doesn’t scroll, so all key content must be visible within the displayed region.

## Materials
<sub>`pages/materials.md`</sub>

- **Don’t use Liquid Glass in the content layer.**
  Liquid Glass works best when it provides a clear distinction between interactive elements and content, and including it in the content layer can result in unnecessary complexity and a confusing visual hierarchy. Instead, use [Standard...
- **Use Liquid Glass effects sparingly.**
  Standard components from system frameworks pick up the appearance and behavior of this material automatically. If you apply Liquid Glass effects to a custom control, do so sparingly. Liquid Glass seeks to bring attention to the...
- **Only use clear Liquid Glass for components that appear over visually rich backgrounds.**
  Liquid Glass provides two variants — [regular](https://developer.apple.com/documentation/swiftui/glass/regular) and [clear](https://developer.apple.com/documentation/swiftui/glass/clear) — that you can choose when building custom...
- **Choose materials and effects based on semantic meaning and recommended usage.**
  Avoid selecting a material or effect based on the apparent color it imparts to your interface, because system settings can change its appearance and behavior. Instead, match the material or vibrancy style to your specific use case.
- **Help ensure legibility by using vibrant colors on top of materials.**
  When you use system-defined vibrant colors, you don’t need to worry about colors seeming too dark, bright, saturated, or low contrast in different contexts. Regardless of the material you choose, use vibrant colors on top of it. For...
- **Consider contrast and visual separation when choosing a material to combine with blur and vibrancy effects.**
  For example, consider that:
- **Choose when to allow vibrancy in custom views and controls.** `[macOS]`
  Depending on configuration and system settings, system views and controls use vibrancy to make foreground content stand out against any background. Test your interface in a variety of contexts to discover when vibrancy enhances the...
- **Choose a background blending mode that complements your interface design.** `[macOS]`
  macOS defines two modes that blend background content: behind window and within window. For developer guidance, see...
- **Prefer translucency to opaque colors in windows.** `[visionOS]`
  Areas of opacity can block people’s view, making them feel constricted and reducing their awareness of the virtual and physical objects around them.
- **If necessary, choose materials that help you create visual separations or indicate interactivity in your app.** `[visionOS]`
  If you need to create a custom component, you may need to specify a system material for it. Use the following examples for guidance.
- **Use materials to provide context in a full-screen modal view.** `[watchOS]`
  Because full-screen modal views are common in watchOS, the contrast provided by material layers can help orient people in your app and distinguish controls and system elements from other content. Avoid removing or replacing material...

## Menus
<sub>`pages/menus.md`</sub>

- **For each menu item, write a label that clearly and succinctly describes it.**
  In general, label a menu item that initiates an action using a verb or verb phrase that describes the action, such as View, Close, or Select. For guidance labeling menu items that show and hide something in the interface or show the...
- **To be consistent with platform experiences, use title-style capitalization.**
  Although a game might have a different writing style, generally prefer using title-style capitalization, which capitalizes every word except articles, coordinating conjunctions, and short prepositions, and capitalizes the last word in...
- **Remove articles like *a*, *an*, and *the* from menu-item labels to save space.**
  In English, articles always lengthen labels, but rarely enhance understanding. For example, changing a menu-item label from View Settings to View the Settings doesn’t provide additional clarification.
- **Show people when a menu item is unavailable.**
  An unavailable menu item often appears dimmed and doesn’t respond to interactions. If all of a menu’s items are unavailable, the menu itself needs to remain available so people can open it and learn about the commands it contains.
- **Append an ellipsis to a menu item’s label when the action requires more information before it can complete.**
  The ellipsis character (…) signals that people need to input information or make additional choices, typically within another view.
- **Represent common actions consistently.**
  The system provides standard icons to represent common actions like Share, Print, and Search. Using standard icons makes your app easier to use and more familiar. For a list of icons that represent common actions, see [Standard...
- **Use menu item icons sparingly and with purpose.**
  Icons allow people to find menu items more quickly, and help clarify what selecting an item does. Use an icon to highlight the most common actions and key features of your app, file system locations, connected devices, visual concepts...
- **Apply a uniform visual treatment across menu items in the same group.**
  For visual consistency and balance, provide icons for all menu items in a group, or none of them.
- **Prefer listing important or frequently used menu items first.**
  People tend to start scanning a menu from the top, so listing high-priority items first often means that people can find what they want without reading the entire menu.
- **Consider grouping logically related items.**
  For example, grouping editing commands like Copy, Cut, and Paste or camera commands like Look Up, Look Down, and Look Left can help people remember where to find them. To help people visually distinguish such groups, use a separator....
- **Prefer keeping all logically related commands in the same group, even if the commands don’t all have the same importance.**
  For example, people generally use Paste and Match Style much less often than they use Paste, but they expect to find both commands in the same group that contains more frequently used editing commands like Copy and Cut.
- **Be mindful of menu length.**
  People need more time and attention to read a long menu, which means they may miss the command they want. If a menu is too long, consider dividing it into separate menus. Alternatively, you might be able to use a submenu to shorten the...
- **Use submenus sparingly.**
  Each submenu adds complexity to the interface and hides the items it contains. You might consider creating a submenu when a term appears in more than two menu items in the same group. For example, instead of offering separate menu items...
- **Limit the depth and length of submenus.**
  It can be difficult for people to reveal multiple levels of hierarchical submenus, so it’s generally best to restrict them to a single level. Also, if a submenu contains more than about five items, consider creating a new menu.
- **Make sure a submenu remains available even when its nested menu items are unavailable.**
  A submenu item — like all menu items — needs to let people open it and learn about the commands it contains.
- **Prefer using a submenu to indenting menu items.**
  Using indentation is inconsistent with the system and doesn’t clearly express the relationships between the menu items.
- **Consider using a changeable label that describes an item’s current state.**
  For example, instead of listing two menu items like Show Map and Hide Map, you could include one menu item whose label changes from Show Map to Hide Map, depending on whether the map is visible.
- **Include a verb if a changeable label isn’t clear enough.**
  For example, people might not know whether the changeable labels HDR On and HDR Off describe actions or states. If you needed to clarify that these items represent actions, you could add verbs to the labels, like Turn HDR On and Turn...
- **If necessary, display both menu items instead of one toggled item.**
  Sometimes, it helps people to view both actions or states at the same time. For example, a game could list both Take Account Online and Take Account Offline items, so when someone’s account is online, only the Take Account Offline menu...
- **Consider using a checkmark to show that an attribute is currently in effect.**
  It’s easy for people to scan for checkmarks in a list of attributes to find the ones that are selected. For example, in the standard Format > Font menu, checkmarks can make it easy for people notice the styles that apply to selected text.
- **Consider offering a menu item that makes it easy to remove multiple toggled attributes.**
  For example, if you let people apply several styles to selected text, it can work well to provide a menu item — such as Plain — that removes all applied formatting attributes at one time.
- **Let players navigate in-game menus using the platform’s default interaction method.**
  People expect to use the same interactions to navigate your menus as they use for navigating other menus on the device. For example, players expect to navigate your game menus using touch in iOS and iPadOS, and direct and indirect...
- **Make sure your menus remain easy to open and read on all platforms you support.**
  Each platform defines specific sizes that work best for fonts and interaction targets. Sometimes, scaling your game content to display on a different screen — especially a mobile device screen — can make in-game menus too small for...
- **Choose a small or medium menu layout when it can help streamline people’s choices.** `[iOS, iPadOS]`
  Consider using the medium layout if your app has three important actions that people often want to perform. For example, Notes uses the medium layout to give people a quick way to perform the Scan, Lock, and Pin actions. Use the small...
- **Prefer displaying a menu near the content it controls.** `[visionOS]`
  Because people need to look at a menu item before tapping it, they might miss the item’s effect if the content it controls is too far away.
- **Prefer the subtle breakthrough effect in most cases.** `[visionOS]`
  This effect blends the presentation with its surrounding content, to maintain legibility and usability while preserving the depth and context of the scene. When you select...

## Modality
<sub>`pages/modality.md`</sub>

- **Present content modally only when there’s a clear benefit.**
  A modal experience takes people out of their current context and requires an action to dismiss, so it’s important to use modality only when it helps people focus or make choices that affect their content or device.
- **Aim to keep modal tasks simple, short, and streamlined.**
  If a modal task is too complicated, people can lose track of the task they suspended when they entered the modal view, especially if the modal view obscures their previous context.
- **Take care to avoid creating a modal experience that feels like an app within your app.**
  In particular, presenting a hierarchy of views within a modal task can make people forget how to retrace their steps. If a modal task must contain subviews, provide a single path through the hierarchy and avoid including buttons that...
- **Consider using a full-screen modal style for in-depth content or a complex task.**
  A modal experience that fills a window or the device display minimizes distractions, so it can work well for presenting videos, photos, or camera views, or to support a multistep task like marking up a document or editing a photo. When...
- **Always give people an obvious way to dismiss a modal view.**
  In general, it works well to follow the platform conventions people already know. For example, in iOS, iPadOS, and watchOS apps, people typically expect to find a button in the top toolbar or swipe down; in macOS and tvOS apps, people...
- **When necessary, help people avoid data loss by getting confirmation before closing a modal view.**
  Regardless of whether people use a dismiss gesture or a button, if closing the view could result in the loss of user-generated content, be sure to explain the situation and give people ways to resolve it. For example, in iOS, you might...
- **Make it easy to identify a modal view’s task.**
  When people enter a modal view, they switch away from their previous context and might not return to it right away. When you provide a title that names the modal view’s task — or additional text that describes the task or provides...
- **Let people dismiss a modal view before presenting another one.**
  Allowing multiple modal views to be visible at the same time tends to create visual clutter and can make your app seem scattered and disorganized. People need to remember the context they were in before a modal view appears, so...

## Motion
<sub>`pages/motion.md`</sub>

- **Add motion purposefully, supporting the experience without overshadowing it.**
  Don’t add motion for the sake of adding motion. Gratuitous or excessive animation can distract people and may make them feel disconnected or physically uncomfortable.
- **Make motion optional.**
  Not everyone can or wants to experience the motion in your app or game, so it’s essential to avoid using it as the only way to communicate important information. To help everyone enjoy your app or game, supplement visual feedback by...
- **Strive for realistic feedback motion that follows people’s gestures and expectations.**
  In nongame apps, accurate, realistic motion can help people understand how something works, but feedback motion that doesn’t make sense can make them feel disoriented. For example, if someone reveals a view by sliding it down from the...
- **Aim for brevity and precision in feedback animations.**
  When animated feedback is brief and precise, it tends to feel lightweight and unobtrusive, and it can often convey information more effectively than prominent animation. For example, when a game displays a succinct animation that’s...
- **In apps, generally avoid adding motion to UI interactions that occur frequently.**
  The system already provides subtle animations for interactions with standard interface elements. For a custom element, you generally want to avoid making people spend extra time paying attention to unnecessary motion every time they...
- **Let people cancel motion.**
  As much as possible, don’t make people wait for an animation to complete before they can do anything, especially if they have to experience the animation more than once.
- **Consider using animated symbols where it makes sense.**
  When you use SF Symbols 5 or later, you can apply animations to SF Symbols or custom symbols. For guidance, see [Animations](https://developer.apple.com/design/human-interface-guidelines/sf-symbols#Animations).
- **Make sure your game’s motion looks great by default on each platform you support.**
  In most games, maintaining a consistent frame rate of 30 to 60 fps typically results in a smooth, visually appealing experience. For each platform you support, use the device’s graphics capabilities to enable default settings that let...
- **Let people customize the visual experience of your game to optimize performance or battery life.**
  For example, consider letting people switch between power modes when the system detects the presence of an external power source.
- **As much as possible, avoid displaying motion at the edges of a person’s field of view.** `[visionOS]`
  People can be particularly sensitive to motion that occurs in their peripheral vision: in addition to being distracting, such motion can even cause discomfort because it can make people feel like they or their surroundings are moving....
- **Help people remain comfortable when showing the movement of large virtual objects.** `[visionOS]`
  If an object is large enough to fill a lot of the [Field of view](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Field-of-view), occluding most or all of [Immersion and...
- **Consider using fades when you need to relocate an object.** `[visionOS]`
  When an object moves from one location to another, people naturally watch the movement. If such movement doesn’t communicate anything useful to people, you can fade the object out before moving it and fade it back in after it’s in the...
- **In general, avoid letting people rotate a virtual world.** `[visionOS]`
  When a virtual world rotates, the experience typically upsets people’s sense of stability, even when they control the rotation and the movement is subtle. Instead, consider using instantaneous directional changes during a quick fade-out.
- **Consider giving people a stationary frame of reference.** `[visionOS]`
  It can be easier for people to handle visual movement when it’s contained within an area that doesn’t move. In contrast, if the entire surrounding area appears to move — for example, in a game that automatically moves a player through...
- **Avoid showing objects that oscillate in a sustained way.** `[visionOS]`
  In particular, you want to avoid showing an oscillation that has a frequency of around 0.2 Hz because people can be very sensitive to this frequency. If you need to show objects oscillating, aim to keep the amplitude low and consider...

## Multitasking
<sub>`pages/multitasking.md`</sub>

- **Pause activities that require people’s attention or active participation when they switch away.**
  If your app is a game or a media-viewing app, for example, make sure people don’t miss anything when they switch to another app. When they switch back, let them continue as if they never left.
- **Respond smoothly to audio interruptions.**
  Occasionally, audio from another app or the system itself may interrupt your app’s audio. For example, an incoming phone call or a music playlist initiated by Siri might interrupt your app’s audio. When situations like these occur,...
- **Finish user-initiated tasks in the background.**
  When someone starts a task like downloading assets or processing a video file, they expect it to finish even if they switch away from your app. If your app is in the middle of performing a task that doesn’t need additional input,...
- **Use notifications sparingly.**
  Your app can send notifications when it’s suspended or running in the background. If people start an important or time-sensitive task in your app, and then switch away from it, they might appreciate receiving a notification when the...
- **Avoid interfering with the system-provided multitasking behavior.** `[visionOS]`
  When people look from one window to another, visionOS applies a feathered mask to the window they look away from to clarify its changed state. To avoid interfering with this visual feedback, don’t change the appearance of a window’s edges.
- **Don’t pause a window’s video playback when people look away from it.** `[visionOS]`
  In visionOS, as in macOS, people expect the playback they start in one window to continue while they view or perform a task in another window.
- **Be prepared for situations where your audio can duck.** `[visionOS]`
  Unless an app is currently the Now Playing app, its audio can duck when people look away from it to another app.

## NFC
<sub>`pages/nfc.md`</sub>

- **Don’t encourage people to make contact with physical objects.**
  To scan a tag, an iOS device must simply be within close proximity of the tag. It doesn’t need to actually touch the tag. Use terms like *scan* and *hold near* instead of *tap* and *touch* when asking people to scan objects.
- **Use approachable terminology.**
  Near-field communication may be unfamiliar to some people. To make it approachable, avoid referring to technical, developer-oriented terms like *NFC*, *Core NFC*, *Near-field communication*, and *tag*. Instead, use friendly,...
- **Provide succinct instructional text for the scanning sheet.**
  Provide a complete sentence, in sentence case, with ending punctuation. Identify the object to scan, and revise the text appropriately for subsequent scans. Keep the text short to avoid truncation.
- **Support both background and in-app tag reading.**
  Your app must still provide an in-app way to scan tags, for people with devices that don’t support background tag reading.

## Nearby interactions
<sub>`pages/nearby-interactions.md`</sub>

- **Consider a task from the perspective of the physical world to find inspiration for a nearby interaction.**
  For example, although people can easily use your app’s UI to transfer a song from their iPhone to their HomePod mini, initiating the transfer by bringing the devices close together makes the task feel rooted in the physical world....
- **Use distance, direction, and context to inform an interaction.**
  Although your app may get information from a variety of sources, prioritizing nearby, contextually relevant information can help you deliver experiences that feel organic. For example, if people want to share content with a friend in a...
- **Consider how changes in physical distance can guide a nearby interaction.**
  In the physical world, people generally expect their perception of an object to sharpen as they get closer to it. A nearby interaction can mirror this experience by providing feedback that changes with the proximity of an object. For...
- **Provide continuous feedback.**
  Continuous feedback reflects the dynamism of the physical world and strengthens the connection between a nearby interaction and the task people are performing. For example, when looking for a lost item in Find My, people get continuous...
- **Consider using multiple feedback types to create a holistic experience.**
  Fluidly transitioning among visual, audible, and haptic feedback can help a nearby interaction’s task feel more engaging and real. Using more than one type of feedback also lets you vary the experience to coordinate with both the task...
- **Avoid using a nearby interaction as the only way to perform a task.**
  You can’t assume that everyone can experience a nearby interaction, so it’s essential to provide alternative ways to get things done in your app.
- **Encourage people to hold the device in portrait orientation.**
  Holding a device in landscape can decrease the accuracy and availability of information about the distance and relative direction of other devices. If you support only portrait orientation while your nearby interaction feature runs,...
- **Design for the device’s directional field of view.**
  Nearby interaction relies on a hardware sensor with a specific field of view similar to that of the Ultra Wide camera in iPhone 11 and later. If a participating device is outside of this field of view, your app might receive information...
- **Help people understand how intervening objects can affect the nearby interaction experience in your app.**
  When other people, animals, or sufficiently large objects come between two participating devices, the accuracy or availability of distance and direction information can decrease. Consider adding advice on avoiding this situation to...

## Notifications
<sub>`pages/notifications.md`</sub>

- **Provide concise, informative notifications.**
  People turn on notifications to get quick updates, so you want to provide valuable information succinctly.
- **Avoid sending multiple notifications for the same thing, even if someone hasn’t responded.**
  People attend to notifications at their convenience. If you send multiple notifications for the same thing, you fill up Notification Center, and people may turn off all notifications from your app.
- **Avoid sending a notification that tells people to perform specific tasks within your app.**
  If it makes sense to offer simple tasks that people can perform without opening your app, you can provide [Notification actions](https://developer.apple.com/design/human-interface-guidelines/notifications#Notification-actions)....
- **Use an alert — not a notification — to display an error message.**
  People are familiar with both alerts and notifications, so you don’t want to cause confusion by using the wrong component. For guidance, see [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts).
- **Handle notifications gracefully when your app is in the foreground.**
  Your app’s notifications don’t appear when your app is in the front, but your app still receives the information. In this scenario, present the information in a way that’s discoverable but not distracting or invasive, such as...
- **Avoid including sensitive, personal, or confidential information in a notification.**
  You can’t predict what people will be doing when they receive a notification, so it’s essential to avoid including private information that could be visible to others.
- **Create a short title if it provides context for the notification content.**
  Prefer brief titles that people can read at a glance, especially on Apple Watch, where space is limited. When possible, take advantage of the prominent notification title area to provide useful information, like a headline, event name,...
- **Write succinct, easy-to-read notification content.**
  Use complete sentences, sentence case, and proper punctuation, and don’t truncate your message — the system does this automatically when necessary.
- **Provide generically descriptive text to display when notification previews aren’t available.**
  In Settings, people can choose to hide notification previews for all apps. In this situation, the system shows only your app icon and the default title *Notification*. To give people sufficient context to know whether they want to view...
- **Avoid including your app name or icon.**
  The system automatically displays a large version of your app icon at the leading edge of each notification; in a communication notification, the system displays the sender’s contact image badged with a small version of your icon.
- **Consider providing a sound to supplement your notifications.**
  Sound can be a great way to distinguish your app’s notifications and get someone’s attention when they’re not looking at the device. You can create a custom sound that coordinates with the style of your app or use a system-provided...
- **Provide beneficial actions that make sense in the context of your notification.**
  Prefer actions that let people perform common, time-saving tasks that eliminate the need to open your app. For each button, use a short, title-case term or phrase that clearly describes the result of the action. Don’t include your app...
- **Avoid providing an action that merely opens your app.**
  When people tap a notification or its preview, they expect your app to display related content, so presenting an action button that does the same thing clutters the detail view and can be confusing.
- **Prefer nondestructive actions.**
  If you must provide a destructive action, make sure people have enough context to avoid unintended consequences. The system gives a distinct appearance to the actions you identify as destructive.
- **Provide a simple, recognizable interface icon for each notification action.**
  An interface icon reinforces an action’s meaning, helping people instantly understand what it does. The system displays your interface icon on the trailing side of the action title. When you use [SF...
- **Use a badge only to show people how many unread notifications they have.**
  Don’t use a badge to convey numeric information that isn’t related to notifications, such as weather-related data, dates and times, stock prices, or game scores.
- **Make sure badging isn’t the only method you use to communicate essential information.**
  People can turn off badging for your app, so if you rely on it to show people when there’s important information, people can miss the message. Always make sure that you make important information easy for people to find as soon as they...
- **Keep badges up to date.**
  Update your app’s badge as soon as people open the corresponding notifications. You don’t want people to think there are new notifications available, only to find that they’ve already viewed them all. Note that reducing a badge’s count...
- **Avoid creating a custom image or component that mimics the appearance or behavior of a badge.**
  People can turn off notification badges if they choose, and will become frustrated if they have done so and then see what appears to be a badge.
- **Avoid using a short look as the only way to communicate important information.** `[watchOS]`
  A short look appears only briefly, giving people just enough time to see what the notification is about and which app sent it. If your notification information is critical, make sure you deliver it in other ways, too.
- **Keep privacy in mind.** `[watchOS]`
  Short looks are intended to be discreet, so it’s important to provide only basic information. Avoid including potentially sensitive information in the notification’s title.
- **Consider using a rich, custom long-look notification to let people get the information they need without launching your app.** `[watchOS]`
  You can use SwiftUI [Animations](https://developer.apple.com/documentation/swiftui/animations) to create engaging, interruptible animations; alternatively, you can use [SpriteKit](https://developer.apple.com/documentation/spritekit) or...
- **At the minimum, provide a static interface; prefer providing a dynamic interface too.** `[watchOS]`
  The system defaults to the static interface when the dynamic interface is unavailable, such as when there is no network or the iPhone companion app is unreachable. Be sure to create the resources for your static interface in advance and...
- **Choose a background appearance for the sash.** `[watchOS]`
  The system-provided sash, at the top of the long-look interface, displays your app icon and name. You can customize the sash’s color or give it a blurred appearance. If you display a photo at the top of the content area, you’ll probably...
- **Choose a background color for the content area.** `[watchOS]`
  By default, the long look’s background is transparent. If you want to match the background color of other system notifications, use white with 18% opacity; otherwise, you can use a custom color, such as a color within your brand’s palette.
- **Provide up to four custom actions below the content area.** `[watchOS]`
  For each long look, the system uses the notification’s type to determine which of your custom actions to display as buttons in the notification UI. In addition, the system always displays a Dismiss button at the bottom of the long-look...
- **Keep double tap in mind when choosing the order of custom actions you present as responses to a notification.** `[watchOS]`
  Because a double tap runs the first nondestructive action, consider placing the action that people use most frequently at the top of the list. For example, a parking app that provides custom actions for extending the time on a paid...

## Offering help
<sub>`pages/offering-help.md`</sub>

- **Let your app’s tasks inform the types of help people might need.**
  For example, you might help people perform simple, one- or two-step tasks by displaying an inline view that succinctly describes the task. In contrast, if your app or game supports complex or multistep tasks you might want to provide a...
- **Use relevant and consistent language and images in your help content.**
  Always make sure guidance is appropriate for the current context. For example, if someone’s using the Siri Remote with your tvOS experience, don’t show tips or images that feature a game controller. Also be sure the terms and...
- **Make sure all help content is inclusive.**
  For guidance, see [Inclusion](https://developer.apple.com/design/human-interface-guidelines/inclusion).
- **Avoid bloating your help content by explaining how standard components or patterns work.**
  Instead, describe the specific action or task that a standard element performs in your app or game. If your experience introduces a unique control or expects people to use an input device in a nonstandard way — such as holding the Siri...
- **Use the most appropriate tip type for your app’s user interface.**
  Display a popover tip when you want to preserve the content flow, or an inline tip when you want to ensure that surrounding information is visible. You can use an annotation-style inline tip when pointing to a specific UI element, or a...
- **Use tips for simple features.**
  Tips work best on features that are easy to describe and that people can complete with a few simple steps. If a feature requires more than three actions, it’s probably too complicated for a tip.
- **Make tips short, actionable, and engaging.**
  A tip’s goal is to encourage people to try new features. Use direct, action-oriented language to describe what the feature does and explain how to use it. Keep your tips to one or two sentences and avoid including content that’s...
- **Define rules to help ensure your tips reach the intended audience.**
  Not everyone benefits from every tip. For example, people who’ve already used a feature won’t appreciate viewing a tip that describes it. Use parameter-based or event-based eligibility rules to control when a tip appears, and only...
- **If there’s an image or symbol that people associate with the feature, consider including it in the tip, and prefer the filled variant.**
  For example, a tip with a star can help people understand that the tip is related to favorites.
- **Use buttons to direct people to information or options.**
  If your feature has settings people can customize, or you want to redirect people to an area where they can learn more about a feature, consider adding a button. Buttons can take people directly to the settings where they make...
- **Describe only the control that people indicate interest in.** `[macOS, visionOS]`
  When people want to know how to use a specific control, they don’t want to learn how to use nearby controls or how to perform a larger task.
- **Explain the action or task the control initiates.** `[macOS, visionOS]`
  It often works well to begin the description with a verb — for example, “Restore default settings” or “Add or remove a language from the list.”
- **In general, avoid repeating a control’s name in its tooltip.** `[macOS, visionOS]`
  Repeating the name takes up space in the tooltip and rarely adds value to the description.
- **Use sentence case.** `[macOS, visionOS]`
  Sentence case tends to appear more casual and approachable. If you write complete sentences, omit ending punctuation unless it’s required to be consistent with your app’s style.
- **Consider offering context-sensitive tooltips.** `[macOS, visionOS]`
  For example, you could provide different text for a control’s different states.

## Onboarding
<sub>`pages/onboarding.md`</sub>

- **Teach through interactivity.**
  People tend to grasp and retain information better when they can actually perform the task they’re learning about instead of just viewing instructional material. As much as possible, provide an interactive onboarding experience where...
- **Consider providing a collection of context-specific tips instead of a single onboarding flow.**
  Integrating contextually relevant tips into your experience can help people learn about their current task while they make progress in your app or game. A context-specific tip can also help people learn better because it lets them...
- **If you need to present a prerequisite onboarding flow, design a brief, enjoyable experience that doesn’t require people to memorize a lot of information.**
  When onboarding is quick and entertaining, people are more likely to complete it. In contrast, if you try to teach too much, people can feel overwhelmed and may be less likely to remember what they learned.
- **If it makes sense to offer a separate tutorial, consider making it optional.**
  If you let people skip the tutorial when they first launch your app or game, don’t present it again on subsequent launches, but make sure it’s easy for people to find if they want to view it later. For example, you could make the...
- **Keep onboarding content focused on the experience you provide.**
  People enter your onboarding flow to learn about your app or game; they don’t need to learn how to use the system or the device.
- **Briefly display a splash screen if necessary.**
  If you need to include a splash screen, design a beautiful graphic that communicates succinctly. Aim to display your splash screen just long enough for people to absorb the information at a glance without feeling that it’s delaying...
- **Don’t let large downloads hinder onboarding.**
  People want to start using your app or game immediately after first launching it, whether they participate in an onboarding flow or skip it. Consider including enough media and other content in your software package to prevent people...
- **Avoid displaying licensing details within your onboarding flow.**
  Let the App Store display agreements and disclaimers so people can read them before downloading your app or game. If you must include these items within the onboarding flow, integrate them in a balanced way that doesn’t disrupt the...
- **Postpone nonessential setup flows or customization steps.**
  Provide reasonable default settings so most people can immediately start interacting with your app or game without performing additional configuration.
- **If your app or game needs access to private data or resources before it can function, consider integrating the permission request into your onboarding flow.**
  In this scenario, making the request during your onboarding flow gives you the opportunity to show people why your app or game needs their permission and the benefits of granting it. Otherwise, present a permission request when people...
- **Prefer letting people experience your app or game before prompting them for ratings or purchases.**
  People can be more likely to respond positively to such requests when they’ve had a chance to become engaged with your app or game.

## Ornaments
<sub>`pages/ornaments.md`</sub>

- **Consider using an ornament to present frequently needed controls or information in a consistent location that doesn’t clutter the window.**
  Because an ornament stays close to its window, people always know where to find it. For example, Music uses an ornament to offer Now Playing controls, ensuring that these controls remain in a predictable location that’s easy to find.
- **In general, keep an ornament visible.**
  It can make sense to hide an ornament when people dive into a window’s content — for example, when they watch a video or view a photo — but in most cases, people appreciate having consistent access to an ornament’s controls.
- **If you need to display multiple ornaments, prioritize the overall visual balance of the window.**
  Ornaments help elevate important actions, but they can sometimes distract from your content. When necessary, consider constraining the total number of ornaments to avoid increasing a window’s visual weight and making your app feel more...
- **Aim to keep an ornament’s width the same or narrower than the width of the associated window.**
  If an ornament is wider than its window, it can interfere with a tab bar or other vertical content on the window’s side.
- **Consider using borderless buttons in an ornament.**
  By default, an ornament’s background is [visionOS](https://developer.apple.com/design/human-interface-guidelines/materials#visionOS), so if you place a button directly on the background, it may not need a visible border. When people...
- **Use system-provided toolbars and tab bars unless you need to create custom components.**
  In visionOS, toolbars and tab bars automatically appear as ornaments, so you don’t need to use an ornament to create these components. For developer guidance, see [Toolbars](https://developer.apple.com/documentation/swiftui/toolbars)...

## Outline views
<sub>`pages/outline-views.md`</sub>

- **Use a table instead of an outline view to present data that’s not hierarchical.**
  For guidance, see [Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables).
- **Expose data hierarchy in the first column only.**
  Other columns can display attributes that apply to the hierarchical data in the primary column.
- **Use descriptive column headings to provide context.**
  Use nouns or short noun phrases with [title-style capitalization](https://help.apple.com/applestyleguide/#/apsgb744e4a3?sub=apdca93e113f1d64) and no punctuation; in particular, avoid adding a trailing colon. Always provide column...
- **Consider letting people click column headings to sort an outline view.**
  In a sortable outline view, people can click a column heading to perform an ascending or descending sort based on that column. You can implement additional sorting based on secondary columns behind the scenes, if necessary. If people...
- **Let people resize columns.**
  Data displayed in an outline view often varies in width. It’s important to let people adjust column width as needed to reveal data that’s wider than the column.
- **Make it easy for people to expand or collapse nested containers.**
  For example, clicking a disclosure triangle for a folder in a Finder window expands only that folder. However, Option-clicking the disclosure triangle expands all of its subfolders.
- **Retain people’s expansion choices.**
  If people expand various levels of an outline view to reach a specific item, store the state so you can display it again the next time. This way, people won’t need to navigate back to the same place again.
- **Consider using alternating row colors in multi-column outline views.**
  Alternating colors can make it easier for people to track row values across columns, especially in wide outline views.
- **Let people edit data if it makes sense in your app.**
  In an editable outline view cell, people expect to be able to single-click a cell to edit its contents. Note that a cell can respond differently to a double click. For example, an outline view listing files might let people single-click...
- **Consider using a centered ellipsis to truncate cell text instead of clipping it.**
  An ellipsis in the middle preserves the beginning and end of the cell text, which can make the content more distinct and recognizable than clipped text.
- **Consider offering a search field to help people find values quickly in a lengthy outline view.**
  Windows with an outline view as the primary feature often include a search field in the toolbar. For guidance, see [Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields).

## Page controls
<sub>`pages/page-controls.md`</sub>

- **Use page controls to represent movement between an ordered list of pages.**
  Page controls don’t represent hierarchical or nonsequential page relationships. For more complex navigation, consider using a sidebar or split view instead.
- **Center a page control at the bottom of the view or window.**
  To ensure people always know where to find a page control, center it horizontally and position it near the bottom of the view.
- **Although page controls can handle any number of pages, don’t display too many**
  . More than about 10 dots are hard to count at a glance. If your app needs to display more than 10 pages as peers, consider using a different arrangement‚ such as a grid, that lets people navigate the content in any order.
- **Make sure custom indicator images are simple and clear.**
  Avoid complex shapes, and don’t include negative space, text, or inner lines, because these details can make an icon muddy and indecipherable at very small sizes. Consider using simple [SF...
- **Customize the default indicator image only when it enhances the page control’s overall meaning.**
  For example, if every page you list contains bookmarks, you might use the `bookmark.fill` symbol as the default indicator image.
- **Avoid using more than two different indicator images in a page control.**
  If your list contains one page with special meaning — like the current-location page in Weather — you can make the page easy to find by giving it a unique indicator image. In contrast, a page control that uses several unique images to...
- **Avoid coloring indicator images.**
  Custom colors can reduce the contrast that differentiates the current-page indicator and makes the page control visible on the screen. To ensure that your page control is easy to use and looks good in different contexts, let the system...
- **Avoid animating page transitions during scrubbing.** `[iOS, iPadOS]`
  People can scrub very quickly, and using the scrolling animation for every transition can make your app lag and cause distracting visual flashes. Use the animated scrolling transition only for tapping.
- **Avoid supporting the scrubber when you use the minimal background style.** `[iOS, iPadOS]`
  The minimal style doesn’t provide visual feedback during scrubbing. If you want to let people scrub a list of pages in your app, use the automatic or prominent background styles.
- **Use page controls on collections of full-screen pages.** `[tvOS]`
  A page control is designed to operate in a full-screen environment where multiple content-rich pages are peers in the page hierarchy. Inclusion of additional controls makes it difficult to maintain focus while moving between pages.
- **Use vertical pagination to separate multiple views into distinct, purposeful pages.** `[watchOS]`
  Give each page a clear purpose, and let people scroll through the pages using the Digital Crown. In watchOS, this design is more effective than horizontal pagination or many levels of hierarchical navigation.
- **Consider limiting the content of an individual page to a single screen height.** `[watchOS]`
  Embracing this constraint encourages each page to serve a clear and distinct purpose and results in a more glanceable design. Use variable-height pages judiciously and, if possible, only place them after fixed-height pages in your app...

## Panels
<sub>`pages/panels.md`</sub>

- **Use a panel to give people quick access to important controls or information related to the content they’re working with.**
  For example, you might use a panel to provide controls or settings that affect the selected item in the active document or window.
- **Consider using a panel to present inspector functionality.**
  An *inspector* displays the details of the currently selected item, automatically updating its contents when the item changes or when people select a new item. In contrast, if you need to present an *Info* window — which always...
- **Prefer simple adjustment controls in a panel.**
  As much as possible, avoid including controls that require typing text or selecting items to act upon because these actions can require multiple steps. Instead, consider using controls like sliders and steppers because these components...
- **Write a brief title that describes the panel’s purpose.**
  Because a panel often floats above other open windows in your app, it needs a title bar so people can position it where they want. Create a short title using a noun — or a noun phrase with [title-style...
- **Show and hide panels appropriately.**
  When your app becomes active, bring all of its open panels to the front, regardless of which window was active when the panel opened. When your app is inactive, hide all of its panels.
- **Avoid including panels in the Window menu’s documents list.**
  It’s fine to include commands for showing or hiding panels in the [Window menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#Window-menu), but panels aren’t documents or standard app windows, and they don’t...
- **In general, avoid making a panel’s minimize button available.**
  People don’t usually need to minimize a panel, because it displays only when needed and disappears when the app is inactive.
- **Refer to panels by title in your interface and in help documentation.**
  In menus, use the panel’s title without including the term *panel*: for example, “Show Fonts,” “Show Colors,” and “Show Inspector.” In help documentation, it can be confusing to introduce “panel” as a different type of window, so it’s...
- **Prefer standard panels.**
  People can be distracted or confused by a HUD when there’s no logical reason for its presence. Also, a HUD might not match the current appearance setting. In general, use a HUD only:
- **Maintain one panel style when your app switches modes.**
  For example, if you use a HUD when your app is in full-screen mode, prefer maintaining the HUD style when people take your app out of full-screen mode.
- **Use color sparingly in HUDs.**
  Too much color in the dark appearance of a HUD can be distracting. Often, you need only small amounts of high-contrast color to highlight important information in a HUD.
- **Keep HUDs small.**
  HUDs are designed to be unobtrusively useful, so letting them grow too large defeats their primary purpose. Don’t let a HUD obscure the content it adjusts, and make sure it doesn’t compete with the content for people’s attention.

## Path controls
<sub>`pages/path-controls.md`</sub>

- **Use a path control in the window body, not the window frame.**
  Path controls aren’t intended for use in toolbars or status bars. Note that the path control in the Finder appears at the bottom of the window body, not in the status bar.

## Photo editing
<sub>`pages/photo-editing.md`</sub>

- **Confirm cancellation of edits.**
  Editing a photo or video can be time consuming. If someone taps the Cancel button, don’t immediately discard their changes. Ask them to confirm that they really want to cancel, and inform them that any edits will be lost after...
- **Don’t provide a custom top toolbar.**
  Your extension loads within a modal view that already includes a toolbar. Providing a second toolbar is confusing and takes space away from the content being edited.
- **Let people preview edits.**
  It’s hard to approve an edit if you can’t see what it looks like. Let people see the result of their work before closing your extension and returning to the Photos app.
- **Use your app icon for your photo editing extension icon.**
  This instills confidence that the extension is in fact provided by your app.

## Pickers
<sub>`pages/pickers.md`</sub>

- **Consider using a picker to offer medium-to-long lists of items.**
  If you need to display a fairly short list of choices, consider using a [Pull-down buttons](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons) instead of a picker. Although a picker makes it easy to scroll...
- **Use predictable and logically ordered values.**
  Before people interact with a picker, many of its values can be hidden. It’s best when people can predict what the hidden values are, such as with an alphabetized list of countries, so they can move through the items quickly.
- **Avoid switching views to show a picker.**
  A picker works well when displayed in context, below or in proximity to the field people are editing. A picker typically appears at the bottom of a window or in a popover.
- **Consider providing less granularity when specifying minutes in a date picker.**
  By default, a minute list includes 60 values (0 to 59). You can optionally increase the minute interval as long as it divides evenly into 60. For example, you might want quarter-hour intervals (0, 15, 30, and 45).
- **Use a compact date picker when space is constrained.** `[iOS, iPadOS]`
  The compact style displays a button that shows the current value in your app’s accent color. When people tap the button, the date picker opens a modal view, providing access to a familiar calendar-style editor and time picker. Within...
- **Choose a date picker style that suits your app.** `[macOS]`
  There are two styles of date pickers in macOS: textual and graphical. The textual style is useful when you’re working with limited space and you expect people to make specific date and time selections. The graphical style is useful when...

## Playing audio
<sub>`pages/playing-audio.md`</sub>

- **Adjust levels automatically when necessary — don’t adjust the overall volume.**
  Your app can adjust relative, independent volume levels to achieve a great mix of audio, but the system volume always governs the final output.
- **Permit rerouting of audio when possible.**
  People often want to select a different audio output device. For example, they may want to listen to music through their living room stereo, car radio, or Apple TV. Support this capability unless there’s a compelling reason not to.
- **Use the system-provided volume view to let people make audio adjustments.**
  The volume view includes a volume-level slider and a control for rerouting audio output. You can customize the appearance of the slider. For developer guidance, see...
- **Choose an audio category that fits the way your app or game uses sound.**
  Depending on the audio category you choose, your app’s sounds can mix with other audio, play while your app is in the background, or stop when people set the Ring/Silent switch to silent. As much as possible, pick a category that helps...
- **Respond to audio controls only when it makes sense.**
  People can control audio playback from outside your app’s interface — such as in Control Center or with controls on their headphones — regardless of whether your app is in the foreground or background. If your app is actively playing...
- **Avoid repurposing audio controls.**
  People expect audio controls to behave consistently in all apps, so it’s essential to avoid redefining the meaning of an audio control in your app. If your app doesn’t support certain controls, don’t respond to them.
- **Consider creating custom audio player controls only if you need to offer commands that the system doesn’t support.**
  For example, you might want to define custom increments for skipping forward or backward, or present content that’s related to the playing audio, such as a sports score.
- **Let other apps know when your app finishes playing temporary audio.**
  If your app can temporarily interrupt the audio of other apps, be sure to flag your audio session in a way that lets other apps know when they can resume. For developer guidance, see...
- **Determine how to respond to audio-session interruptions.**
  For example, if your app supports recording or other audio-related tasks that people don’t want interrupted, you can tell the system to avoid interrupting the currently playing audio for an incoming call unless people choose to accept...
- **When an interruption ends, determine whether to resume audio playback automatically.**
  Sometimes, audio from a different app can interrupt the audio your app is playing. An interruption can be *resumable*, like an incoming phone call, or *nonresumable*, like when people start a new music playlist. Use the interruption...
- **Use the system’s sound services to play short sounds and vibrations.** `[iOS, iPadOS]`
  For developer guidance, see [Audio Services](https://developer.apple.com/documentation/audiotoolbox/audio-services).
- **Prefer playing sound.** `[visionOS]`
  People generally choose to keep sounds audible while they’re wearing the device, so an app that doesn’t play sound — especially in an immersive moment — can feel lifeless and may even seem broken. Throughout the design process, look for...
- **Design custom sounds for custom UI elements.** `[visionOS]`
  In general, a system-provided element plays sound to help people locate it and receive feedback when they interact with it. To help people interact with your custom elements, design sounds that provide feedback and enhance the spatial...
- **Use Spatial Audio to create an intuitive, engaging experience.** `[visionOS]`
  Because people can perceive Spatial Audio as coming from anywhere around them, it works especially well in a fully immersive context as a way to help an experience feel lifelike. *Ambient audio* provides pervasive sounds that can help...
- **Consider defining a range of places from which your app sounds can originate.** `[visionOS]`
  Spatial Audio helps people locate the object that’s making sound, whether it’s stationary or moving in space. For example, when people move an app window that’s playing audio, the sound continues to come directly from the window,...
- **Consider varying sounds that people could perceive as repetitive over time.** `[visionOS]`
  For example, the system subtly varies the pitch and volume of the virtual keyboard’s sounds, suggesting the different sounds a physical keyboard can make as people naturally vary the speed and forcefulness of their typing. An efficient...
- **Decide whether you need to play sound that’s fixed to the wearer or tracked by the wearer.** `[visionOS]`
  People perceive *fixed* sound as if it’s pointed at them, regardless of the direction they look or the virtual objects they move. In contrast, people tend to perceive *tracked* sound as coming from a particular object, so moving the...
- **Use the recommended encoding values for media assets.** `[watchOS]`
  Specifically, use the 64 kbps HE-AAC (High-Efficiency Advanced Audio Coding) format to produce good-quality audio with lower data requirements.

## Playing haptics
<sub>`pages/playing-haptics.md`</sub>

- **Use system-provided haptic patterns according to their documented meanings.**
  People recognize standard haptics because the system plays them consistently on interactions with standard controls. If the documented use case for a pattern doesn’t make sense in your app or game, avoid using the pattern to mean...
- **Use haptics consistently throughout your app or game.**
  It’s important to build a clear, causal relationship between each haptic and the action that causes it so people learn to associate certain haptic patterns with certain experiences. If a haptic doesn’t reinforce a cause-and-effect...
- **Prefer using haptics to complement other feedback in your app or game.**
  When visual, auditory, and tactile feedback are in harmony — as they generally are in the physical world — the user experience is more coherent and can seem more natural. For example, you generally want to match the intensity and...
- **Avoid overusing haptics.**
  Sometimes a haptic can feel just right when it happens occasionally, but become tiresome when it plays frequently. Doing user testing can help you discover a balance that most people appreciate. Often, the best haptic experience is one...
- **In most apps, prefer playing short haptics that complement discrete events.**
  Although long-running haptics that accompany a gameplay flow can enhance the experience, long-running haptics in an app can dilute the meaning of the feedback and distract people from their task. On Apple Pencil Pro, for example,...
- **Make haptics optional.**
  Let people turn off or mute haptics, and make sure people can still enjoy your app or game without them.
- **Be aware that playing haptics might impact other user experiences.**
  By design, haptics produce enough physical force for people to feel the vibration. Ensure that haptic vibrations don’t disrupt experiences involving device features like the camera, gyroscope, or microphone.
- **Notification** `[watchOS]`
- **Notification.** `[watchOS]`
  Tells the person that something significant or out of the ordinary has happened and requires their attention. The system plays this same haptic when a local or remote notification arrives.

## Playing video
<sub>`pages/playing-video.md`</sub>

- **Use the system video player to give people a familiar and convenient experience.**
  The built-in video player provides an exceptional video playback experience that offers consistent interactions and behaviors that let people concentrate on enjoying immersive content. If your app truly requires a custom video player,...
- **Always display video content at its original aspect ratio.**
  When video content uses embedded letterbox or pillarbox padding to conform to a specific aspect ratio, the system may be unable to correctly scale the video based on the current playback mode. Padding embedded within the video frame can...
- **Result of padding a 4:3 video**
- **Result of padding a 21:9 video**
- **Provide additional information when it adds value.**
  In iOS, iPadOS, tvOS, and visionOS, you can customize a video’s additional information by providing an image, title, description, and other useful information. In general, restrict this content so that it doesn’t obscure media playback....
- **Support the interactions people expect, regardless of the input device they’re using to control playback.**
  For example, people expect to press Space on a connected keyboard to play or pause media playback on Apple Vision Pro, Mac, iPhone, iPad, and Apple TV. Similarly, people expect to move through their media on Apple TV by making familiar,...
- **If people need to access playback options or content-specific information in your tvOS app, consider adding a transport control or a custom content tab.**
  People typically open a transport control or content tab while they’re watching a video, so it’s essential to provide only the most useful actions and information. Help people return quickly to the viewing experience by making sure your...
- **Avoid allowing audio from different sources to mix as viewers switch between modes.**
  Mixed audio is an unpleasant and frustrating user experience. In general, audio mixes when at least one of the audio sources fails to handle secondary audio correctly. Here is a typical scenario: While watching a full-screen video, the...
- **Ensure a smooth transition to your app.**
  The TV app fades to black when transitioning to your app and doesn’t show your app’s launch screen. Maintain visual continuity with this transition by immediately presenting your own black screen before starting to play or resume content.
- **Show the expected content immediately.**
  People expect the content they choose to begin playing as soon as the transition to your app completes, especially when resuming playback. Jump right from your app’s black screen into content, and avoid displaying splash screens, detail...
- **Avoid asking people if they want to resume playback.**
  If playback can be resumed, do so automatically without prompting for confirmation.
- **Play or pause playback when people press Space on a connected Bluetooth keyboard.**
  Pressing Space to control media playback is an interaction people expect, regardless of the keyboard they’re using.
- **Make sure content plays for the correct viewer.**
  If your app supports multiple user profiles, the TV app can specify a profile when issuing a playback request. Make your app automatically switch to this profile before starting playback. If a playback request doesn’t specify a profile,...
- **Use the previous end time when resuming playback of a long video clip.**
  Resuming playback at the previous stopping point lets people quickly continue where they left off.
- **Avoid displaying loading screens when possible.**
  A loading screen is unnecessary if your content loads quickly, but if loading takes more than two seconds, consider showing a black loading screen with a centered activity spinner and no surrounding content.
- **Start playback immediately.**
  If you must display a loading screen, display it only until enough content loads for playback to begin. Continue loading remaining content in the background.
- **Minimize loading screen content.**
  If you include branding or images on your loading screen, do so minimally while maintaining the black background that helps provide a seamless transition to playback.
- **Show a contextually relevant screen.**
  When exiting playback, display a detail view for the content the viewer was just watching and include an option to resume playback. If a detail view isn’t available, show either a menu that lists this content or your app’s main menu.
- **Be prepared for an immediate exit.**
  Prepare an exit view as soon as possible after receiving a playback notification so you’re ready to display the view if people exit immediately after playback begins.
- **Defer to content when displaying logos or noninteractive overlays above video.** `[tvOS]`
  A small, unobtrusive logo or countdown timer may be appropriate for your video, but avoid large, distracting overlays that don’t enhance the viewing experience. Also, be aware that some devices are prone to image retention, so it’s...
- **Show interactive overlays gracefully.** `[tvOS]`
  Some videos display interactive overlays, such as quizzes, surveys, and progress check-ins. For the best user experience, implement a minimum delay of 0.5 seconds to pause playing media, and display an interactive overlay. Give people a...
- **Help people stay comfortable when playing video in your app.** `[visionOS]`
  Often, an app doesn’t control the content in the videos it plays, but you can help people stay comfortable by:
- **In a fully immersive experience, avoid letting virtual content obscure playback or transport controls.** `[visionOS]`
  In a fully immersive context, the system automatically places the video player at a predictable location that provides an optimal viewing experience. Use this location to help make sure that no virtual content occludes the default...
- **Avoid automatically starting a fully immersive video playback experience.** `[visionOS]`
  People need control over their experience and they’re unlikely to appreciate being launched into a fully immersive video without warning.
- **Create a thumbnail track if you want to support scrubbing.** `[visionOS]`
  The system displays thumbnails as people scrub to different times in the video, helping them choose the section they want. To improve performance, supply a set of thumbnails that each measure 160 px in width. For developer guidance, see...
- **Avoid expanding an inline video player to fill a window.** `[visionOS]`
  When you display the system-provided player view in a window, playback controls appear in the same plane as the player view and not in an ornament that floats above the window. Inline video needs to be 2D and you want to make sure that...
- **Use a RealityKit video player if you need to play video in a view like a splash screen or a transitional view.** `[visionOS]`
  In situations like these, people generally expect the video to lead into the next experience, so they don’t need playback controls or system-provided integration, like dimming and view anchoring. The RealityKit video player...
- **Keep video clips short.** `[watchOS]`
  Prefer shorter clips of no longer than 30 seconds. Long clips consume more disk space and require people to keep their wrists raised for longer periods of time, which can cause fatigue.
- **Use the recommended sizes and encoding values for media assets.** `[watchOS]`
  In particular, avoid scaling video clips, which affects performance and results in a suboptimal appearance. The following table lists the recommended encoding and resolution values for video assets. The audio encoding values apply to...
- **Avoid creating a poster image that looks like a system control.** `[watchOS]`
  You want people to understand that they can tap a movie element for playback; you don’t want to confuse people by making movie elements look like something else.
- **Consider creating a poster image that represents a video clip’s contents.** `[watchOS]`
  When people tap a poster image, the system replaces the image with the video and begins inline playback. A relevant poster image can help people make an informed decision about whether to view the video. In general, avoid creating a...

## Pointing devices
<sub>`pages/pointing-devices.md`</sub>

- **Be consistent when responding to mouse and trackpad gestures.**
  People expect most gestures to work the same throughout the system, regardless of the app or game they’re using. On a Mac, for example, people rely on the “Swipe between pages” gesture to behave the same way whether they’re browsing...
- **Avoid redefining systemwide trackpad gestures.**
  Even in a game that uses app-specific gestures in a custom way, people expect systemwide gestures to be available; for example, people expect to make familiar gestures to reveal the Dock or Mission Control in macOS. Remember that Mac...
- **Provide a consistent experience in your app, whether people are using gestures, eyes, a pointing device, or a keyboard.**
  People expect to move fluidly between multiple types of input, and they don’t want to learn different interactions for each mode or for each app they use.
- **Let people use the pointer to reveal and hide controls that automatically minimize or fade out.**
  In iPadOS, for example, people can reveal the minimized Safari toolbar by holding the pointer over it (the toolbar minimizes again when the pointer moves away). People can also move the pointer to reveal or hide playback controls while...
- **Provide a consistent experience when people press and hold a modifier key while interacting with objects in your app.**
  For example, if people can duplicate an object by pressing and holding the Option key while they drag that object, ensure the result is the same whether they drag using touch or the pointer.
- **Allow multiple selection in custom views when necessary.** `[iPadOS]`
  In iPadOS 15 and later, people can click and drag the pointer over multiple items to select them. As people use the pointer in this way, it expands into a visible rectangle that selects the items it encompasses. Standard nonlist...
- **Distinguish between pointer and finger input only if it provides value.** `[iPadOS]`
  For example, a scrubber can give people an additional way to target a location in a video when they’re using the pointer. In this scenario, people can drag the playhead using either the pointer or touch, but they can use the pointer to...
- **Use clear, simple images to create custom accessories.** `[iPadOS]`
  A pointer accessory is small, so it’s essential to create an image that communicates the pointer interaction without using too many details.
- **Consider using the accessory transition to signal a change in an element’s state or behavior.** `[iPadOS]`
  In addition to animating the appearance and disappearance of pointer accessories, the system also animates the transitions among accessory shapes and positions that can accompany content effects. For example, you could communicate that...
- **When possible, support the system-provided content effects.** `[iPadOS]`
  People quickly become accustomed to the content effects they see throughout the system and generally expect their experience to apply to every app they use. To provide a consistent user experience, align your interactions with the...
- **Prefer the system-provided pointer appearances for standard buttons and text-entry areas.** `[iPadOS]`
  You can help people feel more comfortable with your app when the pointer behaves in ways they expect.
- **Add padding around interactive elements to create comfortable hit regions.** `[iPadOS]`
  You might need to experiment to determine the right size for an element’s hit region. If the hit region is too small, it can make people feel that they have to be extra precise when interacting with the element. On the other hand, when...
- **Create contiguous hit regions for custom bar buttons.** `[iPadOS]`
  If there’s space between the hit regions of adjacent buttons in a bar, people may experience a distracting motion when the pointer reverts briefly to its default shape as it moves between buttons.
- **Specify the corner radius of a nonstandard element that receives the lift effect.** `[iPadOS]`
  With the system-provided lift effect, the pointer transforms to match the element’s shape as it fades out. By default, the pointer uses the system-defined corner radius to transform into a rounded rectangle. If your element is a...
- **Prefer system-provided pointer effects for custom elements that behave like standard elements.** `[iPadOS]`
  When a custom element behaves like a standard one, people generally expect to interact with it using familiar pointer interactions. For example, if buttons in a custom toolbar don’t use the standard highlight effect, people might think...
- **Use pointer effects in consistent ways throughout your app.** `[iPadOS]`
  For example, if your app helps people draw, provide a similar pointer experience for every drawing area in your app so that people can apply the knowledge they gain in one area to the others.
- **Avoid creating gratuitous pointer and content effects.** `[iPadOS]`
  People notice when the appearance of the pointer or the UI element beneath it changes, and they expect the changes to be useful. Creating a purely decorative pointer effect can distract and even irritate people without providing any...
- **Keep custom pointer shapes simple.** `[iPadOS]`
  Ideally, the pointer’s shape signals the action people can take in the current context without drawing too much attention to itself. If people don’t instantly understand your custom pointer shape, they’re likely to waste time trying to...
- **Consider enhancing the pointer experience by displaying custom annotations that provide useful information.** `[iPadOS]`
  For example, you could display X and Y values when people hold the pointer over a graphing area in your app. Keynote uses annotations to display the current width and height of a resizable image.
- **Avoid displaying instructional text with a pointer.** `[iPadOS]`
  A pointer that displays instructional text can make an app seem complicated and difficult to use. Instead of providing instructions, prioritize clarity and simplicity in your interface, so that people can quickly grasp how to use your...
- **Consider the interplay of shadow, scale, and element spacing when defining custom hover effects.** `[iPadOS]`
  In general, reserve scaling for elements that can increase in size without crowding nearby elements. For example, scaling doesn’t work well for a table row because a row can’t expand without overlapping adjacent rows. For an element...

## Pop-up buttons
<sub>`pages/pop-up-buttons.md`</sub>

- **Use a pop-up button to present a flat list of mutually exclusive options or states.**
  A pop-up button helps people make a choice that affects their content or the surrounding view. Use a [pull-down button](https://developer.apple.com/design/human-interface-guidelines/pull-down-buttons) instead if you need to:
- **Provide a useful default selection.**
  A pop-up button can update its content to identify the current selection, but if people haven’t made a selection yet, it shows the default item you specify. When possible, make the default selection an item that most people are likely...
- **Give people a way to predict a pop-up button’s options without opening it.**
  For example, you can use an introductory label or a button label that describes the button’s effect, giving context to the options.
- **Consider using a pop-up button when space is limited and you don’t need to display all options all the time.**
  Pop-up buttons are a space-efficient way to present a wide array of choices.
- **If necessary, include a Custom option in a pop-up button’s menu to provide additional items that are useful in some situations.**
  Offering a Custom option can help you avoid cluttering the interface with items or controls that people need only occasionally. You can also display explanatory text below the list to help people understand how the options work.
- **Within a popover or modal view, consider using a pop-up button instead of a disclosure indicator to present multiple options for a list item.** `[iPadOS]`
  For example, people can quickly choose an option from the pop-up button’s menu without navigating to a detail view. Consider using a pop-up button in this scenario when you have a fairly small, well-defined set of options that work well...

## Popovers
<sub>`pages/popovers.md`</sub>

- **Use a popover to expose a small amount of information or functionality.**
  Because a popover disappears after people interact with it, limit the amount of functionality in the popover to a few related tasks. For example, a calendar event popover makes it easy for people to change the date or time of an event,...
- **Consider using popovers when you want more room for content.**
  Views like sidebars and panels take up a lot of space. If you need content only temporarily, displaying it in a popover can help streamline your interface.
- **Position popovers appropriately.**
  Make sure a popover’s arrow points as directly as possible to the element that revealed it. Ideally, a popover doesn’t cover the element that revealed it or any essential content people may need to see while using it.
- **Use a Close button for confirmation and guidance only.**
  A Close button, including Cancel or Done, is worth including if it provides clarity, like exiting with or without saving changes. Otherwise, a popover generally closes when people click or tap outside its bounds or select an item in the...
- **Always save work when automatically closing a nonmodal popover.**
  People can unintentionally dismiss a nonmodal popover by clicking or tapping outside its bounds. Discard people’s work only when they click or tap an explicit Cancel button.
- **Show one popover at a time.**
  Displaying multiple popovers clutters the interface and causes confusion. Never show a cascade or hierarchy of popovers, in which one emerges from another. If you need to show a new popover, close the open one first.
- **Don’t show another view over a popover.**
  Make sure nothing displays on top of a popover, except for an alert.
- **When possible, let people close one popover and open another with a single click or tap.**
  Avoiding extra gestures is especially desirable when several different bar buttons each open a popover.
- **Avoid making a popover too big.**
  Make a popover only big enough to display its contents and point to the place it came from. If necessary, the system can adjust the size of a popover to ensure it fits well in the interface.
- **Provide a smooth transition when changing the size of a popover.**
  Some popovers provide both condensed and expanded views of the same information. If you adjust the size of a popover, animate the change to avoid giving the impression that a new popover replaced the old one.
- **Avoid using the word *popover* in help documentation.**
  Instead, refer to a specific task or selection. For example, instead of “Select the Show button at the bottom of the popover,” you might write “Select the Show button.”
- **Avoid using a popover to show a warning.**
  People can miss a popover or accidentally close it. If you need to warn people, use an [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) instead.
- **Avoid displaying popovers in compact views.** `[iOS, iPadOS]`
  Make your app or game dynamically adjust its layout based on the size class of the content area. Reserve popovers for wide views; for compact views, use all available screen space by presenting information in a full-screen modal view...
- **Attached popover** `[macOS]`
- **Detached popover** `[macOS]`
- **Consider letting people detach a popover.** `[macOS]`
  People might appreciate being able to convert a popover into a panel if they want to view other information while the popover remains visible.
- **Make minimal appearance changes to a detached popover.** `[macOS]`
  A panel that looks similar to the original popover helps people maintain context.

## Printing
<sub>`pages/printing.md`</sub>

- **Make printing discoverable.**
  Help people find your print action by placing it in standard system locations. For example, include a Print item in your macOS app’s File menu; in your iOS or iPadOS app, add a toolbar button that opens an [action...
- **Present a printing option only when it’s possible.**
  If there’s nothing onscreen to print, or no printers are available, dim the Print item in a macOS app’s File menu and remove the Print action from the Action sheet in an iOS or iPadOS app. If you implement a custom print button, dim or...
- **Present relevant printing options.**
  If it makes sense to offer options like selecting a page range, requesting multiple copies, or printing on both sides — and the printer supports the options — use the system-provided view to present them.
- **If your macOS app offers app-specific print options that the system doesn’t offer, consider creating a custom category for the print panel.** `[macOS]`
  By default, the print panel offers several categories of settings, such as Layout, Paper Handling, and Media & Quality. Give your custom category a unique name, such as your app name, and include options that help people have a great...
- **If your app supports document-specific page settings, consider presenting a page setup dialog.** `[macOS]`
  A *page setup dialog* includes rarely changed settings for page size, orientation, and scaling that apply to printing a particular document. If this makes sense in your app, avoid implementing features the system already provides. For...
- **Make sure interdependencies between options are clear.** `[macOS]`
  For example, if double-sided printing is available, an option to print on transparencies becomes unavailable.
- **Separate advanced features from frequently used features.** `[macOS]`
  Consider using a disclosure control to hide advanced options until they’re needed. Label advanced options as *Advanced Options*.
- **Consider letting people preview the effect of a setting.** `[macOS]`
  For example, you could update a thumbnail image to show the effect of changing a tone control.
- **Consider storing modified settings with the document.** `[macOS]`
  At minimum, it makes sense to store print settings until the document is closed in case people want to print it again.

## Privacy
<sub>`pages/privacy.md`</sub>

- **Request access only to data that you actually need.**
  Asking for more data than a feature needs — or asking for data before a person shows interest in the feature — can make it hard for people to trust your app. Give people precise control over their data by making your permission requests...
- **Be transparent about how your app collects and uses people’s data.**
  People are less likely to be comfortable sharing data with your app if they don’t understand exactly how you plan to use it. Always respect people’s choices to use system features like Hide My Email and Mail Privacy Protection, and be...
- **Process data on the device where possible.**
  In iOS, for example, you can take advantage of the Apple Neural Engine and custom CreateML models to process the data right on the device, helping you avoid lengthy and potentially risky round trips to a remote server.
- **Adopt system-defined privacy protections and follow security best practices.**
  For example, in iOS 15 and later, you can rely on CloudKit to provide encryption and key management for additional data types, like strings, numbers, and dates.
- **Request permission only when your app clearly needs access to the data or resource.**
  It’s natural for people to be suspicious of a request for personal information or access to a device capability, especially if there’s no obvious need for it. Ideally, wait to request permission until people actually use an app feature...
- **Avoid requesting permission at launch unless the data or resource is required for your app to function.**
  People are less likely to be bothered by a launch-time request when it’s obvious why you’re making it. For example, people understand that a navigation app needs access to their location before they can benefit from it. Similarly,...
- **Write copy that clearly describes how your app uses the ability, data, or resource you’re requesting.**
  The standard alert displays your copy (called a *purpose string* or *usage description string*) after your app name and before the buttons people use to grant or deny their permission. Aim for a brief, complete sentence that’s...
- **Include only one button and make it clear that it opens the system alert.**
  People can feel manipulated when a custom screen or window also includes a button that doesn’t open the alert because the experience diverts them from making their choice. Another type of manipulation is using a term like “Allow” to...
- **Don’t include additional actions in your custom screen or window.**
  For example, don’t provide a way for people to leave the screen or window without viewing the system alert — like offering an option to close or cancel.
- **Never precede the system-provided alert with a custom screen or window that could confuse or mislead people.**
  People sometimes tap quickly to dismiss alerts without reading them. A custom messaging screen, window, or view that takes advantage of such behaviors to influence choices will lead to rejection by App Store review.
- **Imitation request**
- **Alert annotation**
- **Consider using the location button to give people a lightweight way to share their location for specific app features.**
  For example, your app might help people attach their location to a message or post, find a store, or identify a building, plant, or animal they’ve encountered in their location. If you know that people often grant your app *Allow Once*...
- **Consider customizing the location button to harmonize with your UI.**
  Specifically, you can:
- **Avoid relying solely on passwords for authentication.**
  Where possible, use [passkeys](https://developer.apple.com/documentation/authenticationservices/public-private_key_authentication/supporting_passkeys/) to replace passwords. If you need to continue using passwords for authentication,...
- **Store sensitive information in a keychain.**
  A keychain provides a secure, predictable user experience when handling someone’s private information. For developer guidance, see [Keychain services](https://developer.apple.com/documentation/security/keychain-services).
- **Never store passwords or other secure content in plain-text files.**
  Even if you restrict access using file permissions, sensitive information is much safer in an encrypted keychain.
- **Avoid inventing custom authentication schemes.**
  If your app requires authentication, prefer system-provided features like [passkeys](https://developer.apple.com/documentation/authenticationservices/public-private_key_authentication/supporting_passkeys/), [Sign in with...
- **Sign your app with a valid Developer ID.** `[macOS]`
  If you choose to distribute your app outside the store, signing your app with Developer ID identifies you as an Apple developer and confirms that your app is safe to use. For developer guidance, see [Xcode...
- **Protect people’s data with app sandboxing.** `[macOS]`
  Sandboxing provides your app with access to system resources and user data while protecting it from malware. All apps submitted to the Mac App Store require sandboxing. For developer guidance, see [Configuring the macOS App...
- **Avoid making assumptions about who is signed in.** `[macOS]`
  Because of fast user switching, multiple people may be active on the same system.

## Progress indicators
<sub>`pages/progress-indicators.md`</sub>

- **When possible, use a determinate progress indicator.**
  An indeterminate progress indicator shows that a process is occurring, but it doesn’t help people estimate how long a task will take. A determinate progress indicator can help people decide whether to do something else while waiting for...
- **Be as accurate as possible when reporting advancement in a determinate progress indicator.**
  Consider evening out the pace of advancement to help people feel confident about the time needed for the task to complete. Showing 90 percent completion in five seconds and the last 10 percent in 5 minutes can make people wonder if your...
- **Keep progress indicators moving so people know something is continuing to happen.**
  People tend to associate a stationary indicator with a stalled process or a frozen app. If a process stalls for some reason, provide feedback that helps people understand the problem and what they can do about it.
- **When possible, switch a progress bar from indeterminate to determinate.**
  If an indeterminate process reaches a point where you can determine its duration, switch to a determinate progress bar. People generally prefer a determinate progress indicator, because it helps them gauge what’s happening and how long...
- **Don’t switch from the circular style to the bar style.**
  Activity indicators (also called *spinners*) and progress bars are different shapes and sizes, so transitioning between them can disrupt your interface and confuse people.
- **If it’s helpful, display a description that provides additional context for the task.**
  Be accurate and succinct. Avoid vague terms like *loading* or *authenticating* because they seldom add value.
- **Display a progress indicator in a consistent location.**
  Choosing a consistent location for a progress indicator helps people reliably find the status of an operation across platforms or within or between apps.
- **When it’s feasible, let people halt processing.**
  If people can interrupt a process without causing negative side effects, include a Cancel button. If interrupting the process might cause negative side effects — such as losing the downloaded portion of a file — it can be useful to...
- **Let people know when halting a process has a negative consequence.**
  When canceling a process results in lost progress, it’s helpful to provide an [alert](https://developer.apple.com/design/human-interface-guidelines/alerts) that includes an option to confirm the cancellation or resume the process.
- **Perform automatic content updates.** `[iOS, iPadOS]`
  Although people appreciate being able to do an immediate content refresh, they also expect automatic refreshes to occur periodically. Don’t make people responsible for initiating every update. Keep data fresh by updating it regularly.
- **Supply a short title only if it adds value.** `[iOS, iPadOS]`
  Optionally, a refresh control can include a title. In most cases, this is unnecessary, as the animation of the control indicates that content is loading. If you do include a title, don’t use it to explain how to perform a refresh....
- **Prefer an activity indicator (spinner) to communicate the status of a background operation or when space is constrained.** `[macOS]`
  Spinners are small and unobtrusive, so they’re useful for asynchronous background tasks, like retrieving messages from a server. Spinners are also good for communicating progress within a small area, such as within a text field or next...
- **Avoid labeling a spinning progress indicator.** `[macOS]`
  Because a spinner typically appears when people initiate a process, a label is usually unnecessary.

## Pull-down buttons
<sub>`pages/pull-down-buttons.md`</sub>

- **Use a pull-down button to present commands or items that are directly related to the button’s action.**
  The menu lets you help people clarify the button’s target or customize its behavior without requiring additional buttons in your interface. For example:
- **Avoid putting all of a view’s actions in one pull-down button.**
  A view’s primary actions need to be easily discoverable, so you don’t want to hide them in a pull-down button that people have to open before they can do anything.
- **Balance menu length with ease of use.**
  Because people have to interact with a pull-down button before they can view its menu, listing a minimum of three items can help the interaction feel worthwhile. If you need to list only one or two items, consider using alternative...
- **Display a succinct menu title only if it adds meaning.**
  In general, a pull-down button’s content — combined with descriptive menu items — provides all the context people need, making a menu title unnecessary.
- **Let people know when a pull-down button’s menu item is destructive, and ask them to confirm their intent.**
  Menus use red text to highlight actions that you identify as potentially destructive. When people choose a destructive action, the system displays an [Action...
- **Include an interface icon with a menu item when it provides value.**
  If you need to clarify an item’s meaning, you can display an [Icons](https://developer.apple.com/design/human-interface-guidelines/icons) or image after its label. Using [SF...
- **Consider using a More pull-down button to present items that don’t need prominent positions in the main interface.** `[iOS, iPadOS]`
  A More button can help you offer a range of items where space is constrained, but it can also hinder discoverability. Although people generally understand that a More button offers additional functionality related to the current...

## Rating indicators
<sub>`pages/rating-indicators.md`</sub>

- **Make it easy to change rankings.**
  When presenting a list of ranked items, let people adjust the rank of individual items inline without navigating to a separate editing screen.
- **If you replace the star with a custom symbol, make sure that its purpose is clear.**
  The star is a very recognizable ranking symbol, and people may not associate other symbols with a rating scale.

## Ratings and reviews
<sub>`pages/ratings-and-reviews.md`</sub>

- **Ask for a rating only after people have demonstrated engagement with your app or game.**
  For example, you might prompt people when they complete a game level or a significant task. Avoid asking for a rating on first launch or during onboarding, because people haven’t had enough time to gain a clear understanding of your...
- **Avoid interrupting people while they’re performing a task or playing a game.**
  Asking for feedback can disrupt the user experience and feel like a burden. Look for natural breaks or stopping points in your app or game where a rating request is less likely to be bothersome.
- **Avoid pestering people.**
  Repeated rating requests can be irritating, and may even negatively influence people’s opinion of your app. Consider allowing at least a week or two between requests, prompting again after people demonstrate additional engagement with...
- **Prefer the system-provided prompt.**
  iOS, iPadOS, and macOS offer a consistent, nonintrusive way for apps and games to request ratings and reviews. When you identify places in your experience where it makes sense to ask for feedback, the system checks for previous feedback...
- **Weigh the benefits of resetting your summary rating against the potential disadvantage of showing fewer ratings.**
  When you release a new version of your app or game, you can reset the summary of individual ratings you received since the last reset. Although resetting means that the ratings reflect the current version, it also tends to result in...

## Remotes
<sub>`pages/remotes.md`</sub>

- **Prefer using standard gestures to perform standard actions.**
  Unless people are actively playing a game, they expect the remote to behave in standard ways in every app they use. Redefining or repurposing standard remote behaviors can cause confusion and add complexity to your experience. For...
- **Be consistent with the tvOS focus experience.**
  The [Focus and selection](https://developer.apple.com/design/human-interface-guidelines/focus-and-selection) forges a strong connection between people and the content they’re viewing. Reinforce this link in your app by ensuring that you...
- **Provide clear feedback that shows people what happens when they make gestures in your app.**
  For example, lightly resting a thumb on the remote shows people where to swipe down so that they can reveal an info area.
- **Define new gestures only when it makes sense in your app.**
  Within gameplay, for example, custom gestures can be a fun part of the experience. In most other situations, people expect to use standard gestures and may not appreciate having to discover or remember new ones.
- **Differentiate between press and tap, and avoid responding to an inadvertent tap.**
  Pressing is an intentional action, and it works well for choosing a button, confirming a selection, and initiating an action during gameplay. Tap gestures are fine for navigation or showing additional information, but keep in mind that...
- **Consider using the position of a tap to aid with navigation or gameplay.**
  The remote can differentiate between up, down, left, and right tap gestures on the touch surface. Respond to positional taps only if it makes sense in the context of your app and if such behavior is intuitive and discoverable.
- **In almost all cases, open the parent of the current screen when people press the Back button.**
  At the top level of an app or game, the parent is the Apple TV Home Screen; within an app, the parent is defined by the app hierarchy, and isn’t necessarily the previous screen. The exception to this standard behavior is when people are...
- **Respond correctly to the Play/Pause button during media playback.**
  When playing music or video, people expect pressing the Play/Pause button to play, pause, or resume playback.
- **If your live-viewing app provides an EPG, respond to a remote’s EPG-browsing buttons in ways people expect.**
  When people press a “guide” or “browse” button, they expect your EPG to open. While they’re viewing your EPG, people expect to navigate through it by pressing a “page up” or “page down” button. Avoid responding to these buttons in other...
- **While your content plays, respond to a compatible remote’s “page up” or “page down” button by changing the channel.**
  People expect these buttons to behave differently when they switch between viewing content and browsing an EPG.

## ResearchKit
<sub>`pages/researchkit.md`</sub>

- **Always display the onboarding screens in the correct order.**
- **Provide an introduction that informs and provides a call to action.**
  Clearly describe the subject and purpose of your study. Also allow existing participants to quickly log in and continue an in-progress study.
- **Determine eligibility as soon as possible.**
  People don’t need to move on to the consent section if they’re not eligible for the study. Only present eligibility requirements that are necessary for your study. Use simple, straightforward language that describes the requirements,...
- **Make sure participants understand your study before you get their consent.**
  ResearchKit helps you make the consent process concise and friendly, while still allowing you to incorporate into the consent any legal requirements or requirements set by an institutional review board or ethics review board. Make sure...
- **Break a long consent form into easily digestible sections.**
  Each section can cover one aspect of the study, such as data gathering, data use, potential benefits, possible risks, time commitment, how to withdraw, and so on. For each section, use simple, straightforward language to provide a...
- **If it makes sense, provide a quiz that tests the participant’s understanding.**
  You might do this for questions the participant would otherwise be asked when obtaining consent in person.
- **Get the participant’s consent and, if appropriate, some contact information.**
  After agreeing to join the study, participants receive a confirmation dialog, followed by screens in which they provide their signature and contact details. Most research apps email participants a PDF version of the consent form for...
- **Get permission to access the participant’s device or data, and to send notifications.**
  Clearly explain why your research app needs access to location, Health, or other data, and don’t request access to data that isn’t critical to your study. If your app requires it, also ask for permission to send notifications to the...
- **Create surveys that keep participants engaged.**
  ResearchKit provides many customizable screens you can use in your surveys, and makes it easy to present questions that require different types of answers, such as true or false, multiple choice, dates and times, sliding scales, and...
- **Make active tasks easy to understand.**
  An active task requires the participant to engage in an activity, such as speaking into the microphone, tapping fingers on the screen, walking, or performing a memory test. Follow these guidelines to encourage participants to perform an...
- **Use a profile to help participants manage personal data related to your study.**
  A profile screen can let people edit data that might change during the course of the study — such as weight or sleep habits — and remind them of upcoming activities. A profile screen can also provide an easy way to leave a study and...
- **Use a dashboard to show progress and motivate participants to continue.**
  If appropriate for your study, use a dashboard to provide encouraging feedback, such as daily progress, weekly assessments, results from specific activities, and even results that compare the participant’s results with aggregated...

## Right to left
<sub>`pages/right-to-left.md`</sub>

- **Adjust text alignment to match the interface direction, if the system doesn’t do so automatically.**
  For example, if you left-align text with content in the left-to-right (LTR) context, right-align the text to match the content’s mirrored position in the RTL context.
- **Align a paragraph based on its language, not on the current context.**
  When the alignment of a paragraph — defined as three or more lines of text — doesn’t match its language, it can be difficult to read. For example, right-aligning a paragraph that consists of LTR text can make the beginning of each line...
- **Use a consistent alignment for all text items in a list.**
  To ensure a comfortable reading and scanning experience, reverse the alignment of all items in a list, including items that are displayed in a different script.
- **Don’t reverse the order of numerals in a specific number.**
  Regardless of the current language or the surrounding content, the digits in a specific number — such as “541,” a phone number, or a credit card number — always appear in the same order.
- **Reverse the order of numerals that show progress or a counting direction; never flip the numerals themselves.**
  Controls like progress bars, sliders, and rating controls often include numerals to clarify their meaning. If you use numerals in this way, be sure to reverse the order of the numerals to match the direction of the flipped control. Also...
- **Flip controls that show progress from one value to another.**
  Because people tend to view forward progress as moving in the same direction as the language they read, it makes sense to flip controls like sliders and progress indicators in the RTL context. When you do this, also be sure to reverse...
- **Flip controls that help people navigate or access items in a fixed order.**
  For example, in the RTL context, a back button must point to the right so the flow of screens matches the reading order of the RTL language. Similarly, next or previous buttons that let people access items in an ordered list need to...
- **Preserve the direction of a control that refers to an actual direction or points to an onscreen area.**
  For example, if you provide a control that means “to the right,” it must always point right, regardless of the current context.
- **Visually balance adjacent Latin and RTL scripts when necessary.**
  In buttons, labels, and titles, Arabic or Hebrew text can appear too small when next to uppercased Latin text, because Arabic and Hebrew don’t include uppercase letters. To visually balance Arabic or Hebrew text with Latin text that...
- **Avoid flipping images like photographs, illustrations, and general artwork.**
  Flipping an image often changes the image’s meaning; flipping a copyrighted image could be a violation. If an image’s content is strongly connected to reading direction, consider creating a new version of the image instead of flipping...
- **Reverse the positions of images when their order is meaningful.**
  For example, if you display multiple images in a specific order like chronological, alphabetical, or favorite, reverse their positions to preserve the order’s meaning in the RTL context.
- **Flip interface icons that represent text or reading direction.**
  For example, if an interface icon uses left-aligned bars to represent text in the LTR context, right-align the bars in the RTL context.
- **Consider creating a localized version of an interface icon that displays text.**
  Some interface icons include letters or words to help communicate a script-related concept, like font-size choice or a signature. If you have a custom interface icon that needs to display actual text, consider creating a localized...
- **Flip an interface icon that shows forward or backward motion.**
  When something moves in the same direction that people read, they typically interpret that direction as forward; when something moves in the opposite direction, people tend to interpret the direction as backward. An interface icon that...
- **Don’t flip logos or universal signs and marks.**
  Displaying a flipped logo confuses people and can have legal repercussions. Always display a logo in its original form, even if it includes text. People expect universal symbols and marks like the checkmark to have a consistent...
- **In general, avoid flipping interface icons that depict real-world objects.**
  Unless you use the object to indicate directionality, it’s best to avoid flipping an icon that represents a familiar item. For example, clocks work the same everywhere, so a traditional clock interface icon needs to look the same...
- **Before merely flipping a complex custom interface icon, consider its individual components and the overall visual balance.**
  In some cases, a component — like a badge, slash, or magnifying glass — needs to adhere to a visual design language regardless of localization. For example, SF Symbols maintains visual consistency by using the same backslash to...

## SF Symbols
<sub>`pages/sf-symbols.md`</sub>

- **Hierarchical**
  — Applies one color to all layers in a symbol, varying the color’s opacity according to each layer’s hierarchical level.
- **Confirm that a symbol’s rendering mode works well in every context.**
  Depending on factors like the size of a symbol and its contrast with the current background color, different rendering modes can affect how well people can discern the symbol’s details. You can use the automatic setting to get a...
- **Use variable color to communicate change — don’t use it to communicate depth.**
  To convey depth and visual hierarchy, use Hierarchical rendering mode to elevate certain layers and distinguish foreground and background elements in a symbol.
- **Variable color**
  — Incrementally varies the opacity of layers within a symbol. This animation can be cumulative or iterative. When cumulative, color changes persist for each layer until the animation cycle is complete. When iterative, color changes...
- **Magic Replace**
  — Performs a smart transition between two symbols with related shapes. For example, slashes can draw on and off, and badges can appear or disappear, or you can replace them independently of the base symbol. Magic Replace is the new...
- **Draw On / Draw Off**
  — In SF Symbols 7 and later, draws the symbol along a path through a set of guide points, either from offscreen to onscreen (Draw On) or from onscreen to offscreen (Draw Off). You can draw all layers at once, stagger them, or draw each...
- **Apply symbol animations judiciously.**
  While there’s no limit to how many animations you can add to a view, too many animations can overwhelm an interface and distract people.
- **Make sure that animations serve a clear purpose in communicating a symbol’s intent.**
  Each type of animation has a discrete movement that communicates a certain type of action or elicits a certain response. Consider how people might interpret an animated symbol and whether the animation, or combination of animations,...
- **Use symbol animations to communicate information more efficiently.**
  Animations provide visual feedback, reinforcing that something happened in your interface. You can use animations to present complex information in a simple way and without taking up a lot of visual space.
- **Consider your app’s tone when adding animations.**
  When animating a symbol, think about what the animation can convey and how that might align with your brand identity and your app’s overall style and tone. For guidance, see...
- **Use the template as a guide.**
  Create a custom symbol that’s consistent with the ones the system provides in level of detail, optical weight, alignment, position, and perspective. Strive to design a symbol that is:
- **Assign negative side margins to your custom symbol if necessary.**
  SF Symbols supports negative side margins to aid optical horizontal alignment when a symbol contains a badge or other elements that increase its width. For example, negative side margins can help you horizontally align a stack of folder...
- **Optimize layers to use animations with custom symbols.**
  If you want to animate your symbol by layer, make sure to annotate the layers in the SF Symbols app. The Z-order determines the order that you want to apply colors to the layers of a variable color symbol, and you can choose whether to...
- **Test animations for custom symbols.**
  It’s important to test your custom symbols with all of the animation presets because the shapes and paths might not appear how you expect when the layers are in motion. To get the most out of this feature, consider drawing your custom...
- **Avoid making custom symbols that include common variants, such as enclosures or badges.**
  The SF Symbols app offers a component library for creating variants of your custom symbol. Using the component library allows you to create commonly used variants of your custom symbol while maintaining design consistency with the...
- **Provide alternative text labels for custom symbols.**
  Alternative text labels — or accessibility descriptions — let VoiceOver describe visible UI and content, making navigation easier for people with visual disabilities. For guidance, see...
- **Don’t design replicas of Apple products.**
  Apple products are copyrighted and you can’t reproduce them in your custom symbols. Also, you can’t customize a symbol that SF Symbols identifies as representing an Apple feature or product.

## Scroll views
<sub>`pages/scroll-views.md`</sub>

- **Support default scrolling gestures and keyboard shortcuts.**
  People are accustomed to the systemwide scrolling behavior and expect it to work everywhere. If you build custom scrolling for a view, make sure your scroll indicators use the elastic behavior that people expect.
- **Make it apparent when content is scrollable.**
  Because scroll indicators aren’t always visible, it can be helpful to make it obvious when content extends beyond the view. For example, displaying partial content at the edge of a view indicates that there’s more content in that...
- **Avoid putting a scroll view inside another scroll view with the same orientation.**
  Nesting scroll views that have the same orientation can create an unpredictable interface that’s difficult to control. It’s alright to place a horizontal scroll view inside a vertical scroll view (or vice versa), however.
- **Consider supporting page-by-page scrolling if it makes sense for your content.**
  In some situations, people appreciate scrolling by a fixed amount of content per interaction instead of scrolling continuously. On most platforms, you can define the size of such a *page* — typically the current height or width of the...
- **In some cases, scroll automatically to help people find their place.**
  Although people initiate almost all scrolling, automatic scrolling can be helpful when relevant content is no longer in view, such as when:
- **If you support zoom, set appropriate maximum and minimum scale values.**
  For example, zooming in on text until a single character fills the screen doesn’t make sense in most situations.
- **Prefer the automatic scroll edge effect style.**
  Where possible, use the default [automatic](https://developer.apple.com/documentation/swiftui/scrolledgeeffectstyle/automatic) style of the scroll edge effect. This style provides a more opaque visual separation for top toolbars that...
- **Only use a scroll edge effect when a scroll view is behind floating interface elements.**
  Scroll edge effects aren’t decorative. They don’t block or darken like overlays; they exist to ensure controls stay visually distinct.
- **Apply one scroll edge effect per view.**
  In split view layouts on iPad and Mac, each pane can have its own scroll edge effect; in this case, keep them consistent in height to maintain alignment.
- **Consider showing a page control when a scroll view is in page-by-page mode.** `[iOS, iPadOS]`
  [Page controls](https://developer.apple.com/design/human-interface-guidelines/page-controls) show how many pages, screens, or other chunks of content are available and indicates which one is currently visible. For example, Weather uses...
- **If necessary, use small or mini scroll bars in a panel.** `[macOS]`
  When space is tight, you can use smaller scroll bars in panels that need to coexist with other windows. Be sure to use the same size for all controls in such a panel.
- **If necessary, account for the size of the scroll indicator.** `[visionOS]`
  Although the indicator’s overall size is small, it’s a little thicker than the same component in iOS. If your content uses tight margins, consider increasing them to prevent the scroll indicator from overlapping the content.
- **Support Look to Scroll for reading or browsing views.** `[visionOS]`
  Because Look to Scroll doesn’t work by default, you need to add support for it to each individual scroll view. If your app contains reading or browsing views, add support for Look to Scroll to provide a comfortable and hands-free...
- **Avoid using Look to Scroll for secondary content.** `[visionOS]`
  In general, support standard gestures — but not Look to Scroll — in views that contain UI controls or dense information that requires quick, precise scrolling. For example, the Notes app offers Look to Scroll within the main view to let...
- **Maintain consistency across content.** `[visionOS]`
  If you support Look to Scroll for one view in your app, make sure to support it for all similar views. For example, if you offer several collection views of videos throughout your app, support Look to Scroll for each of these views so...
- **Define clear scroll areas within your app.** `[visionOS]`
  In views that support Look to Scroll, prefer making the view the full width or full height of the window. This gives people generous space to scroll and provides clear edges. If you inset a scroll view from a window, like in the Notes...
- **If your app uses custom scroll effects or animations, remove them before supporting Look to Scroll.** `[visionOS]`
  Custom effects that use scroll position to change content, such as parallax effects and animations, can cause Look to Scroll to behave unexpectedly.
- **Prefer vertically scrolling content.** `[watchOS]`
  People are accustomed to using the Digital Crown to navigate to and within apps on Apple Watch. If your app contains a single list or content view, rotating the Digital Crown scrolls vertically when your app’s content is taller than the...
- **Use tab views to provide page-by-page scrolling.** `[watchOS]`
  watchOS displays tab views as pages. If you place tab views in a vertical stack, people can rotate the Digital Crown to move vertically through full-screen pages of content. In this scenario, the system displays a page indicator next to...
- **When displaying paged content, consider limiting the content of an individual page to a single screen height.** `[watchOS]`
  Embracing this constraint clarifies the purpose of each page, helping you create a more glanceable design. However, if your app has long pages, people can still use the Digital Crown both to navigate between shorter pages and to scroll...

## Search fields
<sub>`pages/search-fields.md`</sub>

- **Use placeholder text to help people know what they can search for.**
  Placeholder text can be helpful when you need to reinforce the scope of your search or to educate people about the type of content that search has access to.
- **If possible, start search immediately when a person types.**
  Searching while someone types makes the search experience feel more responsive because it provides results that are continuously refined as the text becomes more specific.
- **Consider showing suggested search terms.**
  For example, you can display recent searches before search begins, or predictive search suggestions as a person types. This can help someone search faster, even when the search itself doesn’t begin immediately.
- **Simplify search results.**
  Provide the most relevant search results first to minimize the need for someone to scroll to find what they’re looking for. In addition to prioritizing the most likely results, consider categorizing them to help people find what they want.
- **Consider letting people filter search results.**
  For example, you can include a scope bar in the search results content area to help people quickly and easily filter search results.
- **Use a scope bar to filter among clearly defined search categories.**
  A scope bar can help someone move from a broader scope to a narrower one. For example, in Mail on iPhone, a scope bar helps people move from searching their entire mailbox to just the specific mailbox they’re viewing. For developer...
- **Default to a broader scope and let people refine it as they need.**
  A broader scope provides context for the full set of available results, which helps guide people in a useful direction when they choose to narrow the scope.
- **Use tokens to filter by common search terms or items.**
  When you define a token, the term it represents gains a visual treatment that encapsulates it, indicating that people can select and edit it as a single item. Tokens can clarify a search term, like filtering by a specific contact in...
- **Consider pairing tokens with search suggestions.**
  People may not know which tokens are available, so pairing them with search suggestions can help people learn how to use them.
- **Choose the standard tab style to provide suggestions, promote discovery, and encourage exploration.** `[iOS]`
  This style of search tab creates a dedicated landing page for search, providing an opportunity to reveal any content or suggestions that might be helpful before someone taps the field to begin the search. This approach is great for an...
- **Choose the button appearance to help people quickly find what they need.** `[iOS]`
  When someone interacts with this style of search tab, the keyboard immediately appears with the search field above it, ready to begin the search. This approach provides a more transient experience that brings people directly back to...
- **Place search at the bottom if there’s room.** `[iOS]`
  You can either add a search field to an existing toolbar, or as a new toolbar where search is the only item. Search at the bottom is useful in any situation where search is a priority, since it keeps the search experience easy to reach....
- **Place search at the top when itʼs important to defer to content at the bottom of the screen, or thereʼs no bottom toolbar.** `[iOS]`
  Use search at the top in cases where covering the content might interfere with a primary function of the app. The Wallet app, for example, includes event passes in a stack at the bottom of the screen for easy access and viewing at a glance.
- **Place search as an inline field when its position alongside the content it searches strengthens that relationship.** `[iOS]`
  When you need to filter or search within a single view, it can be helpful to have search appear directly next to content to illustrate that the search applies to it, rather than globally. This pattern is useful if your app has more than...
- **When at the top, position an inline search field above the list it searches, and consider pinning it to the top toolbar when scrolling.** `[iOS]`
  This helps keep it distinct from search that appears in other locations.
- **Put a search field at the trailing side of the toolbar for many common uses.** `[iPadOS, macOS]`
  Many apps benefit from the familiar pattern of search in the toolbar, particularly apps with split views that need to search across multiple columns of information, like Mail, Notes, and Voice Memos. This placement makes great use of...
- **Include search at the top of the sidebar when filtering content or navigation there.** `[iPadOS, macOS]`
  Apps such as Settings take advantage of search to quickly filter the sidebar and expose sections that may be multiple levels deep, providing a simple way for people to search, preview, and navigate to the section or setting they’re...
- **Include search as an item in the sidebar or tab bar when you want an area dedicated to discovery.** `[iPadOS, macOS]`
  If your search is paired with rich suggestions, categories, or content that needs more space, it can be helpful to have a dedicated area for it. This is particularly useful for apps where browsing and search go hand in hand, like Music...
- **In a search field in a dedicated area, consider immediately focusing the field when a person navigates to the area to help them search faster and locate the field more easily.** `[iPadOS, macOS]`
  An exception to this is on iPad when only a virtual keyboard is available, in which case it’s better to leave the field unfocused to prevent the keyboard from unexpectedly covering the view.
- **Account for window resizing with the placement of the search field.** `[iPadOS, macOS]`
  On iPad, the search field fluidly resizes with the app window like it does on Mac. However, for compact views on iPad, itʼs important to ensure that search is available where it’s most contextually useful. For example, Notes and Mail...
- **Provide suggestions to make searching easier.** `[tvOS]`
  People typically don’t want to do a lot of typing in tvOS. To improve the search experience, provide popular and context-specific search suggestions, including recent searches when available. For developer guidance, see [Using suggested...

## Searching
<sub>`pages/searching.md`</sub>

- **If search is important, give it a primary position in your app or view.**
  For example, in the Notes app, a search field is in the bottom [Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars) alongside other important actions. In apps that use [Tab...
- **Aim to make your app’s content searchable through a single location.**
  People appreciate having one clearly identified location they can use to find anything they’re looking for in your app. For apps with clearly distinct sections, it may still be useful to offer a local search. For example, search acts as...
- **Clearly display the current scope of a search.**
  Use a descriptive placeholder text, a [Scope bars and tokens](https://developer.apple.com/design/human-interface-guidelines/search-fields#Scope-bars-and-tokens), or a title to help reinforce what someone is currently searching. For...
- **Provide suggestions to make searching easier.**
  When you display a personʼs recent searches before they start typing or offer predictive search suggestions while they’re typing, you can help people search faster and type less. For developer guidance, see...
- **Take privacy into consideration before displaying search history.**
  People might not appreciate having their search history appear where others might see it. If you do show search history, provide a way for people to clear it if they want.
- **Make your app’s content searchable in Spotlight.**
  You can share content with Spotlight by making it indexable and specifying descriptive attributes known as *metadata*. Spotlight extracts, stores, and organizes this information to allow for fast, comprehensive searches.
- **Define metadata for custom file types you handle.**
  Supply a Spotlight File Importer plug-in that describes the types of metadata your file format contains. For developer guidance, see [CSImportExtension](https://developer.apple.com/documentation/corespotlight/csimportextension).
- **Use Spotlight to offer advanced file-search capabilities within the context of your app.**
  For example, you might include a button that instantly initiates a Spotlight search based on the current selection. You might then display a custom view that presents the search results or a filtered subset of them.
- **Prefer using the system-provided open and save views.**
  The system-provided open and save views generally include a built-in search field that people can use to search and filter the entire system. For related guidance, see [File...
- **Implement a Quick Look generator if your app produces custom file types.**
  A Quick Look generator helps Spotlight and other apps show previews of your documents. For developer guidance, see [Quick Look](https://developer.apple.com/documentation/quicklook).

## Segmented controls
<sub>`pages/segmented-controls.md`</sub>

- **Use a segmented control to provide closely related choices that affect an object, state, or view.**
  For example, a segmented control in an inspector could let people choose one or more attributes to apply to a selection, or a segmented control in a toolbar could offer a set of actions to perform on the current view.
- **Consider a segmented control when it’s important to group functions together, or to clearly show their selection state.**
  Unlike other button styles, segmented controls preserve their grouping regardless of the view size or where they appear. This grouping can also help people understand at a glance which controls are currently selected.
- **Keep control types consistent within a single segmented control.**
  Don’t assign actions to segments in a control that otherwise represents selection state, and don’t show a selection state for segments in a control that otherwise performs actions.
- **Limit the number of segments in a control.**
  Too many segments can be hard to parse and time-consuming to navigate. Aim for no more than about five to seven segments in a wide interface and no more than about five segments on iPhone.
- **In general, keep segment size consistent.**
  When all segments have equal width, a segmented control feels balanced. To the extent possible, it’s best to keep icon and title widths consistent too.
- **Prefer using either text or images — not a mix of both — in a single segmented control.**
  Although individual segments can contain text labels or images, mixing the two in a single control can lead to a disconnected and confusing interface.
- **As much as possible, use content with a similar size in each segment.**
  Because all segments typically have equal width, it doesn’t look good if content fills some segments but not others.
- **Use nouns or noun phrases for segment labels.**
  Write text that describes each segment and uses [title-style capitalization](https://support.apple.com/guide/applestyleguide/c-apsgb744e4a3/web#apdca93e113f1d64). A segmented control that displays text labels doesn’t need introductory text.
- **Consider a segmented control to switch between closely related subviews.** `[iOS, iPadOS]`
  A segmented control can be useful as a way to quickly switch between related subviews. For example, the segmented control in Calendar’s New Event sheet switches between the subviews for creating a new event and a new reminder. For...
- **Consider using introductory text to clarify the purpose of a segmented control.** `[macOS]`
  When the control uses symbols or interface icons, you could also add a label below each segment to clarify its meaning. If your app includes tooltips, provide one for each segment in a segmented control.
- **Use a tab view in the main window area — instead of a segmented control — for view switching.** `[macOS]`
  A [Tab views](https://developer.apple.com/design/human-interface-guidelines/tab-views) supports efficient view switching and is similar in appearance to a [Boxes](https://developer.apple.com/design/human-interface-guidelines/boxes)...
- **Consider supporting spring loading.** `[macOS]`
  On a Mac equipped with a Magic Trackpad, spring loading lets people activate a segment by dragging selected items over it and force clicking without dropping the selected items. People can also continue dragging the items after a...
- **Consider using a split view instead of a segmented control on screens that perform content filtering.** `[tvOS]`
  People generally find it easy to navigate back and forth between content and filtering options using a split view. Depending on its placement, a segmented control may not be as easy to access.
- **Avoid putting other focusable elements close to segmented controls.** `[tvOS]`
  Segments become selected when focus moves to them, not when people click them. Carefully consider where you position a segmented control relative to other interface elements. If other focusable elements are too close, people might...

## Settings
<sub>`pages/settings.md`</sub>

- **Aim to provide default settings that give the best experience to the largest number of people.**
  For example, you can automatically maximize performance for the device your game is running on instead of asking players to make this choice after your game launches (for developer guidance, see [Improving your game’s graphics...
- **Minimize the number of settings you offer.**
  Although people appreciate having control over an app or game, too many settings can make the experience feel less approachable, while also making it hard to find a particular setting.
- **Make settings available in ways people expect.**
  For example, when a physical keyboard is connected, people often use the standard Command-Comma (,) keyboard shortcut to open an app’s settings, whereas in a game, players often use the Esc (Escape) key.
- **Avoid using settings to ask for setup information you can get in other ways.**
  For example, a game can automatically detect a connected controller or accessory instead of asking the player to identify it; an app can detect whether people are currently using Dark Mode.
- **Respect people’s systemwide settings and avoid including redundant versions of them in your custom settings area.**
  People expect to use the system-provided Settings app to manage global options like accessibility accommodations, scrolling behavior, and authentication methods, and they expect all apps and games to adhere to their choices. Including...
- **Put general, infrequently changed settings in your custom settings area.**
  People must suspend what they’re doing to open an app’s or game’s settings area, so you want to include options that people don’t need to change all the time. For example, an app might list options for adjusting window configuration; a...
- **When possible, prefer letting people modify task-specific options without going to your settings area.**
  For example, if people can adjust things like showing or hiding parts of the current view, reordering a collection of items, or filtering a list, make these options available in the screens they affect, where they’re discoverable and...
- **Add only the most rarely changed options to the system-provided Settings app.**
  If it makes sense to add your app’s or game’s settings to the system-provided Settings app, consider providing a button that opens it directly from your interface.
- **Include a settings item in the [App menu](https://developer.apple.com/design/human-interface-guidelines/the-menu-bar#App-menu).** `[macOS]`
  Avoid adding settings buttons to a window’s toolbar, because doing so decreases the space available for essential commands that people use frequently. If you provide document-level options, add this item to your app’s [File...
- **Dim a settings window’s minimize and maximize buttons.** `[macOS]`
  It’s quick to open a custom settings window using the standard Command–Comma (,) keyboard command, so there’s no need to keep the window in the Dock, and because a settings window accommodates the size of the current pane, people don’t...
- **In your settings window, use a noncustomizable toolbar that remains visible and always indicates the active toolbar button.** `[macOS]`
  A settings window’s toolbar identifies the areas people can customize and helps people navigate among those areas. People rely on a stable settings interface to help them find what they need.
- **Update the window’s title to reflect the currently visible pane.** `[macOS]`
  If your settings window doesn’t have multiple panes, use the title *App Name* Settings.
- **Restore the most recently viewed pane.** `[macOS]`
  People often adjust related settings more than once, so it can be convenient when a settings window opens to the last pane people used.

## SharePlay
<sub>`pages/shareplay.md`</sub>

- **Let people know that you support SharePlay.**
  People often expect media playback experiences to be shareable, so indicate this capability in your interface. For example, you can use the `shareplay` SF Symbol to identify the content or experiences in your app that support SharePlay.
- **If part of your app requires a subscription, consider ways to help nonsubscriber participants quickly join a group activity.**
  For example, you might offer temporary or provisional access to nonsubscribers or let an existing subscriber send a one-time pass to a friend. To make it easy for family members to share your content in a SharePlay experience, you can...
- **Support Picture in Picture (PiP) when possible.**
  On iPhone and iPad, people can open a shared video in a PiP window. On a Mac, a shared video opens in a background window that people can move into the foreground when they want to watch.
- **Use the term *SharePlay* correctly.**
  You can use *SharePlay* as a noun — as in “Join SharePlay” — and also as a verb when describing a direct action in your interface. For example, in a button or sheet that lets people share a movie-viewing activity, you can use a phrase...
- **Briefly describe each activity.**
  When people receive an invitation to participate in an activity, your description helps them understand the experience they’re about to share. For example, a video-viewing app might associate its descriptive movie view with a...
- **Make it easy to start sharing an activity.**
  If there’s no session available when people start a shareable activity, you can present UI that lets them start a group activity. In response, the system asks people if they want to share or continue the experience solo.
- **Help people prepare to join a session before displaying the activity.**
  For example, if people must log in, download content, or make a payment before they can participate, display views that help them perform these tasks before showing the activity UI. Make these tasks as simple and effortless as possible...
- **When possible, defer app tasks that might delay a shared activity.**
  For example, if your app needs to know a participant’s profile, consider asking for this information at a convenient time, like when playback pauses or finishes.
- **Choose the spatial Persona template that suits your shared activity.** `[visionOS]`
  When you design a shared activity, you can use a spatial Persona template to specify a layout for arranging spatial Personas in the shared activity space. The system provides three spatial Persona templates: side-by-side, surround, and...
- **Be prepared to launch directly into your shared activity.** `[visionOS]`
  When one person shares your activity with others on a FaceTime call, the system minimizes friction by automatically launching your app for everyone. In this scenario, you want to avoid displaying any windows that aren’t related to the...
- **Help people enter a shared activity together, but don’t force them.** `[visionOS]`
  When one participant changes their level of immersion, the system tells you so you can synchronize the experience for everyone. Before synchronizing, check whether changing a person’s level of immersion would disrupt their current task;...
- **Smoothly update a shared activity when new participants join.** `[visionOS]`
  When someone joins an in-progress activity, you need to integrate them without disrupting the experience for everyone else. For example, it’s important to update shared immersive content to keep all participants synchronized. Also,...
- **Make sure everyone views the same state of your app.** `[visionOS]`
  If your app has more than one state — such as a media app that provides both minimal and theater-like viewing modes — you need to avoid letting different participants view different states, because doing so can diminish people’s sense...
- **Use Spatial Audio to enrich your shared activity.** `[visionOS]`
  Playing Spatial Audio can help you strengthen the realism of the shared experience. For guidance, see [Playing audio](https://developer.apple.com/design/human-interface-guidelines/playing-audio).
- **When possible, let people discover natural, social solutions to confusions or conflicts that might arise during a shared experience.** `[visionOS]`
  For example, if only one participant at a time can use a virtual tool, avoid displaying UI, like tool-use controls or notifications, and instead let people speak or gesture to the group when they want to use the tool. If conflicts can...
- **Help people keep their private and shared content separate.** `[visionOS]`
  By default, the system clearly differentiates a shared window from windows that aren’t shared. For example, when people use Music to listen together, the shared Music window appears as a new window for everyone, while any individual’s...
- **Let people personalize their experience without changing the experience for others.** `[visionOS]`
  For example, people might need to adjust various settings, like volume or subtitles, to make views and interactions accessible or make themselves more comfortable.
- **Consider when to give each participant a unique view of the shared content.** `[visionOS]`
  Some content looks best when people view it from a specific perspective. For example, people can share a Spatial Capture in a standard window with other people’s spatial Personas visible around it. However, to perceive the depth in a...
- **Make it easy for people to exit and rejoin a shared activity.** `[visionOS]`
  Sometimes, people need to perform an unrelated task in your app or a different one, or engage with their physical surroundings. When this happens, you need to present a control or other component that lets people quickly rejoin the...

## ShazamKit
<sub>`pages/shazamkit.md`</sub>

- **Stop recording as soon as possible.**
  When people allow your app to record audio for recognition, they don’t expect the microphone to stay on. To help preserve privacy, only record for as long as it takes to get the sample you need.
- **Let people opt in to storing your app’s recognized songs to their iCloud library.**
  If your app can store recognized songs to iCloud, give people a way to first approve this action. Even though both the Music Recognition control and the Shazam app show your app as the source of the recognized song, people appreciate...

## Sheets
<sub>`pages/sheets.md`</sub>

- **For complex or prolonged user flows, consider alternatives to sheets.**
  For example, iOS and iPadOS offer a full-screen style of modal view that can work well to display content like videos, photos, or camera views or to help people perform multistep tasks like document or photo editing. (For developer...
- **Display only one sheet at a time from the main interface.**
  When people close a sheet, they expect to return to the parent view or window. If closing a sheet takes people back to another sheet, they can lose track of where they are in your app. If something people do within a sheet results in...
- **Use a nonmodal view when you want to present supplementary items that affect the main task in the parent view.**
  To give people access to information and actions they need while continuing to interact with the main window, consider using a [Split views](https://developer.apple.com/design/human-interface-guidelines/split-views) in visionOS or a...
- **Provide an alternative to the Done button.**
  If you provide a Done button, always pair it with a Cancel button to give people a clear way to dismiss the sheet without confirming or saving their changes, or a Back button to move to a previous step in the sheet. Relying solely on...
- **Subsequent step** `[iOS, iPadOS]`
- **In an iPhone app, consider supporting the medium detent to allow progressive disclosure of the sheet’s content.** `[iOS, iPadOS]`
  For example, a share sheet displays the most relevant items within the medium detent, where they’re visible without resizing. To view more items, people can scroll or expand the sheet. In contrast, you might not want to support the...
- **Include a grabber in a resizable sheet.** `[iOS, iPadOS]`
  A grabber shows people that they can drag the sheet to resize it; they can also tap it to cycle through the detents. In addition to providing a visual indicator of resizability, a grabber also works with VoiceOver so people can resize...
- **Support swiping to dismiss a sheet.** `[iOS, iPadOS]`
  People expect to swipe vertically to dismiss a sheet instead of tapping a dismiss button. If people have unsaved changes in the sheet when they begin swiping to dismiss it, use an action sheet to let them confirm their action.
- **Prefer using the page or form sheet presentation styles in an iPadOS app.** `[iOS, iPadOS]`
  Each style uses a default size for the sheet, centering its content on top of a dimmed background view and providing a consistent experience. For developer guidance, see...
- **Present a sheet in a reasonable default size.** `[macOS]`
  People don’t generally expect to resize sheets, so it’s important to use a size that’s appropriate for the content you display. In some cases, however, people appreciate a resizable sheet — such as when they need to expand the contents...
- **Let people interact with other app windows without first dismissing a sheet.** `[macOS]`
  When a sheet opens, you bring its parent window to the front — if the parent window is a document window, you also bring forward its modeless document-related panels. When people want to interact with other windows in your app, make...
- **Use a panel instead of a sheet if people need to repeatedly provide input and observe results.** `[macOS]`
  A find and replace panel, for example, might let people initiate replacements individually, so they can observe the result of each search for correctness. For guidance, see...
- **Avoid displaying a sheet that emerges from the bottom edge of a window.** `[visionOS]`
  To help people view the sheet, prefer centering it in their [Field of view](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Field-of-view).
- **Present a sheet in a default size that helps people retain their context.** `[visionOS]`
  Avoid displaying a sheet that covers most or all of its window, but consider letting people resize the sheet if they want.
- **Use a sheet only when your modal task requires a custom title or custom content presentation.** `[watchOS]`
  If you need to give people important information or present a set of choices, consider using an [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) or [Action...
- **Keep sheet interactions brief and occasional.** `[watchOS]`
  Use a sheet only as a temporary interruption to the current workflow, and only to facilitate an important task. Avoid using a sheet to help people navigate your app’s content.
- **If you change the default label, prefer using SF Symbols to represent the action.** `[watchOS]`
  Avoid using a label that might mislead people into thinking that the sheet is part of a hierarchical navigation interface. Also, if the text in the top-leading corner looks like a page or app title, people won’t know how to dismiss the...

## Sidebars
<sub>`pages/sidebars.md`</sub>

- **Extend visually rich content beneath the sidebar.**
  In iOS, iPadOS, and macOS, as with other controls such as toolbars and tab bars, sidebars can float above content in the [Liquid Glass](https://developer.apple.com/design/human-interface-guidelines/materials#Liquid-Glass) layer. To...
- **When possible, let people customize the contents of a sidebar.**
  A sidebar lets people navigate to important areas in your app, so it works well when people can decide which areas are most important and in what order they appear.
- **Group hierarchy with disclosure controls if your app has a lot of content.**
  Using [Disclosure controls](https://developer.apple.com/design/human-interface-guidelines/disclosure-controls) helps keep the sidebar’s vertical space to a manageable level.
- **Consider using familiar symbols to represent items in the sidebar.**
  [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols) provides a wide range of customizable symbols you can use to represent items in your app. If you need to use a custom icon, consider creating a...
- **Consider letting people hide the sidebar.**
  People sometimes want to hide the sidebar to create more room for content details or to reduce distraction. When possible, let people hide and show the sidebar using the platform-specific interactions they already know. For example, in...
- **In general, show no more than two levels of hierarchy in a sidebar.**
  When a data hierarchy is deeper than two levels, consider using a split view interface that includes a content list between the sidebar items and detail view.
- **If you need to include two levels of hierarchy in a sidebar, use succinct, descriptive labels to title each group.**
  To help keep labels short, omit unnecessary words.
- **Make sure any sidebar icon colors you choose serve a clear purpose.**
  By default, sidebar icons use your app’s [App accent colors](https://developer.apple.com/design/human-interface-guidelines/color#App-accent-colors). In macOS, people can change the system accent color, which applies to all apps. When...
- **Consider using a tab bar first.** `[iOS, iPadOS]`
  A tab bar provides more space to feature content, and offers enough flexibility to navigate between many apps’ main areas. If you need to expose more areas than fit in a tab bar, the tab bar’s convertible sidebar-style appearance can...
- **If necessary, apply the correct appearance to a sidebar.** `[iOS, iPadOS]`
  If you’re not using SwiftUI to create a sidebar, you can use the...
- **Consider automatically hiding and revealing a sidebar when its container window resizes.** `[macOS]`
  For example, reducing the size of a Mail viewer window can automatically collapse its sidebar, making more room for message content.
- **Avoid putting critical information or actions at the bottom of a sidebar.** `[macOS]`
  People often relocate a window in a way that hides its bottom edge.
- **If your app’s hierarchy is deep, consider using a sidebar within a tab in a tab bar.** `[visionOS]`
  In this situation, a sidebar can support secondary navigation within the tab. If you do this, be sure to prevent selections in the sidebar from changing which tab is currently open.

## Sign in with Apple
<sub>`pages/sign-in-with-apple.md`</sub>

- **Ask people to sign in only in exchange for value.**
  People need to understand why you’re asking them to sign in, so it can work well to display a brief, approachable description of sign-in benefits. For example, you might want to tell people that signing in lets them personalize the app...
- **Delay sign-in as long as possible.**
  People often abandon apps when they’re forced to sign in before doing anything useful. Give them a chance to familiarize themselves with your app before making a commitment. For example, a live-streaming app could let people explore...
- **If you require an account, ask people to set it up before offering any sign-in options.**
  Start by explaining the reasons for requiring an account. Then, after people complete account setup, let them choose a convenient way to sign in to their new account by offering Sign in with Apple and any other sign-in methods you support.
- **Consider letting people link an existing account to Sign in with Apple.**
  When you support this type of linking, people can get the convenience of using Sign in with Apple while maintaining access to the information in an account they’ve already set up. You can offer account linking before or after people...
- **In a commerce app, wait until after people make a purchase before asking them to create an account.**
  If you support a guest checkout system, give people a quick way to create an account after the transaction completes. For example, if you support Apple Pay, let people create an account on the order confirmation page. In cases where...
- **As soon as Sign in with Apple completes, welcome people to their new account.**
  Help people use their new account right away; don’t delay the experience by asking for information that isn’t required.
- **Indicate when people are currently signed in.**
  You can help people confirm their sign-in method by displaying a phrase like “Using Sign in with Apple” in places like a settings or account interface.
- **Clarify whether the additional data you request is required or just recommended.**
  If the data is legally or contractually required — such as an agreement to terms of service, country or region of residence, birth date, or information required by a region’s real-identity laws — make sure people understand that they...
- **Don’t ask people to supply a password.**
  A key benefit of Sign in with Apple is that people don’t have to create and memorize additional passwords. Unless people have stopped using Sign in with Apple with your app or website, don’t ask for a password.
- **Avoid asking for a personal email address when people supply a private relay address.**
  Using Sign in with Apple, people can choose to share a private relay address that automatically forwards messages to their verified personal email account. It’s essential to respect this choice and avoid overriding it by asking for a...
- **Give people a chance to engage with your app before asking for optional data.**
  As people use your app, you can help them discover places where they can benefit from sharing more information with you. For example, you might suggest that they provide a contact phone number if they want real-time text updates, or...
- **Be transparent about the data you collect.**
  People value knowing how you use the data that they share with you. One way you can be transparent is to welcome people by using the name or email address they shared. Doing this helps establish how you use this information and, for a...
- **Prominently display a Sign in with Apple button.**
  Make a Sign in with Apple button no smaller than other sign-in buttons, and avoid making people scroll to see the button.
- **Adjust the corner radius to match the appearance of other buttons in your app.**
  By default, the Sign in with Apple button has rounded corners. In iOS, macOS, and the web, you can change the corner radius to produce a button with square corners or a capsule-shape button. For developer guidance, see...
- **Maintain the minimum button size and margin around the button in iOS, macOS, and the web.**
  Be mindful that the button title may vary in length depending on the locale. Use the following values for guidance.
- **Choose the format of the logo file based on the height of your button.**
  Because SVG and PDF are vector-based formats, you can use these files in buttons of any height. Use the PNG files only in buttons that are 44 points tall, which is the default (and recommended) button height in iOS. Logos are available...
- **Prefer the system font for the title — that is, Sign in with Apple, Sign up with Apple, or Continue with Apple.**
  Regardless of the font you choose, the title and button height of your custom button need to use the same proportions that the system uses. Using the system font for example, the title’s font size would be 43% of the button’s height —...
- **In general, preserve the capitalization style of the title.**
  By default, all variants of the button title capitalize the first word — that is, *Sign* or *Continue* — and *Apple*; all other letters are lowercase. Avoid changing this style unless your interface uses only uppercase.
- **Keep the title and logo vertically aligned within the button.**
  To do this, vertically align the title to the middle of the button, then add the logo image, making sure its height matches the height of the button. Because the logo image includes top and bottom padding, vertically aligning the title...
- **Inset the logo if necessary.**
  If you need to horizontally align the Apple logo with other authentication logos, you can adjust the space between the logo and the button’s leading edge.
- **Maintain a minimum margin between the title and the right edge of the button.**
  Ensure the margin measures at least 8% of the button’s width.
- **Maintain the minimum button size and margin around the button.**
  Be mindful that the button title may vary in length depending on the locale. Use the following values for guidance.
- **Choose the format of the logo file based on the size of your button.**
  The downloadable artwork for logo-only buttons is available in SVG, PDF, and PNG formats. Use the vector-based SVG and PDF formats for buttons of any size; use the PNG format only in buttons that measure 44x44 pt.
- **Don’t add horizontal padding to a logo-only image.**
  A logo-only Sign in with Apple button always has a 1:1 aspect ratio, and the artwork already includes the correct padding on all sides.
- **Use a mask to change the default square shape of the logo-only image.**
  For example, you might want to use a circular or rounded rectangular shape to present all logo-only sign-in buttons. Never crop the Apple-provided artwork to decrease its built-in padding or use the logo by itself, and avoid including...
- **Maintain a minimum margin around the button.**
  Ensure the margin measures at least 1/10 of the button’s height.

## Siri
<sub>`pages/siri.md`</sub>

- **Identify your app’s most popular actions, and when and where they occur.**
  Understanding the contexts where those actions are relevant, such as in a hands-free environment or on a particular device, can help you prioritize which actions and content to expose as app intents and entities, and inform how you...
- **Use familiar terms for your content and actions.**
  When you create an app intent or entity, you choose the terminology that represents it. For example, you could refer to an audio file as a track, a song, or a podcast. Using language for your features and content that people are most...
- **Offer relevant content.**
  Instead of telling Spotlight about all of your app’s content, consider things that are particularly relevant to someone’s personal context — things they’ve recently searched for, their favorite items or bookmarks, or the content of a...
- **Don’t advertise.**
  Don’t include advertisements, marketing, or in-app purchase sales pitches in content that Siri delivers.
- **Only provide a custom response if built-in responses don’t meet your app’s needs.**
  Siri is designed to anticipate a wide variety of natural language requests and respond helpfully without additional configuration.
- **Write response dialogue that’s clear and descriptive.**
  An effective response clearly conveys what happens when Siri performs the action. If you ask follow-up questions, be sure to customize the default dialogue for clarity. For example, “Which soup?” is clearer than “Which one?”
- **Keep responses as succinct as possible.**
  People might interact with Siri frequently, so they may hear the same response multiple times when answering follow-up questions or dealing with errors. Use the context of the current conversation to remove as many details as possible....
- **Provide responses that Siri can deliver audibly and visually.**
  This lets Siri decide which communication method works best for the current situation. For example, if someone using iPhone asks for the weather, the forecast appears onscreen; if they’re using AirPods, Siri speaks the forecast instead....
- **Design inclusive interactions.**
  Create welcoming interactions for everyone by avoiding specific pronouns when they’re not necessary. For example, in response to “Send a message to my best friend,” instead of saying “What’s his or her name?” say “Who should I send it...
- **Ask an open-ended question when the full list of options is too long.**
  If the full list of options is too long for Siri to read in a timely way, follow up with an open-ended question to narrow the scope or get additional detail. For example, “What kind of shoes are you interested in?” in response to a...
- **Keep responses device-independent whenever possible.**
  People can initiate a Siri request on one device and have it take effect on another, so device-specific wording can easily become confusing or misleading. If you must reference a specific device in a response, make sure it’s accurate...
- **Omit your app name from responses.**
  The system already provides verbal and visual attribution for your app when responding to people.
- **Use appropriate language and respect parental controls.**
  Don’t include offensive language in dialogue text that you provide. Many families use parental controls to restrict explicit content and other material that’s based on specific rating levels. Be aware that Siri may also respond aloud,...
- **Help people understand errors and failures.**
  The system provides some default error descriptions, but it’s best to enhance error responses so that they’re specific to the current situation. For example, if the chicken noodle soup is sold out, an error like “Sorry, we’re out of...
- **Refer to Siri by name.**
  Don’t reference Siri using pronouns like *she*, *him*, or *her*. Ideally, just use the word *Siri*. For example, “After you add a shortcut to Siri, you can run the shortcut anytime by asking Siri.” For additional guidance, see...
- **Be aware that the system reserves important actions and phrases for Siri.**
  Never impersonate Siri, attempt to reproduce the functionality that Siri provides, or provide a response that appears to come from Apple. Don’t use reserved phrases like “Call 911” or “Hey Siri.”
- **In a localized context, translate only the word *Hey* in the phrase “Hey Siri.”**
  As an Apple trademark, *Siri* is never translated. Here is a list of acceptable translations for the phrase “Hey Siri”:

## Sliders
<sub>`pages/sliders.md`</sub>

- **Customize a slider’s appearance if it adds value.**
  You can adjust a slider’s appearance — including track color, thumb image and tint color, and left and right icons — to blend with your app’s design and communicate intent. A slider that adjusts image size, for example, could show a...
- **Use familiar slider directions.**
  People expect the minimum and maximum sides of sliders to be consistent in all apps, with minimum values on the leading side and maximum values on the trailing side (for horizontal sliders) and minimum values at the bottom and maximum...
- **Consider supplementing a slider with a corresponding text field and stepper.**
  Especially when a slider represents a wide range of values, people may appreciate seeing the exact slider value and having the ability to enter a specific value in a text field. Adding a stepper provides a convenient way for people to...
- **Don’t use a slider to adjust audio volume.** `[iOS, iPadOS]`
  If you need to provide volume control in your app, use a volume view, which is customizable and includes a volume-level slider and a control for changing the active audio output device. For guidance, see [Playing...
- **Consider giving live feedback as the value of a slider changes.** `[macOS]`
  Live feedback shows people results in real time. For example, your Dock icons are dynamically scaled when adjusting the Size slider in Dock settings.
- **Choose a slider style that matches peoples’ expectations.** `[macOS]`
  A horizontal slider is ideal when moving between a fixed starting and ending point. For example, a graphics app might offer a horizontal slider for setting the opacity level of an object between 0 and 100 percent. Use circular sliders...
- **Consider using a label to introduce a slider.** `[macOS]`
  Labels generally use [sentence-style capitalization](https://help.apple.com/applestyleguide/#/apsgb744e4a3?sub=apdca93e113f1d64) and end with a colon. For guidance, see...
- **Use tick marks to increase clarity and accuracy.** `[macOS]`
  Tick marks help people understand the scale of measurements and make it easier to locate specific values.
- **Consider adding labels to tick marks for even greater clarity.** `[macOS]`
  Labels can be numbers or words, depending on the slider’s values. It’s unnecessary to label every tick mark unless doing so is needed to reduce confusion. In many cases, labeling only the minimum and maximum values is sufficient. When...
- **Prefer horizontal sliders.** `[visionOS]`
  It’s generally easier for people to gesture from side to side than up and down.
- **If necessary, create custom glyphs to communicate what the slider does.** `[watchOS]`
  The system displays plus and minus signs by default.

## Snippets
<sub>`pages/snippets.md`</sub>

- **Ensure legibility.**
  Check for sufficient contrast between the snippet’s custom content and the system-provided background in both light and dark appearances, and keep consistent margins for the content within the view. This clarifies the layout and helps...
- **Keep content concise.**
  Snippets exist to facilitate lightweight, quick interactions, so it’s important to keep their content short and easily legible. To ensure all content is visible, create custom views that are no taller than the 400-point maximum height....
- **Choose a descriptive label for a confirmation snippet’s primary button.**
  You can choose an appropriate label from among those that the [ConfirmationActionName](https://developer.apple.com/documentation/appintents/confirmationactionname), or you can supply a custom label. For example, when designing a snippet...
- **Communicate a snippet’s purpose visually.**
  Don’t rely on showing the dialogue text to convey a snippet’s purpose. While the spoken app intent dialogue is essential for interactions when someone isn’t looking at the screen, prefer to omit it from a snippet’s visual representation...

## Spatial layout
<sub>`pages/spatial-layout.md`</sub>

- **Center important content within the field of view.**
  By default, visionOS launches an app directly in front of people, placing it within their field of view. In an immersive experience, you can help people keep their attention on important content by keeping it centered and not displaying...
- **Upright viewing**
- **Angled viewing**
- **Avoid anchoring content to the wearer’s head.**
  Although you generally want your app to stay within the field of view, anchoring content so that it remains statically in front of someone can make them feel stuck, confined, and uncomfortable, especially if the content obscures a lot...
- **Provide visual cues that accurately communicate the depth of your content.**
  If visual cues are missing or they conflict with a person’s real-world experience, people can experience visual discomfort.
- **Use depth to communicate hierarchy.**
  Depth helps an object appear to stand out from surrounding content, making it more noticeable. People also tend to notice changes in depth: for example, when a sheet appears over a window, the window recedes along the z-axis, allowing...
- **In general, avoid adding depth to text.**
  Text that appears to hover above its background is difficult to read, which slows people down and can sometimes cause vision discomfort.
- **Make sure depth adds value.**
  In general, you want to use depth to clarify and delight — you don’t need to use it everywhere. As you add depth to your design, think about the size and relative importance of objects. Depth is great for visually separating large,...
- **Consider using fixed scale when you want a virtual object to look exactly like a physical object.**
  For example, you might want to maintain the life-size scale of a product you offer so it can look more realistic when people view it in their space. Because interactive content needs to scale to maintain usability as it gets closer or...
- **Avoid displaying too many windows.**
  Too many windows can obscure people’s surroundings, making them feel overwhelmed, constricted, and even uncomfortable. It can also make it cumbersome for people to relocate an app because it means moving a lot of windows.
- **Prioritize standard, indirect gestures.**
  People can make an *indirect* gesture without moving their hand into their field of view. In contrast, making a *direct* gesture requires people to touch the virtual object with their finger, which can be tiring, especially when the...
- **Rely on the Digital Crown to help people recenter windows in their field of view.**
  When people move or turn their head, content might no longer appear where they want it to. If this happens, people can press the [Digital Crown](https://developer.apple.com/design/human-interface-guidelines/digital-crown) when they want...
- **Include enough space around interactive components to make them easy for people to look at.**
  When people look at an interactive element, visionOS displays a visual hover effect that helps them confirm the element is the one they want. It’s crucial to include enough space around an interactive component so that looking at it is...
- **Let people use your app with minimal or no physical movement.**
  Unless some physical movement is essential to your experience, help everyone enjoy it while remaining stationary.
- **Use the floor to help you place a large immersive experience.**
  If your immersive experience includes content that extends up from the floor, place it using a flat horizontal plane. Aligning this plane with the floor can help it blend seamlessly with people’s surroundings and provide a more...

## Split views
<sub>`pages/split-views.md`</sub>

- **To support navigation, persistently highlight the current selection in each pane that leads to the detail view.**
  The selected appearance clarifies the relationship between the content in various panes and helps people stay oriented.
- **Consider letting people drag and drop content between panes.**
  Because a split view provides access to multiple levels of hierarchy, people can conveniently move content from one part of your app to another by dragging items to different panes. For guidance, see [Drag and...
- **Prefer using a split view in a regular — not a compact — environment.** `[iOS]`
  A split view needs horizontal space in which to display multiple panes. In a compact environment, such as iPhone in portrait orientation, it’s difficult to display multiple panes without wrapping or truncating the content, making it...
- **Account for narrow, compact, and intermediate window widths.** `[iPadOS]`
  Since iPad windows are fluidly resizable, it’s important to consider the design of a split view layout at multiple widths. In particular, ensure that it’s possible to navigate between the various panes in a logical way. For guidance,...
- **Set reasonable defaults for minimum and maximum pane sizes.** `[macOS]`
  If people can resize the panes in your app’s split view, make sure to use sizes that keep the divider visible. If a pane gets too small, the divider can seem to disappear, becoming difficult to use.
- **Consider letting people hide a pane when it makes sense.** `[macOS]`
  If your app includes an editing area, for example, consider letting people hide other panes to reduce distractions or allow more room for editing — in Keynote, people can hide the navigator and presenter notes panes when they want to...
- **Provide multiple ways to reveal hidden panes.** `[macOS]`
  For example, you might provide a toolbar button or a menu command — including a keyboard shortcut — that people can use to restore a hidden pane.
- **Prefer the thin divider style.** `[macOS]`
  The thin divider measures one point in width, giving you maximum space for content while remaining easy for people to use. Avoid using thicker divider styles unless you have a specific need. For example, if both sides of a divider...
- **Choose a split view layout that keeps the panes looking balanced.** `[tvOS]`
  By default, a split view devotes a third of the screen width to the primary pane and two-thirds to the secondary pane, but you can also specify a half-and-half layout.
- **Display a single title above a split view, helping people understand the content as a whole.** `[tvOS]`
  People already know how to use a split view to navigate and filter content; they don’t need titles that describe what each pane contains.
- **Choose the title’s alignment based on the type of content the secondary pane contains.** `[tvOS]`
  Specifically, when the secondary pane contains a content collection, consider centering the title in the window. In contrast, if the secondary pane contains a single main view of important content, consider placing the title above the...
- **To display supplementary information, prefer a split view instead of a new window.** `[visionOS]`
  A split view gives people convenient access to more information without leaving the current context, whereas a new window may confuse people who are trying to navigate or reposition content. Opening more windows also requires you to...
- **Automatically display the most relevant detail view.** `[watchOS]`
  When your app launches, show people the most pertinent information. For example, display information relevant to their location, the time, or their recent actions.
- **If your app displays multiple detail pages, place the detail views in a vertical [Tab views](https://developer.apple.com/design/human-interface-guidelines/tab-views).** `[watchOS]`
  People can then use the Digital Crown to scroll between the detail view’s tabs. watchOS also displays a page indicator next to the Digital Crown, indicating the number of tabs and the currently selected tab.

## Status bars
<sub>`pages/status-bars.md`</sub>

- **Obscure content under the status bar.**
  By default, the background of the status bar is transparent, allowing content beneath to show through. This transparency can make it difficult to see information presented in the status bar. If controls are visible behind the status...
- **Consider temporarily hiding the status bar when displaying full-screen media.**
  A status bar can be distracting when people are paying attention to media. Temporarily hide these elements to provide a more immersive experience. The Photos app, for example, hides the status bar and other interface elements when...
- **Avoid permanently hiding the status bar.**
  Without a status bar, people have to leave your app to check the time or see if they have a Wi-Fi connection. Let people redisplay a hidden status bar with a simple, discoverable gesture. For example, when browsing full-screen photos in...

## Steppers
<sub>`pages/steppers.md`</sub>

- **Make the value that a stepper affects obvious.**
  A stepper itself doesn’t display any values, so make sure people know which value they’re changing when they use a stepper.
- **Consider pairing a stepper with a text field when large value changes are likely.**
  Steppers work well by themselves for making small changes that require a few taps or clicks. By contrast, people appreciate the option to use a field to enter specific values, especially when the values they use can vary widely. On a...
- **For large value ranges, consider supporting Shift-click to change the value quickly.** `[macOS]`
  If your app benefits from larger changes in a stepper’s value, it can be useful to let people Shift-click the stepper to change the value by more than the default increment (by 10 times the default, for example).

## Tab bars
<sub>`pages/tab-bars.md`</sub>

- **Use a tab bar to support navigation, not to provide actions.**
  A tab bar lets people navigate among different sections of an app, like the Alarm, Stopwatch, and Timer tabs in the Clock app. If you need to provide controls that act on elements in the current view, use a...
- **Make sure the tab bar is visible when people navigate to different sections of your app.**
  If you hide the tab bar, people can forget which area of the app they’re in. The exception is when a modal view covers the tab bar, because a modal is temporary and self-contained.
- **Use the appropriate number of tabs required to help people navigate your app.**
  As a representation of your app’s hierarchy, it’s important to weigh the complexity of additional tabs against the need for people to frequently access each section; keep in mind that it’s generally easier to navigate among fewer tabs....
- **Avoid overflow tabs.**
  Depending on device size and orientation, the number of visible tabs can be smaller than the total number of tabs. If horizontal space limits the number of visible tabs, the trailing tab becomes a More tab in iOS and iPadOS, revealing...
- **Don’t disable or hide tab bar buttons, even when their content is unavailable.**
  Having tab bar buttons available in some cases but not others makes your app’s interface appear unstable and unpredictable. If a section is empty, explain why its content is unavailable.
- **Include tab labels to help with navigation.**
  A tab label appears beneath or beside a tab bar icon, and can aid navigation by clearly describing the type of content or functionality the tab contains. Use single words whenever possible.
- **Consider using SF Symbols to provide familiar, scalable tab bar icons.**
  When you use [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols), tab bar icons automatically adapt to different contexts. For example, the tab bar can be regular or compact, depending on the device...
- **Use a badge to indicate that critical information is available.**
  You can display a badge — a red oval containing white text and either a number or an exclamation point — on a tab to indicate that there’s new or updated information in the section that warrants a person’s attention. Reserve badges for...
- **Avoid applying a similar color to tab labels and content layer backgrounds.**
  If your app already has bright, colorful content in the content layer, prefer a monochromatic appearance for tab bars, or choose an accent color with sufficient visual differentiation. For more guidance, see [Liquid Glass...
- **Prefer a tab bar for navigation.** `[iPadOS]`
  A tab bar provides access to the sections of your app that people use most. If your app is more complex, you can provide the option to convert the tab bar to a sidebar so people can access a wider set of navigation options.
- **Let people customize the tab bar.** `[iPadOS]`
  In apps with a lot of sections that people might want to access, it can be useful to let people select items that they use frequently and add them to the tab bar, or remove items that they use less frequently. For example, in the Music...
- **Be aware of tab bar scrolling behaviors.** `[tvOS]`
  By default, people can scroll the tab bar offscreen when the current tab contains a single main view. You can see examples of this behavior in the Watch Now, Movies, TV Show, Sports, and Kids tabs in the TV app. The exception is when a...
- **In a live-viewing app, organize tabs in a consistent way.** `[tvOS]`
  For the best experience, organize content in live-streaming apps with tabs in the following order:
- **Supply a symbol and a text label for each tab.** `[visionOS]`
  A tab’s symbol is always visible in the tab bar. When people look at the tab bar, the system reveals tab labels, too. Even though the tab bar expands, you need to keep tab labels short so people can read them at a glance.
- **If it makes sense in your app, consider using a sidebar within a tab.** `[visionOS]`
  If your app’s hierarchy is deep, you might want to use a [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars) to support secondary navigation within a tab. If you do this, be sure to prevent selections in...

## Tab views
<sub>`pages/tab-views.md`</sub>

- **Use a tab view to present closely related areas of content.**
  The appearance of a tab view provides a strong visual indication of enclosure. People expect each tab to display content that is in some way similar or related to the content in the other tabs.
- **Make sure the controls within a pane affect content only in the same pane.**
  Panes are mutually exclusive, so ensure they’re fully self-contained.
- **Provide a label for each tab that describes the contents of its pane.**
  A good label helps people predict the contents of a pane before clicking or tapping its tab. In general, use nouns or short noun phrases for tab labels. A verb or short verb phrase may make sense in some contexts. Use title-style...
- **Avoid using a pop-up button to switch between tabs.**
  A tabbed control is efficient because it requires a single click or tap to make a selection, whereas a pop-up button requires two. A tabbed control also presents all choices onscreen at the same time, whereas people must click a pop-up...
- **Avoid providing more than six tabs in a tab view.**
  Having more than six tabs can be overwhelming and create layout issues. If you need to present six or more tabs, consider another way to implement the interface. For example, you could instead present each tab as a view option in a...
- **In general, inset a tab view by leaving a margin of window-body area on all sides of a tab view.**
  This layout looks clean and leaves room for additional controls that aren’t directly related to the contents of the tab view. You can extend a tab view to meet the window edges, but this layout is unusual.

## Tap to Pay on iPhone
<sub>`pages/tap-to-pay-on-iphone.md`</sub>

- **Help merchants accept Tap to Pay on iPhone terms and conditions before they begin interacting with their customers.**
  Merchants must accept the terms and conditions before you perform the initial device configuration, so it works well when they can do so before they begin a checkout or other customer-facing flow. For example, you can provide buttons...
- **Present Tap to Pay on iPhone terms and conditions only to an administrative user.**
  If a nonadministrator tries to activate the feature, present a message explaining that administrator access is required. If your app’s primary users are enterprise or nonadministrative users, you can let an administrator accept Tap to...
- **If necessary, help merchants make sure their device is up to date.**
  If your PSP requires specific versions of iOS, be sure to present the terms and conditions only after the merchant updates their device.
- **Provide a tutorial that describes the supported payment types and shows how to use Tap to Pay on iPhone to accept each type.**
  You can offer this tutorial by:
- **Provide Tap to Pay on iPhone as a checkout option whether the feature is enabled or not.**
  Including a Tap to Pay on iPhone button gives merchants the flexibility to use the feature without exiting the checkout flow. When merchants tap the button, present the terms and conditions if necessary and automatically display the Tap...
- **Avoid making merchants wait to use Tap to Pay on iPhone.**
  In addition to performing the initial configuration for each device, you need to perform a subsequent configuration each time your app becomes frontmost. To minimize potential wait times, prepare the feature as soon as your app starts...
- **Make sure the Tap to Pay on iPhone checkout option is available even if configuration is continuing in the background.**
  Merchants must always be able to select the Tap to Pay on iPhone checkout option in a checkout flow. During configuration, let merchants select the checkout option and then display a progress indicator — avoid waiting for configuration...
- **If your app supports multiple payment-acceptance methods, make the Tap to Pay on iPhone button easy to find.**
  Avoid making merchants scroll to access the feature. If your app doesn’t support other payment acceptance options, open Tap to Pay on iPhone automatically when checkout begins.
- **Make it easy for merchants to switch between Tap to Pay on iPhone and the hardware accessories you support.**
  Even though your support for Tap to Pay on iPhone is separate from your support for a hardware accessory, such as a Bluetooth chip and PIN card reader, you can streamline the user experience by helping merchants set up both methods at...
- **For the label of the button that activates the feature, use “Tap to Pay on iPhone” or, if space is constrained, “Tap to Pay.”**
  The exception is if Tap to Pay on iPhone is the only payment-acceptance method you support. In this case, you can reuse your existing Charge or Checkout buttons to activate Tap to Pay on iPhone. If you support multiple...
- **Design your Tap to Pay on iPhone button to match the other buttons in your app.**
  Although you must use the labels “Tap to Pay on iPhone” or “Tap to Pay” as described above, you can use the button color and shape that coordinate best with your interface.
- **Determine the final amount that customers need to pay before merchants initiate the Tap to Pay on iPhone experience.**
  For example, if your app supports tipping or other customer interactions that can affect the total, make sure merchants offer these interactions before displaying the Tap to Pay on iPhone screen. Aim to display the final amount...
- **If you support pre-payment options in your checkout flow, display them before the Tap to Pay on iPhone screen.**
  For example, if you support the selection of different payment types, you can display these options in your checkout screen after a merchant taps the Tap to Pay on iPhone button and before you open the Tap to Pay on iPhone screen.
- **Start processing a transaction as soon as possible.**
  The system provides API you can use to request the result of a successful tap before the Tap to Pay on iPhone screen finishes displaying the checkmark animation that indicates tap completion. For developer guidance, see...
- **Display a progress indicator while payment is authorizing before you show your transaction result screen.**
  Transaction authorization can take several seconds to complete, depending on factors like connectivity for both the PSP and the merchant’s device. To ensure a smooth visual transition, display your authorization [Progress...
- **Clearly display the result of a transaction, whether it’s declined or successful.**
  A transaction can be declined for reasons like insufficient funds, suspicion of fraud, or when the customer enters an incorrect PIN. As much as possible, also give the merchant ways to offer customers a digital receipt, such as through...
- **Help merchants complete the checkout flow when a payment can’t complete with Tap to Pay on iPhone.**
  For example, a tap can fail when a card isn’t readable, isn’t from a supported payment network, doesn’t allow transactions at the stated amount, or doesn’t allow online PIN entry. In cases like these, you can:
- **If the system returns an error that the merchant must address, display a clear description of the problem and recommend an appropriate resolution.**
  For example, if the device’s version of iOS doesn’t support Tap to Pay on iPhone, present an [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts) that recommends updating to the latest version. For developer...
- **Make it easy for merchants to get help with issues they can’t resolve.**
  For example, direct merchants to the help content in your app or on your website, and provide an action that contacts your support team.
- **Use a generic label in a button that opens the Tap to Pay on iPhone screen to read a payment card when there’s no transaction amount.**
  Don’t include “Tap to Pay on iPhone” or “Tap to Pay” in such a label; instead, use a generic label like “Look Up,” “Store Card,” “Verify,” or “Refund.”
- **If your app supports an independent loyalty card transaction, distinguish this flow from a payment-acceptance flow that uses Tap to Pay on iPhone.**
  It works well to give merchants a separate, clearly labeled button to initiate a loyalty card transaction. To help merchants avoid choosing the wrong button by mistake, avoid including “Tap to Pay on iPhone,” “Tap to Pay,” or other...

## Text fields
<sub>`pages/text-fields.md`</sub>

- **Use a text field to request a small amount of information, such as a name or an email address.**
  To let people input larger amounts of text, use a [Text views](https://developer.apple.com/design/human-interface-guidelines/text-views) instead.
- **Show a hint in a text field to help communicate its purpose.**
  A text field can contain placeholder text — such as “Email” or “Password” — when there’s no other text in the field. Because placeholder text disappears when people start typing, it can also be useful to include a separate label...
- **Use secure text fields to hide private data.**
  Always use a secure text field when your app asks for sensitive data, such as a password. For developer guidance, see [SecureField](https://developer.apple.com/documentation/swiftui/securefield).
- **To the extent possible, match the size of a text field to the quantity of anticipated text.**
  The size of a text field helps people visually gauge the amount of information to provide.
- **Evenly space multiple text fields.**
  If your layout includes multiple text fields, leave enough space between them so people can easily see which input field belongs with each introductory label. Stack multiple text fields vertically when possible, and use consistent...
- **Ensure that tabbing between multiple fields flows as people expect.**
  When tabbing between fields, move focus in a logical sequence. The system attempts to achieve this result automatically, so you won’t need to customize this too often.
- **Validate fields when it makes sense.**
  For example, if the only legitimate value for a field is a string of digits, your app needs to alert people if they’ve entered characters other than digits. The appropriate time to check the data depends on the context: when entering an...
- **Use a number formatter to help with numeric data.**
  A number formatter automatically configures the text field to accept only numeric values. It can also display the value in a specific way, such as with a certain number of decimal places, as a percentage, or as currency. Don’t assume...
- **Adjust line breaks according to the needs of the field.**
  By default, the system clips any text extending beyond the bounds of a text field. Alternatively, you can set up a text field to wrap text to a new line at the character or word level, or to truncate (indicated by an ellipsis) at the...
- **Consider using an expansion tooltip to show the full version of clipped or truncated text.**
  An expansion tooltip behaves like a regular [tooltip](https://developer.apple.com/design/human-interface-guidelines/offering-help#macOS-visionOS) and appears when someone places the pointer over the field.
- **In iOS, iPadOS, tvOS, and visionOS apps, show the appropriate keyboard type.**
  Several different keyboard types are available, each designed to facilitate a different type of input, such as numbers or URLs. To streamline data entry, display the keyboard that’s appropriate for the type of content people are...
- **Minimize text entry in your tvOS and watchOS apps.**
  Entering long passages of text or filling out numerous text fields is time-consuming on Apple TV and Apple Watch. Minimize text input and consider gathering information more efficiently, such as with buttons.
- **Display a Clear button in the trailing end of a text field to help people erase their input.** `[iOS, iPadOS]`
  When this element is present, people can tap it to clear the text field’s contents, without having to keep tapping the Delete key.
- **Use images and buttons to provide clarity and functionality in text fields.** `[iOS, iPadOS]`
  You can display custom images in both ends of a text field, or you can add a system-provided button, such as the Bookmarks button. In general, use the leading end of a text field to indicate a field’s purpose and the trailing end to...
- **Consider using a combo box if you need to pair text input with a list of choices.** `[macOS]`
  For related guidance, see [Combo boxes](https://developer.apple.com/design/human-interface-guidelines/combo-boxes).
- **Present a text field only when necessary.** `[watchOS]`
  Whenever possible, prefer displaying a list of options rather than requiring text entry.

## Text views
<sub>`pages/text-views.md`</sub>

- **Use a text view when you need to display text that’s long, editable, or in a special format.**
  Text views differ from [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields) and [Labels](https://developer.apple.com/design/human-interface-guidelines/labels) in that they provide the most options for...
- **Keep text legible.**
  Although you can use multiple fonts, colors, and alignments in creative ways, it’s essential to maintain the readability of your content. It’s a good idea to adopt Dynamic Type so your text still looks good if people change text size on...
- **Make useful text selectable.**
  If a text view contains useful information such as an error message, a serial number, or an IP address, consider letting people select and copy it for pasting elsewhere.
- **Show the appropriate keyboard type.** `[iOS, iPadOS]`
  Several different keyboard types are available, each designed to facilitate a different type of input. To streamline data entry, the keyboard you display when editing a text view needs to be appropriate for the type of content. For...

## The menu bar
<sub>`pages/the-menu-bar.md`</sub>

- **Support the default system-defined menus and their ordering.**
  People expect to find menus and menu items in an order they’re familiar with. In many cases, the system implements the functionality of standard menu items so you don’t have to. For example, when people select text in a standard text...
- **Always show the same set of menu items.**
  Keeping menu items visible helps people learn what actions your app supports, even if they’re unavailable in the current context. If a menu bar item isn’t actionable, disable the action instead of hiding it from the menu.
- **Represent menu item actions with familiar icons.**
  Icons help people recognize common actions throughout your app. Use the same icons as the system to represent actions such as Copy, Share, and Delete, wherever they appear. For a list of icons that represent common actions, see...
- **Support the keyboard shortcuts defined for the standard menu items you include.**
  People expect to use the keyboard shortcuts they already know for standard menu items, like Copy, Cut, Paste, Save, and Print. Define custom keyboard shortcuts only when necessary. For guidance, see [Standard keyboard...
- **Prefer short, one-word menu titles.**
  Various factors — like different display sizes and the presence of menu bar extras — can affect the spacing and appearance of your menus. One-word menu titles work especially well in the menu bar because they take little space and are...
- **Display the About menu item first.**
  Include a separator after the About menu item so that it appears by itself in a group.
- **Determine whether Find menu items belong in the Edit menu.**
  For example, if your app lets people search for files or other types of objects, Find menu items might be more appropriate in the File menu.
- **Provide a View menu even if your app supports only a subset of the standard view functions.**
  For example, if your app doesn’t include a tab bar, toolbar, or sidebar, but does support full-screen mode, provide a View menu that includes only the Enter/Exit Full Screen menu item.
- **Ensure that each show/hide item title reflects the current state of the corresponding view.**
  For example, when the toolbar is hidden, provide a Show Toolbar menu item; when the toolbar is visible, provide a Hide Toolbar menu item.
- **Provide app-specific menus for custom commands.**
  People look in the menu bar when searching for app-specific commands, especially when using an app for the first time. Even when commands are available elsewhere in your app, it’s important to list them in the menu bar. Putting commands...
- **As much as possible, reflect your app’s hierarchy in app-specific menus.**
  For example, Mail lists the Mailbox, Message, and Format menus in an order that mirrors the relationships of these items: mailboxes contain messages, and messages contain formatting.
- **Aim to list app-specific menus in order from most to least general or commonly used.**
  People tend to expect menus in the leading end of a list to be more specialized than menus in the trailing end.
- **Provide a Window menu even if your app has only one window.**
  Include the Minimize and Zoom menu items so people using Full Keyboard Access can use the keyboard to invoke these functions.
- **Consider including menu items for showing and hiding panels.**
  A [Panels](https://developer.apple.com/design/human-interface-guidelines/panels) provides information, configuration options, or tools for interacting with content in a primary window, and typically appears only when people need it....
- **Avoid making a dynamic menu item the only way to accomplish a task.**
  Dynamic menu items are hidden by default, so they’re best suited to offer shortcuts to advanced actions that people can accomplish in other ways. For example, if someone hasn’t discovered the *Minimize All* dynamic menu item in the...
- **Use dynamic menu items primarily in menu bar menus.**
  Adding a dynamic menu item to contextual or Dock menus can make the item even harder for people to discover.
- **Require only a single modifier key to reveal a dynamic menu item.**
  It can be physically awkward to press more than one key while simultaneously opening a menu and choosing a menu item, in addition to reducing the discoverability of the dynamic behavior. For developer guidance, see...
- **Because the menu bar is often hidden when running an app full screen, ensure that people can access all of your app’s functions through its UI.** `[iPadOS]`
  In particular, always offer other ways to accomplish tasks assigned to dynamic menu items, since these are only available when a hardware keyboard is connected. Avoid using the menu bar as a catch-all location for functionality that...
- **Reserve the YourAppName > Settings menu item for opening your app’s page in iPadOS Settings.** `[iPadOS]`
  If your app includes its own internal preferences area, link to it with a separate menu item beneath Settings in the same group. Place any other custom app-wide configuration options in this section as well.
- **For apps with tab-style navigation, consider adding each tab as a menu item in the View menu.** `[iPadOS]`
  Since each tab is a different view of the app, the View menu is a natural place to offer an additional way to navigate between tabs. If you do this, consider assigning key bindings to each tab to make navigation even more convenient.
- **Consider grouping menu items into submenus to conserve vertical space.** `[iPadOS]`
  Menu item rows on iPad use more space than on Mac to make them easier to tap. Because of this, and the smaller screen sizes of some iPads, it can be helpful to group related items into submenus more frequently than in the menu bar on Mac.
- **Consider using a symbol to represent your menu bar extra.** `[macOS]`
  You can create an [Icons](https://developer.apple.com/design/human-interface-guidelines/icons) or you can choose one of the [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols), using it as-is or...
- **Display a menu — not a popover — when people click your menu bar extra.** `[macOS]`
  Unless the app functionality you want to expose is too complex for a menu, avoid presenting it in a [Popovers](https://developer.apple.com/design/human-interface-guidelines/popovers).
- **Let people — not your app — decide whether to put your menu bar extra in the menu bar.** `[macOS]`
  Typically, people add a menu bar extra to the menu bar by changing a setting in an app’s settings window. To ensure discoverability, however, consider giving people the option of doing so during setup.
- **Avoid relying on the presence of menu bar extras.** `[macOS]`
  The system hides and shows menu bar extras regularly, and you can’t be sure which other menu bar extras people have chosen to display or predict the location of your menu bar extra.
- **Consider exposing app-specific functionality in other ways, too.** `[macOS]`
  For example, you can provide a [Dock menu](https://developer.apple.com/design/human-interface-guidelines/dock-menus) that appears when people Control-click your app’s Dock icon. People can hide or choose not to use your menu bar extra,...

## Toggles
<sub>`pages/toggles.md`</sub>

- **Use a toggle to help people choose between two opposing values that affect the state of content or a view.**
  A toggle always lets people manage the state of something, so if you need to support other types of actions — such as choosing from a list of items — use a different component, like a [Pop-up...
- **Clearly identify the setting, view, or content the toggle affects.**
  In general, the surrounding context provides enough information for people to understand what they’re turning on or off. In some cases, often in macOS apps, you can also supply a label to describe the state the toggle controls. If you...
- **Make sure the visual differences in a toggle’s state are obvious.**
  For example, you might add or remove a color fill, show or hide the background shape, or change the inner details you display — like a checkmark or dot — to show that a toggle is on or off. Avoid relying solely on different colors to...
- **Use the switch toggle style only in a list row.** `[iOS, iPadOS]`
  You don’t need to supply a label in this situation because the content in the row provides the context for the state the switch controls.
- **Change the default color of a switch only if necessary.** `[iOS, iPadOS]`
  The default green color tends to work well in most cases, but you might want to use your app’s accent color instead. Be sure to use a color that provides enough contrast with the uncolored appearance to be perceptible.
- **Outside of a list, use a button that behaves like a toggle, not a switch.** `[iOS, iPadOS]`
  For example, the Phone app uses a toggle on the filter button to let users filter their recent calls. The app adds a blue highlight to indicate when the toggle is active, and removes it when the toggle is inactive.
- **Avoid supplying a label that explains the button’s purpose.** `[iOS, iPadOS]`
  The interface icon you create — combined with the alternative background appearances you supply — help people understand what the button does. For developer guidance, see...
- **Use switches, checkboxes, and radio buttons in the window body, not the window frame.** `[macOS]`
  In particular, avoid using these components in a toolbar or status bar.
- **Prefer a switch for settings that you want to emphasize.** `[macOS]`
  A switch has more visual weight than a checkbox, so it looks better when it controls more functionality than a checkbox typically does. For example, you might use a switch to let people turn on or off a group of settings, instead of...
- **Within a grouped form, consider using a mini switch to control the setting in a single row.** `[macOS]`
  The height of a mini switch is similar to the height of buttons and other controls, resulting in rows that have a consistent height. If you need to present a hierarchy of settings within a grouped form, you can use a regular switch for...
- **In general, don’t replace a checkbox with a switch.** `[macOS]`
  If you’re already using a checkbox in your interface, it’s probably best to keep using it.
- **Use a checkbox instead of a switch if you need to present a hierarchy of settings.** `[macOS]`
  The visual style of checkboxes helps them align well and communicate grouping. By using alignment — generally along the leading edge of the checkboxes — and indentation, you can show dependencies, such as when the state of a checkbox...
- **Consider using radio buttons if you need to present a set of more than two mutually exclusive options.** `[macOS]`
  When people need to choose from options in addition to just “on” or “off,” using multiple radio buttons can help you clarify each option with a unique label.
- **Consider using a label to introduce a group of checkboxes if their relationship isn’t clear.** `[macOS]`
  Describe the set of options, and align the label’s baseline with the first checkbox in the group.
- **Accurately reflect a checkbox’s state in its appearance.** `[macOS]`
  A checkbox’s state can be on, off, or mixed. If you use a checkbox to globally turn on and off multiple subordinate checkboxes, show a mixed state when the subordinate checkboxes have different states. For example, you might need to...
- **Prefer a set of radio buttons to present mutually exclusive options.** `[macOS]`
  If you need to let people choose multiple options in a set, use checkboxes instead.
- **Avoid listing too many radio buttons in a set.** `[macOS]`
  A long list of radio buttons takes up a lot of space in the interface and can be overwhelming. If you need to present more than about five options, consider using a component like a [Pop-up...
- **To present a single setting that can be on or off, prefer a checkbox.** `[macOS]`
  Although a single radio button can also turn something on or off, the presence or absence of the checkmark in a checkbox can make the current state easier to understand at a glance. In rare cases where a single checkbox doesn’t clearly...
- **Use consistent spacing when you display radio buttons horizontally.** `[macOS]`
  Measure the space needed to accommodate the longest button label, and use that measurement consistently.

## Token fields
<sub>`pages/token-fields.md`</sub>

- **Add value with a context menu.**
  People often benefit from a [context menu](https://developer.apple.com/design/human-interface-guidelines/context-menus) with additional options or information about a token.
- **Consider providing additional ways to convert text into tokens.**
  By default, text people enter turns into a token whenever they type a comma. You can specify additional shortcuts, such as pressing Return, that also invoke this action.
- **Consider customizing the delay the system uses before showing suggested tokens.**
  By default, suggestions appear immediately. However, suggestions that appear too quickly may distract people while they’re typing. If your app suggests tokens, consider adjusting the delay to a comfortable level.

## Toolbars
<sub>`pages/toolbars.md`</sub>

- **Choose items deliberately to avoid overcrowding.**
  People need to be able to distinguish and activate each item, so you don’t want to put too many items in the toolbar. To accommodate variable view widths, define which items move to the overflow menu as the toolbar becomes narrower.
- **Add a More menu to contain additional actions.**
  Prioritize less important actions for inclusion in the More menu. Try to include all actions in the toolbar if possible, and only add this menu if you really need it.
- **In iPadOS and macOS apps, consider letting people customize the toolbar to include their most common items.**
  Toolbar customization is especially useful in apps that provide a lot of items — or that include advanced functionality that not everyone needs — and in apps that people tend to use for long periods of time. For example, it works well...
- **Reduce the use of toolbar backgrounds and tinted controls.**
  Any custom backgrounds and appearances you use might overlay or interfere with background effects that the system provides. Instead, use the content layer to inform the color and appearance of the toolbar, and use a...
- **Avoid applying a similar color to toolbar item labels and content layer backgrounds.**
  If your app already has bright, colorful content in the content layer, prefer using the default monochromatic appearance of toolbars. For more guidance, see [Liquid Glass...
- **Prefer using standard components in a toolbar.**
  By default, standard buttons, text fields, headers, and footers have corner radii that are concentric with bar corners. If you need to create a custom component, ensure that its corner radius is also concentric with the bar’s corners.
- **Consider temporarily hiding toolbars for a distraction-free experience.**
  Sometimes people appreciate a minimal interface to reduce distractions or reveal more content. If you support this, do so contextually when it makes the most sense, and offer ways to reliably restore hidden interface elements. For...
- **Provide a useful title for each window.**
  A title helps people confirm their location as they navigate your app, and differentiates between the content of multiple open windows. If titling a toolbar seems redundant, you can leave the title area empty. For example, Notes doesn’t...
- **Don’t title windows with your app name.**
  Your app’s name doesn’t provide useful information about your content hierarchy or any window or area in your app, so it doesn’t work well as a title.
- **Write a concise title.**
  Aim for a word or short phrase that distills the purpose of the window or view, and keep the title under 15 characters long so you leave enough room for other controls.
- **Use the standard Back and Close buttons.**
  People know that the standard Back button lets them retrace their steps through a hierarchy of information, and the standard Close button closes a modal view. Prefer the standard symbols for each, and don’t use a text label that says...
- **Provide actions that support the main tasks people perform.**
  In general, prioritize the commands that people are most likely to want. These commands are often the ones people use most frequently, but in some apps it might make sense to prioritize commands that map to the highest level or most...
- **Make sure the meaning of each control is clear.**
  Don’t make people guess or experiment to figure out what a toolbar item does. Prefer simple, recognizable symbols for items instead of text, except for actions like *edit* that aren’t well-represented by symbols. For guidance on symbols...
- **Prefer system-provided symbols without borders.**
  System-provided symbols are familiar, automatically receive appropriate coloring and vibrancy, and respond consistently to user interactions. Borders (like outlined circle symbols) aren’t necessary because the section provides a visible...
- **Use the `.prominent` style for key actions such as Done or Submit.**
  This separates and tints the action so there’s a clear focal point. Only specify one primary action, and put it on the trailing side of the toolbar.
- **Group toolbar items logically by function and frequency of use.**
  For example, Keynote includes several sections that are based on functionality, including one for presentation-level commands, one for playback commands, and one for object insertion.
- **Group navigation controls and critical actions like Done, Close, or Save in dedicated, familiar, and visually distinct sections.**
  This reflects their importance and helps people discover and understand these actions.
- **Keep consistent groupings and placement across platforms.**
  This helps people develop familiarity with your app and trust that it behaves similarly regardless of where they use it.
- **Minimize the number of groups.**
  Too many groups of controls can make a toolbar feel cluttered and confusing, even with the added space on iPad and Mac. In general, aim for a maximum of three.
- **Keep actions with text labels separate.**
  Placing an action with a text label next to an action with a symbol can create the illusion of a single action with a combined text and symbol, leading to confusion and misinterpretation. If your toolbar includes multiple text-labeled...
- **Prioritize only the most important items for inclusion in the main toolbar area.** `[iOS]`
  Because space is so limited, carefully consider which actions are essential to your app and include those first. Create a More menu to include additional items.
- **Use a large title to help people stay oriented as they navigate and scroll.** `[iOS]`
  By default, a large title transitions to a standard title as people begin scrolling the content, and transitions back to large when people scroll to the top, reminding them of their current location. For developer guidance, see...
- **Consider combining a toolbar with a tab bar.** `[iPadOS]`
  In iPadOS, a toolbar and a [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) can coexist in the same horizontal space at the top of the view. This is particularly useful for layouts where you want to...
- **Make every toolbar item available as a command in the menu bar.** `[macOS]`
  Because people can customize the toolbar or hide it, it can’t be the only place that presents a command. In contrast, it doesn’t make sense to provide a toolbar item for every menu item, because not all menu commands are important...
- **Prefer using a system-provided toolbar.** `[visionOS]`
  The standard toolbar has a consistent and familiar appearance and is optimized to work well with eye and hand input. In addition, the system automatically places a standard toolbar in the correct position in relation to its window.
- **Avoid creating a vertical toolbar.** `[visionOS]`
  In visionOS, [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars) are vertical, so presenting a vertical toolbar could confuse people.
- **Try to prevent windows from resizing below the width of the toolbar.** `[visionOS]`
  visionOS doesn’t include a menu bar where each app lists all its actions, so it’s important for the toolbar to provide reliable access to essential controls regardless of a window’s size.
- **If your app can enter a modal state, consider offering contextually relevant toolbar controls.** `[visionOS]`
  For example, a photo-editing app might enter a modal state to help people perform a multistep editing task. In this scenario, the controls in the modal editing view are different from the controls in the main window. Be sure to...
- **Avoid using a pull-down menu in a toolbar.** `[visionOS]`
  A pull-down menu lets you offer additional actions related to a toolbar item, but can be difficult for people to discover and may clutter your interface. Because a toolbar is located at the bottom edge of a window in visionOS, a...
- **Use a scrolling toolbar button for an important action that isn’t a primary app function.** `[watchOS]`
  A toolbar button gives you the flexibility to offer important functionality in a view whose primary purpose is related to that functionality, but may not be the same. For example, Mail provides the essential New Message action in a...

## Top Shelf
<sub>`pages/top-shelf.md`</sub>

- **Help people jump right into your content.**
  Top Shelf provides a path to the content people care about most. Two of the system-provided layout templates — [Carousel actions](https://developer.apple.com/design/human-interface-guidelines/top-shelf#Carousel-actions) and [Carousel...
- **Feature new content.**
  For example, showcase new releases or episodes, highlight upcoming movies and shows, and avoid promoting content that people have already purchased, rented, or watched.
- **Personalize people’s favorite content.**
  People typically put the apps they use most often into Top Shelf. You can personalize their experience by showing targeted recommendations in the Top Shelf content you supply, letting people resume media playback or jump back into...
- **Avoid showing advertisements or prices.**
  People put your app into Top Shelf because you’ve already sold them on it, so they may not appreciate seeing lots of ads from your app. Showing purchasable content in the Top Shelf is fine, but prefer putting the focus on new and...
- **Showcase compelling dynamic content that can help draw people in and encourage them to view more.**
  If necessary, you can supply static images, but people typically prefer a captivating, dynamic Top Shelf experience that features the newest or highest rated content. To provide this experience, prefer creating [Layered...
- **If you don’t provide the recommended full-screen content, supply at least one static image as a fallback.**
  The system displays a static image when your app is in the Dock and in focus and full-screen content is unavailable. tvOS flips and blurs the image, ensuring that it fits into a width of 1920 pixels at the 16:9 aspect ratio. Use the...
- **Avoid implying interactivity in a static image.**
  A static Top Shelf image isn’t focusable, and you don’t want to make people think it’s interactive.
- **Provide a title.**
  Include a succinct title, like the title of the show or movie or the title of a photo album. If necessary, you can also provide a brief subtitle. For example, a subtitle for a photo album could be a range of dates; a subtitle for an...
- **Provide a title that identifies the currently playing content.**
  The content title appears near the top of the screen so it’s easy for people to read it at a glance. Above the title, you can also provide a succinct phrase or app attribution, like “Featured on *My App*.”
- **Provide enough content to constitute a complete row.**
  At a minimum, load enough images in a sectioned content row to span the full width of the screen. In addition, include at least one label for greater platform consistency and to provide additional context.
- **Be aware of additional scaling when combining image sizes.**
  If your Top Shelf design includes a mixture of image sizes, keep in mind that images will automatically scale up to match the height of the tallest image if necessary. For example, a 16:9 image scales to 500 pixels high if included in a...
- **Provide three to eight images.**
  A minimum of three images is recommended for a scrolling banner to feel effective. More than eight images can make it hard to navigate to a specific image.
- **If you need text, add it to your image.**
  This layout style doesn’t show labels under content, so all text must be part of the image itself. In layered images, consider elevating text by placing it on a dedicated layer above the others. Add the text to the accessibility label...

## Typography
<sub>`pages/typography.md`</sub>

- **Use font sizes that most people can read easily.**
  People need to be able to read your content at various viewing distances and under a variety of conditions. Follow the recommended default and minimum text sizes for each platform — for both custom and system fonts — to ensure your text...
- **Test legibility in different contexts.**
  For example, you need to test game text for legibility on each platform on which your game runs. If testing shows that some of your text is difficult to read, consider using a larger type size, increasing contrast by modifying the text...
- **In general, avoid light font weights.**
  For example, if you’re using system-provided fonts, prefer Regular, Medium, Semibold, or Bold font weights, and avoid Ultralight, Thin, and Light font weights, which can be difficult to see, especially when text is small.
- **Adjust font weight, size, and color as needed to emphasize important information and help people visualize hierarchy.**
  Be sure to maintain the relative hierarchy and visual distinction of text elements when people adjust text sizes.
- **Minimize the number of typefaces you use, even in a highly customized interface.**
  Mixing too many different typefaces can obscure your information hierarchy and hinder readability, in addition to making an interface feel internally inconsistent or poorly designed.
- **Prioritize important content when responding to text-size changes.**
  Not all content is equally important. When someone chooses a larger text size, they typically want to make the content they care about easier to read; they don’t always want to increase the size of every word on the screen. For example,...
- **San Francisco (SF)**
  is a sans serif typeface family that includes the SF Pro, SF Compact, SF Arabic, SF Armenian, SF Georgian, SF Hebrew, and SF Mono variants.
- **New York (NY)**
  is a serif typeface family designed to work well by itself and alongside the SF fonts.
- **Consider using the built-in text styles.**
  The system-defined text styles give you a convenient and consistent way to convey your information hierarchy through font size and weight. Using text styles with the system fonts also ensures support for Dynamic Type and larger...
- **Modify the built-in text styles if necessary.**
  System APIs define font adjustments — called *symbolic traits* — that let you modify some aspects of a text style. For example, the bold trait adds weight to text, letting you create another level of hierarchy. You can also use symbolic...
- **If necessary, adjust tracking in interface mockups.**
  In a running app, the system font dynamically adjusts tracking at every point size. To produce an accurate interface mockup of an interface that uses the variable system fonts, you don’t have to choose a discrete optical size at certain...
- **Make sure custom fonts are legible.**
  People need to be able to read your custom font easily at various viewing distances and under a variety of conditions. While using a custom font, be guided by the recommended minimum font sizes for various styles and weights in...
- **Implement accessibility features for custom fonts.**
  System fonts automatically support Dynamic Type (where available) and respond when people turn on accessibility features, such as Bold Text. If you use a custom font, make sure it implements the same behaviors. For developer guidance,...
- **Make sure your app’s layout adapts to all font sizes.**
  Verify that your design scales, and that text and glyphs are legible at all font sizes. On iPhone or iPad, turn on Larger Accessibility Text Sizes in Settings > Accessibility > Display & Text Size > Larger Text, and confirm that your...
- **Increase the size of meaningful interface icons as font size increases.**
  If you use interface icons to communicate important information, make sure they’re easy to view at larger font sizes too. When you use [SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols), you get icons...
- **Keep text truncation to a minimum as font size increases.**
  In general, aim to display as much useful text at the largest accessibility font size as you do at the largest standard font size. Avoid truncating text in scrollable regions unless people can open a separate view to read the rest of...
- **Consider adjusting your layout at large font sizes.**
  When font size increases in a horizontally constrained context, inline items (like glyphs and timestamps) and container boundaries can crowd text and cause truncation or overlapping. To improve readability, consider using a stacked...
- **Maintain a consistent information hierarchy regardless of the current font size.**
  For example, keep primary elements toward the top of a view even when the font size is very large, so that people don’t lose track of these elements.
- **When necessary, use dynamic system font variants to match the text in standard controls.** `[macOS]`
  Dynamic system font variants give your text the same look and feel of the text that appears in system-provided controls. Use the variants listed below to achieve a look that’s consistent with other apps on the platform.
- **In general, prefer 2D text.** `[visionOS]`
  The more visual depth text characters have, the more difficult they can be to read. Although a small amount of 3D text can provide a fun visual element that draws people’s attention, if you’re going to display content that people need...
- **Make sure text looks good and remains legible when people scale it.** `[visionOS]`
  Use a text style that makes the text look good at full scale, then test it for legibility at different scales.
- **Maximize the contrast between text and the background of its container.** `[visionOS]`
  By default, the system displays text in white, because this color tends to provide a strong contrast with the default system background material, making text easier to read. If you want to use a different text color, be sure to test it...
- **If you need to display text that’s not on a background, consider making it bold to improve legibility.** `[visionOS]`
  In this situation, you generally want to avoid adding shadows to increase text contrast. The current space might not include a visual surface on which to cast an accurate shadow, and you can’t predict the size and density of shadow that...
- **Keep text facing people as much as possible.** `[visionOS]`
  If you display text that’s associated with a point in space, such as a label for a 3D object, you generally want to use *billboarding* — that is, you want the text to face the wearer regardless of how they or the object move. If you...

## Undo and redo
<sub>`pages/undo-and-redo.md`</sub>

- **Help people predict the results of undo and redo as much as possible.**
  On iPhone, for example, you can describe the result in the alert that displays when people shake the device, giving them the option of performing the undo or canceling it. If you provide undo and redo menu items, you can modify the menu...
- **Show the results of an undo or redo.**
  Sometimes, the most recent action that people want to undo affects content or an area that’s no longer visible. In cases like this, it’s crucial to highlight the result of each undo and redo to keep people from thinking that the action...
- **Let people undo multiple times.**
  Avoid placing unnecessary limits on the number of times people can undo or redo. People generally expect to undo every action they’ve performed since taking a logical step like opening a document or saving their work.
- **Consider giving people the option to revert multiple changes at once.**
  In some scenarios, people might appreciate the ability to undo a batch of discrete but related actions — like incremental adjustments to a single property or attribute — so they don’t have to undo each individual adjustment. In other...
- **Provide undo and redo buttons only when necessary.**
  People generally expect to initiate undo and redo in system-supported ways, such as choosing the items in a macOS app’s Edit menu, using keyboard shortcuts on a Mac or iPad, or shaking their iPhone. If it’s important to provide...
- **Avoid redefining standard gestures for undo and redo.** `[iOS, iPadOS]`
  For example, people can use a three-finger swipe to initiate an undo or redo, or shake their iPhone. As with all standard gestures, redefining them in your interface runs the risk of confusing people and making your experience...
- **Briefly and precisely describe the operation to be undone or redone.** `[iOS, iPadOS]`
  The undo and redo alert title automatically includes a prefix of “Undo ” or “Redo ” (including the trailing space). You need to provide an additional word or two that describes what’s being undone or redone, to appear after this prefix....
- **Place undo and redo commands in the Edit menu and support the standard keyboard shortcuts.** `[macOS]`
  Mac users expect to find undo and redo at the top of the Edit menu; they also expect to use Command–Z and Shift–Command–Z to perform undo and redo, respectively.

## Virtual keyboards
<sub>`pages/virtual-keyboards.md`</sub>

- **Choose a keyboard that matches the type of content people are editing.**
  For example, you can help people enter numeric data by providing the numbers and punctuation keyboard. When you specify a semantic meaning for a text input area, the system can automatically provide a keyboard that matches the type of...
- **ASCII capable**
- **ASCII capable number pad**
- **Email address**
- **Name phone pad**
- **Numbers and punctuation**
- **Consider customizing the Return key type if it helps clarify the text-entry experience.**
  The Return key type is based on the keyboard type you choose, but you can change this if it makes sense in your app. For example, if your app initiates a search, you can use a search Return key type rather than the standard one so the...
- **Make sure your custom input view makes sense in the context of your app.**
  In addition to making data entry simple and intuitive, you want people to understand the benefits of using your custom input view. Otherwise, they may wonder why they can’t regain the system keyboard while in your app.
- **Play the standard keyboard sound while people type.**
  The keyboard sound provides familiar feedback when people tap a key on the system keyboard, so they’re likely to expect the same sound when they tap keys in your custom input view. People can turn keyboard sounds off for all keyboard...
- **Provide an obvious and easy way to switch between keyboards.**
  People know that the Globe key on the standard keyboard — which replaces the dedicated Emoji key when multiple keyboards are available — quickly switches to other keyboards, and they expect a similarly intuitive experience in your keyboard.
- **Avoid duplicating system-provided keyboard features.**
  On some devices, the Emoji/Globe key and Dictation key automatically appear beneath the keyboard, even when people are using custom keyboards. Your app can’t affect these keys, and it’s likely to be confusing if you repeat them in your...
- **Consider providing a keyboard tutorial in your app.**
  People are used to the standard keyboard, and learning how to use a new keyboard can take time. You can help make the process easier by providing usage instructions in your app — for example, you might tell people how to choose your...
- **Use the keyboard layout guide to make the keyboard feel like an integrated part of your interface.** `[iOS, iPadOS]`
  Using the layout guide also helps you keep important parts of your interface visible while the virtual keyboard is onscreen. For developer guidance, see [Adjusting your layout with keyboard layout...
- **Place custom controls above the keyboard thoughtfully.** `[iOS, iPadOS]`
  Some apps position an input accessory view containing custom controls above the keyboard to offer app-specific functionality related to the data people are working with. For example, Numbers displays controls that help people apply...

## VoiceOver
<sub>`pages/voiceover.md`</sub>

- **Provide alternative labels for all key interface elements.**
  VoiceOver uses alternative labels (which aren’t visible onscreen) to audibly describe your app’s interface. System-provided controls have generic labels by default, but you should provide more descriptive labels that convey your app’s...
- **Describe meaningful images.**
  If you don’t describe key images in your app’s content, people can’t use VoiceOver to fully experience them within your app. Because VoiceOver helps people understand the interface surrounding images too, such as nearby captions,...
- **Make charts and other infographics fully accessible.**
  Provide a concise description of each infographic that explains what it conveys. If people can interact with the infographic to get more or different information, make these interactions available to people using VoiceOver, too. The...
- **Exclude purely decorative images from VoiceOver.**
  It’s unnecessary to describe images that are decorative and don’t convey useful or actionable information. Excluding these images shows respect for people’s time and reduces cognitive load when they use VoiceOver. For developer...
- **Use titles and headings to help people navigate your information hierarchy.**
  The title is the first information someone receives from an assistive technology when arriving on a page or screen in your app. Offer unique titles that succinctly describe each page’s content and purpose. Likewise, use accurate section...
- **Specify how elements are grouped, ordered, or linked.**
  Proximity, alignment, and other visible contextual cues help sighted people perceive the relationships between elements. Examine your app for places where relationships among elements are visual only. Then, describe these relationships...
- **Inform VoiceOver when visible content or layout changes occur.**
  People may find an unexpected content or layout change confusing because it means their mental map of the content is no longer accurate. It’s crucial to report visible changes so VoiceOver and other assistive technologies can help...
- **Support the VoiceOver rotor when possible.**
  People can use an interface element called the VoiceOver rotor to navigate a document or webpage by headings, links, and other content types. You can help people navigate content in your app by identifying these elements to the rotor....
- **Be mindful that custom gestures aren’t always accessible.** `[visionOS]`
  When VoiceOver is turned on in visionOS, apps and games that define custom gestures don’t receive hand input by default. This ensures people can explore the interface using their voice, without an app responding to hand input at the...

## Wallet
<sub>`pages/wallet.md`</sub>

- **Offer to add new passes to Wallet.**
  When an action results in a new pass, like purchasing an event ticket or registering for a store reward program, you can present system UI that adds the pass to Wallet with one tap. For frequent, predictable actions like checking in for...
- **Help people add a pass created outside your app.**
  If someone creates a pass using your website or another device, suggest adding it to Wallet the next time they open your app. If people decline your suggestion, don’t ask them again.
- **Add related passes as a group.**
  If your app generates multiple passes, like boarding passes for a multi-connection flight, add all passes at once so people don’t have to add each one individually. If your website distributes a group of passes, such as a set of event...
- **Display an Add to Apple Wallet button to let people add an existing pass not already in Wallet.**
  If someone previously declined your suggestion to add a pass to Wallet — or if they removed the pass — a button makes it easy to add the pass if they change their mind. You can display an Add to Apple Wallet button wherever...
- **Let people jump from your app to their pass in Wallet.**
  Wherever your app displays information about a pass that exists in Wallet, you can offer a link that opens it directly. Label the link something like “View in Wallet.”
- **Tell the system when your passes expire.**
  Wallet automatically hides expired passes to reduce crowding, and provides a button that lets people revisit them. To help ensure the system hides passes appropriately, set the expiration date, relevant date, and voided properties of...
- **Always get permission before deleting passes from Wallet.**
  For example, you could include an in-app setting that lets people specify whether they want to delete passes manually or allow automatic removal. If necessary, you can show an alert before deleting a pass.
- **Help the system suggest a pass when relevant.**
  Ideally, passes automatically appear when they’re needed so people don’t have to manually locate them. When you provide information about when and where your pass is relevant, the system can display a link to it on the Lock Screen when...
- **Keep passes up to date.**
  Physical passes don’t typically change, but a digital pass can reflect changes as they happen. An airline boarding pass, for example, can automatically update to display flight delays and gate changes.
- **Use change messages only for updates to time-critical information.**
  A change message interrupts people, so send one only for updates they need to know about. For example, people need to know when there’s a gate change for a flight, but they don’t need to know when a customer service phone number...
- **Design a pass that looks great and works well on all devices.**
  Passes can look different depending on the device. For example, a pass on Apple Watch shows less information and fewer images than on iPhone. Don’t put essential information in elements that might be unavailable on certain devices, and...
- **Keep the pass front uncluttered.**
  Show essential information, like an event date or account balance, in the header so people can see it when the pass is collapsed in Wallet. Use the rest of the pass front for information people need quick access to. Place details people...
- **Make your pass instantly identifiable.**
  Use brand colors and visual elements like images, icons, and full-art backgrounds to help people recognize your pass at a glance.
- **Ensure sufficient contrast between background and text colors.**
  Pick label colors that keep text legible against both solid backgrounds and background images.
- **Use language that works on any device.**
  Passes can appear on multiple devices, so use text that makes sense everywhere. For example, “Slide to view” is meaningful on iPhone but doesn’t apply on Apple Watch.
- **Reserve pass images for visual content.**
  Embedded text isn’t accessible and may not be visible if images don’t display on all devices. For text information, use text fields and semantic tags instead. Use Pass Designer or corresponding APIs to add barcodes rather than embedding...
- **Keep image file sizes small.**
  People can receive passes via email or a webpage. To make downloads as fast as possible, use the smallest image files that still look great.
- **Provide a pass icon.**
  The system uses it to represent your pass on the Lock Screen, in Mail, and on passes in Wallet. You can use your app icon or design a separate one.
- **Avoid inner drop shadows on logo artwork.**
  They can reduce legibility when the logo renders on the pass.
- **Non-poster pass backgrounds**
- **Poster pass backgrounds**
- **Make it easy for people to add an order to Wallet.**
  For example, when a customer completes an Apple Pay transaction in your app or website, use [PKPaymentOrderDetails](https://developer.apple.com/documentation/passkit/pkpaymentorderdetails) (app) or...
- **Make information about an order available immediately after people place it.**
  People need to confirm that their order was received, even when payment, processing, and fulfillment are still pending. If you won’t have details until a later time, provide the data you have at the time of the order and supply a status...
- **Provide fulfillment information as soon as it’s available, and keep the status up to date.**
  When you supply fulfillment data or you change the status of an order, the system updates the order information and can automatically send a notification to customers. The system uses the fulfillment status you report to update the...
- **Supply a high-resolution logo image that uses a nontransparent background.**
  The system displays your logo image in the dashboard and detail view, so you want to make sure that people can instantly recognize it at various sizes. Use the PNG or JPEG format to create a logo image that measures 300x300 pixels. To...
- **Supply distinct, high-resolution product images that use nontransparent backgrounds.**
  The system displays a product’s image — along with descriptive information you supply — in the detail views, order dashboard, and notifications for an order or a fulfillment. When creating a product image, use a straightforward...
- **In general, keep text brief.**
  People appreciate being able to read text at a glance, and the system can truncate text that’s too long.
- **Use clear, approachable language, and localize the text you provide.**
  You want to make sure that all your customers can read the information in an order. Also, make sure the price you show matches the final price the customer confirmed.
- **Provide a link to an area where people manage their order.**
  When you provide a universal link, people can open your order management area even if they don’t have your app installed. To learn more about universal links, see [Allowing apps and websites to link to your...
- **Clearly describe each item so people can verify that their order contains everything they expect.**
  You can use the [LineItem](https://developer.apple.com/documentation/walletorders/lineitem) property to provide information like a product’s price, name, and image. An order lists the line items for every item the customer ordered; a...
- **Supply a prioritized list of your apps that might be installed on the device.**
  The system uses this list when it needs to display a link to your app within the order details view. For example, if you provide multiple apps and more than one of them is installed on the device, the system displays a link to the...
- **Avoid sending duplicate notifications.**
  For example, you can tell the system to avoid sending order-related notifications through Wallet when the customer has one of your associated apps installed.
- **Make it easy for customers to contact the merchant.**
  Provide multiple contact methods, so people can choose the one that works best for them. At minimum, you need to provide a link to the merchant’s website or landing page, but you can also provide a Messages for Business link, a phone...
- **Help people track their order.**
  A multi-item order can have multiple fulfillments, where each fulfillment is either shipping or pickup. For example, if a customer orders a pair of shoes and a T-shirt, the customer might want to have one item shipped, while picking up...
- **Keep the fulfillment screen centered on order tracking.**
  For example, if you recommend your app or other services to customers, be sure to prioritize order-tracking information over other content in the screen.
- **Choose shipping-fulfillment values that match the details you have about the shipping process.**
  If you know the carrier, enter its name in the `carrier` property; otherwise, leave the default “Track Shipment” value. If you can access details about a carrier’s interim shipping steps — such as when a fulfillment is on the way or out...
- **Keep customers informed through relevant fulfillment status descriptions.**
  A great status message is approachable, accurate, and clearly related to the status it describes. In addition to supplying information that helps people understand the status of their order, a status message also gives you an...
- **Be direct and thorough when describing an Issue or Canceled status.**
  People generally need to know why there’s a problem and what they can do about it.
- **Present a Wallet verification option only when the device supports it.**
  If the current device can’t return the identity information you request, don’t display a Verify with Apple Wallet button. Be prepared to present a fallback view that offers a different verification method if Verify with Apple Wallet...
- **Ask for identity information only at the precise moment you need it.**
  People can be suspicious of a request for personal information if it doesn’t seem to be related to their current action. If your app needs identity verification, for example, wait to ask for this information until people are completing...
- **Clearly and succinctly describe the reason you need the information you’re requesting.**
  You must write text that explains why people need to share identity information with your app (this text is called a *purpose string* or *usage description string*). The system displays your purpose string in the verification sheet so...
- **Ask only for the data you actually need.**
  People may lose trust in your app if you ask for more data than you need to complete the current task or action. For example, if you need to ensure that a customer is at least a certain age, use a request that specifies an age...
- **Clearly indicate whether you will keep the data and — if you need to keep it — specify how long you’ll do so.**
  To help people trust your app, it’s essential to explain how long you might need to keep the personal information they agree to share with you. When you use PassKit APIs to specify a duration — such as a particular period, indefinitely,...
- **Choose the system-provided verification button that matches your use case and the visual design of your app.**
  The system provides the following button labels to support various use cases:

## Watch faces
<sub>`pages/watch-faces.md`</sub>

- **Help people discover your app by sharing watch faces that feature your complications.**
  Ideally, you support multiple complications so that you can showcase them in a shareable watch face and provide a curated experience. For some watch faces, you can also specify a system accent color, images, or styles. If people add...
- **Display a preview of each watch face you share.**
  Displaying a preview that highlights the advantages of your watch face can help people visualize its benefits. You can get a preview by using the iOS Watch app to email the watch face to yourself. The preview includes an illustrated...
- **Aim to offer shareable watch faces for all Apple Watch devices.**
  Some watch faces are available on Series 4 and later — such as California, Chronograph Pro, Gradient, Infograph, Infograph Modular, Meridian, Modular Compact, and Solar Dial — and Explorer is available on Series 3 (with cellular) and...
- **Respond gracefully if people choose an incompatible watch face.**
  The system sends your app an error when people try to use an incompatible watch face on Series 3 or earlier. In this scenario, consider immediately offering an alternative configuration that uses a compatible face instead of displaying...

## Web views
<sub>`pages/web-views.md`</sub>

- **Support forward and back navigation when appropriate.**
  Web views support forward and back navigation, but this behavior isn’t available by default. If people are likely to use your web view to visit multiple pages, allow forward and back navigation, and provide corresponding controls to...
- **Avoid using a web view to build a web browser.**
  Using a web view to let people briefly access a website without leaving the context of your app is fine, but Safari is the primary way people browse the web. Attempting to replicate the functionality of Safari in your app is unnecessary...

## Widgets
<sub>`pages/widgets.md`</sub>

- **Extra large portrait**
- **Accessory circular**
- **Accessory corner**
- **Accessory inline**
- **Accessory rectangular**
- **iPhone Lock Screen**
- **Watch complication**
- **Smart Stack on Apple Watch**
- **Choose simple ideas that relate to your app’s main purpose.**
  Include timely content and relevant functionality. For example, people who use the Weather app are often most interested in the current high and low temperatures and weather conditions, so the Weather widgets prioritize this information.
- **Aim to create a widget that gives people quick access to the content they want.**
  People appreciate widgets that display meaningful content and offer useful actions and deep links to key areas of your app. Replicating an app icon offers little additional value, and people may be less likely to keep it on their screens.
- **Prefer dynamic information that changes throughout the day.**
  If a widget’s content never appears to change, people may not keep it in a prominent position. Although widgets don’t update from minute to minute, it’s important to find ways to keep their content fresh to invite frequent viewing.
- **Look for opportunities to surprise and delight.**
  For example, you might design a unique visual treatment for your calendar widget to display on meaningful occasions, like birthdays or holidays.
- **Offer widgets in multiple sizes when doing so adds value.**
  Small widgets use their limited space to typically show a single piece of information while larger sizes support additional layers of information and actions. Avoid expanding a smaller widget’s content to simply fill a larger area. It’s...
- **Balance information density.**
  Sparse layouts can make the widget seem unnecessary, while overly dense layouts are less glanceable. Create a layout that provides essential information at a glance and allows people to view additional details by taking a longer look....
- **Display only the information that’s directly related to the widget’s main purpose.**
  In larger widgets, you can display more data — or more detailed visualizations of the data — but you don’t want to lose sight of the widget’s primary purpose. For example, all Calendar widgets display a person’s upcoming events. In each...
- **Use brand elements thoughtfully.**
  Incorporate brand colors, typefaces, and stylized glyphs to make your widget recognizable but don’t overpower useful information or make your widget look out of place. When you include brand elements, people seldom need your logo or app...
- **Choose between automatically displaying content and letting people customize displayed information.**
  In some cases, people need to configure a widget to ensure it displays the information that’s most useful for them. For example, the Stocks widget lets people select the stocks they wish to track. In contrast, some widgets — like the...
- **Avoid mirroring your widget’s appearance within your app.**
  Including an element in your app that looks like your widget but doesn’t behave like it can confuse people. Additionally, people may be less likely to try other ways to interact with such an element in your app because they expect it to...
- **Let people know when authentication adds value.**
  If your widget provides additional functionality when someone is signed in to your app, make sure people know that. For example, an app that shows upcoming reservations might include a message like “Sign in to view reservations” when...
- **Keep your widget up to date.**
  Finding the appropriate update frequency for your widget depends on knowing how often the data changes and estimating when people need to see new data. For example, a widget that provides information about tidal conditions at a beach is...
- **Use system functionality to refresh dates and times in your widget.**
  Because widget update frequency is limited, let the system automatically refresh date and time information to preserve update opportunities. Determine the update frequency that fits with the data you display and show content quickly...
- **Use animated transitions to bring attention to data updates.**
  By default, many SwiftUI views animate content updates. Additionally, use standard and custom animations with a duration of up to two seconds to let people know when new information is available or when content displays differently. For...
- **Offer simple, relevant functionality and reserve complexity for your app.**
  Useful widgets offer an easy way to complete a task or action that’s directly related to its content.
- **Ensure that a widget interaction opens your app at the right location.**
  Deep link to details and actions that directly relate to the widget’s content, and don’t make people navigate to the relevant area in the app. For example, when people click or tap a medium Stocks widget, the Stocks app opens to a page...
- **Offer interactivity while remaining glanceable and uncluttered.**
  Multiple interaction targets — SwiftUI links, buttons, and toggles — might make sense for your content, but avoid creating app-like layouts in your widgets. Pay attention to the size of targets and make sure people can tap or click them...
- **In general, use standard margins to ensure legibility.**
  Use the standard margin width for widgets — 16 points for most widgets — to avoid crowding their edges and creating a cluttered appearance. If you need to use tighter margins — for example, to create content groupings for graphics,...
- **Coordinate the corner radius of your content with the corner radius of the widget.**
  To ensure that your content looks good within a widget’s rounded corners, use a SwiftUI container to apply the correct corner radius. For developer guidance, see...
- **Prefer using the system font, text styles, and SF Symbols.**
  Using the system font helps your widget look at home on any platform, while making it easier for you to display great-looking text in a variety of weights, styles, and sizes. Use SF Symbols to align and scale symbols with text that uses...
- **Avoid very small font sizes.**
  In general, display text using fonts at 11 points or larger. Text in a font that’s smaller than 11 points can be too hard for many people to read.
- **Avoid rasterizing text.**
  Always use text elements and styles to ensure that your text scales well and to allow VoiceOver to speak your content.
- **Use color to enhance a widget’s appearance without competing with its content.**
  Beautiful colors draw the eye, but they’re best when they don’t prevent people from absorbing a widget’s information at a glance. In your asset catalog, you can also specify the colors you want the system to use as it generates your...
- **Convey meaning without relying on specific colors to represent information.**
  Widgets can appear monochromatic (with or without a custom tint color), and in watchOS, the system may invert colors depending on the watch face a person chooses. Use text and iconography in addition to color to express meaning.
- **Use full-color images judiciously.**
  When a person chooses a tinted or clear appearance for their widgets, the system by default desaturates full-color images. You can choose to render images in full-color, even when a person chooses a tinted or clear widget appearance....
- **Support light and dark appearances.**
  Prefer light backgrounds for the light appearance and dark backgrounds for the dark appearance, and consider using the semantic system colors for text and backgrounds to let the colors dynamically adapt to the current appearance. You...
- **Group widget components into an accented and a primary group.**
  The accented rendering mode divides the widget’s view hierarchy into an accent group and a primary group. On iPhone, iPad, and Mac, the system tints primary and accented content white. On Apple Watch, the system tints primary content...
- **Offer enough contrast to ensure legibility.**
  In the vibrant rendering mode, the opacity of pixels within an image determines the strength of the blurred background material effect. Fully transparent pixels let the background material pass through as is. The brightness of pixels...
- **Create optimized assets for the best vibrant effect.**
  Render content like images, numbers, and text at full opacity. Use white or light gray for the most prominent content and darker grayscale values for secondary elements to establish hierarchy. Confirm that image content has sufficient...
- **Design a realistic preview to display in the widget gallery.**
  Highlighting your widget’s capabilities — and clearly representing the experiences each widget type or size can provide — helps people make an informed decision. You can display real data in your widget preview, but if the data takes...
- **Design placeholder content that helps people recognize your widget.**
  An installed widget displays placeholder content while its data loads. Create an effective placeholder appearance by combining static interface components with semi-opaque shapes that stand in for dynamic content. For example, use...
- **Write a succinct widget description.**
  The widget gallery displays descriptions that help people understand what each widget does. Begin a description with an action verb — for example, “See the current weather conditions and forecast for a location” or “Keep track of your...
- **Group your widget’s sizes together, and provide a single description.**
  If your widget is available in multiple sizes, group them together so people don’t think each size is a different widget. Provide a single description of your widget — regardless of how many sizes you offer — to avoid repetition and to...
- **Consider coloring the Add button.**
  After people choose your app in the widget gallery, an Add button appears below the group of widgets you offer. You can specify a color for this button to help remind people of your brand.
- **Support the Always-On display on iPhone.** `[iOS, iPadOS]`
  Devices with the Always-On display render widgets on the Lock Screen with reduced luminance. Use levels of gray that provide enough contrast in the Always-On display, and make sure your content remains legible.
- **Offer Live Activities to show real-time updates.** `[iOS, iPadOS]`
  Widgets don’t show real-time information. If your app allows people to track the progress of a task or event for a limited amount of time with frequent updates, consider offering Live Activities. Widgets and Live Activities use the same...
- **Limit usage of rich images or color to convey meaning in StandBy.** `[iOS, iPadOS]`
  Instead, make use of the additional space by scaling up and rearranging text so people can glance at the widget content from a greater distance. To seamlessly blend with the black background, don’t use background colors for your widget...
- **Correct usage** `[iOS, iPadOS]`
- **Incorrect usage** `[iOS, iPadOS]`
- **Adapt your design and content for the spatial experience Apple Vision Pro provides.** `[visionOS]`
  In visionOS, widgets don’t float in isolation but are part of living rooms, kitchens, offices, and more. Consider this context early and think of widgets as part of someone’s surroundings when you bring your existing widgets to visionOS...
- **Test your widgets across the full range of system color palettes and in different lighting conditions.** `[visionOS]`
  Make sure your widget’s tone, contrast, and legibility remain consistent and intentional. If you choose to exclude UI elements from tinting, test your widget in every provided tint color palette to make sure the untinted elements remain...
- **Design a responsive layout that shows the right level of detail for each of the two thresholds.** `[visionOS]`
  When a person views the widget at a distance, display a simplified version of your widget that shows fewer details and has a larger type size, and remove interactive elements like buttons or toggles. When a person views the widget from...
- **Offer widget family sizes that fit a person’s surroundings well.** `[visionOS]`
  Widgets map to real-world dimensions and have a permanent presence in a person’s spatial environment. Think about where people might place your widget — mounted to a wall, placed on a sideboard, or sitting next to a workplace — and...
- **Display content in a way that remains legible from a range of distances.** `[visionOS]`
  To make a widget feel intentional and proportionate to where they place it, people can scale a widget from 75 to 125 percent in size. Use print design principles like clear hierarchy, strong typography, and scale to make sure your...
- **Choose the mounting style that fits your content and the experience you want to create.** `[visionOS]`
  By default, visionOS widgets use the elevated mounting style, which is ideal for content that you want to stand out and feel present, like reminders, media, or glanceable data. Recessed widgets are ideal for immersive or ambient...
- **Test your elevated widget designs with each system-provided frame width.** `[visionOS]`
  People can choose from different system-defined frame widths for widgets that use the elevated mounting style. You can’t change your layout based on the frame width a person chooses, so make sure your widget layout stays visually...
- **Choose the paper style for a print-like look that feels more like a real object in the room.** `[visionOS]`
  The entire widget responds to the ambient lighting and blends naturally into its surroundings. For example, the Music poster widget uses the paper style to display albums and playlists like framed artwork on a wall.
- **Choose the glass style for information-rich widgets.** `[visionOS]`
  Glass visually separates foreground and background elements, allowing you to decide which parts of your interface adapt to the surroundings and which stay visually consistent. Foreground elements appear in full color, unaffected by...
- **Provide a colorful background that conveys meaning.** `[watchOS]`
  By default, widgets in the Smart Stack use a black background. Consider using a custom background color that provides additional meaning. For example, the Stocks app uses a red background for falling stock values and a green background...
- **Encourage the system to display or elevate the position of your watchOS widget in the Smart Stack.** `[watchOS]`
  Relevancy information helps the system show your widget when people need it most. Relevance can be location-based or specific to ongoing system actions, like a workout. For developer guidance, see...

## Windows
<sub>`pages/windows.md`</sub>

- **Make sure that your windows adapt fluidly to different sizes to support multitasking and multiwindow workflows.**
  For guidance, see [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) and [Multitasking](https://developer.apple.com/design/human-interface-guidelines/multitasking).
- **Choose the right moment to open a new window.**
  Opening content in a separate window is great for helping people multitask or preserve context. For example, Mail opens a new window whenever someone selects the Compose action, so both the new message and the existing email are visible...
- **Consider providing the option to view content in a new window.**
  While it’s best to avoid opening new windows as default behavior unless it benefits your user experience, it’s also great to give people the flexibility of viewing content in multiple ways. Consider letting people view content in a new...
- **Avoid creating custom window UI.**
  System-provided windows look and behave in a way that people understand and recognize. Avoid making custom window frames or controls, and don’t try to replicate the system-provided appearance. Doing so without perfectly matching the...
- **Use the term *window* in user-facing content.**
  The system refers to app windows as *windows* regardless of type. Using different terms — including *scene*, which refers to window implementation — is likely to confuse people.
- **Make sure window controls don’t overlap toolbar items.** `[iPadOS]`
  When windowed, app windows include window controls at the leading edge of the toolbar. If your app has toolbar buttons at the leading edge, they might be hidden by window controls when they appear. To prevent this, instead of placing...
- **Consider letting people use a gesture to open content in a new window.** `[iPadOS]`
  For example, people can use the pinch gesture to expand a Notes item into a new window. For developer guidance, see...
- **Make sure custom windows use the system-defined appearances.** `[macOS]`
  People rely on the visual differences between windows to help them identify the foreground window and know which window will accept their input. When you use system-provided components, a window’s background and button appearances...
- **Avoid putting critical information or actions in a bottom bar, because people often relocate a window in a way that hides its bottom edge.** `[macOS]`
  If you must include one, use it only to display a small amount of information directly related to a window’s contents or to a selected item within it. For example, Finder uses a bottom bar (called the status bar) to display the total...
- **Prefer using a window to present a familiar interface and to support familiar tasks.** `[visionOS]`
  Help people feel at home in your app by displaying an interface they’re already comfortable with, reserving more [Immersive experiences](https://developer.apple.com/design/human-interface-guidelines/immersive-experiences) for the...
- **Retain the window’s glass background.** `[visionOS]`
  The default glass background helps your content feel like part of people’s surroundings while adapting dynamically to lighting and using specular reflections and shadows to communicate the window’s scale and position. Removing the glass...
- **Choose an initial window size that minimizes empty areas within it.** `[visionOS]`
  By default, a window measures 1280x720 pt. When a window first opens, the system places it about two meters in front of the wearer, giving it an apparent width of about three meters. Too much empty space inside a window can make it look...
- **Aim for an initial shape that suits a window’s content.** `[visionOS]`
  For example, a default Keynote window is wide because slides are wide, whereas a default Safari window is tall because most webpages are much longer than they are wide. For games, a tower-building game is likely to open in a taller...
- **Choose a minimum and maximum size for each window to help keep your content looking great.** `[visionOS]`
  People appreciate being able to resize windows as they customize their space, but you need to make sure your layout adjusts well across all sizes. If you don’t set a minimum and maximum size for a window, people could make it so small...
- **Minimize the depth of 3D content you display in a window.** `[visionOS]`
  The system adds highlights and shadows to the views and controls within a window, giving them the appearance of [Depth](https://developer.apple.com/design/human-interface-guidelines/spatial-layout#Depth) and helping them feel more...
- **Prefer using a volume to display rich, 3D content.** `[visionOS]`
  In contrast, if you want to present a familiar, UI-centric interface, it generally works best to use a [visionOS windows](https://developer.apple.com/design/human-interface-guidelines/windows#visionOS-windows).
- **Place 2D content so it looks good from multiple angles.** `[visionOS]`
  Because a person’s perspective changes as they move around a volume, the location of 2D content within it might appear to change in ways that don’t make sense. To pin 2D content to specific areas of 3D content inside a volume, you can...
- **In general, use dynamic scaling.** `[visionOS]`
  Dynamic scaling helps a volume’s content remain comfortably legible and easy to interact with, even when it’s far away from the viewer. On the other hand, if you want a volume’s content to represent a real-world object, like a product...
- **Take advantage of the default baseplate appearance to help people discern the edges of a volume.** `[visionOS]`
  In visionOS 2 and later, the system automatically makes a volume’s horizontal “floor,” or *baseplate*, visible by displaying a gentle glow around its border when people look at it. If your content doesn’t fill the volume, the...
- **Consider offering high-value content in an ornament.** `[visionOS]`
  In visionOS 2 and later, a volume can include an ornament in addition to a toolbar and tab bar. You can use an ornament to reduce clutter in a volume and elevate important views or controls. When you use an attachment anchor to specify...
- **Choose an alignment that supports the way people interact with your volume.** `[visionOS]`
  As people move a volume, the baseplate can remain parallel to the floor of a person’s surroundings, or it can tilt to match the angle at which a person is looking. In general, a volume that remains parallel to the floor works well for...

## Workouts
<sub>`pages/workouts.md`</sub>

- **In a watchOS fitness app, use workout sessions to provide useful data and relevant controls.**
  During a fitness app’s active workout sessions, watchOS continues to display the app as time passes between wrist raises, so it’s important to provide the workout data people are most likely to care about. For example, you might show...
- **Avoid distracting people from a workout with information that’s not relevant.**
  For example, people don’t need to review the list of workouts you offer or access other parts of your app while they’re working out. Here is an arrangement that many watchOS workout apps use, including Workout:
- **Use a distinct visual appearance to indicate an active workout.**
  During a workout, people appreciate being able to recognize an active session at a glance. The metrics page can be a good way to show that a session is active because the values update in real time. In addition to displaying updating...
- **Provide workout controls that are easy to find and tap.**
  In addition to making it easy for people to pause, resume, and stop a workout, be sure to provide clear feedback that indicates when a session starts or stops.
- **Help people understand the health information your app records if sensor data is unavailable during a workout.**
  For example, water may prevent a heart-rate measurement, but your app can still record data like the distance people swam and the number of calories they burned. If your app supports the *Swimming* or *Other* workout types, explain the...
- **Provide a summary at the end of a session.**
  A summary screen confirms that a workout is finished and displays the recorded information. Consider enhancing the summary by including Activity rings, so that people can easily check their current progress.
- **Discard extremely brief workout sessions.**
  If a session ends a few seconds after it starts, either discard the data automatically or ask people if they want to record the data as a workout.
- **Make sure text is legible for when people are in motion.**
  When a session requires movement, use large font sizes, high-contrast colors, and arrange text so that the most important information is easy to read.
- **Use Activity rings correctly.**
  The Activity rings view is an Apple-designed element featuring one or more rings whose colors and meanings match those in the Activity app. Use them only for their documented purpose.

## Writing
<sub>`pages/writing.md`</sub>

- **Determine your app’s voice.**
  Think about who you’re talking to, so you can figure out the type of vocabulary you’ll use. What types of words are familiar to people using your app? How do you want people to feel? The words for a banking app might convey trust and...
- **Match your tone to the context.**
  Once you’ve established your app’s voice, vary your tone based on the situation. Consider what people are doing while they’re using your app — both in the physical world and within the app itself. Are they exercising and reached a goal?...
- **Write for everyone.**
  For your app to be useful for as many people as possible, it needs to speak to as many people as possible. Choose simple, plain language and write with accessibility and localization in mind, avoiding jargon and gendered terminology....
- **Consider each screen’s purpose**
  . Pay attention to the order of elements on a screen, and put the most important information first. Format your text to make it easy to read. If you’re trying to convey more than one idea, consider breaking up the text onto multiple...
- **Be action oriented.**
  Active voice and clear labels help people navigate through your app from one step to the next, or from one screen to another. When labeling buttons and links, it’s almost always best to use a verb. Prioritize clarity and avoid the...
- **Build language patterns.**
  Consistency builds familiarity, helping your app feel cohesive, intuitive, and thoughtfully designed. It also makes writing for your app easier, as you can return to these patterns again and again.
- **Adopt capitalization rules that align with your app’s style, then apply them consistently.**
  While certain components, like [Content](https://developer.apple.com/design/human-interface-guidelines/buttons#Content), have specific guidelines, how you format text reflects your app’s voice. Title case is generally considered formal,...
- **Give clear guidance and use consistent language throughout processes with multiple steps.**
  If your app has a flow that spans multiple screens, decide how you want to label the actions that take people from one step to the next. Begin with language like “Get Started” to indicate you’re starting a flow. You can use the button...
- **Use possessive pronouns sparingly.**
  Possessive pronouns like *my* and *your* are often unnecessary to establish context. For example, “Favorites” conveys the same message as “Your Favorites,” and is more succinct. If you do use possessive pronouns, use them consistently...
- **Write for how people use each device.**
  People may use your app on several types of devices. While your language needs to be consistent across them, think about where it would be helpful to adjust your text to make it suitable for different devices. Make sure you describe...
- **Provide clear next steps on any blank screens.**
  An empty state, like a completed to-do list or bookmarks folder with nothing in it, can provide a good opportunity to make people feel welcome and educate them about your app. Empty states can also showcase your app’s voice, but make...
- **Write clear error messages.**
  It’s always best to help people avoid errors. When an error message is necessary, display it as close to the problem as possible, avoid blame, and be clear about what someone can do to fix it. For example, “That password is too short”...
- **Choose the right delivery method.**
  There are many ways to get people’s attention, whether or not they are actively using your app. When there’s something you want to communicate, consider the urgency and importance of the message. Think about the context in which someone...
- **Keep settings labels clear and simple.**
  Help people easily find the settings they need by labeling them as practically as possible. If the setting label isn’t enough, add an explanation. Describe what it does when turned on, and people can infer the opposite. In the...
- **Show hints in text fields.**
  If your app allows people to enter their own text, like account or contact information, label all fields clearly, and use hint or placeholder text so people know how to format the information. You can give an example in hint text, like...

## iCloud
<sub>`pages/icloud.md`</sub>

- **Make it easy to use your app with iCloud.**
  People turn on iCloud in Settings and expect apps to work with it automatically. If you think people might want to choose whether to use iCloud with your app, show a simple option the first time your app opens that provides a choice...
- **Avoid asking which documents to keep in iCloud.**
  Most people expect all of their content to be available in iCloud and don’t want to manage the storage of individual documents. Consider how your app handles and exposes content, and try to perform more file-management tasks automatically.
- **Keep content up to date when possible.**
  In an app that supports iCloud, it’s best when people always have access to the most recent content. However, you need to balance this experience with respect to device storage and bandwidth constraints. If your app works with very...
- **Respect iCloud storage space.**
  iCloud is a finite resource for which people pay. Use iCloud to store information people create and understand, and avoid using it for app resources or content you can regenerate. Even if your app doesn’t implement iCloud support,...
- **Make sure your app behaves appropriately when iCloud is unavailable.**
  If someone manually turns off iCloud or turns on Airplane Mode, you don’t need to display an alert notifying them iCloud is unavailable. However, it may still be helpful to unobtrusively let people know that changes they make won’t be...
- **Keep app state information in iCloud.**
  In addition to storing documents and other files, you can use iCloud to store settings and information about the state of your app. For example, a magazine app might store the last page viewed so when the app is opened on another...
- **Warn about the consequences of deleting a document.**
  When someone deletes a document in an app that supports iCloud, the document is removed from iCloud and all other devices too. Show a warning and ask for confirmation before performing the deletion.
- **Make conflict resolution prompt and easy.**
  To the extent possible, try to detect and resolve version conflicts automatically. If this can’t be done, display an unobtrusive notification that makes it easy to differentiate and choose between the conflicting versions. Ideally,...
- **Include iCloud content in search results.**
  People with iCloud accounts assume their content is universally available, and they expect search results to reflect this perspective.
- **For games, consider saving player progress in iCloud.**
  Although you can implement this functionality yourself, the GameSave framework offers an efficient solution. It synchronizes save data across devices and offers built-in alerts you can use to help players handle syncing issues during...

## iMessage apps and stickers
<sub>`pages/imessage-apps-and-stickers.md`</sub>

- **Prefer providing one primary experience in your iMessage app.**
  People are in a conversational flow when they choose your app, so your functionality or content needs to be easy to understand and immediately available. If you want to provide multiple types of functionality or different collections of...
- **Consider surfacing content from your iOS or iPadOS app.**
  For example, your iMessage app could offer app-specific information that people might want to share — such as a shopping list or a trip itinerary — or support a simple, collaborative task, like deciding where to go for a meal or which...
- **Present essential features in the compact view.**
  People can experience your iMessage app in a compact view that appears below the message transcript, or they can expand the view to occupy most of the window. Make sure the most frequently used items are available in the compact view,...
- **In general, let people edit text only in the expanded view.**
  The compact view occupies roughly the same space as the keyboard. To ensure that the iMessage app’s content remains visible while people edit, display the keyboard in the expanded view.
- **Create stickers that are expressive, inclusive, and versatile.**
  Whether your stickers are rich, static images or short animations, make sure that each one remains legible against a wide range of backgrounds and when rotated or scaled. You can also use transparency to help people visually integrate a...
- **For each sticker, provide a localized alternative description.**
  VoiceOver can help people use your sticker pack by speaking a sticker’s alternative description.
