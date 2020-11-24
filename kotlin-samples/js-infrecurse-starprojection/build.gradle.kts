plugins {
    id("org.jetbrains.kotlin.js") version "1.4.20-RC"
}

repositories {
    mavenCentral()
    maven("https://dl.bintray.com/kotlin/kotlin-eap")
    maven("https://kotlin.bintray.com/kotlinx")
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