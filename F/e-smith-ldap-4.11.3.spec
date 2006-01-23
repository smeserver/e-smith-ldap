Summary: e-smith server and gateway - LDAP module
%define name e-smith-ldap
Name: %{name}
%define version 4.11.3
%define release 08
Version: %{version}
Release: %{release}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-ldap-4.11.3-02.mitel_patch
Patch1: e-smith-ldap-4.11.3-02.domain_change.patch
Patch2: e-smith-ldap-4.11.3-02.public_access.patch
Patch3: e-smith-ldap-4.11.3-02.public_access.patch2
Patch4: e-smith-ldap-4.11.3-utf8.patch
Packager: e-smith developers <bugs@e-smith.com>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-base
Requires: e-smith-lib >= 1.15.1-16
Requires: openldap >= 2.0.0, perl(Net::LDAP)
BuildRequires: e-smith-devtools >= 1.13.1-03
AutoReqProv: no

%description
e-smith server and gateway software - LDAP module.

%changelog
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
- removed extraneous rmdir in %setup that was breaking the build

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
rm root/etc/e-smith/events/actions/ldap-rebuild
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
mkdir -p root/etc/e-smith/tests
perl createlinks
mkdir -p root/etc/rc.d/rc7.d
ln -s /etc/rc.d/init.d/e-smith-service root/etc/rc.d/rc7.d/S80ldap
mkdir -p root/home/e-smith/db/ldap

mkdir -p root/etc/rc.d/init.d/supervise
ln -s ../daemontools root/etc/rc.d/init.d/supervise/ldap

mkdir -p root/service
ln -s /var/service/ldap root/service/ldap
touch root/var/service/ldap/down

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    --file /var/service/ldap/run 'attr(0750,root,root)' \
    --file /var/service/ldap/finish 'attr(0750,root,root)' \
    > %{name}-%{version}-%{release}-filelist
echo "%doc COPYING" >> %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
