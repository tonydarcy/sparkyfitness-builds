# sparkyfitness-builds

Personal test builds of the SparkyFitness mobile app from branches of
tonydarcy/SparkyFitness. Both builds use the app's *dev* variant, so they
install alongside the official app.

## Android

Run **Build Android test APK** from the Actions tab. The signed APK is published
as the latest release, and Obtainium installs and updates it.

## iPhone and iPad (free Apple ID, no developer fee)

Run **Build iOS sideload IPA** from the Actions tab (about 30 to 50 minutes on a
macOS runner, free because this repo is public). It publishes an
`ios-build-N` release with a `.ipa` that is not signed for distribution.
SideStore signs it on your device with a free Apple ID.

### One-time setup (needs the Mac once, about 15 minutes)

1. On the iPhone or iPad: Settings > Privacy & Security > Developer Mode, turn it
   on and restart. (It appears after the first sideloaded app if it is not
   there yet.)
2. Install **LocalDevVPN** from the App Store. SideStore uses it to refresh apps
   without a computer.
3. On the Mac, download **iloader** from sidestore.io (or follow the current
   install guide at docs.sidestore.io). Plug the device in with USB, trust the
   computer, sign in with your Apple ID, and install SideStore. It also places
   the pairing file SideStore needs.
4. Open SideStore on the device and sign in with the same Apple ID.

A second Apple ID made just for this is fine, and keeps your main one out of it.

### Install or update SparkyFitness

1. Open the latest `ios-build-N` release on GitHub in Safari and download the
   `.ipa` (it lands in Files > Downloads).
2. Turn on LocalDevVPN, open SideStore > My Apps > **+**, and pick the `.ipa`.
3. When asked about app extensions, keep them for widgets and the workout Live
   Activity, or remove them if you run out of app IDs (see limits below).

The app shows as **Sparky Dev**. A newer build installs over the old one and
keeps its data.

### Updates from SideStore

Add the source once on each device: SideStore > **Sources** > **+**, and paste

    https://raw.githubusercontent.com/tonydarcy/sparkyfitness-builds/main/altstore-source.json

Every iOS build adds itself to that source. A new build then appears in
SideStore's **Updates** tab (pull down to refresh); tap **Update** with
LocalDevVPN on. iOS does not allow silent installs, so the tap is needed.

### Weekly refresh

Free signing lasts 7 days. Before it runs out, turn on LocalDevVPN and tap
**Refresh All** in SideStore; no computer needed. SideStore can also do this
from a Shortcuts automation (for example daily, or when charging). If it does
lapse the app just will not open until refreshed; its data stays.

### Limits of a free Apple ID

- 3 sideloaded apps active per device, and SideStore itself is one of them.
- 10 app IDs per 7 days per Apple ID. This app uses 3 (the app and its two
  widget extensions), or 1 if you remove the extensions. The Apple Watch app
  is left out unless the build is run with "Include the Apple Watch app".
- Push notifications and NFC tags are not available (the app only uses local
  notifications, which still work). HealthKit, camera, location and widgets
  are allowed for free accounts.
- Siri and Lock Screen actions may need you to open the app first, because the
  shared keychain group gets a different prefix after re-signing.

### Using the Mac instead

Sideloadly (sideloadly.io) installs the same `.ipa` over USB or Wi-Fi with a
free Apple ID, but the weekly refresh then needs the Mac. Xcode can also build
`SparkyFitnessMobile` directly with a Personal Team (`APP_VARIANT=dev`), with
the same 7-day limit.
