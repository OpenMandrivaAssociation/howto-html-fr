%define DATE	20080722
%define    language  French
%define    lang      fr
%define format1      html-%{lang}
%define format2      HTML/%{lang}

Summary:   %language HOWTO documents (html format) from the Linux Documentation Project
Name:      howto-%{format1}
Version:	%DATE
Release:	%mkrel 5
Group:		Books/Howtos

Source0:   %name.tar

#	ftp://ftp.traduc.org:/pub/HOWTO/FR/
Url:		http://www.linuxdoc.org/docs.html#howto
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-root
BuildArch:	noarch

BuildRequires: howto-utils
Requires:    locales-%lang, xdg-utils

%description
Linux HOWTOs are detailed documents which describe a specific aspect of 
configuring or using Linux.  Linux HOWTOs are a great source of
practical information about your system.  The latest versions of these
documents are located at http://www.linuxdoc.org/docs.html#howto

%prep
%setup -q -n %name

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}
untar_howtos; makehowtoindex %lang %language > index.html; cp -a * $RPM_BUILD_ROOT%{_docdir}/HOWTO/%{format2}

install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/applications
cat > %{buildroot}%_datadir/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Howto %language
Comment=HOWTO documents (html format) from the Linux Documentation Project in %language
Exec=xdg-open %_datadir/doc/HOWTO/HTML/%lang/index.html
Icon=documentation_section
Terminal=false
Type=Application
Categories=Documentation;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_docdir}/HOWTO/%{format2}
%{_datadir}/applications/*.desktop

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 20080722-4mdv2011.0
+ Revision: 665422
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 20080722-3mdv2011.0
+ Revision: 605865
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 20080722-2mdv2010.1
+ Revision: 520700
- rebuilt for 2010.1

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 20080722-1mdv2009.0
+ Revision: 239663
- new snapshot

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 10.1-4mdv2009.0
+ Revision: 218432
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 10.1-4mdv2008.1
+ Revision: 150263
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 08 2007 Funda Wang <fwang@mandriva.org> 10.1-3mdv2008.0
+ Revision: 82165
- Rebuild for new era
- Import howto-html-fr



* Thu Jul 07 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 10.1-2mdk
- fix menu entry (#16627)

* Sat Aug 14 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 10.1-1mdk
- new snapshot

* Mon Mar 01 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 10-1mdk
- new snapshot

* Tue Sep 09 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.2-1mdk
- new snapshot

* Tue Jul 01 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-0.7mdk
- new snapshot

* Thu Feb 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-0.6mdk
- new menu scheme

* Sat Feb 15 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-0.5mdk
- fix menu generation

* Thu Feb 13 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-0.3mdk
- synchronize all howtos spec files
- use new howto-utils

* Wed Feb 05 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-0.3mdk
- fix menu entry

* Wed Jan 29 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-0.2mdk
- rebuild for latest makehowtoindex %%lang %%language > index.html)

* Tue Jan 21 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.1-0.1mdk
- new snapshot

* Fri Aug 02 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.0-0.2mdk
- rpmlint fixes

* Thu Aug 01 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 9.0-0.1mdk
- new snapshot
- add real url
- sanitize menu entry (fix menu-command-not-in-package)

* Tue Apr 09 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 8.3-1mdk
- resync with howto spec template
- 20020409 snapshot
- s!bzcat | tar ! tar xfj

* Thu Jan 29 2002 Adrien DEMAREZ <ademarez@mandrakesoft.com> 8.2-2mdk
- Updated the howtos

* Thu Jan 17 2002 David BAUDENS <baudens@mandrakesoft.com> 8.2-1mdk
- Fix menu entry (icon)

* Fri Sep 07 2001 Etienne FAURE <etienne@mandrakesoft.com> 8.1-3mdk
- Modified menu entry so that it works with KDE and gnome

* Fri Aug 31 2001 Etienne FAURE <etienne@mandrakesoft.com> 8.1-2mdk
- Oups, added missing icons.

* Thu Aug 30 2001 Etienne FAURE <etienne@mandrakesoft.com> 8.1-1mdk
- Automatically updated

* Tue Mar 13 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 8.0-1mdk
- bump release number
- fix tmppath
- build with new howto-utils

* Thu Mar 01 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 7.3-2mdk
- let makehowtoindex %%lang %%language > index.html)

* Wed Feb 28 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 7.3-1mdk
- reput howto where they should have been so that the menu is correctely
  generated (ie readd ln touch)
- update version to at least 7.3 ... for the moment

* Sat Jan 13 2001 Etienne Faure  <etienne@mandrakesoft.com> 7.1-8mdk
- modified menu entry

* Sat Dec  9 2000 Etienne Faure  <etienne@mandraksoft.com> 7.1-7mdk
- updated to more recent howtos


* Thu Aug 17 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 7.1-6mdk
- add LN touch

* Fri Aug 11 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 7.1-5mdk
- fix menu for BM

* Fri Aug 11 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 7.1-4mdk
- use new tool to autogenerate the menu (which was previously handly built by
  dadou :-( )
- fix buildrequires
- new snapshots

* Wed Aug 02 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 7.1-3mdk
- update to 20000802 howtos
- use new macros

* Mon Apr 24 2000 Pixel <pixel@mandrakesoft.com> 7.1-2mdk
- change require (add locales-XX, change netscape to webclient)

* Thu Apr 20 2000 David BAUDENS <baudens@mandrakesoft.com> 7.1-1mdk
- 7.1

* Wed Apr 05 2000 David BAUDENS <baudens@mandrakesoft.com> 7.0-2mdk
- 20000405

* Fri Jan 07 2000 - David BAUDENS <baudens@mandrakesoft.com>
- Build for 7.0

* Tue Dec 30 1999 - David BAUDENS <baudens@mandrakesoft.com>
- French HTML version

* Sat Dec 04 1999 - David BAUDENS <baudens@mandrakesoft.com>
- 19991204
- Keep only html format (others are in contribs)

* Fri May 14 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adaptations.

* Tue Mar 23 1999 Bill Nottingham <notting@redhat.com>
- no <BASE HREF...> in howto-index.html

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Tue Jan 26 1999 Cristian Gafton <gafton@redhat.com>
- updated howtos
- marked translations with %%lang(XX)
- get rid of pdf, ps and dvi formats

* Thu Oct 01 1998 Cristian Gafton <gafton@redhat.com>
- added the Serbian Howtos

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- updated archive
- added croatian and slovenian subpackages

* Wed Apr 15 1998 Cristian Gafton <gafton@redhat.com>
- updated archive
- subpackages for each language

* Fri Oct 24 1997 Otto Hammersmith <otto@redhat.com>
- fixed missing HOWTOs because the download ran out of space
- added an index html page for the howto-html package

* Thu Oct 23 1997 Otto Hammersmith <otto@redhat.com>
- untarred the html tarballs to obsolete the ldp package

* Wed Oct 22 1997 Otto Hammersmith <otto@redhat.com>
- updated version
- fixed description for the right date

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- made a noarch package

* Sat Apr 19 1997 Otto Hammersmith <otto@redhat.com>
- Updated to more recent HOWTOs.
- In the next major version, %%{_docdir} really ought to be cleaned out.
  Right now, the ldp and howto packages overlap somewhat. (HTML docs,
  the former, however, only has tar.gz files)
  I didn't want to rearrange too much for 4.2, and there are other
  documentation issues such as /usr/info.
