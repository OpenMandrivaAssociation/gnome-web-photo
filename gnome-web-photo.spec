Summary:	Generate full images and thumbnails from web pages
Name:		gnome-web-photo
Version:	0.10.6
Release:	1
License:	LGPLv2+
Group:		Graphical desktop/GNOME
URL:		http://ftp.gnome.org/pub/gnome/sources/gnome-web-photo/
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-web-photo/%{version}/gnome-web-photo-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(webkitgtk-3.0)

%description
GNOME Web Photographer is a tool to generate full-size image files and
thumbnails from HTML files and web pages.

%prep
%setup -q

%build
%configure2_5x \
	--with-gtk=3.0

%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/gnome-web-photo
%{_bindir}/gnome-web-print
%{_bindir}/gnome-web-thumbnail
%{_datadir}/gnome-web-photo
%{_datadir}/thumbnailers/gnome-web-photo.thumbnailer



%changelog
* Wed May 16 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.10.6-1
+ Revision: 799214
- new version 0.10.6
- built with gtk+3.0
- cleaned up spec

* Mon Jun 20 2011 Funda Wang <fwang@mandriva.org> 0.10.1-2
+ Revision: 686166
- rebuild for new webkit

* Sun May 22 2011 Funda Wang <fwang@mandriva.org> 0.10.1-1
+ Revision: 677249
- new version 0.10.1
- rebuild to add gconf2 as req

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Sun Jan 17 2010 Funda Wang <fwang@mandriva.org> 0.9-2mdv2010.1
+ Revision: 492595
- fix build with xulrunner 1.9.2

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 0.9-1mdv2010.0
+ Revision: 446594
- update to new version 0.9

* Sat Aug 22 2009 Funda Wang <fwang@mandriva.org> 0.8-3mdv2010.0
+ Revision: 419465
- rebuild

* Tue Aug 04 2009 Funda Wang <fwang@mandriva.org> 0.8-2mdv2010.0
+ Revision: 408679
- use correct libxul libpath for linking

* Mon Jun 29 2009 Götz Waschk <waschk@mandriva.org> 0.8-1mdv2010.0
+ Revision: 390607
- update to new version 0.8

* Tue Apr 14 2009 Götz Waschk <waschk@mandriva.org> 0.7-1mdv2009.1
+ Revision: 366975
- update to new version 0.7

* Tue Mar 17 2009 Götz Waschk <waschk@mandriva.org> 0.6-1mdv2009.1
+ Revision: 356679
- update to new version 0.6

* Thu Mar 12 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.5-1mdv2009.1
+ Revision: 354218
- Replace BuildRequires for libxulrunner-unstable-devel by
  xulrunner-devel-unstable, otherwise wrong 32-bit devel version of
  package is chosen on x86_64.
- Added missing BuildRequires: gnome-vfs2-devel, intltool,
  libGConf2-devel
- import gnome-web-photo


