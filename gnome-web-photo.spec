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

