#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: f4a13a5
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : kitemviews
Version  : 6.10.0
Release  : 93
URL      : https://download.kde.org/stable/frameworks/6.10/kitemviews-6.10.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.10/kitemviews-6.10.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.10/kitemviews-6.10.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.0
Requires: kitemviews-data = %{version}-%{release}
Requires: kitemviews-lib = %{version}-%{release}
Requires: kitemviews-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KItemViews
Set of item views extending the Qt model-view framework
## Introduction

%package data
Summary: data components for the kitemviews package.
Group: Data

%description data
data components for the kitemviews package.


%package dev
Summary: dev components for the kitemviews package.
Group: Development
Requires: kitemviews-lib = %{version}-%{release}
Requires: kitemviews-data = %{version}-%{release}
Provides: kitemviews-devel = %{version}-%{release}
Requires: kitemviews = %{version}-%{release}

%description dev
dev components for the kitemviews package.


%package lib
Summary: lib components for the kitemviews package.
Group: Libraries
Requires: kitemviews-data = %{version}-%{release}
Requires: kitemviews-license = %{version}-%{release}

%description lib
lib components for the kitemviews package.


%package license
Summary: license components for the kitemviews package.
Group: Default

%description license
license components for the kitemviews package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n kitemviews-6.10.0
cd %{_builddir}/kitemviews-6.10.0
pushd ..
cp -a kitemviews-6.10.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1736537386
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
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
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
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
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
export SOURCE_DATE_EPOCH=1736537386
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kitemviews
cp %{_builddir}/kitemviews-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kitemviews/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kitemviews-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kitemviews/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kitemviews-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kitemviews/20079e8f79713dce80ab09774505773c926afa2a || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/locale/af/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/as/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/ast/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/az/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/be/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/bn/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/br/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/crh/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/csb/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/cy/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/da/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/de/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/el/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/es/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/et/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/fa/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/fy/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/gd/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/gu/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/ha/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/he/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/hne/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/hy/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/id/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/is/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/it/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/km/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/kn/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/ku/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/lb/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/mai/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/mk/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/ms/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/ne/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/oc/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/or/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/ps/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/sa/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/se/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/si/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/sq/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/ta/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/te/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/th/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/tt/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/uz/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/vi/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/wa/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/xh/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/zh_HK/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kitemviews6_qt.qm
/usr/share/qlogging-categories6/kitemviews.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KItemViews/KCategorizedSortFilterProxyModel
/usr/include/KF6/KItemViews/KCategorizedView
/usr/include/KF6/KItemViews/KCategoryDrawer
/usr/include/KF6/KItemViews/KExtendableItemDelegate
/usr/include/KF6/KItemViews/KListWidgetSearchLine
/usr/include/KF6/KItemViews/KTreeWidgetSearchLine
/usr/include/KF6/KItemViews/KTreeWidgetSearchLineWidget
/usr/include/KF6/KItemViews/KWidgetItemDelegate
/usr/include/KF6/KItemViews/kcategorizedsortfilterproxymodel.h
/usr/include/KF6/KItemViews/kcategorizedview.h
/usr/include/KF6/KItemViews/kcategorydrawer.h
/usr/include/KF6/KItemViews/kextendableitemdelegate.h
/usr/include/KF6/KItemViews/kitemviews_export.h
/usr/include/KF6/KItemViews/kitemviews_version.h
/usr/include/KF6/KItemViews/klistwidgetsearchline.h
/usr/include/KF6/KItemViews/ktreewidgetsearchline.h
/usr/include/KF6/KItemViews/ktreewidgetsearchlinewidget.h
/usr/include/KF6/KItemViews/kwidgetitemdelegate.h
/usr/lib64/cmake/KF6ItemViews/KF6ItemViewsConfig.cmake
/usr/lib64/cmake/KF6ItemViews/KF6ItemViewsConfigVersion.cmake
/usr/lib64/cmake/KF6ItemViews/KF6ItemViewsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6ItemViews/KF6ItemViewsTargets.cmake
/usr/lib64/libKF6ItemViews.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6ItemViews.so.6.10.0
/V3/usr/lib64/qt6/plugins/designer/kitemviews6widgets.so
/usr/lib64/libKF6ItemViews.so.6
/usr/lib64/libKF6ItemViews.so.6.10.0
/usr/lib64/qt6/plugins/designer/kitemviews6widgets.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kitemviews/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kitemviews/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kitemviews/e712eadfab0d2357c0f50f599ef35ee0d87534cb
