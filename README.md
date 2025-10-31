***Note App API – FastAPI Backend***

Bu proje, Connectinno Flutter Developer Case kapsamında oluşturulmuş bir not yönetim API'sidir.
API, kullanıcı kimlik doğrulamasını Supabase üzerinden yapar ve her kullanıcının yalnızca kendi notlarını yönetebilmesini sağlar.

**Özellikler**

FastAPI tabanlı REST API

Supabase veritabanı bağlantısı

JWT doğrulaması (Supabase Auth token’ı)

CRUD işlemleri (create, read, update, delete)

Kullanıcıya özel veri erişimi (user_id doğrulaması)

Hatalı istekler için anlamlı hata mesajları

Temiz, modüler proje yapısı

**Kurulum**
1. Depoyu klonlayın
 
git clone https://github.com/alperenmfol/Note-App-Api.git

cd notes-backend-api

2. Gerekli bağımlılıkları yükleyin

pip install -r requirements.txt

3. Ortam değişkenlerini yapılandırın

Proje kök dizininde bir .env dosyası oluşturun.
Aşağıdaki değişkenleri kendi Supabase projenize göre doldurun:

SUPABASE_URL=

SUPABASE_SERVICE_KEY=

JWT_SECRET=

Ayrıca .env.example dosyası örnek olarak projede mevcuttur.

**Çalıştırma**

1. Sunucuyu başlatın

uvicorn app.main:app --reload veya python run.py



**API Endpoint’leri**

GET	/notes	Kullanıcının notlarını listeler

POST	/notes	Yeni not oluşturur

PUT	/notes/{id}	Belirli bir notu günceller

DELETE	/notes/{id}	Belirli bir notu siler

Güvenlik

Tüm isteklerde Supabase JWT doğrulaması yapılır.

Token geçerli değilse 401 Unauthorized döner.

Kullanıcı yalnızca kendi notlarını görebilir ve düzenleyebilir.
