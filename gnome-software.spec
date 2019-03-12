#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-software
Version  : 3.30.6
Release  : 21
URL      : https://download.gnome.org/sources/gnome-software/3.30/gnome-software-3.30.6.tar.xz
Source0  : https://download.gnome.org/sources/gnome-software/3.30/gnome-software-3.30.6.tar.xz
Summary  : GNOME Software is a software center for GNOME
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: gnome-software-bin = %{version}-%{release}
Requires: gnome-software-data = %{version}-%{release}
Requires: gnome-software-lib = %{version}-%{release}
Requires: gnome-software-libexec = %{version}-%{release}
Requires: gnome-software-license = %{version}-%{release}
Requires: gnome-software-locales = %{version}-%{release}
Requires: gnome-software-man = %{version}-%{release}
Requires: clr-bundle-icons
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : gtk-doc
BuildRequires : liboauth-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(appstream-glib)
BuildRequires : pkgconfig(flatpak)
BuildRequires : pkgconfig(fwupd)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(gspell-1)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(oauth)
BuildRequires : pkgconfig(packagekit-glib2)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(valgrind)
BuildRequires : source-highlight
BuildRequires : valgrind-dev
BuildRequires : zstd-dev
Patch1: 0001-WIP-Integrating-swupd-to-gnome-software.patch
Patch2: 0001-CLR-custimizations.patch

%description
This is the first paragraph in the example package spec file.

This is the second paragraph.

%package bin
Summary: bin components for the gnome-software package.
Group: Binaries
Requires: gnome-software-data = %{version}-%{release}
Requires: gnome-software-libexec = %{version}-%{release}
Requires: gnome-software-license = %{version}-%{release}
Requires: gnome-software-man = %{version}-%{release}

%description bin
bin components for the gnome-software package.


%package data
Summary: data components for the gnome-software package.
Group: Data

%description data
data components for the gnome-software package.


%package dev
Summary: dev components for the gnome-software package.
Group: Development
Requires: gnome-software-lib = %{version}-%{release}
Requires: gnome-software-bin = %{version}-%{release}
Requires: gnome-software-data = %{version}-%{release}
Provides: gnome-software-devel = %{version}-%{release}

%description dev
dev components for the gnome-software package.


%package doc
Summary: doc components for the gnome-software package.
Group: Documentation
Requires: gnome-software-man = %{version}-%{release}

%description doc
doc components for the gnome-software package.


%package lib
Summary: lib components for the gnome-software package.
Group: Libraries
Requires: gnome-software-data = %{version}-%{release}
Requires: gnome-software-libexec = %{version}-%{release}
Requires: gnome-software-license = %{version}-%{release}

%description lib
lib components for the gnome-software package.


%package libexec
Summary: libexec components for the gnome-software package.
Group: Default
Requires: gnome-software-license = %{version}-%{release}

%description libexec
libexec components for the gnome-software package.


%package license
Summary: license components for the gnome-software package.
Group: Default

%description license
license components for the gnome-software package.


%package locales
Summary: locales components for the gnome-software package.
Group: Default

%description locales
locales components for the gnome-software package.


%package man
Summary: man components for the gnome-software package.
Group: Default

%description man
man components for the gnome-software package.


%prep
%setup -q -n gnome-software-3.30.6
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552123268
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain -Denable-packagekit=false -Denable-ubuntuone=false -Denable-ubuntu-reviews=false -Denable-snap=false -Denable-gtk-doc=false  -Dpackagekit=false -Dfwupd=false  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-software
cp COPYING %{buildroot}/usr/share/package-licenses/gnome-software/COPYING
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-software

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-software
/usr/bin/gnome-software-editor

%files data
%defattr(-,root,root,-)
/usr/share/app-info/xmls/org.gnome.Software.Featured.xml
/usr/share/applications/gnome-software-local-file.desktop
/usr/share/applications/org.gnome.Software.Editor.desktop
/usr/share/applications/org.gnome.Software.desktop
/usr/share/dbus-1/services/org.gnome.Software.service
/usr/share/glib-2.0/schemas/org.gnome.software.gschema.xml
/usr/share/gnome-shell/search-providers/org.gnome.Software-search-provider.ini
/usr/share/gnome-software/featured-ardour-bg.png
/usr/share/gnome-software/featured-ardour.png
/usr/share/gnome-software/featured-blender.png
/usr/share/gnome-software/featured-builder-bg.jpg
/usr/share/gnome-software/featured-builder.png
/usr/share/gnome-software/featured-chess.png
/usr/share/gnome-software/featured-firefox.png
/usr/share/gnome-software/featured-gimp.png
/usr/share/gnome-software/featured-gnome-sudoku.png
/usr/share/gnome-software/featured-inkscape.svg
/usr/share/gnome-software/featured-maps-bg.png
/usr/share/gnome-software/featured-maps.png
/usr/share/gnome-software/featured-mypaint.png
/usr/share/gnome-software/featured-polari.svg
/usr/share/gnome-software/featured-transmission.png
/usr/share/gnome-software/featured-weather-bg.png
/usr/share/gnome-software/featured-weather.png
/usr/share/gnome-software/upgrade-bg.png
/usr/share/icons/hicolor/16x16/apps/org.gnome.Software.png
/usr/share/icons/hicolor/22x22/apps/org.gnome.Software.png
/usr/share/icons/hicolor/24x24/apps/org.gnome.Software.png
/usr/share/icons/hicolor/256x256/apps/org.gnome.Software.png
/usr/share/icons/hicolor/32x32/apps/org.gnome.Software.png
/usr/share/icons/hicolor/48x48/apps/org.gnome.Software.png
/usr/share/icons/hicolor/scalable/apps/org.gnome.Software-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/software-installed-symbolic.svg
/usr/share/metainfo/org.gnome.Software.Plugin.Epiphany.metainfo.xml
/usr/share/metainfo/org.gnome.Software.Plugin.Flatpak.metainfo.xml
/usr/share/metainfo/org.gnome.Software.Plugin.Odrs.metainfo.xml
/usr/share/metainfo/org.gnome.Software.Plugin.Steam.metainfo.xml
/usr/share/metainfo/org.gnome.Software.appdata.xml

%files dev
%defattr(-,root,root,-)
/usr/include/gnome-software/gnome-software.h
/usr/include/gnome-software/gs-app-list.h
/usr/include/gnome-software/gs-app.h
/usr/include/gnome-software/gs-auth.h
/usr/include/gnome-software/gs-category.h
/usr/include/gnome-software/gs-os-release.h
/usr/include/gnome-software/gs-plugin-event.h
/usr/include/gnome-software/gs-plugin-types.h
/usr/include/gnome-software/gs-plugin-vfuncs.h
/usr/include/gnome-software/gs-plugin.h
/usr/include/gnome-software/gs-price.h
/usr/include/gnome-software/gs-utils.h
/usr/lib64/pkgconfig/gnome-software.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/gnome\-software/*
/usr/share/gtk-doc/html/gnome-software/api.html
/usr/share/gtk-doc/html/gnome-software/gnome-software-GsApp.html
/usr/share/gtk-doc/html/gnome-software/gnome-software-GsAppList.html
/usr/share/gtk-doc/html/gnome-software/gnome-software-GsAuth.html
/usr/share/gtk-doc/html/gnome-software/gnome-software-GsOsRelease.html
/usr/share/gtk-doc/html/gnome-software/gnome-software-GsPlugin-Exports.html
/usr/share/gtk-doc/html/gnome-software/gnome-software-GsPlugin.html
/usr/share/gtk-doc/html/gnome-software/gnome-software-GsPluginEvent.html
/usr/share/gtk-doc/html/gnome-software/gnome-software-GsUtils.html
/usr/share/gtk-doc/html/gnome-software/gnome-software-gs-category.html
/usr/share/gtk-doc/html/gnome-software/gnome-software.devhelp2
/usr/share/gtk-doc/html/gnome-software/gs-example-details.png
/usr/share/gtk-doc/html/gnome-software/gs-example-installed.png
/usr/share/gtk-doc/html/gnome-software/gs-example-search.png
/usr/share/gtk-doc/html/gnome-software/home.png
/usr/share/gtk-doc/html/gnome-software/index.html
/usr/share/gtk-doc/html/gnome-software/left-insensitive.png
/usr/share/gtk-doc/html/gnome-software/left.png
/usr/share/gtk-doc/html/gnome-software/right-insensitive.png
/usr/share/gtk-doc/html/gnome-software/right.png
/usr/share/gtk-doc/html/gnome-software/style.css
/usr/share/gtk-doc/html/gnome-software/tutorial.html
/usr/share/gtk-doc/html/gnome-software/up-insensitive.png
/usr/share/gtk-doc/html/gnome-software/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/gs-plugins-12/libgs_plugin_appstream.so
/usr/lib64/gs-plugins-12/libgs_plugin_desktop-categories.so
/usr/lib64/gs-plugins-12/libgs_plugin_desktop-menu-path.so
/usr/lib64/gs-plugins-12/libgs_plugin_dpkg.so
/usr/lib64/gs-plugins-12/libgs_plugin_dummy.so
/usr/lib64/gs-plugins-12/libgs_plugin_epiphany.so
/usr/lib64/gs-plugins-12/libgs_plugin_fedora-pkgdb-collections.so
/usr/lib64/gs-plugins-12/libgs_plugin_flatpak.so
/usr/lib64/gs-plugins-12/libgs_plugin_generic-updates.so
/usr/lib64/gs-plugins-12/libgs_plugin_hardcoded-blacklist.so
/usr/lib64/gs-plugins-12/libgs_plugin_hardcoded-featured.so
/usr/lib64/gs-plugins-12/libgs_plugin_hardcoded-popular.so
/usr/lib64/gs-plugins-12/libgs_plugin_icons.so
/usr/lib64/gs-plugins-12/libgs_plugin_key-colors-metadata.so
/usr/lib64/gs-plugins-12/libgs_plugin_key-colors.so
/usr/lib64/gs-plugins-12/libgs_plugin_modalias.so
/usr/lib64/gs-plugins-12/libgs_plugin_odrs.so
/usr/lib64/gs-plugins-12/libgs_plugin_os-release.so
/usr/lib64/gs-plugins-12/libgs_plugin_provenance-license.so
/usr/lib64/gs-plugins-12/libgs_plugin_provenance.so
/usr/lib64/gs-plugins-12/libgs_plugin_repos.so
/usr/lib64/gs-plugins-12/libgs_plugin_rewrite-resource.so
/usr/lib64/gs-plugins-12/libgs_plugin_shell-extensions.so
/usr/lib64/gs-plugins-12/libgs_plugin_steam.so
/usr/lib64/gs-plugins-12/libgs_plugin_swupd.so
/usr/lib64/gs-plugins-12/libgs_plugin_ubuntu-reviews.so
/usr/lib64/gs-plugins-12/libgs_plugin_ubuntuone.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gnome-software-cmd
/usr/libexec/gnome-software-restarter

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-software/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gnome-software-editor.1
/usr/share/man/man1/gnome-software.1

%files locales -f gnome-software.lang
%defattr(-,root,root,-)

