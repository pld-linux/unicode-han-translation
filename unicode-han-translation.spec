Summary:	Translation of Unicode East Asian ideographs definitions
Summary(pl):	T³umaczenia definicji unikodowych ideogramów wschodnioazjatyckich
Name:		unicode-han-translation
Version:	0.0.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://freedesktop.org/Software/unicode-translation/releases/%{name}-%{version}.tar.gz
# Source0-md5:	b991e8d361f31a4abdfdeb55051584b3
# it's not directory, don't add /
URL:		http://freedesktop.org/Software/unicode-translation
BuildRequires:	intltool >= 0.22
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unicode-han-translation project aims to translate Unicode
definitions of East Asian ideographs.

%description -l pl
Celem projektu unicode-han-translation jest przet³umaczenie definicji
unikodowych ideogramów wschodnioazjatyckich.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no translations yet
#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
# -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%{_pkgconfigdir}/*.pc
