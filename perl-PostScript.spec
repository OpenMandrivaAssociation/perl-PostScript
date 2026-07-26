%define upstream_name	 PostScript
Name:		perl-%{upstream_name}
Version:	0.06
Release:	6

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        https://metacpan.org/dist/PostScript
Source0:	https://cpan.metacpan.org/authors/id/S/SH/SHAWNPW/PostScript-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is the %{upstream_name} module for perl.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/PostScript
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 404350
- rebuild using %0.06 Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.06-5mdv2009.0
+ Revision: 241844
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-3mdv2008.0
+ Revision: 86817
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-2mdv2007.0
- Rebuild

* Mon Mar 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdk
- first mdk release

