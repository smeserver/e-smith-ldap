# $Id: e-smith-ldap.spec,v 1.87 2010/12/02 00:46:05 slords Exp $

Summary: e-smith server and gateway - LDAP module
%define name e-smith-ldap
Name: %{name}
%define version 5.2.0
%define release 74
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: %{name}-%{version}.backend
Patch1: %{name}-%{version}-schema.patch
Patch2: %{name}-%{version}-convert_ldif.patch
Patch3: %{name}-%{version}-password.patch
Patch4: %{name}-%{version}-tls.patch
Patch5: %{name}-%{version}-user-lock-event.patch
Patch6: %{name}-%{version}-admin_user.patch
Patch7: %{name}-%{version}-users_groups_ous.patch2
Patch8: %{name}-%{version}-attributes.patch
Patch9: %{name}-%{version}-mailboxRelatedObject.patch
Patch10: %{name}-%{version}-force_ssl_tls_for_auth.patch
Patch11: %{name}-%{version}-sme8b-db.patch
Patch12: %{name}-%{version}-admin_user2.patch
Patch13: %{name}-%{version}-ibay_password.patch
Patch14: %{name}-%{version}-fix-indention.patch
Patch15: %{name}-%{version}-email-domain-change.patch
Patch16: %{name}-%{version}-update-admin.patch
Patch17: %{name}-%{version}-empty_group.patch
Patch18: e-smith-ldap-5.2.0-ldap_logs.patch
Patch19: e-smith-ldap-5.2.0-force_enabled.patch
Patch20: e-smith-ldap-5.2.0-index_memberuid.patch
Patch21: e-smith-ldap-5.2.0-expand_slapd_on_ldap_update.patch
Patch22: e-smith-ldap-5.2.0-split_acl_templates.patch
Patch23: e-smith-ldap-5.2.0-exop.patch
Patch24: e-smith-ldap-5.2.0-dump_ldif.patch
Patch25: e-smith-ldap-5.2.0-add_computers_ou.patch
Patch26: e-smith-ldap-5.2.0-add_posixaccount_attr_in_ldap.patch
Patch27: e-smith-ldap-5.2.0-full_path_to_config.patch
Patch28: e-smith-ldap-5.2.0-add_samba_attr_in_ldap.patch
Patch29: e-smith-ldap-5.2.0-code_cleanup.patch
Patch30: e-smith-ldap-5.2.0-base_oid.patch
Patch31: e-smith-ldap-5.2.0-rename_old_record.patch
Patch32: e-smith-ldap-5.2.0-add_ibay_machine.patch
Patch33: e-smith-ldap-5.2.0-rename_old_record_fix.patch
Patch34: e-smith-ldap-5.2.0-rename_old_record_fix2.patch
Patch35: e-smith-ldap-5.2.0-delete_extra_items.patch
Patch36: e-smith-ldap-5.2.0-ldif_template.patch
Patch37: e-smith-ldap-5.2.0-fix_ldap_delete.patch
Patch38: e-smith-ldap-5.2.0-better_ldif.patch
Patch39: e-smith-ldap-5.2.0-ldap_update_several_groups.patch
Patch40: e-smith-ldap-5.2.0-anonymous_acl.patch
Patch41: e-smith-ldap-5.2.0-users_acl.patch
Patch42: e-smith-ldap-5.2.0-toggle_anonymous_access.patch
Patch43: e-smith-ldap-5.2.0-fix_anonymous_toggle.patch
Patch44: e-smith-ldap-5.2.0-link_ldap_update.patch
Patch45: e-smith-ldap-5.2.0-update_group_membership_on_delete.patch
Patch46: e-smith-ldap-5.2.0-ldap_update_later.patch
Patch47: e-smith-ldap-5.2.0-allow_authenticated_users_to_read_attrs.patch
Patch48: e-smith-ldap-5.2.0-add_nobody_and_shared_in_ldap.patch
Patch49: e-smith-ldap-5.2.0-fix_nobody_and_shared_group.patch
Patch50: e-smith-ldap-5.2.0-add_www_move_nobody.patch
Patch51: e-smith-ldap-5.2.0-fix_ldap_update.patch
Patch52: e-smith-ldap-5.2.0-ldap-init-script.patch
Patch53: e-smith-ldap-5.2.0-enable_ldap_init.patch
Patch54: e-smith-ldap-5.2.0-ldap-auth.patch
Patch55: e-smith-ldap-5.2.0-unix-cleanup.patch
Patch56: e-smith-ldap-5.2.0-group-attrs.patch
Patch57: e-smith-ldap-5.2.0-simple-ldap-update.patch
Patch58: e-smith-ldap-5.2.0-fixe_ldif_templates.patch
Patch59: e-smith-ldap-5.2.0-locked-passwd.patch
Patch60: e-smith-ldap-5.2.0-startup-order.patch
Patch61: e-smith-ldap-5.2.0-remove_bogus_junk.patch
Patch62: e-smith-ldap-5.2.0-ldapmodify.patch
Patch63: e-smith-ldap-5.2.0-fix-department.patch
Patch64: e-smith-ldap-5.2.0-update-ldap-later.patch
Patch65: e-smith-ldap-5.2.0-ldap-init.patch
Patch66: e-smith-ldap-5.2.0-replace-logic.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-base
Requires: e-smith-lib >= 1.15.1-16
Requires: openldap >= 2.0.0
Requires: openldap-clients
Requires: perl(Net::LDAP)
Requires: e-smith-formmagick >= 1.4.0-9
BuildRequires: e-smith-devtools >= 1.13.1-03
AutoReqProv: no

%description
e-smith server and gateway software - LDAP module.

%changelog
* Wed Dec 1 2010 Shad L. Lords <slord@mail.com> 5.2.0-74.sme
- Fix replace logic in ldif-fix [SME: 6423]

* Wed Dec 1 2010 Shad L. Lords <slord@mail.com> 5.2.0-73.sme
- Fix permissions on ldif-fix script [SME: 6244]

* Wed Dec 1 2010 Shad L. Lords <slord@mail.com> 5.2.0-72.sme
- Replace convert_ldif with ldif-fix script [SME: 6244]
- Remove ldif template and expansion [SME: 6421]
- Simplify ldap-update call by calling ldif-fix [SME: 6422]

* Tue Nov 30 2010 Shad L. Lords <slord@mail.com> 5.2.0-71.sme
- Update ldap database later to pick up samba group maps [SME: 6419]

* Tue Nov 30 2010 Shad L. Lords <slord@mail.com> 5.2.0-70.sme
- Use correct field (Dept) for ou ldap field [SME: 6417]

* Tue Nov 30 2010 Shad L. Lords <slord@mail.com> 5.2.0-69.sme
- Add rfc2739.schem back in and include in config so upgrades work [SME: 5159]

* Tue Nov 30 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-68.sme
- Use ldapmodify to load ldif, add -a if no changetype [SME: 6413]

* Tue Nov 23 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-67.sme
- Remove bogus junk attribute from ldif templates [SME: 6396]

* Mon Nov 22 2010 Shad L. Lords <slord@mail.com> 5.2.0-66.sme
- Change startup order for ldap [SME: 6390]

* Thu Nov 11 2010 Shad L. Lords <slord@mail.com> 5.2.0-65.sme
- Store locked password instead of expired password [SME: 6360]

* Wed Nov 10 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-64.sme
- Fixed ldif templates error [SME: 6356]

* Mon Nov 8 2010 Shad L. Lords <slords@mail.com> 5.2.0-63.sme
- Simplify ldap-update for most events [SME: 6354]

* Fri Nov 5 2010 Shad L. Lords <slords@mail.com> 5.2.0-62.sme
- Adjust call to ldap-update later create/modify/delete [SME: 6284]

* Thu Nov 4 2010 Shad L. Lords <slords@mail.com> 5.2.0-61.sme
- Apply correct patch for group descriptions/password [SME: 6337]

* Thu Nov 4 2010 Shad L. Lords <slords@mail.com> 5.2.0-60.sme
- groups don't have password, some don't have description [SME: 6337]

* Tue Nov 2 2010 Shad L. Lords <slords@mail.com> 5.2.0-59.sme
- Remove unix users/groups if ldap is master [SME: 6325]

* Tue Nov 2 2010 Shad L. Lords <slords@mail.com> 5.2.0-58.sme
- Disable ldap-delete if ldap is master [SME: 6324]

* Tue Nov 02 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-57.sme
- Enable the new ldap.init service [SME: 6231]

* Sat Oct 30 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-56.sme
- Fix a small typo in reset-ldap-bootstrap [SME: 6231]

* Fri Oct 29 2010 Shad L. Lords <slords@mail.com> 5.2.0-55.sme
- Add ldap.init script to allow update on reconfig/reboot [SME: 6231]

* Thu Oct 28 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-54.sme
- Fix minor errors in ldap-update [SME: 6312]

* Wed Oct 27 2010 Shad L. Lords <slords@mail.com> 5.2.0-53.sme
- Add www user/group to ldap [SME: 6312]

* Wed Oct 27 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-52.sme
- Fixes for nobody and shared groups [SME: 6310]

* Wed Oct 27 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-51.sme
- Add nobody and shared groups in LDAP [SME: 6310]

* Thu Oct 14 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-50.sme
- Allow authenticated users to read posixAccount and shadowAccount attrs [SME: 6254]

* Wed Oct 13 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-49.sme
- call ldap-update later during group and user creation [SME: 6284]

* Thu Oct 7 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-48.sme
- Update group membership for deleted accounts [SME: 6276]

* Thu Oct 7 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-47.sme
- Don't call ldap-update on deleted accounts [SME: 6239]

* Thu Oct 7 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-46.sme
- Link ldap-update scripts in needed events [SME: 6239]

* Sat Oct 2 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-45.sme
- Fix toggle anonymous access [SME: 6255]

* Sat Oct 2 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-44.sme
- Toggle anonymous access with AnonymousAccess property [SME: 6255]

* Sat Oct 2 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-43.sme
- Allow authenticated users to see more than just their own entry [SME: 6079]

* Sat Oct 2 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-42.sme
- Deny access to some attributes for anonymous users [SME: 6254]

* Mon Sep 27 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-41.sme
- Add ldap-update support for several accounts [SME: 6249]

* Mon Sep 27 2010 Shad L. Lords <slords@mail.com> 5.2.0-40.sme
- Make ldif template create single hash [SME: 6240]

* Mon Sep 27 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-39.sme
- Fix ldap-delete script [SME: 6238]

* Sun Sep 26 2010 Shad L. Lords <slords@mail.com> 5.2.0-38.sme
- Update ldif template to match stored data [SME: 6240]

* Sun Sep 26 2010 Shad L. Lords <slords@mail.com> 5.2.0-37.sme
- Delete all ldap objects that we now create [SME: 6238]

* Sat Sep 25 2010 Shad L. Lords <slords@mail.com> 5.2.0-36.sme
- Ensure required attributes are present for rename [SME: 6235]

* Sat Sep 25 2010 Shad L. Lords <slords@mail.com> 5.2.0-35.sme
- Fix old record lookups from sme7 [SME: 6235]

* Sat Sep 25 2010 Shad L. Lords <slords@mail.com> 5.2.0-34.sme
- Add ibay and machine accounts into ldap [SME: 6236]

* Sat Sep 25 2010 Shad L. Lords <slords@mail.com> 5.2.0-33.sme
- Rename old ldap record from sme7 if exists [SME: 6235]

* Sat Sep 25 2010 Shad L. Lords <slords@mail.com> 5.2.0-32.sme
- Fix/add base ou entries needed for new schema [SME: 6234]

* Sat Sep 25 2010 Shad L. Lords <slords@mail.com> 5.2.0-31.sme
- Rewrite ldap-update to make adding classes easier [SME: 6233]

* Fri Sep 24 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-30.sme
- Add sambaSamAccount attributes in LDAP [SME: 6232]

* Thu Sep 23 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-29.sme
- Use full path to config in the run script [SME: 6222]

* Thu Sep 23 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-28.sme
- Add posixAccount attributes in LDAP [SME: 6074]

* Thu Sep 23 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-27.sme
- Create the Computers OU [SME: 6230]

* Thu Sep 23 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-26.sme
- Dump ldap data during the pre-backup event [SME: 6226]

* Wed Sep 22 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-25.sme
- Send slapd logs in /var/log/ldap (multilog) [SME: 6222]
- Force the service to be enabled [SME: 6221]
- Indexe memberUid attribute [SME: 6220]
- Expand slapd.conf during ldap-update event [SME: 6224]
- Split slapd ACL template [SME: 6225]
- Prevent users from reading their password over a unsecured link [SME: 6252]
- Use md5crypt hash when client requests exop [SME: 6223]

* Wed Sep 22 2010 Daniel Berteaud <daniel@firewall-services.com> 5.2.0-24.sme
- Restrict access to the ldif file [SME: 6217]

* Tue Jun 10 2010 Jonathan Martens <smeserver-contribs@snetram.nl> 5.2.0-23.sme
- Fix ldap-create errors when adding empty groups [SME: 5920]

* Mon Jun  7 2010 Federico Simoncelli <federico.simoncelli@gmail.com> 5.2.0-22.sme
- Update email addresses on domain change (thanks Daniel) [SME: 5984]
- Update admin information (thanks Daniel) [SME: 6014]

* Tue May 4 2010 Jonathan Martens <smeserver-contribs@snetram.nl> 5.2.0-21.sme
- Fix indentation in S25ldap-update script [SME: 5914]

* Fri Apr 30 2010 Filippo Carletti <filippo.carletti@gmail.com> 5.2.0-20.sme
- Don't try to save ibay password to ldap [SME: 5906]

* Mon Mar  1 2010 Daniel B. <daniel@firewall-services.com> 5.2.0-19.sme
- Fix bug reference in spec file

* Mon Mar  1 2010 Filippo Carletti <filippo.carletti@gmail.com> 5.2.0-18.sme
- Fix admin user password change (Daniel B.) [SME: 5810]

* Tue Feb  9 2010 Filippo Carletti <filippo.carletti@gmail.com> 5.2.0-17.sme
- Init database if the ldif dump is empty (ie from sme8b) [SME: 5747]

* Fri Feb 5 2010 Stephen Noble <support@dungog.net> 5.2.0-16.sme
- revert re-init database [SME:5747]

* Fri Feb 5 2010 Stephen Noble <support@dungog.net> 5.2.0-15.sme
- re-init readonly database on post-upgrade [SME:5747]

* Thu Feb 4 2010 Daniel B. <daniel@firewall-services.com> 5.2.0-14.sme
- Force SSL/TLS for remote authentication [SME: 5748]

* Wed Feb 3 2010 Stephen Noble <support@dungog.net> 5.2.0-13.sme
- reuse users_groups_ous.patch2 [SME: 5743]

* Wed Feb 3 2010 Stephen Noble <support@dungog.net> 5.2.0-12.sme
- Separate groups and users with mailboxRelatedObject [SME:5749]

* Wed Feb 3 2010 Stephen Noble <support@dungog.net> 5.2.0-11.sme
- Set readonly access [SME:5752]

* Sun Jan 31 2010 Stephen Noble <support@dungog.net> 5.2.0-10.sme
- Fix ldap-update action script to user-lock event [SME: 5720]

* Sun Jan 31 2010 Stephen Noble <support@dungog.net> 5.2.0-9.sme
- Fix Groups entries [SME: 5743]

* Sun Jan 31 2010 Stephen Noble <support@dungog.net> 5.2.0-8.sme
- Add Groups entries [SME: 5743]

* Sun Jan 31 2010 Stephen Noble <support@dungog.net> 5.2.0-7.sme
- Add admin user as a standard user [SME: 5742]

* Sat Jan 30 2010 Jonathan Martens <smeserver-contribs@snetram.nl> 5.2.0-6.sme
- Add ldap-update action script to user-lock event [SME: 5720]

* Wed Jan 27 2010 Federico Simoncelli <federico.simoncelli@gmail.com> 5.2.0-5.sme
- Add ldap authentication and tls support [SME: 5720]

* Wed Jan 13 2010 Filippo Carletti <filippo.carletti@gmail.com> 5.2.0-4.sme
- Update schema for newer openldap and remove calFBurl [SME: 5159]
- Convert ldif dump [SME: 5446]

* Sun Feb  8 2009 Charlie Brady <charlie_brady@mitel.com> 5.2.0-3.sme
- Create bdb log directory. [SME: 3018]

* Tue Jan 27 2009 Charlie Brady <charlie_brady@mitel.com> 5.2.0-2.sme
- Change ldap backend to bdb, and fix initialisation problem.
  [SME: 3018, 2859]

* Tue Oct 7 2008 Shad L. Lords <slords@mail.com> 5.2.0-1.sme
- Roll new stream to separate sme7/sme8 trees [SME: 4633]

* Wed Aug 20 2008 Shad L. Lords <slords@mail.com> 4.13.0-1
- Roll new dev stream.

* Fri Jul 25 2008 Shad L. Lords <slords@mail.com> 4.12.0-11
- Separate template to avoid breaking schema [SME: 4171]

* Sat Jul 5 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 4.12.0-10
- Add common <base> tags to e-smith-formmagick's general [SME: 4279]

* Tue Apr 1 2008 Shad L. Lords <slords@mail.com> 4.12.0-9
- Add free/busy URL entry to help kronolith contribs [SME: 1806]

* Wed Feb 13 2008 Stephen Noble <support@dungog.net> 4.12.0-8
- Remove <base> tags now in general [SME: 3919]

* Tue Jun 26 2007 Charlie Brady <charlie_brady@mitel.com>
- Fix format error in ldif template. [SME: 3107]

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Mon Feb 19 2007 Charlie Brady <charlie_brady@mitel.com> 4.12.0-6
- Don't tell slapd to create pid and args files that we don't need
  and don't use (and can't create with later openldap version).
  [SME: 2477]

* Sat Jan 13 2007 Shad L. Lords <slords@mail.com> 4.12.0-5
- Make success/failure messages standard [SME: 2289]

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Wed Nov 08 2006 Charlie Brady <charlie_brady@mitel.com> 4.12.0-03
- Correct permissions on slapd.conf. [SME: 2037]

* Thu Sep 28 2006 Charlie Brady <charlie_brady@mitel.com> 4.12.0-02
- Don't attempt to create IPv6 socket (log noise). [SME: 1946]

* Wed Mar 15 2006 Charlie Brady <charlie_brady@mitel.com> 4.12.0-01
- Roll stable stream version. [SME: 1016]

* Sun Jan 22 2006 Charlie Brady <charlieb@e-smith.com> 4.11.3-08
- Use correct utf8 encoding for non-ascii attributes. [SME: 537]

* Fri Jan 20 2006 Charlie Brady <charlieb@e-smith.com> 4.11.3-07
- Reexpand hosts.allow template during ldap-update. [SME: 520]

* Thu Jan 19 2006 Charlie Brady <charlieb@e-smith.com> 4.11.3-06
- Reexpand masq template during ldap-update. [SME: 520]

* Mon Jan 16 2006 Charlie Brady <charlieb@e-smith.com> 4.11.3-05
- Remove obsolete ldap-rebuild script. [SME: 463]

* Sun Jan 15 2006 Charlie Brady <charlieb@e-smith.com> 4.11.3-04
- Delete old contents of directory if domain name is changed.
  [SME: 393]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 4.11.3-03
- Bump release number only

* Mon Nov 21 2005 Charlie Brady <charlieb@e-smith.com>
- [4.11.3-02]
- Work around slapd's failure to accept 'objectClass: group' (in spite
  of schema checking being disabled). [SF: 1362868]

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.11.3-01]
- Remove L10Ns from base packages [SF: 1309520]

* Fri Oct 14 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.11.2-01]
- New dev stream before relocating L10Ns

* Fri Sep 30 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.11.1-19]
- Added Italian L10N - Thanks Filippo Carletti [SF: 1309266]

* Mon Sep 26 2005 Gordon Rowell <gordonr@e-smith.com>
- [4.11.1-18]
- Added German L10N - Thanks Dietmar Berteld [SF: 1293325]

* Tue Sep  6 2005 Charlie Brady <charlieb@e-smith.com>
- [4.11.1-17]
- Add template fragment to allow bind using LDAP version
  2. [SF: 1282697]

* Wed Jul 27 2005 Charlie Brady <charlieb@e-smith.com>
- [4.11.1-16]
- Move masq fragement from template to db [SF: 1241415]
- Remove all use of deprecated esmith::config API.

* Mon Jun 13 2005 Charlie Brady <charlieb@e-smith.com>
- [4.11.1-15]
- Remove unused and deprecated kerberosobject schema.

* Fri Apr 15 2005 Charlie Brady <charlieb@e-smith.com>
- [4.11.1-14]
- Fix typo in services2adjust symlink for apache.

* Fri Apr 15 2005 Charlie Brady <charlieb@e-smith.com>
- [4.11.1-13]
- Drop back to simple schema, and 6.x version of ldap-update script.
  More thought needed about how to extend the schema and how to handle
  property deletions.

* Thu Apr 14 2005 Charlie Brady <charlieb@e-smith.com>
- [4.11.1-12]
- Remove full restart of apache from panel, and add sigusr1 to ldap-update
  event handling.
- Update ldif file templates and ldap-update script to fill out the schema
  a little, to remove bogus adding of user attribute to group entries, and
  to allow removal of properties which have been nulled out.

* Fri Apr  1 2005 Charlie Brady <charlieb@e-smith.com>
- [4.11.1-11]
- Comment out for now the utf8 conversion, as it's not working
  yet.

* Wed Mar 23 2005 Charlie Brady <charlieb@e-smith.com>
- [4.11.1-10]
- Remove explicit generic_template_expand symlink in ldap-update
  event - not required.
- Create "finish" script to do ldif file dump on shutdown.
- Add templates for ldif file used during ldap rebuild.
- Handle latin->utf8 conversion in ldif templates.

* Tue Mar  8 2005 Charlie Brady <charlieb@e-smith.com>
- [4.11.1-09]
- Use generic adjust-services in place of adjust-masq [MN00065576]

* Tue Mar  8 2005 Charlie Brady <charlieb@e-smith.com>
- [4.11.1-08]
- Remove dangling ldap-conf symlink. [MN00064130]

* Tue Jan 25 2005 Charlie Brady <charlieb@e-smith.com>
- [4.11.1-07]
- Remove ldap-delete-dumps from post-backup event. It leaves ldap
  stopped and with no directory contents. [MN00025069]
- Added ldap-delete-dumps to post-backup to prevent potential ldap database
  clobbering on post-upgrade. [msoulier MN00025069]
- Update e-smith-devtools BuildRequires, and createlinks script.
  [MN00064130]

* Tue Jan 18 2005 Charlie Brady <charlieb@e-smith.com>
- [4.11.1-06]
- Use generic_template_expand action where possible, in place
  of specific actions. Update e-smith-lib dependency. [MN00064130]

* Wed Dec 29 2004 Charlie Brady <charlieb@e-smith.com>
- [4.11.1-05]
- Create missing /service symlink, and add down file to service
  directory to control startup sequence. [charlieb MN00062133]

* Mon Dec 20 2004 Charlie Brady <charlieb@e-smith.com>
- [4.11.1-04]
- Use supervise to run slapd. [charlieb MN00062133]

* Tue Nov  9 2004 Charlie Brady <charlieb@e-smith.com>
- [4.11.1-03]
- Include redhat/rfc822-MailMember.schema specification from earlier
  RedHat openldap packages (missing in RHEL3). [charlieb MN00056724]
- Remove deprecated ldap-startup script. Add ldap service default fragments
  and a migrate fragment to initialize the password. [charlieb MN00056726]
- Remove obsolete conf-migrate-ldap-variables action [charlieb MN00056733]

* Tue Sep 28 2004 Michael Soulier <msoulier@e-smith.com>
- [4.11.1-02]
- Updated requires with new perl dependencies. [msoulier MN00040240]

* Mon May 10 2004 Michael Soulier <msoulier@e-smith.com>
- [4.11.1-01]
- Updated createlinks.
- Added ldap-delete-dumps to post-backup to prevent potential ldap database
  clobbering on post-upgrade. [msoulier MN00025069]

* Thu Sep  4 2003 Charlie Brady <charlieb@e-smith.com>
- [4.11.0-01]
- Changing version to development stream number - 4.11.0

* Wed Jul  9 2003 Charlie Brady <charlieb@e-smith.com>
- [4.10.0-02]
- Avoid restart of slapd during bootstrap-console-save event.
  [charlieb 9338]

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [4.10.0-01]
- Changing version to stable stream number - 4.10.0

* Tue May  6 2003 Lijie Deng <lijied@e-smith.com>
- [4.9.0-12]
- Add Spanish lexicon for directory panel [lijied 3793]

* Wed Apr 16 2003 Michael Soulier <msoulier@e-smith.com>
- [4.9.0-11]
- Modified French translation [lijied 7949]
- Modified ldap-dump to take its domainname from /etc/openldap/ldap.conf, and
  be aware of domainname changes. [msoulier 6747]

* Thu Apr  3 2003 Lijie Deng <lijied@e-smith.com>
- [4.9.0-10]
- Removed 'Mitel Networks SME Server' branding [lijied 8016]

* Thu Mar 27 2003 Lijie Deng <lijied@e-smith.com>
- [4.9.0-09]
- Modified French lexicon to use lang="fr", rename the lexicon
  directory to fr [lijied 6787]

* Tue Mar 25 2003 Lijie Deng <lijied@e-smith.com>
- [4.9.0-08]
- Modified directory access en-us and fr-ca text [lijied 4081]
 
* Tue Mar 18 2003 Lijie Deng <lijied@e-smith.com>
- [4.9.0-07]
- Split out ./etc/openldap/ldap.conf/template-begin [lijied 3295]

* Mon Mar 17 2003 Lijie Deng <lijied@e-smith.com>
- [4.9.0-06]
- Deleted empty template-end file [lijied 3295]

* Thu Mar  6 2003 Lijie Deng <lijied@e-smith.com>
- [4.9.0-05]
- Modified directory panel order [lijied 7356]

* Tue Mar  4 2003 Lijie Deng <lijied@e-smith.com>
- [4.9.0-04]
- Split en-us lexicon from directory panel [lijied 4030]

* Fri Feb 28 2003 Lijie Deng <lijied@e-smith.com>
- [4.9.0-03]
- s/HostsAllowSpec/hosts_allow_spec/ [charlieb 5650]
- Remodified the lexicon file  [lijied 5003]

* Fri Feb 28 2003 Charlie Brady <charlieb@e-smith.com>
- [4.9.0-02]
- Added French lexicon for directory [lijied 5003]
- Re-do hosts.allow template to use esmith::ConfigDB::HostsAllowSpec.
  Add dependency on up-to-date e-smith-lib. [charlieb 5650]

* Wed Nov 20 2002 Mike Dickson <miked@e-smith.com>
- [4.9.0-01]
- Changing to development stream; version upped to 4.9.0

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [4.8.0-01]
- Roll to maintained version number to 4.8.0

* Wed Oct  2 2002 Charlie Brady <charlieb@e-smith.com>
- [4.7.6-14]
- Override the default backgrounding of ldap restart in 
  gentle-ldap-dump action [charlieb 2745]
- Remove deprecated serviceControl enable/disable calls from
  ldap-startup [charlieb 4458]

* Tue Sep 24 2002 Mark Knox <markk@e-smith.com>
- [4.7.6-13]
- Use esmith::util and shut down LDAP in foreground [markk 2745]

* Tue Sep 24 2002 Mark Knox <markk@e-smith.com>
- [4.7.6-12]
- Add pre-restore event and ldap-delete-dumps action [markk 2745]

* Thu Sep 12 2002 Charlie Brady <charlieb@e-smith.com>
- [4.7.6-11]
- Fix permission/ownership of /etc/openldap/slapd.conf. [charlieb 4862]

* Tue Sep 10 2002 Charlie Brady <charlieb@e-smith.com>
- [4.7.6-10]
- Remove redundant "my" in ldap-rebuild (causes warning). [charlieb 2745]

* Thu Sep  5 2002 Charlie Brady <charlieb@e-smith.com>
- [4.7.6-09]
- Remove stray ; (where are those code police?). [charlieb 2745]

* Tue Sep  3 2002 Charlie Brady <charlieb@e-smith.com>
- [4.7.6-08]
- Fix $c->get('DomainName') => $c->get('DomainName')->value snafu
  [charlieb 2745]

* Mon Sep  2 2002 Charlie Brady <charlieb@e-smith.com>
- [4.7.6-07]
- Fix Domain => DomainName snafu. [charlieb 2745]

* Thu Aug 29 2002 Charlie Brady <charlieb@e-smith.com>
- [4.7.6-06]
- Create new gentle-ldap-dump action, and include it in pre-backup
  event. [charlieb 2745]

* Thu Aug 29 2002 Charlie Brady <charlieb@e-smith.com>
- [4.7.6-05]
- Revert ldap-dump to slapcat version, and remove symlinks from all
  actions. The ldap init script is being modified to call ldap-dump
  after slapd shutdown. [charlieb 4739]

* Tue Aug 27 2002 Charlie Brady <charlieb@e-smith.com>
- [4.7.6-04]
- Rewrite ldap-dump to use Net::LDAP::LDIF so that it reads data from
  ldap daemon rather than directly from ldap db files. [charlieb 4057]

* Tue Aug 27 2002 Charlie Brady <charlieb@e-smith.com>
- [4.7.6-03]
- Fix run-time problems in OO conversion of ldap-update [charlieb 4057]

* Fri Aug 23 2002 Charlie Brady <charlieb@e-smith.com>
- [4.7.6-02]
- Change ldap-rebuild to build directory using LDIF dump if found,
  and new data otherwise.  [charlieb 4057]
- Re-write ldap-update and ldap-rebuild to use OO db accesses,
  for clarity.  [charlieb 4057]
- Dump LDAP directory every time we change it. [charlieb 4057]

* Tue Aug 20 2002 Charlie Brady <charlieb@e-smith.com>
- [4.7.6-01]
- Add program to do LDIF dump of ldap directory. [charlieb 4057]

* Mon Aug 19 2002 Charlie Brady <charlieb@e-smith.com>
- [4.7.5-01]
- Remove unnecessary actions: ldap-rebuild from console-save event and
  ldap-conf from ldap-update event. [charlieb 4057]
- Change ldap-update action so that when run during the ldap-update
  event it iterates through user and group accounts and updates records
  with current values. Link ldap-update action into ldap-update event
  in place of ldap-rebuild action. [charlieb 4057]

* Mon Aug 19 2002 Charlie Brady <charlieb@e-smith.com>
- [4.7.4-01]
- Use new adjust-masq action rather than restart-masq during ldap-update.
  [charlieb 4501]

* Thu Aug 15 2002 Charlie Brady <charlieb@e-smith.com>
- [4.7.3-01]
- Add rc7.d symlink and don't set deprecated InitscriptsOrder property
  [charlieb 4458]
- Change use of allow_tcp_in() function to allow dynamic reconfig.
  [charlieb 4501]

* Thu Aug  8 2002 Charlie Brady <charlieb@e-smith.com>
- [4.7.2-01]
- Change inbound rule to use allow_tcp_in() function. The
  function actually implements connection tracking. [charlieb 4499]

* Wed Jul 17 2002 Charlie Brady <charlieb@e-smith.com>
- [4.7.1-01]
- Change masq script fragment to use iptables. [charlieb 1268]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [4.7.0-01]
- Changing version to development stream number 4.7.0

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [4.6.0-01]
- Changing version to maintained stream number to 4.6.0

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.5.10-01]
- RPM rebuild forced by cvsroot2rpm

* Mon May  6 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.5.9-01]
- Localise SAVE button [gordonr 3222]

* Fri May  3 2002 Charlie Brady <charlieb@e-smith.com>
- [4.5.8-01]
- Remove /etc/e-smith/tests/.dummy. Make empty /etc/e-smith/tests in %build.
  [charlieb 3343]

* Wed May  1 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.5.7-01]
- esmith::AccountDB -> esmith::AccountsDB [schwern 3287]

* Thu Apr 25 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.5.6-01]
- Added header and footer to page [gordonr 3223]
- Added nav bar entries to lexicon [gordonr 3155]

* Mon Apr 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.5.5-01]
- Adjusted site-perl -> site_perl

* Mon Apr 15 2002 Gordon Rowell <gordonr@e-smith.com>
- [4.5.4-01]
- Language en-> en-us

* Wed Apr 10 2002 Kirrily Robert <skud@e-smith.com>
- [4.5.3-01]
- Added i18n'd directory panel

* Mon Mar 25 2002 Kirrily Robert <skud@e-smith.com>
- [4.5.2-01]
- Checking for success of CVS import

* Mon Mar 25 2002 Kirrily Robert <skud@e-smith.com>
- [4.5.1-01]
- rollRPM: Rolled version number to 4.5.1-01. Includes patches up to 4.5.0-02.

* Mon Mar 25 2002 Kirrily Robert <skud@e-smith.com>
- [4.5.0-02]
- removed extraneous rmdir in setup section that was breaking the build

* Mon Mar 25 2002 Kirrily Robert <skud@e-smith.com>
- [4.5.0-01]
- rollRPM: Rolled version number to 4.5.0-01. Includes patches up to 4.4.0-08.

* Fri Nov 16 2001 Charlie Brady <charlieb@e-smith.com>
- [4.4.0-08]
- Fix code which adds the "ldap" user - it was trying to use "ldap" as
  a supplementary group (using -G) rather than as initial group (-g).
- Remove two $! from warn statements as they are won't contain useful
  information.

* Wed Nov 07 2001 Tony Clayton <tonyc@e-smith.com>
- [4.4.0-07]
- rebranding to Mitel Networks

* Thu Oct 18 2001 Charlie Brady <charlieb@e-smith.com>
- [4.4.0-06]
- Fix regeneration of ldap password every time slapd.conf was
  re-expanded. See Bugzilla #1966 for details.

* Thu Oct 18 2001 Charlie Brady <charlieb@e-smith.com>
- [4.4.0-05]
- Added code to add "ldap" user and group if necessary

* Tue Aug 28 2001 Gordon Rowell <gordonr@e-smith.com>
- [4.4.0-04]
- Removed deprecated post-restore event directory

* Fri Aug 17 2001 Adrian Chung <adrianc@e-smith.com>
- [4.4.0-03]
- Add restart-httpd-full call to end of web panel, after
  user confirmation of update has been sent.

* Fri Aug 17 2001 gordonr
- [4.4.0-02]
- Autorebuild by rebuildRPM

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [4.4.0-01]
- Rolled version number to 4.4.0-01. Includes patches upto 4.3.1-05.

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [4.3.1-05]
- Use Net::LDAP module in ldap-delete and ldap-update. Something broke
  in the ldap{add,modify,delete} versions of the scripts, and it's easy
  to debug, and probably more efficient to just write to the perl API.

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [4.3.1-04]
- Change uid/gid before execing slapadd, so that created db files have
  correct ownership
- Reformat ldap-rebuild to fit in 80 columns.

* Tue Aug 7 2001 Charlie Brady <charlieb@e-smith.com>
- [4.3.1-03]
- Use slapadd instead of ldif2ldbm program for ldap-rebuild. Use pipe
  rather than temp file.
- Re-add "schemacheck off" to slapd.conf - we don't pass the strict
  checking which is recommended.

* Tue Aug 7 2001 Charlie Brady <charlieb@e-smith.com>
- [4.3.1-02]
- openldap v2 changes - change ownership of slapd.conf, use different
  bundled schema files, and add indexes.

* Tue Aug 7 2001 Charlie Brady <charlieb@e-smith.com>
- [4.3.1-01]
- Rolled version number to 4.3.1-01. Includes patches upto 4.3.0-07.

* Thu Aug 07 2001 Charlie Brady <charlieb@e-smith.com>
- [4.3.0-07]
- Break slapd.conf template into fragments, and include in-line
  at.conf and co.conf fragements, rather than use include feature.
  This is to make configuration stable across versions of openldap.

* Thu Aug 02 2001 Gordon Rowell <gordonr@e-smith.com>
- [4.3.0-06]
- More branding changes

* Sun Jul 29 2001 Jason Miller <jmiller@e-smith.com>
- [4.3.0-05]
- Branding text changes to the directory web panel

* Fri Jul 6 2001 Peter Samuel <peters@e-smith.com>
- [4.3.0-04]
- Change license to GPL

* Wed Jul 04 2001 Gordon Rowell <gordonr@e-smith.com>
- [4.3.0-03]
- Use esmith::util::LdapPassword instead of direct file access

* Tue May 29 2001 Tony Clayton <tonyc@e-smith.com>
- [4.3.0-02]
- fixed actions that had tied %conf when calling serviceControl (2 actions)

* Sun Apr 29 2001 Charlie Brady <charlieb@e-smith.com>
- [4.3.0-01]
- Rolled version number to 4.3.0-01. Includes patches upto 4.2.0-03.

* Thu Feb  8 2001 Adrian Chung <adrianc@e-smith.com>
- Rolling release number for GPG signing.

* Fri Jan 26 2001 Charlie Brady <charlieb@e-smith.com>
- [4.2.0-01]
- Added packet filter fragment to selectively allow external LDAP access
- Linked conf- and restart-masq actions into update-ldap event

* Thu Jan 25 2001 Peter Samuel <peters@e-smith.com>
- [4.2.0-01]
- Rolled version number to 4.2.0-01. Includes patches upto 4.1.0-17.

* Tue Jan 16 2001 Adrian Chung <adrianc@e-smith.com>
- [4.1.0-17]
- Add ldap-rebuild to bootstrap-console-save
- required to initialize ldap database.

* Fri Jan 12 2001 Charlie Brady <charlieb@e-smith.com>
- [4.1.0-16]
- Remove ldap-conf from post-upgrade action (it was occuring before
  ldap-startup, which caused a problem).
- Delete obsolete post-restore action.

* Fri Jan 12 2001 Adrian Chung <adrianc@e-smith.com>
- [4.1.0-15]
- split ldap-rebuild into ldap-conf and ldap-rebuild.

* Thu Jan 11 2001 Gordon Rowell <gordonr@e-smith.com>
- [4.1.0-14]
- Use serviceControl()

* Thu Jan 11 2001 Charlie Brady <charlieb@e-smith.com>
- [4.1.0-13]
- Fix perl warning in migrate variables script - simplify a chunk of code
  while doing it.

* Wed Jan 10 2001 Charlie Brady <charlieb@e-smith.com>
- [4.1.0-12]
- Add genLdapPassword to ldap-startup - it somehow has been lost and never
  happens.
- Remove ldap-startup from console-save
- Add ldap-startup to post-restore action
- Add new bootstrap-console-save event
- Change demo phone number from 999... to 555.... to save UK emergency
  services

* Tue Jan 09 2001 Jason Miller <jmiller@e-smith.com>
- [4.1.0-11]
- updated ldap-startup to set the defaults on a fresh
  installation
- undid some bad changes to the conf-migrate-ldap-variables
  script

* Mon Jan 08 2001 Jason Miller <jmiller@e-smith.com>
- [4.1.0-5] through [4.1.0-9]
- changed directory web panel to read from new configuration
  database parameters
- updated action scripts to take into account the new ldap
  database parameters
- added conf-migrate-ldap-variables as a new action in
  both post-upgrade and post-restore

* Fri Jan 05 2001 Jason Miller <jmiller@e-smith.com>
- [4.1.0-4]
- updated copyright and fixed directory panel error in
  not checking prototypes for subroutines

* Tue Dec 12 2000 Gordon Rowell <gordonr@e-smith.com>
- [4.1.0-3]
- Fixed e-smith-lib dependency

* Mon Dec 11 2000 Tony Clayton <tonyc@e-smith.com>
- [4.1.0-2]
- upgraded ldap-rebuild action to conform to new processTemplate
- created dependency on e-smith-lib-4.1.0-13

* Wed Dec 06 2000 Peter Samuel <peters@e-smith.com>
- [4.1.0-1]
- Rolled version to 4.1.0-1. Includes patches up to 4.0.6-3

* Tue Oct 31 2000 Charlie Brady <charlieb@e-smith.com>
- Fix some old bugs in event scripts - esmith::db was not in use
  list.
- Replace db_get_type calls with db_get_prop
- Re-write ldap hosts.allow template.
- Remove duplicate my $status in ldap-rebuild.

* Mon Oct 30 2000 Charlie Brady <charlieb@e-smith.com>
- Merge services database back into configuration

* Wed Oct 25 2000 Charlie Brady <charlieb@e-smith.com>
- Roll version number to 4.0.6-1.

* Thu Oct 19 2000 Adrian Chung <adrian.chung@e-smith.com>
- Update web/functions/directory script to pass merged
  confServicesCombined hash to esmith::cgi::gen...
  functions.

* Thu Oct 12 2000 Charlie Brady <charlieb@e-smith.com>
- Fix obsolete reference to LDAPServerMode.
- Reformat to break long lines.

* Fri Oct 06 2000 Charlie Brady <charlieb@e-smith.com>
- Delete %post action, and set the default services db value
  in post-install action

* Thu Oct 05 2000 Jason Miller <jay@e-smith.com>
- change .spec to use db:setdefault() function

* Wed Oct 04 2000 Jason Miller <jay@e-smith.com>
- %post event for enabling ldap service automatically
  (no more post-install code required)
- dependencies on e-smith-lib > 0.1-21
- only expand templates if ldapd enabled
- only add to hosts.allow if ldapd enabled
- enable/disable service dependant on services database

* Tue Oct 03 2000 Charlie Brady <charlieb@e-smith.com>
- Update services database when enabling/disabling startup.

* Tue Oct 03 2000 Adrian Chung <mac@e-smith.com>
- Added ldap service checking wrapper to action scripts.

* Mon Sep 25 2000 Paul Nesbit <pkn@e-smith.com>
- replaced references to e-smith.net with e-smith.com

* Fri Aug 25 2000 Charlie Brady <charlieb@e-smith.com>
- Added build dependency on e-smith-devtools, and dependency on
  e-smith-lib. Generate file list with genfilelist.

* Thu Aug 24 2000 Gordon Rowell <gordonr@e-smith.com>
- Rewrote ldap-startup to use serviceControl()

* Wed Jul 12 2000 Joseph Morrison <jdm@e-smith.net>
- Add -1 argument to split commands to handle null final values in
  configuration records

* Fri Jun 16 2000 Charlie Brady <charlieb@e-smith.net>
- Rewrite createlinks in perl
- Don't mark template files as config files.

* Mon Jun 12 2000 Charlie Brady <charlieb@e-smith.net>
- Use new multi-arg form of backgroundCommand.

* Fri Jun 1 2000 Charlie Brady <charlieb@e-smith.net>
- First created - broken out of e-smith-base 4.0.11.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1

%build
mkdir -p root/etc/e-smith/tests
perl createlinks
mkdir -p root/home/e-smith/db/ldap

mkdir -p root/etc/rc.d/init.d/supervise
ln -s ../daemontools root/etc/rc.d/init.d/supervise/ldap

mkdir -p root/service
ln -s /var/service/ldap root/service/ldap
touch root/var/service/ldap/down

mkdir -p root/var/log/bdb
mkdir -p root/var/log/ldap
mkdir -p root/var/service/ldap/ssl
mkdir -p root/etc/e-smith/ldap/init

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    --file /var/service/ldap/run 'attr(0750,root,root)' \
    --file /var/service/ldap/log/run 'attr(0750,root,root)' \
    --file /var/service/ldap/ldif-fix 'attr(0750,root,root)' \
    --file /var/service/ldap/finish 'attr(0750,root,root)' \
    --file /var/service/ldap/control/1 'attr(0750,root,root)' \
    --dir /var/log/bdb 'attr(0700,ldap,ldap)' \
    --dir /home/e-smith/db/ldap 'attr(0750,root,ldap)' \
    --dir /var/log/ldap 'attr(0750,smelog,smelog)' \
    > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
