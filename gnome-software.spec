#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-software
Version  : 43.4
Release  : 70
URL      : https://download.gnome.org/sources/gnome-software/43/gnome-software-43.4.tar.xz
Source0  : https://download.gnome.org/sources/gnome-software/43/gnome-software-43.4.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-software-bin = %{version}-%{release}
Requires: gnome-software-data = %{version}-%{release}
Requires: gnome-software-lib = %{version}-%{release}
Requires: gnome-software-libexec = %{version}-%{release}
Requires: gnome-software-license = %{version}-%{release}
Requires: gnome-software-locales = %{version}-%{release}
Requires: gnome-software-man = %{version}-%{release}
Requires: clr-bundle-icons
Requires: clr-bundle-screenshots
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : gtk-doc
BuildRequires : libsoup-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(appstream)
BuildRequires : pkgconfig(appstream-glib)
BuildRequires : pkgconfig(flatpak)
BuildRequires : pkgconfig(gnome-desktop-3.0)
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(gspell-1)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libadwaita-1)
BuildRequires : pkgconfig(libhandy-1)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(polkit-gobject-1)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(xmlb)
BuildRequires : source-highlight
BuildRequires : valgrind-dev
BuildRequires : zstd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![Build Status](https://gitlab.gnome.org/GNOME/gnome-software/badges/main/pipeline.svg)](https://gitlab.gnome.org/GNOME/gnome-software/pipelines)

%package bin
Summary: bin components for the gnome-software package.
Group: Binaries
Requires: gnome-software-data = %{version}-%{release}
Requires: gnome-software-libexec = %{version}-%{release}
Requires: gnome-software-license = %{version}-%{release}

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
Requires: gnome-software = %{version}-%{release}

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
%setup -q -n gnome-software-43.4
cd %{_builddir}/gnome-software-43.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676051776
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dfwupd=false \
-Dgtk_doc=false \
-Dmalcontent=false \
-Dpackagekit=false \
-Dpackagekit_autoremove=false \
-Drpm_ostree=false \
-Dsnap=false \
-Dsysprof=disabled \
-Dhardcoded_foss_webapps=false \
-Dhardcoded_proprietary_webapps=false \
-Dwebapps=false \
-Dtests=false  builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-software
cp %{_builddir}/gnome-software-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-software/4cc77b90af91e615a64ae04893fdffa7939db84c || :
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-software

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-software

%files data
%defattr(-,root,root,-)
/usr/share/applications/gnome-software-local-file-flatpak.desktop
/usr/share/applications/org.gnome.Software.desktop
/usr/share/dbus-1/services/org.gnome.Software.service
/usr/share/glib-2.0/schemas/org.gnome.software.gschema.xml
/usr/share/gnome-shell/search-providers/org.gnome.Software-search-provider.ini
/usr/share/icons/hicolor/scalable/actions/app-remove-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/org.gnome.Software.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Software-symbolic.svg
/usr/share/metainfo/org.gnome.Software.Plugin.Flatpak.metainfo.xml
/usr/share/metainfo/org.gnome.Software.metainfo.xml
/usr/share/swcatalog/xml/org.gnome.Software.Curated.xml
/usr/share/swcatalog/xml/org.gnome.Software.Featured.xml

%files dev
%defattr(-,root,root,-)
/usr/include/gnome-software/gnome-software.h
/usr/include/gnome-software/gs-app-collation.h
/usr/include/gnome-software/gs-app-list.h
/usr/include/gnome-software/gs-app-permissions.h
/usr/include/gnome-software/gs-app-query.h
/usr/include/gnome-software/gs-app.h
/usr/include/gnome-software/gs-appstream.h
/usr/include/gnome-software/gs-category-manager.h
/usr/include/gnome-software/gs-category.h
/usr/include/gnome-software/gs-desktop-data.h
/usr/include/gnome-software/gs-download-utils.h
/usr/include/gnome-software/gs-enums.h
/usr/include/gnome-software/gs-external-appstream-utils.h
/usr/include/gnome-software/gs-icon.h
/usr/include/gnome-software/gs-ioprio.h
/usr/include/gnome-software/gs-key-colors.h
/usr/include/gnome-software/gs-metered.h
/usr/include/gnome-software/gs-odrs-provider.h
/usr/include/gnome-software/gs-os-release.h
/usr/include/gnome-software/gs-plugin-event.h
/usr/include/gnome-software/gs-plugin-helpers.h
/usr/include/gnome-software/gs-plugin-job-list-apps.h
/usr/include/gnome-software/gs-plugin-job-list-categories.h
/usr/include/gnome-software/gs-plugin-job-list-distro-upgrades.h
/usr/include/gnome-software/gs-plugin-job-manage-repository.h
/usr/include/gnome-software/gs-plugin-job-refine.h
/usr/include/gnome-software/gs-plugin-job-refresh-metadata.h
/usr/include/gnome-software/gs-plugin-job.h
/usr/include/gnome-software/gs-plugin-loader-sync.h
/usr/include/gnome-software/gs-plugin-loader.h
/usr/include/gnome-software/gs-plugin-types.h
/usr/include/gnome-software/gs-plugin-vfuncs.h
/usr/include/gnome-software/gs-plugin.h
/usr/include/gnome-software/gs-remote-icon.h
/usr/include/gnome-software/gs-test.h
/usr/include/gnome-software/gs-utils.h
/usr/include/gnome-software/gs-worker-thread.h
/usr/lib64/pkgconfig/gnome-software.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/gnome\-software/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/gnome-software/libgnomesoftware.so
/usr/lib64/gnome-software/libgnomesoftware.so.19
/usr/lib64/gnome-software/plugins-19/libgs_plugin_appstream.so
/usr/lib64/gnome-software/plugins-19/libgs_plugin_dpkg.so
/usr/lib64/gnome-software/plugins-19/libgs_plugin_dummy.so
/usr/lib64/gnome-software/plugins-19/libgs_plugin_fedora-langpacks.so
/usr/lib64/gnome-software/plugins-19/libgs_plugin_fedora-pkgdb-collections.so
/usr/lib64/gnome-software/plugins-19/libgs_plugin_flatpak.so
/usr/lib64/gnome-software/plugins-19/libgs_plugin_generic-updates.so
/usr/lib64/gnome-software/plugins-19/libgs_plugin_hardcoded-blocklist.so
/usr/lib64/gnome-software/plugins-19/libgs_plugin_icons.so
/usr/lib64/gnome-software/plugins-19/libgs_plugin_modalias.so
/usr/lib64/gnome-software/plugins-19/libgs_plugin_os-release.so
/usr/lib64/gnome-software/plugins-19/libgs_plugin_provenance-license.so
/usr/lib64/gnome-software/plugins-19/libgs_plugin_provenance.so
/usr/lib64/gnome-software/plugins-19/libgs_plugin_repos.so
/usr/lib64/gnome-software/plugins-19/libgs_plugin_rewrite-resource.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gnome-software-cmd
/usr/libexec/gnome-software-restarter

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-software/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gnome-software.1

%files locales -f gnome-software.lang
%defattr(-,root,root,-)

