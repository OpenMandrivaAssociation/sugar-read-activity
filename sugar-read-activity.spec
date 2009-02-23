# NOTE: Do not edit, file was generated by jhconvert

Name: sugar-read-activity
Version: 64
Release: %mkrel 1
Summary: Read activity for Sugar
License: GPL
Group: Graphical desktop/Other
Url: http://sugarlabs.org/

Source: http://download.sugarlabs.org/sources/sucrose/fructose/Read/Read-64.tar.bz2

Requires: sugar-toolkit >= 0.83.7
Requires: evince >= 2.25.90
Requires: gnome-python-evince >= 2.25.90

BuildRequires: sugar-toolkit >= 0.83.7
BuildRequires: gettext  

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
Read activity for Sugar

%prep
%setup -q -n Read-64


%build
python  \
	setup.py \
	build

%install
rm -rf %{buildroot}
[ -f setup.py ] && chmod 0755 setup.py
python  \
	setup.py \
	install \
	--prefix=%{buildroot}/%{_prefix}
%find_lang org.laptop.sugar.ReadActivity

%clean
rm -rf %{buildroot}

%files -f org.laptop.sugar.ReadActivity.lang
%defattr(-,root,root,-)
%{_datadir}/sugar/activities/*
%doc AUTHORS COPYING

