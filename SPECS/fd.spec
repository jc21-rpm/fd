%global debug_package %{nil}

Name:           fd
Version:        7.3.0
Release:        1%{?dist}
Summary:        fd is a simple, fast and user-friendly alternative to find.

Group:          Applications/System
License:        GPLv2
URL:            https://github.com/sharkdp/%{name}

BuildRequires:  cmake, libgit2, openssl-devel
%{?el7:BuildRequires: cargo, rust}

%description
- Convenient syntax: fd PATTERN instead of find -iname '*PATTERN*'.
- Colorized terminal output (similar to ls).
- It's fast (see benchmarks below).
- Smart case: the search is case-insensitive by default. It switches to case-sensitive if the pattern contains an uppercase character*.
- Ignores hidden directories and files, by default.
- Ignores patterns from your .gitignore, by default.
- Regular expressions.
- Unicode-awareness.
- The command name is 50 percent shorter* than find :-).
- Parallel command execution with a syntax similar to GNU Parallel.

%prep
wget https://github.com/sharkdp/%{name}/archive/v%{version}.tar.gz
tar xzf v%{version}.tar.gz


%build
cd %{name}-%{version}
cargo build --release


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp %{name}-%{version}/target/release/fd %{buildroot}/usr/bin/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc %{name}-%{version}/LICENSE* %{name}-%{version}/*.md
/usr/bin/fd


%changelog
* Thu Feb 14 2018 Jamie Curnow <jc@jc21.com> - 7.3.0-1
- v7.3.0 <3

* Mon Oct 29 2018 Jamie Curnow <jc@jc21.com> - 7.2.0-1
- v7.2.0

* Fri Aug 31 2018 Jamie Curnow <jc@jc21.com> - 7.1.0-1
- Initial spec

