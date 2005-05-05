#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	VimColor
Summary:	Text::VimColor - syntax color text in HTML or XML using Vim
Summary(pl):	Text::VimColor - kolorowanie sk³adni tekstu w HTML-u lub XML-u przy u¿yciu Vima
Name:		perl-Text-VimColor
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d525da57e7b047eaba81f672cf4b435a
%if %{with tests}
BuildRequires:	perl-Path-Class
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module tries to markup text files according to their syntax. It
can be used to produce web pages with pretty-printed colourful source
code samples. It can produce output in the following formats:
- HTML 
 Valid XHTML 1.0, with the exact colouring and style left to a CSS
 stylesheet
- XML 
 Pieces of text are marked with XML elements in a simple vocabulary,
 which can be converted to other formats, for example, using XSLT
- Perl array 
 A simple Perl data structure, so that Perl code can be used to turn
 it into whatever is needed
This module works by running the Vim text editor and getting it to
apply its excellent syntax highlighting (aka 'font-locking') to an
input file, and mark pieces of text according to whether it thinks
they are comments, keywords, strings, etc.

%description -l pl
Ten modu³ próbuje oznaczyæ pliki tekstowe zgodnie z ich sk³adni±. Mo¿e
byæ u¿ywany do tworzenia stron WWW z ³adnie wydrukowanymi, kolorowymi
przyk³adami kodu ¼ród³owego. Modu³ mo¿e tworzyæ wynik w nastêpuj±cych
formatach:
- HTML - poprawny XHTML 1.0, z dok³adnym kolorowaniem i stylem
  pozostawionym dla arkusza CSS
- XML - fragmenty tekstu oznaczane elementami XML-a z prostym
  s³ownictwem; mo¿na to skonwertowaæ do innych formatów, na przyk³ad
  przy u¿yciu XSLT
- tablica perlowa - prosta struktura danych w Perlu, dziêki czemu
  mo¿na u¿yæ perlowego kodu do przekszta³cenia jej w co tylko
  potrzeba.
Ten modu³ dzia³a poprzez uruchomienie edytora tekstu Vim i zmuszenie
go do zastosowania swojego ¶wietnego pod¶wietlania sk³adni (znanego
tak¿e jako 'font-locking') dla pliku wej¶ciowego oraz oznaczenia
fragmentów tekstu zale¿nie od tego, czy uwa¿a je za komentarze, s³owa
kluczowe, ³añcuchy itp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/Text/*
%{_mandir}/man3/*
%{_mandir}/man1/*
