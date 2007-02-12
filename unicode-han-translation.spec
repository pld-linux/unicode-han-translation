Summary:	Translation of Unicode East Asian ideographs definitions
Summary(pl.UTF-8):   Tłumaczenia definicji unikodowych ideogramów wschodnioazjatyckich
Name:		unicode-han-translation
Version:	0.0.2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://freedesktop.org/Software/unicode-translation/releases/%{name}-%{version}.tar.gz
# Source0-md5:	7f51d96137af6f01adc118d26834b5e6
# it's not directory, don't add /
URL:		http://freedesktop.org/Software/unicode-translation
BuildRequires:	intltool >= 0.22
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unicode-han-translation project aims to translate Unicode
definitions of East Asian ideographs.

%description -l pl.UTF-8
Celem projektu unicode-han-translation jest przetłumaczenie definicji
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

#%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_pkgconfigdir}/*.pc
