# Prints "<bundle id>\t<entitlements file>" for every target in the generated
# Xcode project, so the unsigned build can be ad-hoc signed with each bundle's
# own entitlements (SideStore and AltStore read them from the signature).
require 'xcodeproj'
ios_dir = ARGV[0]
proj = Xcodeproj::Project.open(Dir.glob(File.join(ios_dir, '*.xcodeproj')).first)
proj.native_targets.each do |t|
  cfg = t.build_configurations.find { |c| c.name == 'Release' } || t.build_configurations.first
  bid = cfg.build_settings['PRODUCT_BUNDLE_IDENTIFIER']
  ent = cfg.build_settings['CODE_SIGN_ENTITLEMENTS']
  next if bid.nil? || ent.nil?
  path = File.expand_path(ent.gsub('$(SRCROOT)', ios_dir).gsub('$(PROJECT_DIR)', ios_dir), ios_dir)
  puts "#{bid}\t#{path}" if File.exist?(path)
end
