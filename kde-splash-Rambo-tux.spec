
%define		_splash		Rambo-tux

Summary:	KDE splash screen
Summary(pl):	Ekran startowy KDE
Name:		kde-splash-%{_splash}
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Amusements
#Source0:	http://www.kde-look.org/content/download.php?content=12624&id=1
Source0:	http://www.kde-look.org/content/files/12624-aranio.tar.gz
# Source0-md5:	ffcc9dd26a25b7c7d8647257863e600a
Patch0:		%{name}.patch
URL:		http://www.kde-look.org/content/show.php?content=12624
Provides:	kde-splash
Requires:	kdebase-desktop >= 9:3.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rambo Tux in action! Better start running if you are using Windows :)

%description -l pl
Rambo Tux w akcji! Je¿eli u¿ywasz Windows to lepiej zacznij ju¿ uciekaæ :)

%prep
%setup -q -c %{_splash} -n %{_splash}
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}
install aranio/* $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/%{_splash}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/*
