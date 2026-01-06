# Full Stack Developer Capstone Project

A comprehensive car dealership management system built with modern web technologies.

## English

### Overview

This is a full-stack web application for managing car dealerships, inventory, and customer reviews. The system features a React frontend, Django backend, Node.js database service, and a Flask-based sentiment analysis microservice.

### Features

- **User Management**: Registration and authentication system
- **Dealership Management**: Browse and manage car dealerships
- **Inventory Management**: View and manage car inventory
- **Review System**: Post and view dealership reviews with sentiment analysis
- **Microservices**: Sentiment analysis for review text using NLP

### Technology Stack

- **Frontend**: React.js with React Router
- **Backend**: Django (Python)
- **Database Service**: Node.js/Express with MongoDB/Mongoose
- **Microservices**: Flask for sentiment analysis
- **Containerization**: Docker and Docker Compose
- **CI/CD**: GitHub Actions for automated linting

### Project Structure

```
├── server/
│   ├── frontend/          # React frontend application
│   ├── djangoapp/         # Django application
│   ├── database/          # Node.js database service
│   └── microservices/     # Flask sentiment analysis service
├── .github/workflows/     # CI/CD configuration
└── setup.cfg             # Python linting configuration
```

### Getting Started

#### Prerequisites

- Python 3.12+
- Node.js 18+
- Docker and Docker Compose
- MongoDB

#### Installation

1. Clone the repository
2. Install Python dependencies:
   ```bash
   pip install -r server/requirements.txt
   ```

3. Install Node.js dependencies:
   ```bash
   cd server/database
   npm install
   cd ../frontend
   npm install
   ```

4. Set up the database using Docker:
   ```bash
   cd server/database
   docker-compose up -d
   ```

5. Run the Django application:
   ```bash
   cd server
   python manage.py runserver
   ```

6. Run the frontend:
   ```bash
   cd server/frontend
   npm start
   ```

### CI/CD

The project includes GitHub Actions workflows that automatically lint Python and JavaScript code on push and pull requests.

---

## Türkçe

### Genel Bakış

Bu proje, araba bayilikleri, envanter ve müşteri yorumlarını yönetmek için geliştirilmiş kapsamlı bir full-stack web uygulamasıdır. Sistem, React frontend, Django backend, Node.js veritabanı servisi ve Flask tabanlı duygu analizi mikroservisi içermektedir.

### Özellikler

- **Kullanıcı Yönetimi**: Kayıt ve kimlik doğrulama sistemi
- **Bayilik Yönetimi**: Araba bayiliklerini görüntüleme ve yönetme
- **Envanter Yönetimi**: Araba envanterini görüntüleme ve yönetme
- **Yorum Sistemi**: Duygu analizi ile bayilik yorumları yayınlama ve görüntüleme
- **Mikroservisler**: NLP kullanarak yorum metinleri için duygu analizi

### Teknoloji Yığını

- **Frontend**: React.js ve React Router
- **Backend**: Django (Python)
- **Veritabanı Servisi**: Node.js/Express ile MongoDB/Mongoose
- **Mikroservisler**: Duygu analizi için Flask
- **Konteynerleştirme**: Docker ve Docker Compose
- **CI/CD**: Otomatik linting için GitHub Actions

### Proje Yapısı

```
├── server/
│   ├── frontend/          # React frontend uygulaması
│   ├── djangoapp/         # Django uygulaması
│   ├── database/          # Node.js veritabanı servisi
│   └── microservices/     # Flask duygu analizi servisi
├── .github/workflows/     # CI/CD yapılandırması
└── setup.cfg             # Python linting yapılandırması
```

### Başlangıç

#### Gereksinimler

- Python 3.12+
- Node.js 18+
- Docker ve Docker Compose
- MongoDB

#### Kurulum

1. Depoyu klonlayın
2. Python bağımlılıklarını yükleyin:
   ```bash
   pip install -r server/requirements.txt
   ```

3. Node.js bağımlılıklarını yükleyin:
   ```bash
   cd server/database
   npm install
   cd ../frontend
   npm install
   ```

4. Docker kullanarak veritabanını kurun:
   ```bash
   cd server/database
   docker-compose up -d
   ```

5. Django uygulamasını çalıştırın:
   ```bash
   cd server
   python manage.py runserver
   ```

6. Frontend'i çalıştırın:
   ```bash
   cd server/frontend
   npm start
   ```

### CI/CD

Proje, push ve pull request'lerde Python ve JavaScript kodlarını otomatik olarak lint eden GitHub Actions iş akışları içermektedir.

---

## License

See LICENSE file for details.
