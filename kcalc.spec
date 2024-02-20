#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: da8b975
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kcalc
Version  : 23.08.5
Release  : 63
URL      : https://download.kde.org/stable/release-service/23.08.5/src/kcalc-23.08.5.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.5/src/kcalc-23.08.5.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.5/src/kcalc-23.08.5.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0
Requires: kcalc-bin = %{version}-%{release}
Requires: kcalc-data = %{version}-%{release}
Requires: kcalc-license = %{version}-%{release}
Requires: kcalc-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : gmp-dev
BuildRequires : mpfr-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n kcalc-23.08.5
cd %{_builddir}/kcalc-23.08.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1708409317
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1708409317
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcalc
cp %{_builddir}/kcalc-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kcalc/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kcalc-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kcalc/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe || :
cp %{_builddir}/kcalc-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kcalc/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kcalc-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcalc/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kcalc
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kcalc
/usr/bin/kcalc

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kcalc.desktop
/usr/share/config.kcfg/kcalc.kcfg
/usr/share/kconf_update/kcalcrc.upd
/usr/share/kglobalaccel/org.kde.kcalc.desktop
/usr/share/metainfo/org.kde.kcalc.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kcalc/commands.docbook
/usr/share/doc/HTML/ca/kcalc/index.cache.bz2
/usr/share/doc/HTML/ca/kcalc/index.docbook
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
/usr/share/doc/HTML/sr@latin/kcalc/commands.docbook
/usr/share/doc/HTML/sr@latin/kcalc/index.cache.bz2
/usr/share/doc/HTML/sr@latin/kcalc/index.docbook
/usr/share/doc/HTML/sv/kcalc/commands.docbook
/usr/share/doc/HTML/sv/kcalc/index.cache.bz2
/usr/share/doc/HTML/sv/kcalc/index.docbook
/usr/share/doc/HTML/uk/kcalc/commands.docbook
/usr/share/doc/HTML/uk/kcalc/index.cache.bz2
/usr/share/doc/HTML/uk/kcalc/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcalc/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kcalc/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kcalc/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kcalc/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe

%files locales -f kcalc.lang
%defattr(-,root,root,-)

