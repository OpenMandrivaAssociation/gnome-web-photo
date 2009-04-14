Name:		gnome-web-photo
Version:	0.7
Release:	%mkrel 1
Summary:	Generate full images and thumbnails from web pages
License:	LGPLv2+
Group:		Graphical desktop/GNOME
URL:		http://ftp.gnome.org/pub/gnome/sources/gnome-web-photo/
Source:		http://ftp.gnome.org/pub/gnome/sources/gnome-web-photo/%{version}/gnome-web-photo-%{version}.tar.bz2
BuildRequires:	gnome-common
BuildRequires:	gnome-vfs2-devel
BuildRequires:	intltool
BuildRequires:	libGConf2-devel
BuildRequires:	xulrunner-devel-unstable
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
GNOME Web Photographer is a tool to generate full-size image files and
thumbnails from HTML files and web pages.

%prep
%setup -q

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# avoid conflict with nautilus_thumbnailers
mv %{buildroot}%{_sysconfdir}/gconf/schemas/thumbnailer.schemas \
   %{buildroot}%{_sysconfdir}/gconf/schemas/gnome-web-thumbnail.schemas

%find_lang %{name}

%preun
%preun_uninstall_gconf_schemas gnome-web-thumbnail

%files -f %{name}.lang
%defattr(0755,root,root,0755)
%{_bindir}/gnome-web-print
%{_bindir}/gnome-web-thumbnail
%{_bindir}/gnome-web-photo
%defattr(0644,root,root,0755)
%{_datadir}/gnome-web-photo
%{_sysconfdir}/gconf/schemas/gnome-web-thumbnail.schemas
