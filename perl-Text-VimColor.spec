#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	VimColor
Summary:	Syntax color text in HTML or XML using Vim
Name:		perl-Text-VimColor
Version:	0.07
Release:	1
# same as Perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6d19512fb68787d06818b3e8093886e7
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Path-Class
%endif
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
