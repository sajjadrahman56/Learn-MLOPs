---
reviewers:
- sig-api-machinery
- sig-architecture
- sig-cli
- sig-cluster-lifecycle
- sig-node
- sig-release
title: সংস্করণ স্কেও(Skew) নীতি
type: docs
description: >
  বিভিন্ন কুবারনেটিসের উপাদানগুলির মধ্যে সমর্থিত সর্বাধিক সংস্করণ স্ক্যু(skew)।
---

<!-- overview -->
এই ডকুমেন্টটি বিভিন্ন কুবারনেটিসের উপাদানগুলির মধ্যে সমর্থিত সর্বাধিক সংস্করণ স্ক্যু(skew) বর্ণনা করে।
নির্দিষ্ট ক্লাস্টার সরঞ্জামগুলি সংস্করণ স্ক্যুতে(skew) অতিরিক্ত সীমাবদ্ধতা স্থাপন করতে পারে৷

<!-- body -->

## সমর্থিত সংস্করণগুলি

কুবারনেটিস সংস্করণ **x.y.z** হিসাবে প্রকাশ করা হয়,
যেখানে **x** হল মুখ্য সংস্করণ, **y** হল গৌণ সংস্করণ এবং **z** হল প্যাচ ভার্সন (patch version),
যা [শব্দার্থিক সংস্করণ](https://semver.org/) পরিভাষা অনুসরণ করে হয়। অতিরিক্ত তথ্যসমূহের জন্য, দেখুন
[কুবারনেটিস রিলিজ সংস্করণ](https://git.k8s.io/sig-release/release-engineering/versioning.md#kubernetes-release-versioning)।

কুবারনেটিস প্রজেক্ট সাম্প্রতিক তিনটি পর্যন্ত ছোট রিলিজের জন্য রিলিজ শাখা বজায় রাখে
({{< skew latestVersion >}}, {{< skew prevMinorVersion >}}, {{< skew oldestMinorVersion >}})।
কুবারনেটিস 1.19 এবং নতুন ভার্সন [আনুমানিক 1 বছরের প্যাচ সাপোর্ট পায়(patch support)](/bn/releases/patch-releases/#support-period)
কুবারনেটিস 1.18 এবং তার বেশি বয়সীরা প্রায় 9 মাস প্যাচ সাপোর্ট (patch support) পেয়েছে।

প্রযোজ্য সংশোধন, নিরাপত্তা সংশোধন সহ, তীব্রতা এবং সম্ভাব্যতার উপর নির্ভর করে,
সেই তিনটি রিলিজ শাখায় ব্যাকপোর্ট করা যেতে পারে। প্যাচ রিলিজগুলি এই শাখাগুলি থেকে একটি
[নিয়মিত ক্যাডেন্স](/bn/releases/patch-releases/#cadence) এ কাটা হয়, এবং প্রয়োজনে অতিরিক্ত জরুরী রিলিজগুলি।

এ [রিলিজ ম্যানেজার](/bn/releases/release-managers/) গ্রুপ এই সিদ্ধান্তের মালিক।

আরও তথ্যের জন্য, কুবারনেটিস [প্যাচ রিলিজ](/bn/releases/patch-releases/) পৃষ্ঠাটি দেখুন।

## সংস্করণ সমর্থিত স্ক্যু(skew)

### কুবে-এপিসার্ভার (kube-apiserver)

[অত্যন্ত-উপলব্ধ (HA) ক্লাস্টারে](/bn/docs/setup/production-environment/tools/kubeadm/high-availability/),,
নতুন এবং প্রাচীনতম `kube-apiserver` উদাহরণগুলি অবশ্যই একটি ছোট সংস্করণের মধ্যে থাকতে হবে৷

উদাহরণ:

* নতুন `kube-apiserver` **{{< skew currentVersion >}}** এ আছে 
* অন্যান্য `kube-apiserver` ইন্সট্যান্সগুলি **{{< skew currentVersion >}}** এবং **{{< skew currentVersionAddMinor -1 >}}** এ সমর্থিত

### kubelet

* `kubelet` নতুন হওয়া উচিত নয় `kube-apiserver` এর চেয়ে।
* `kubelet` তিনটি ছোট সংস্করণ পর্যন্ত পুরানো হতে পারে `kube-apiserver` এর চেয়ে (`kubelet` < 1.25 শুধুমাত্র দুটি ছোট সংস্করণ পর্যন্ত পুরানো হতে পারে `kube-apiserver` এর চেয়ে).

উদাহরণ:

* `kube-apiserver` **{{< skew currentVersion >}}** এ আছে 
* `kubelet` **{{< skew currentVersion >}}**, **{{< skew currentVersionAddMinor -1 >}}**,
  **{{< skew currentVersionAddMinor -2 >}}**, এবং **{{< skew currentVersionAddMinor -3 >}}** সমর্থিত

{{< note >}}
If version skew exists between `kube-apiserver` instances in an HA cluster, this narrows the allowed `kubelet` versions.
{{</ note >}}

উদাহরণ:

* `kube-apiserver` ইন্সট্যান্সগুলিতে **{{< skew currentVersion >}}** এবং **{{< skew currentVersionAddMinor -1 >}}**  আছে
* `kubelet` **{{< skew currentVersionAddMinor -1 >}}**, **{{< skew currentVersionAddMinor -2 >}}**,
  এবং **{{< skew currentVersionAddMinor -3 >}}** এ সমর্থিত (**{{< skew currentVersion >}}** সমর্থিত নয় কারণ
  এটি সংস্করণ **{{< skew currentVersionAddMinor -1 >}}** -এ `kube-apiserver` ইন্সট্যান্সের চেয়ে নতুন হবে)

### kube-proxy

* `kube-proxy` নতুন হওয়া উচিত নয় `kube-apiserver` এর চেয়ে।
* `kube-proxy` তিনটি ছোট সংস্করণ পর্যন্ত পুরানো হতে পারে `kube-apiserver` এর চেয়ে
  (`kube-proxy` < 1.25 শুধুমাত্র দুটি ছোট সংস্করণ পর্যন্ত পুরানো হতে পারে `kube-apiserver`) এর চেয়ে।
* `kube-proxy` তিনটি ছোট সংস্করণ পর্যন্ত পুরানো বা নতুন হতে পারে `kubelet` ইন্সট্যান্সের(instance) থেকে
  পাশাপাশি এটি চলে (`kube-proxy` < 1.25 শুধুমাত্র দুটি ছোট সংস্করণ পর্যন্ত পুরানো বা নতুন হতে পারে
  `kubelet` ইন্সট্যান্সের থেকে পাশাপাশি এটি চলে )।

উদাহরণ:

* `kube-apiserver` **{{< skew currentVersion >}}** এ আছে 
* `kube-proxy` তে **{{< skew currentVersion >}}**, **{{< skew currentVersionAddMinor -1 >}}**,
  **{{< skew currentVersionAddMinor -2 >}}**, এবং **{{< skew currentVersionAddMinor -3 >}}** এ সমর্থিত

{{< note >}}
If version skew exists between `kube-apiserver` instances in an HA cluster, this narrows the allowed `kube-proxy` versions.
{{</ note >}}

উদাহরণ:

* `kube-apiserver` ইন্সট্যান্সে **{{< skew currentVersion >}}** এবং **{{< skew currentVersionAddMinor -1 >}}** আছে
* `kube-proxy` **{{< skew currentVersionAddMinor -1 >}}**, **{{< skew currentVersionAddMinor -2 >}}**,
  এবং **{{< skew currentVersionAddMinor -3 >}}** এ সমর্থিত (**{{< skew currentVersion >}}** সমর্থিত নয় কারণ
  এটি সংস্করণ **{{< skew currentVersionAddMinor -1 >}}** -এ `kube-apiserver` ইন্সট্যান্সের চেয়ে নতুন হবে)

### কুবে-কন্ট্রোলার-ম্যানেজার, কুবে-শিডিউলার, এবং ক্লাউড-কন্ট্রোলার-ম্যানেজার (kube-controller-manager, kube-scheduler, and cloud-controller-manager)

`kube-controller-manager`, `kube-scheduler`, এবং `cloud-controller-manager` নতুন হওয়া উচিত নয়
`kube-apiserver` থেকে ইন্সট্যান্সগুলির সাথে তারা যোগাযোগ করে। তারা `kube-apiserver` ক্ষুদ্র সংস্করণের সাথে মিলবে বলে আশা করা হচ্ছে,
কিন্তু একটি ছোট সংস্করণ পর্যন্ত পুরানো হতে পারে (লাইভ আপগ্রেডের অনুমতি দেওয়ার জন্য)।

উদাহরণ:

* `kube-apiserver` **{{< skew currentVersion >}}** এ আছে 
* `kube-controller-manager`, `kube-scheduler`, এবং `cloud-controller-manager` সমর্থিত আছে
  **{{< skew currentVersion >}}** এবং **{{< skew currentVersionAddMinor -1 >}}**

{{< note >}}
If version skew exists between `kube-apiserver` instances in an HA cluster, and these components
can communicate with any `kube-apiserver` instance in the cluster (for example, via a load balancer),
this narrows the allowed versions of these components.
{{< /note >}}

উদাহরণ:

* `kube-apiserver` ইন্সট্যান্সে **{{< skew currentVersion >}}** এবং **{{< skew currentVersionAddMinor -1 >}}** আছে
* `kube-controller-manager`, `kube-scheduler`, এবং `cloud-controller-manager` একটি লোড ব্যালেন্সারের সাথে যোগাযোগ করে
  যে কোনো `kube-apiserver` ইন্সট্যান্সে রুট করতে পারে
* `kube-controller-manager`, `kube-scheduler`, এবং `cloud-controller-manager` সমর্থিত আছে
  **{{< skew currentVersionAddMinor -1 >}}** (**{{< skew currentVersion >}}** সমর্থিত নয়
  কারণ এটি **{{< skew currentVersionAddMinor -1 >}}** সংস্করণে নতুন হবে `kube-apiserver` ইন্সট্যান্সের চেয়ে নতুন হবে)

### kubectl

`kubectl` একটি ছোট সংস্করণ (পুরানো বা নতুন) `kube-apiserver` এর মধ্যে সমর্থিত।

উদাহরণ:

* `kube-apiserver` আছে **{{< skew currentVersion >}}**
* `kubectl` সমর্থিত আছে **{{< skew currentVersionAddMinor 1 >}}**, **{{< skew currentVersion >}}**,
  এবং **{{< skew currentVersionAddMinor -1 >}}**

{{< note >}}
If version skew exists between `kube-apiserver` instances in an HA cluster, this narrows the supported `kubectl` versions.
{{< /note >}}

উদাহরণ:

* `kube-apiserver` ইন্সট্যান্সে আছে **{{< skew currentVersion >}}** এবং **{{< skew currentVersionAddMinor -1 >}}**
* `kubectl` সমর্থিত আছে **{{< skew currentVersion >}}** এবং **{{< skew currentVersionAddMinor -1 >}}**
  (অন্যান্য সংস্করণগুলি `kube-apiserver` উপাদানগুলির একটি থেকে একের বেশি ছোটখাট সংস্করণ হবে )

## উপাদান সমর্থিত আপগ্রেড অর্ডার

উপাদানগুলির মধ্যে সমর্থিত সংস্করণের স্কুটির প্রভাব রয়েছে যে ক্রম 
অনুসারে উপাদানগুলিকে আপগ্রেড করতে হবে৷ এই বিভাগটি 
**{{< skew currentVersionAddMinor -1 >}}** সংস্করণ থেকে **{{< skew currentVersion >}}** সংস্করণে একটি বিদ্যমান 
ক্লাস্টার রূপান্তর করতে উপাদানগুলিকে আপগ্রেড করতে হবে তা বর্ণনা করে৷

ঐচ্ছিকভাবে, আপগ্রেড করার প্রস্তুতির সময়, কুবারনেটস প্রজেক্ট সুপারিশ করে যে 
আপনি আপগ্রেড করার সময় যতটা সম্ভব রিগ্রেশন এবং বাগ ফিক্স থেকে উপকৃত হতে 
নিম্নলিখিতগুলি করুন:

* নিশ্চিত করুন যে উপাদানগুলি আপনার বর্তমান ছোট সংস্করণের সবচেয়ে সাম্প্রতিক প্যাচ 
  সংস্করণে রয়েছে৷
* ক্ষুদ্র লক্ষ্য সংস্করণের সবচেয়ে সাম্প্রতিক প্যাচ সংস্করণে উপাদান আপগ্রেড 
  করুন।

উদাহরণস্বরূপ, আপনি যদি {{<skew currentVersionAddMinor -1>}} সংস্করণ চালাচ্ছেন,
তাহলে নিশ্চিত করুন যে আপনি সাম্প্রতিক প্যাচ সংস্করণে আছেন৷ তারপর, {{<skew currentVersion>}}-এর সবচেয়ে 
সাম্প্রতিক প্যাচ সংস্করণে আপগ্রেড করুন৷

### kube-apiserver

পূর্বশর্তসমূহ:

* একটি একক-ইন্সট্যান্স ক্লাস্টারে, বিদ্যমান `kube-apiserver` ইন্সট্যান্স হল **{{< skew currentVersionAddMinor -1 >}}**
* একটি HA ক্লাস্টারে, সমস্ত `kube-apiserver` ইন্সট্যান্সগুলি **{{< skew currentVersionAddMinor -1 >}}** বা
  **{{< skew currentVersion >}}** এ থাকে (এটি প্রাচীনতম এবং নতুন `kube-apiserver` ইন্সট্যান্সের মধ্যে সর্বাধিক 1 টি ছোট সংস্করণ নিশ্চিত করে )
* এই সার্ভারের সাথে যোগাযোগকারী `কুব-কন্ট্রোলার-ম্যানেজার`, `কুব-শিডিউলার` এবং `ক্লাউড-কন্ট্রোলার-ম্যানেজার`
  ইনস্ট্যান্সগুলি **{{< skew currentVersionAddMinor -1 >}}** সংস্করণে রয়েছে
  (এটি নিশ্চিত করে যে তারা বিদ্যমান API সার্ভার সংস্করণের চেয়ে নতুন নয় ,এবং এর মধ্যে রয়েছে নতুন API সার্ভার সংস্করণের 1টি ছোট সংস্করণ)
* সমস্ত নোডের `kubelet` ইনস্ট্যান্সগুলি **{{< skew currentVersionAddMinor -1 >}}** or **{{< skew currentVersionAddMinor -2 >}}** সংস্করণে রয়েছে
  (এটি নিশ্চিত করে যে তারা বিদ্যমান API সার্ভার সংস্করণের চেয়ে নতুন নয় ,এবং নতুন API সার্ভার সংস্করণের 2টি ছোট সংস্করণের মধ্যে রয়েছে)
* নিবন্ধিত ভর্তির ওয়েবহুকগুলি নতুন `কুবে-এপিসার্ভার` ইনস্ট্যান্স যে ডেটা পাঠাবে তা পরিচালনা করতে সক্ষম:
  * `ValidatingWebhookConfiguration` এবং `MutatingWebhookConfiguration` অবজেক্ট অন্তর্ভুক্ত করার জন্য আপডেট করা হয়েছে
    REST রিসোর্সের যেকোন নতুন সংস্করণ **{{< skew currentVersion >}}** এ যোগ করা হয়েছে 
    (বা ব্যবহার করুন [`matchPolicy: Equivalent` option](/bn/docs/reference/access-authn-authz/extensible-admission-controllers/#matching-requests-matchpolicy) v1.15+ এ সহজলভ্য)
  * ওয়েবহুকগুলি REST সংস্থানগুলির যে কোনও নতুন সংস্করণ পরিচালনা করতে সক্ষম যা তাদের কাছে পাঠানো হবে,
    এবং **{{< skew currentVersion >}}**-এ বিদ্যমান সংস্করণগুলিতে যে কোনও নতুন ক্ষেত্র যুক্ত করা হবে।

`kube-apiserver`  আপগ্রেড করুন **{{< skew currentVersion >}}**

{{< note >}}
Project policies for [API deprecation](/docs/reference/using-api/deprecation-policy/) and
[API change guidelines](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api_changes.md)
require `kube-apiserver` to not skip minor versions when upgrading, even in single-instance clusters.
{{< /note >}}

### কুবে-কন্ট্রোলার-ম্যানেজার, কুবে-শিডিউলার, এবং ক্লাউড-কন্ট্রোলার-ম্যানেজার(kube-controller-manager, kube-scheduler, and cloud-controller-manager)

পূর্বশর্তসমূহ:

* `kube-apiserver` ইনস্ট্যান্সগুলির সাথে এই উপাদানগুলি **{{< skew currentVersion >}}** -এ যোগাযোগ করে
  (HA ক্লাস্টারে যেখানে এই কন্ট্রোল প্লেন উপাদানগুলি ক্লাস্টারের যেকোনো `kube-apiserver` ইনস্ট্যান্সের সাথে যোগাযোগ
  করতে পারে, এই উপাদানগুলি আপগ্রেড করার আগে সমস্ত `kube-apiserver` ইনস্ট্যান্সগুলি আপগ্রেড করা আবশ্যক)

**{{< skew currentVersion >}}** থেকে  আপগ্রেড করুন  `kube-controller-manager`, `kube-scheduler`, এবং
`cloud-controller-manager` । `kube-controller-manager`, `kube-scheduler`, 
`cloud-controller-manager`  এর মধ্যে কোনো প্রয়োজনীয় আপগ্রেড অর্ডার নেই।
আপনি যে কোনো ক্রমে এই উপাদান আপগ্রেড করতে পারেন, বা
এমনকি একই সাথে।

### kubelet

পূর্বশর্তসমূহ:

* যে `kube-apiserver`  দৃইনস্ট্যান্স  `kubelet` এর সাথে যোগাযোগ করে তা **{{< skew currentVersion >}}**-এ।

ঐচ্ছিকভাবে `kubelet` ইনস্ট্যান্সগুলিকে **{{< skew currentVersion >}}** তে আপগ্রেড করুন (অথবা সেগুলি
**{{< skew currentVersionAddMinor -1 >}}**, **{{< skew currentVersionAddMinor -2 >}}**, বা **{{< skew currentVersionAddMinor -3 >}}** এ ছেড়ে দেওয়া যেতে পারে)

{{< note >}}
Before performing a minor version `kubelet` upgrade, [drain](/docs/tasks/administer-cluster/safely-drain-node/) pods from that node.
In-place minor version `kubelet` upgrades are not supported.
{{</ note >}}

{{< warning >}}
Running a cluster with `kubelet` instances that are persistently three minor versions behind
`kube-apiserver` means they must be upgraded before the control plane can be upgraded.
{{</ warning >}}

### kube-proxy

পূর্বশর্তসমূহ:

* যে `kube-apiserver`  ইনস্ট্যান্স `kube-proxy` এর সাথে যোগাযোগ করে তা **{{< skew currentVersion >}}**-এ।

ঐচ্ছিকভাবে `kube-proxy` ইনস্ট্যান্সগুলিকে **{{< skew currentVersion >}}** তে আপগ্রেড করুন
(অথবা সেগুলি **{{< skew currentVersionAddMinor -1 >}}**, **{{< skew currentVersionAddMinor -2 >}}**,
বা **{{< skew currentVersionAddMinor -3 >}}** এ ছেড়ে দেওয়া যেতে পারে)

{{< warning >}}
Running a cluster with `kube-proxy` instances that are persistently three minor versions behind
`kube-apiserver` means they must be upgraded before the control plane can be upgraded.
{{</ warning >}}
