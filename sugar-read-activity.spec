# NOTE: Please do not edit this file, it was auto generated by jhconvert
#       See http://wiki.sugarlabs.org/go/Deployment_Team/jhconvert for details

Name: sugar-read-activity
Version: 78
Release: %mkrel 1
Summary: Read activity for Sugar
License: GPL
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/fructose/Read/Read-78.tar.bz2

Requires: python-beautifulsoup  
Requires: evince >= 2.26.0
Requires: gnome-python-evince >= 2.26.0
Requires: python-lxml  
Requires: python-webkitgtk  
Requires: sugar-toolkit >= 0.88.0

BuildRequires: gettext  
BuildRequires: sugar-toolkit >= 0.88.0

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
Read activity for Sugar

%prep
%setup -q -n Read-78


%build

rm -f MANIFEST
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --prefix=%{buildroot}/%{_prefix}
find %{buildroot} -name '*.py.orig' -print0 | xargs -0 rm -f
rm -rf %{buildroot}/%{_datadir}/sugar/activities/*/epubview/modules
%find_lang org.laptop.sugar.ReadActivity

%clean
rm -rf %{buildroot}

%files -f org.laptop.sugar.ReadActivity.lang
%defattr(-,root,root,-)
%{_datadir}/sugar/activities/*
%doc AUTHORS COPYING

