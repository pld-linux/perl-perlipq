%include	/usr/lib/rpm/macros.perl
%define	pdir	perlipq
Summary:	IPTables::IPv4::IPQueue − Perl extension for libipq
#Summary(pl.UTF-8):	
Name:		perl-perlipq
Version:	1.25
Release:	2
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/J/JM/JMORRIS/perlipq-1.25.tar.gz
# Source0-md5:	212b66e26a80fb9e474b0d9c8c683c2e
URL:		http://search.cpan.org/dist/perlipq/
BuildRequires:	iptables-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perlipq (IPTables::IPv4::IPQueue) is a Perl extension for iptables
userspace packet queuing via libipq.

Packets may be selected from the stack via the iptables QUEUE target and
passed to userspace.  Perlipq allows these packets to be manipulated in
Perl and passed back to the stack.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"IPTables::IPv4::IPQueue", LIBS=>"-lipq", VERSION=>"%{version}")' \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README *.pl
%{perl_vendorarch}/IPTables/IPv4/*.pm
%dir %{perl_vendorarch}/auto/IPTables/IPv4/IPQueue
%{perl_vendorarch}/auto/IPTables/IPv4/IPQueue/*.ix
%attr(755,root,root) %{perl_vendorarch}/auto/IPTables/IPv4/IPQueue/*.so
%{_mandir}/man3/*
