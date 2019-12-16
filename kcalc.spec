#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kcalc
Version  : 19.12.0
Release  : 16
URL      : https://download.kde.org/stable/release-service/19.12.0/src/kcalc-19.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.0/src/kcalc-19.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.0/src/kcalc-19.12.0.tar.xz.sig
Summary  : Scientific Calculator
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: kcalc-bin = %{version}-%{release}
Requires: kcalc-data = %{version}-%{release}
Requires: kcalc-lib = %{version}-%{release}
Requires: kcalc-license = %{version}-%{release}
Requires: kcalc-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : gmp-dev
BuildRequires : mpfr-dev

%description
KCalc
=====
KCalc is currently covered under the GPL version 2.  A copy of this
license can be found in a file named COPYING, in the toplevel directory.

%package bin
Summary: bin components for the kcalc package.
Group: Binaries
Requires: kcalc-data = %{version}-%{release}
Requires: kcalc-license = %{version}-%{release}

%description bin
bin components for the kcalc package.


%package data
Summary: data components for the kcalc package.
Group: Data

%description data
data components for the kcalc package.


%package doc
Summary: doc components for the kcalc package.
Group: Documentation

%description doc
doc components for the kcalc package.


%package lib
Summary: lib components for the kcalc package.
Group: Libraries
Requires: kcalc-data = %{version}-%{release}
Requires: kcalc-license = %{version}-%{release}

%description lib
lib components for the kcalc package.


%package license
Summary: license components for the kcalc package.
Group: Default

%description license
license components for the kcalc package.


%package locales
Summary: locales components for the kcalc package.
Group: Default

%description locales
locales components for the kcalc package.


%prep
%setup -q -n kcalc-19.12.0
cd %{_builddir}/kcalc-19.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576530017
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1576530017
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcalc
cp %{_builddir}/kcalc-19.12.0/COPYING %{buildroot}/usr/share/package-licenses/kcalc/7c203dee3a03037da436df03c4b25b659c073976
cp %{_builddir}/kcalc-19.12.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/kcalc/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd clr-build
%make_install
popd
%find_lang kcalc

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kcalc

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kcalc.desktop
/usr/share/config.kcfg/kcalc.kcfg
/usr/share/kcalc/scienceconstants.xml
/usr/share/kconf_update/kcalcrc.upd
/usr/share/kxmlgui5/kcalc/kcalcui.rc
/usr/share/metainfo/org.kde.kcalc.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/de/kcalc/commands.docbook
/usr/share/doc/HTML/de/kcalc/index.cache.bz2
/usr/share/doc/HTML/de/kcalc/index.docbook
/usr/share/doc/HTML/en/kcalc/commands.docbook
/usr/share/doc/HTML/en/kcalc/index.cache.bz2
/usr/share/doc/HTML/en/kcalc/index.docbook
/usr/share/doc/HTML/es/kcalc/commands.docbook
/usr/share/doc/HTML/es/kcalc/index.cache.bz2
/usr/share/doc/HTML/es/kcalc/index.docbook
/usr/share/doc/HTML/et/kcalc/commands.docbook
/usr/share/doc/HTML/et/kcalc/index.cache.bz2
/usr/share/doc/HTML/et/kcalc/index.docbook
/usr/share/doc/HTML/fr/kcalc/commands.docbook
/usr/share/doc/HTML/fr/kcalc/index.cache.bz2
/usr/share/doc/HTML/fr/kcalc/index.docbook
/usr/share/doc/HTML/gl/kcalc/commands.docbook
/usr/share/doc/HTML/gl/kcalc/index.cache.bz2
/usr/share/doc/HTML/gl/kcalc/index.docbook
/usr/share/doc/HTML/it/kcalc/commands.docbook
/usr/share/doc/HTML/it/kcalc/index.cache.bz2
/usr/share/doc/HTML/it/kcalc/index.docbook
/usr/share/doc/HTML/lt/kcalc/commands.docbook
/usr/share/doc/HTML/lt/kcalc/index.cache.bz2
/usr/share/doc/HTML/lt/kcalc/index.docbook
/usr/share/doc/HTML/nl/kcalc/commands.docbook
/usr/share/doc/HTML/nl/kcalc/index.cache.bz2
/usr/share/doc/HTML/nl/kcalc/index.docbook
/usr/share/doc/HTML/pt/kcalc/commands.docbook
/usr/share/doc/HTML/pt/kcalc/index.cache.bz2
/usr/share/doc/HTML/pt/kcalc/index.docbook
/usr/share/doc/HTML/pt_BR/kcalc/commands.docbook
/usr/share/doc/HTML/pt_BR/kcalc/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kcalc/index.docbook
/usr/share/doc/HTML/ru/kcalc/commands.docbook
/usr/share/doc/HTML/ru/kcalc/index.cache.bz2
/usr/share/doc/HTML/ru/kcalc/index.docbook
/usr/share/doc/HTML/sr/kcalc/commands.docbook
/usr/share/doc/HTML/sr/kcalc/index.cache.bz2
/usr/share/doc/HTML/sr/kcalc/index.docbook
/usr/share/doc/HTML/sv/kcalc/commands.docbook
/usr/share/doc/HTML/sv/kcalc/index.cache.bz2
/usr/share/doc/HTML/sv/kcalc/index.docbook
/usr/share/doc/HTML/uk/kcalc/commands.docbook
/usr/share/doc/HTML/uk/kcalc/index.cache.bz2
/usr/share/doc/HTML/uk/kcalc/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkdeinit5_kcalc.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcalc/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/kcalc/9a1929f4700d2407c70b507b3b2aaf6226a9543c

%files locales -f kcalc.lang
%defattr(-,root,root,-)

