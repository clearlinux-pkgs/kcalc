#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kcalc
Version  : 21.12.2
Release  : 37
URL      : https://download.kde.org/stable/release-service/21.12.2/src/kcalc-21.12.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.12.2/src/kcalc-21.12.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.12.2/src/kcalc-21.12.2.tar.xz.sig
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
BuildRequires : kdoctools-dev
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
%setup -q -n kcalc-21.12.2
cd %{_builddir}/kcalc-21.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644019708
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1644019708
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kcalc
cp %{_builddir}/kcalc-21.12.2/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kcalc/29fb05b49e12a380545499938c4879440bd8851e
cp %{_builddir}/kcalc-21.12.2/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kcalc/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe
cp %{_builddir}/kcalc-21.12.2/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kcalc/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
cp %{_builddir}/kcalc-21.12.2/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kcalc/3e8971c6c5f16674958913a94a36b1ea7a00ac46
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
/usr/share/kconf_update/kcalcrc.upd
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kcalc/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kcalc/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kcalc/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kcalc/f1946dab78e58c04c8c25ec6b074f5fc5c2830fe

%files locales -f kcalc.lang
%defattr(-,root,root,-)

