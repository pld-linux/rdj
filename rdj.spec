Summary:	Yet another movie player for linux
Name:		rdj
Version:	0.3.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://mimms.sf.net/%{name}-%{version}.tgz
Patch0:		%{name}-X11R6_path.patch
URL:		http://mimms.sf.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix /usr/X11R6

%description
Premiere gtk+ radio controller. If you think it's rather small, then
you got author's point. This radio program is designed for the
video4linux driver and the license is GNU GPL.

%prep
%setup -q
%patch0 -p1

%build
cd src
CFLAGS="%{rpmcflags}"
%{__make} rdj

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/%{name}/xpm,%{_bindir},%{_mandir}/man1} \
		$RPM_BUILD_ROOT{%{_applnkdir}/Multimedia,%{_pixmapsdir}}
		
install src/{rdj,rdj_scan,rdj_term,fscan} $RPM_BUILD_ROOT%{_bindir}
install rdj.desktop $RPM_BUILD_ROOT%{_applnkdir}/Multimedia
install rdj_icon.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install rdj.1 $RPM_BUILD_ROOT%{_mandir}/man1
install xpm/* $RPM_BUILD_ROOT%{_datadir}/%{name}/xpm

gzip -9nf KNOWN_BUGS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Multimedia/rdj.desktop
%{_datadir}/%{name}
%{_pixmapsdir}/*
%{_mandir}/man1/*
