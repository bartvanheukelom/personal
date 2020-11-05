plugins {
    id("org.jetbrains.kotlin.js") version "1.4.10"
}

repositories {
    mavenCentral()
}

dependencies {
    implementation(kotlin("stdlib-js"))
}

kotlin {
    js(IR) {
        nodejs()
        binaries.executable()
    }
}