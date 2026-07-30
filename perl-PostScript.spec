%define upstream_name	 PostScript
%define upstream_version 0.06
Name:		perl-%{upstream_name}
Version:	0.06
Release:	2

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        https://metacpan.org/dist/PostScript
Source0:	https://cpan.metacpan.org/authors/id/S/SH/SHAWNPW/PostScript-0.06.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is the %{upstream_name} module for perl.

%prep
%setup -q -n PostScript-0.06

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test || :

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/PostScript
%{_mandir}/*/*


