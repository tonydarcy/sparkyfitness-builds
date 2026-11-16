"""Adds a build to altstore-source.json, the SideStore/AltStore source that
lets installed copies of Sparky Dev see new builds in SideStore's Updates tab.

Usage: update_altstore_source.py SOURCE_JSON IPA_URL IPA_SIZE VERSION BUILD COMMIT
"""
import json
import sys
from datetime import datetime, timezone

path, url, size, version, build, commit = sys.argv[1:7]
BUNDLE_ID = "org.SparkyApps.SparkyFitnessMobile1.dev"
ICON = "https://raw.githubusercontent.com/tonydarcy/SparkyFitness/tdmain/SparkyFitnessMobile/assets/icons/appstore.png"
KEEP = 5

try:
    with open(path) as f:
        source = json.load(f)
except FileNotFoundError:
    source = {}

source.update({
    "name": "Sparky Dev builds",
    "identifier": "io.github.tonydarcy.sparkyfitness-builds",
    "subtitle": "Test builds of SparkyFitness from tonydarcy/SparkyFitness",
    "iconURL": ICON,
    "website": "https://github.com/tonydarcy/sparkyfitness-builds",
})
source.setdefault("news", [])
apps = source.setdefault("apps", [])
app = next((a for a in apps if a.get("bundleIdentifier") == BUNDLE_ID), None)
if app is None:
    app = {"bundleIdentifier": BUNDLE_ID, "versions": []}
    apps.append(app)
app.update({
    "name": "Sparky Dev",
    "developerName": "tonydarcy",
    "subtitle": "SparkyFitness test build",
    "localizedDescription": "SparkyFitness built from Tony's fork. Installs alongside the official app.",
    "iconURL": ICON,
    "tintColor": "#E53238",
    "category": "health-fitness",
    "appPermissions": {"entitlements": [], "privacy": {}},
})
entry = {
    "version": version,
    "buildVersion": build,
    "date": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "localizedDescription": f"Build {build} from commit {commit}.",
    "downloadURL": url,
    "size": int(size),
    "minOSVersion": "16.4",
}
versions = [v for v in app.get("versions", []) if v.get("buildVersion") != build]
app["versions"] = ([entry] + versions)[:KEEP]

with open(path, "w") as f:
    json.dump(source, f, indent=2)
    f.write("\n")
