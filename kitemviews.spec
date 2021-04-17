#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kitemviews
Version  : 5.81.0
Release  : 41
URL      : https://download.kde.org/stable/frameworks/5.81/kitemviews-5.81.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.81/kitemviews-5.81.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.81/kitemviews-5.81.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: kitemviews-data = %{version}-%{release}
Requires: kitemviews-lib = %{version}-%{release}
Requires: kitemviews-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n kitemviews-5.81.0
cd %{_builddir}/kitemviews-5.81.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618620667
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1618620667
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kitemviews
cp %{_builddir}/kitemviews-5.81.0/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kitemviews/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/kitemviews-5.81.0/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kitemviews/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/kitemviews-5.81.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kitemviews/20079e8f79713dce80ab09774505773c926afa2a
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/locale/af/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/as/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/az/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/be/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/bn/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/br/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/crh/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/csb/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/cy/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/da/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/de/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/el/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/es/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/et/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/fa/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/fy/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/gd/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/gu/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/ha/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/he/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/hne/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/hy/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/id/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/is/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/it/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/km/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/kn/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/ku/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/lb/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/mai/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/mk/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/ms/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/ne/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/oc/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/or/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/ps/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/se/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/si/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/sq/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/ta/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/te/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/th/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/tt/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/uz/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/vi/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/wa/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/xh/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/zh_HK/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kitemviews5_qt.qm
/usr/share/qlogging-categories5/kitemviews.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KItemViews/KCategorizedSortFilterProxyModel
/usr/include/KF5/KItemViews/KCategorizedView
/usr/include/KF5/KItemViews/KCategoryDrawer
/usr/include/KF5/KItemViews/KExtendableItemDelegate
/usr/include/KF5/KItemViews/KFilterProxySearchLine
/usr/include/KF5/KItemViews/KListWidgetSearchLine
/usr/include/KF5/KItemViews/KTreeWidgetSearchLine
/usr/include/KF5/KItemViews/KTreeWidgetSearchLineWidget
/usr/include/KF5/KItemViews/KWidgetItemDelegate
/usr/include/KF5/KItemViews/kcategorizedsortfilterproxymodel.h
/usr/include/KF5/KItemViews/kcategorizedview.h
/usr/include/KF5/KItemViews/kcategorydrawer.h
/usr/include/KF5/KItemViews/kextendableitemdelegate.h
/usr/include/KF5/KItemViews/kfilterproxysearchline.h
/usr/include/KF5/KItemViews/kitemviews_export.h
/usr/include/KF5/KItemViews/klistwidgetsearchline.h
/usr/include/KF5/KItemViews/ktreewidgetsearchline.h
/usr/include/KF5/KItemViews/ktreewidgetsearchlinewidget.h
/usr/include/KF5/KItemViews/kwidgetitemdelegate.h
/usr/include/KF5/kitemviews_version.h
/usr/lib64/cmake/KF5ItemViews/KF5ItemViewsConfig.cmake
/usr/lib64/cmake/KF5ItemViews/KF5ItemViewsConfigVersion.cmake
/usr/lib64/cmake/KF5ItemViews/KF5ItemViewsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5ItemViews/KF5ItemViewsTargets.cmake
/usr/lib64/libKF5ItemViews.so
/usr/lib64/qt5/mkspecs/modules/qt_KItemViews.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5ItemViews.so.5
/usr/lib64/libKF5ItemViews.so.5.81.0
/usr/lib64/qt5/plugins/designer/kitemviews5widgets.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kitemviews/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kitemviews/e712eadfab0d2357c0f50f599ef35ee0d87534cb
