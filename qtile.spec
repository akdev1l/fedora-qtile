Summary: A pure-Python tiling window manager
Name: qtile
Version: 0.9.1
Release: 3%{?dist}
Source0: https://github.com/qtile/qtile/archive/v%{version}.tar.gz
License: MIT and GPLv3+ and ASL 2.0
# All MIT except for:
# libqtile/widget/pacman.py:GPL (v3 or later)
# libqtile/widget/google_calendar.py:Apache (v2.0)
BuildArch: noarch
Url: http://qtile.org

Source1:  qtile.desktop

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-cffi
BuildRequires:  python-nose-cov
BuildRequires:  python-xcffib
BuildRequires:  python-trollius
BuildRequires:  python-cairocffi
BuildRequires:  python-six
BuildRequires:  python-pycparser

Requires:  python-cairocffi
Requires:  python-cffi
Requires:  python-xcffib
Requires:  python-trollius

%description

A pure-Python tiling window manager.

Features
========

    * Simple, small and extensible. It's easy to write your own layouts,
      widgets and commands.
    * Configured in Python.
    * Command shell that allows all aspects of
      Qtile to be managed and inspected.
    * Complete remote scriptability - write scripts to set up workspaces,
      manipulate windows, update status bar widgets and more.
    * Qtile's remote scriptability makes it one of the most thoroughly
      unit-tested window mangers around.


%prep
%setup -q -n qtile-%{version} 

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --single-version-externally-managed -O1 --root=%{buildroot} --record=INSTALLED_FILES
mkdir -p %{buildroot}%{_datadir}/xsessions/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/xsessions/
chmod a+x %{buildroot}%{python_sitelib}/libqtile/confreader.py
chmod a+x %{buildroot}%{python_sitelib}/libqtile/widget/yahoo_weather.py
chmod a+x %{buildroot}%{python_sitelib}/libqtile/widget/bitcoin_ticker.py
chmod a+x %{buildroot}%{python_sitelib}/libqtile/widget/sensors.py



%files
%license LICENSE
%doc README.rst
%{_mandir}/man1/qsh.1*
%{_mandir}/man1/qtile.1*
%{_bindir}/qsh
%{_bindir}/qtile
%{_bindir}/qtile-run
%{_bindir}/qtile-session
%{python2_sitelib}/qtile-%{version}-py%{python2_version}.egg-info
%{python2_sitelib}/qtile-%{version}-py%{python2_version}.egg-info/*
%{python2_sitelib}/libqtile
%{python2_sitelib}/libqtile/*
%{_datadir}/xsessions/qtile.desktop


%changelog
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb 22 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.9.1-2
- Final update to licensing

* Sat Feb 14 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.9.1-1
- Update for new upstream release
- Fix license headers.

* Sun Feb 01 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.9.0-2
- Update spec for qtile-0.9.0
- Include in Fedora.

* Wed Oct 08 2014 John Dulaney <jdulaney@fedoraproject.org> - 0.8.0-1
- Initial packaging
- Spec based on python-nose
