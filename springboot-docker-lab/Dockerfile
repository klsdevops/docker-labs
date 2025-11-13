# --------------------------------------------------------------------------------
# STAGE 1: Build the Spring Boot Application (using a dedicated Maven image)
# --------------------------------------------------------------------------------

# Use a standard Maven image with JDK 17 as the build environment
FROM maven:3.9.5-eclipse-temurin-17 AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy the Maven project file first to cache dependencies efficiently
COPY pom.xml .

# Copy the source code directory (MUST match the local structure)
COPY src ./src

# Build the Spring Boot application
RUN mvn clean package -DskipTests

# --------------------------------------------------------------------------------
# STAGE 2: Create the final, minimal Runtime Image
# --------------------------------------------------------------------------------

# Use a lightweight JRE image for the final runtime (smaller size, more secure)
FROM eclipse-temurin:17-jre-focal

# Set a label for the maintainer 
LABEL maintainer="docker-user@example.com"

# Expose the port the Spring Boot application runs on (default is 8080)
EXPOSE 8080

# Define the argument for the application JAR file name
ARG JAR_FILE=target/demo-0.0.1-SNAPSHOT.jar

# Copy the executable JAR from the 'builder' stage into the final image
COPY --from=builder /app/${JAR_FILE} app.jar

# The entry point command to run the application
ENTRYPOINT ["java", "-jar", "/app.jar"]