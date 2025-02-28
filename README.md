# Group Tasks Repository

This repository is designed for submitting group programming tasks for the Advanced Python course. Please follow these instructions carefully to submit your group's work.

## Repository Structure

Each group has their own designated folder within this repository. Only group leaders have write access to their group's folder as specified in the CODEOWNERS file.

## How to Submit Group Tasks

### 1. Initial Setup (All Group Members)
```bash
# Clone the repository
git clone <repository-url>
cd Group-Tasks

# Create and switch to a new branch for your feature
git checkout -b task/group-<number>/feature-name
```

### 2. Adding Your Work (All Group Members)
- Place your files ONLY in your group's designated folder
- Make sure to include:
  - Source code files (.py)
  - Requirements.txt (if needed)
  - Documentation explaining your solution
  - Your name and contribution description

### 3. Collaboration Process
1. Each group member can:
   - Create new branches for their features
   - Commit and push their code
   - Create pull requests to the group's task branch
2. Group leader is responsible for:
   - Reviewing pull requests from team members
   - Approving or requesting changes
   - Ensuring code quality and consistency
   - Managing the final submission

### 4. Committing and Pushing (All Group Members)
```bash
# Add your changes
git add your-group-folder/*

# Commit with a descriptive message
git commit -m "Add feature X for Group Task Y"

# Push to your feature branch
git push origin task/group-<number>/feature-name
```

### 5. Creating Pull Requests
1. Group members:
   - Create pull requests to the group's task branch
   - Write clear descriptions of their contributions
   - Address review comments from the group leader
2. Group leader:
   - Reviews and manages pull requests
   - Ensures all contributions are properly integrated
   - Creates the final pull request to main branch

## Important Notes

- ⚠️ Never commit directly to the main branch
- ⚠️ Only modify files within your group's folder
- ✅ Create feature branches for your contributions
- ✅ Wait for group leader's review before merging
- ✅ Group leader approves final submission to main
- ❌ Pull requests modifying other groups' folders will be rejected

## Best Practices

1. Coordinate with your group members effectively
2. Use consistent coding style across the group
3. Review each other's code before submission
4. Test thoroughly as a group
5. Document group decisions and implementation choices

## Need Help?

If you encounter any issues with the group submission process, please contact the course instructor or teaching assistants.

---

<div dir="rtl">

# مخزن تکالیف گروهی

این مخزن برای ارسال تکالیف برنامه‌نویسی گروهی دوره پایتون پیشرفته طراحی شده است. لطفاً این دستورالعمل‌ها را برای ارسال کار گروه خود با دقت دنبال کنید.

## ساختار مخزن

هر گروه در این مخزن یک پوشه اختصاصی دارد. همه اعضای گروه می‌توانند کد را تغییر دهند و درخواست pull بدهند.

## نحوه ارسال تکالیف گروهی

### ۱. راه‌اندازی اولیه (همه اعضای گروه)
```bash
# Clone کردن مخزن
git clone <repository-url>
cd Group-Tasks

# ایجاد و تغییر به شاخه جدید برای ویژگی
git checkout -b task/group-<number>/feature-name
```

### ۲. اضافه کردن کار (همه اعضای گروه)
- فایل‌ها را فقط در پوشه گروه خود قرار دهید
- حتماً موارد زیر را شامل شود:
  - فایل‌های کد منبع (.py)
  - Requirements.txt (در صورت نیاز)
  - مستندات توضیح راه‌حل
  - نام و شرح مشارکت شما

### ۳. فرآیند همکاری
۱. هر عضو گروه می‌تواند:
   - شاخه‌های جدید برای ویژگی‌ها ایجاد کند
   - کد را commit و push کند
   - به شاخه تکلیف گروه درخواست pull بدهد
۲. سرگروه مسئول است:
   - بررسی درخواست‌های pull از اعضای تیم
   - تأیید یا درخواست تغییرات
   - اطمینان از کیفیت کد
   - مدیریت ارسال نهایی

### ۴. Commit و Push (همه اعضای گروه)
```bash
# اضافه کردن تغییرات
git add your-group-folder/*

# Commit با پیام توصیفی
git commit -m "اضافه کردن ویژگی X برای تکلیف گروه Y"

# Push به شاخه ویژگی
git push origin task/group-<number>/feature-name
```

### ۵. ایجاد درخواست‌های Pull
۱. اعضای گروه:
   - درخواست‌های pull به شاخه تکلیف گروه ایجاد کنند
   - توضیحات واضحی از مشارکت‌های خود بنویسند
   - به نظرات بررسی از سرگروه پاسخ دهند
۲. سرگروه:
   - درخواست‌های pull را بررسی و مدیریت کند
   - اطمینان حاصل کند که همه مشارکت‌ها به درستی ادغام شده‌اند
   - درخواست نهایی را به شاخه اصلی ایجاد کند

## نکات مهم

- ⚠️ هرگز به شاخه اصلی مستقیماً commit نکنید
- ⚠️ فقط فایل‌های داخل پوشه گروه خود را تغییر دهید
- ✅ برای مشارکت‌های خود شاخه‌های ویژگی ایجاد کنید
- ✅ قبل از ادغام، منتظر بررسی سرگروه باشید
- ✅ سرگروه تأیید نهایی را به شاخه اصلی انجام دهد
- ❌ درخواست‌های pull که پوشه‌های گروه‌های دیگر را تغییر می‌دهند، رد خواهند شد

## بهترین روش‌ها

۱. با اعضای گروه خود به طور مؤثر هماهنگ کنید
۲. از سبک کدنویسی یکسان در سراسر گروه استفاده کنید
۳. کد یکدیگر را قبل از ارسال بررسی کنید
۴. به عنوان یک گروه به طور کامل تست کنید
۵. تصمیمات گروه و انتخاب‌های پیاده‌سازی را مستند کنید

## نیاز به کمک دارید؟

اگر در فرآیند ارسال گروهی با مشکلی مواجه شدید، لطفاً با مدرس دوره یا دستیاران آموزشی تماس بگیرید.

</div>