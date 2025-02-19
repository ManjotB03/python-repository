# Introduction to NoSQL and MongoDB

## What is a Database?
A **database** is an organized collection of structured information or data, typically stored electronically. Its primary purpose is to keep information organized and easily accessible.

## Understanding SQL Databases
Before introducing NoSQL databases, it's important to understand **SQL databases**:

- **SQL Database (Relational Database):** Stores data in tables with predefined relationships between them.
- **Relational Data Model:** Avoids data redundancy by linking related information across different tables.

### Example:
Consider a database containing information about customer orders:
- **Orders Table:** Contains order details.
- **Customers Table:** Contains customer details (e.g., address, email, personal information).
- **Stores Table:** Contains information about physical stores or websites.

Relationships:
- **Orders Table** includes `CustomerID` → Links to **Customers Table**.
- **Orders Table** includes `StoreID` → Links to **Stores Table**.

Query Example: To find the total order value for order number `104` and the customer's email address, SQL queries are used to retrieve and combine data from these tables.

## Introduction to NoSQL Databases
**NoSQL databases** store data in a **non-tabular format**. There are several types of NoSQL databases:

### 1. Document Databases (e.g., MongoDB):
- Store data as **documents** containing field-value pairs.
- Documents can include arrays and nested documents.
- Documents are grouped into **collections**.

### 2. Key-Value Databases:
- Store data as **key-value pairs**.
- Each key is unique.
- Simplest type of NoSQL database.

### 3. Wide-Column Databases:
- Store data in **columns** rather than rows.

### 4. Graph Databases:
- Specialize in **network data** and **highly interrelated datasets**.
- Useful for representing organizational hierarchies or social networks.

## Focus of the Course
The primary focus of this course is on **document databases**, specifically **MongoDB**. Subsequent lectures will explore MongoDB in more detail.

# MongoDB as a Document Database

## Overview
MongoDB is a **document database** that stores data as **field-value pairs** inside **documents**. These documents are organized into **collections**, and collections are stored inside the **database**.

## Flexible and Polymorphic Structure
One of MongoDB's key strengths is that its documents are **polymorphic**, meaning they have a **flexible structure**. Unlike relational databases, MongoDB is **schemaless**:
- Each document can contain different fields.
- Documents in the same collection can have **similar but not identical structures**.
- You can **store as much information as possible within a single document**.

## Example
Consider the following two documents in a customer collection:

**Document 1:**
```json
{
  "CustomerID": 1,
  "Name": "John Doe",
  "Email": "john@example.com",
  "Address": "123 Main St"
}
```

**Document 2:**
```json
{
  "CustomerID": 2,
  "Name": "Jane Smith",
  "Email": "jane@example.com",
  "Address": "456 Elm St",
  "PhoneNumber": "123-456-7890"
}
```

- **Document 1** contains four fields.
- **Document 2** contains an additional field, `PhoneNumber`.
- Both documents are part of the **same collection**, but they **differ in structure**.

## Comparison with SQL Databases
In **SQL databases**, the structure is **rigid**:
- Adding a new field like `PhoneNumber` requires **adding a new column**.
- Rows **without a phone number** will **store null values**.
- Adding columns can **affect table constraints and relationships**.
- Large tables with many columns often result in **many null values and redundant data**.

## Key Benefits of MongoDB
- **Flexible structure:** Easily adapt to data structure changes.
- **Efficient storage:** Each document **stores only the field-value pairs it needs**.
- **Simpler modifications:** Adding fields does not require altering the entire collection.

## Conclusion
MongoDB's **polymorphic and schemaless nature** makes it **adaptable to changes in data structure** and **efficient in storage**, offering **greater flexibility** compared to traditional SQL databases.

# MongoDB Document Structure

## Overview
MongoDB databases contain **collections**, and collections contain **documents**. Documents are made up of **key-value pairs** that represent information.

## JSON Format
Documents in MongoDB use the **JSON format** (JavaScript Object Notation):
- Documents **start and end with curly braces `{}`**.
- **Key-value pairs** are **separated by colons `:`**.
- **Keys and string values** must be **enclosed in double quotes `""`**.
- **Key-value pairs** are **separated by commas `,`**.

Example:
```json
{
  "CustomerID": 1,
  "Name": "John Doe",
  "Email": "john@example.com",
  "Address": "123 Main St"
}
```

## Unique Identifier (_id)
Each document **contains a unique identifier field called `_id`**:
- If not specified, **MongoDB automatically generates `_id`**.
- The `_id` field **is unique within a collection**.

Example:
```json
{
  "_id": "abc123",
  "CustomerID": 1,
  "Name": "John Doe",
  "Email": "john@example.com",
  "Address": "123 Main St"
}
```

## Subdocuments (Embedded Documents)
MongoDB allows **embedding documents inside other documents**:
- This is known as **Subdocuments**.
- Subdocuments **start and end with curly braces `{}`** within a field.

Example:
```json
{
  "CustomerID": 1,
  "Name": "John Doe",
  "Email": "john@example.com",
  "Address": {
    "Street": "123 Main St",
    "Town": "Springfield",
    "Postcode": "SP1 2AB"
  }
}
```

## Arrays
MongoDB allows **storing arrays as values**:
- Arrays **start and end with square brackets `[]`**.
- Values **inside arrays are separated by commas `,`**.

Example:
```json
{
  "CustomerID": 1,
  "Name": "John Doe",
  "PhoneNumbers": ["123-456-7890", "987-654-3210"]
}
```

## Flexible Structure
MongoDB is **schemaless and polymorphic**:
- **Documents in the same collection can have different fields**.
- This **allows for flexibility**, but **consistent field names across documents are recommended** to **avoid query issues**.

Example:
```json
{
  "CustomerID": 1,
  "Phone": "123-456-7890"
}

{
  "CustomerID": 2,
  "CellPhone": "987-654-3210"
}
```
In the above example, **`Phone`** and **`CellPhone`** are different fields, which can cause **inconsistencies during queries**.

## Data Types
MongoDB **supports various data types**, such as:
- **Strings**
- **Numbers**
- **Dates**
- **Booleans**
- **Arrays**
- **Subdocuments**

Fields can **store different data types** unless **explicitly restricted**:
```json
{
  "Values": ["Text", 123, {"Nested": true}]
}
```

## Key Takeaways
- **Documents** use **JSON format** with **key-value pairs**.
- Each document **has a unique `_id` field**.
- **Subdocuments** and **arrays** are supported.
- **Flexible structure**, but **consistent field names are advised**.
- **Supports multiple data types** for flexibility.

Refer to the **official MongoDB documentation** for **a complete list of supported data types**.

# MongoDB Ecosystem

## Overview

MongoDB offers a range of products, with the **document database** being the core component. This database stores data in the form of **collections** and **documents** containing **key-value pairs**.

## Deployment Options

### On-Premises Solutions

- **Community Edition**: Free and open-source version.
- **Enterprise Edition**: Includes additional **operational and management features**.

### Cloud Solutions

- **MongoDB Atlas**: Fully managed cloud database solution hosted on:
  - **AWS**
  - **Microsoft Azure**
  - **Google Cloud Platform**
- **Free tier available (512 MB of storage)**, sufficient for training purposes.
- **Atlas represents over 50% of MongoDB’s revenue** due to its popularity.

## Visualization & Mobile Solutions

- **MongoDB Charts**: Tool to **visualize data stored in MongoDB databases**.
- **MongoDB Realm**: Suite of **services for mobile application development**.
- **Mobile Database**: Allows **MongoDB usage on mobile devices**.

## Supporting Tools

### Shell

- **Mongo Shell**: Command-line interface to **interact with MongoDB databases**.

### Drivers

- **MongoDB Drivers**: Allow developers to **write queries in various programming languages**, such as:
  - **JavaScript**
  - **Python**

### API Connectors

- **API Connectors**: Integrate **MongoDB with third-party tools**, such as:
  - **QlikSense**
  - **Tableau**

### Compass

- **MongoDB Compass**: Graphical User Interface (GUI) to **interact with MongoDB databases** from a local system.
- Provides a **user-friendly interface for working with data**.

## Operational & Management Solutions

MongoDB offers **additional tools** to **support operational and management tasks**, improving **database performance and maintenance**.

## Key Takeaways

- **Core product is the document database** with **on-premises and cloud options**.
- **MongoDB Atlas is a fully managed cloud solution**.
- **MongoDB Charts, Realm, and Mobile** provide **data visualization and mobile development capabilities**.
- **Shell, Drivers, API Connectors, and Compass** simplify **database interaction and integration**.
- **Operational tools** enhance **database management**.

# MongoDB Document Structure

## Overview

MongoDB databases contain **collections**, and collections contain **documents**. Documents are made up of **key-value pairs** that represent information.

## JSON Format

Documents in MongoDB use the **JSON format** (JavaScript Object Notation):

- Documents **start and end with curly braces \*\*\*\*\*\*\*\*****`{}`**.
- **Key-value pairs** are **separated by colons \*\*\*\*\*\*\*\*****`:`**.
- **Keys and string values** must be **enclosed in double quotes \*\*\*\*\*\*\*\*****`""`**.
- **Key-value pairs** are **separated by commas \*\*\*\*\*\*\*\*****`,`**.

Example:

```json
{
  "CustomerID": 1,
  "Name": "John Doe",
  "Email": "john@example.com",
  "Address": "123 Main St"
}
```

## Unique Identifier (\_id)

Each document **contains a unique identifier field called \*\*\*\*\*\*\*\*****`_id`**:

- If not specified, **MongoDB automatically generates \*\*\*\*\*\*\*\*****`_id`**.
- The `_id` field **is unique within a collection**.

Example:

```json
{
  "_id": "abc123",
  "CustomerID": 1,
  "Name": "John Doe",
  "Email": "john@example.com",
  "Address": "123 Main St"
}
```

## Subdocuments (Embedded Documents)

MongoDB allows **embedding documents inside other documents**:

- This is known as **Subdocuments**.
- Subdocuments \*\*start and end with curly braces \*\***`{}`** within a field.

Example:

```json
{
  "CustomerID": 1,
  "Name": "John Doe",
  "Email": "john@example.com",
  "Address": {
    "Street": "123 Main St",
    "Town": "Springfield",
    "Postcode": "SP1 2AB"
  }
}
```

## Arrays

MongoDB allows **storing arrays as values**:

- Arrays **start and end with square brackets \*\*\*\*\*\*\*\*****`[]`**.
- Values **inside arrays are separated by commas \*\*\*\*\*\*\*\*****`,`**.

Example:

```json
{
  "CustomerID": 1,
  "Name": "John Doe",
  "PhoneNumbers": ["123-456-7890", "987-654-3210"]
}
```

## Flexible Structure

MongoDB is **schemaless and polymorphic**:

- **Documents in the same collection can have different fields**.
- This **allows for flexibility**, but **consistent field names across documents are recommended** to **avoid query issues**.

Example:

```json
{
  "CustomerID": 1,
  "Phone": "123-456-7890"
}

{
  "CustomerID": 2,
  "CellPhone": "987-654-3210"
}
```

In the above example, **`Phone`** and **`CellPhone`** are different fields, which can cause **inconsistencies during queries**.

## Data Types

MongoDB **supports various data types**, such as:

- **Strings**
- **Numbers**
- **Dates**
- **Booleans**
- **Arrays**
- **Subdocuments**

Fields can **store different data types** unless **explicitly restricted**:

```json
{
  "Values": ["Text",r 123, {"Nested": true}]
}
```

## MongoDB Replica Sets and Clusters

MongoDB offers a range of products and tools to manage and interact with your databases:

### MongoDB Database

- **Community Edition**: Free, open-source version.
- **Enterprise Edition**: Paid version with additional features for operational and management purposes.
- **MongoDB Atlas**: Fully managed cloud database hosted on AWS, Azure, or Google Cloud Platform. The **free tier includes up to 512 MB of storage**.

### MongoDB Charts

- **Visualize your data stored in MongoDB databases**.

### MongoDB Realm

- **Suite of services for mobile application development**.
- **Mobile solution** to **run MongoDB on mobile devices**.

### Supporting Tools

- **Mongo Shell**: Command-line interface to interact with MongoDB.
- **Drivers**: Write queries in languages like **JavaScript** and **Python**.
- **API Connectors**: Integrate MongoDB with tools like **QlikSense** and **Tableau**.
- **MongoDB Compass**: GUI tool to **interact with MongoDB databases** from your local machine.

## Distributed Systems in MongoDB

MongoDB offers **distributed data solutions** for **fault tolerance, scalability, and performance**:

### Replica Sets

- **Group of 3 machines (instances)**.
- **Each machine contains a complete replica of data**.
- **Ensures data availability** if one machine fails.

### Sharded Clusters

- **Partitions data across multiple servers**.
- **Consists of the following components**:
  - **Shards**: Store a subset of the data.
  - **Mongos**: Query router that interfaces between applications and the sharded cluster.
  - **Config Servers**: Store metadata and configuration settings.

### Sharding Example

MongoDB **uses a shard key** to **distribute data across shards**:

- Example: Customers with **names A-H on Shard 1**, **I-P on Shard 2**, and **Q-Z on Shard 3**.

### Key Benefits

- **Fault Tolerance**: Data replication ensures data is available during failures.
- **Scalability**: Sharding increases storage capacity as data volume grows.
- **Data Locality**: Deploy data close to users, e.g., **European customers in Europe** and **American customers in North America**.

## Key Takeaways

- **Documents** use **JSON format** with **key-value pairs**.
- Each document **has a unique ************`_id`************ field**.
- **Subdocuments** and **arrays** are supported.
- **Flexible structure**, but **consistent field names are advised**.
- **Supports multiple data types** for flexibility.
- **MongoDB Product Suite** includes **Atlas, Charts, Realm, Compass, Shell, Drivers, and more**.
- **Replica Sets and Sharded Clusters** provide **fault tolerance and scalability**.

Refer to the **official MongoDB documentation** for **a complete list of supported data types and detailed information**.

# Benefits of MongoDB

## Introduction
Throughout this module, we have explored how MongoDB databases work and the various benefits they offer. This lecture consolidates those benefits into a single overview.

## Relational Databases vs. MongoDB
### Structure
In a **relational database**, data is stored in **multiple related tables**. Queries often require **joining multiple tables** to retrieve data.

Example:
- You need the **order details for order ID 1104** and the **customer's email address**.
- This would require **querying multiple tables** and performing **joins** to **compile the result into a single set**.
- **Joins can become complex** when **multiple tables** are involved.

### Flexibility
MongoDB **stores data more efficiently and flexibly**:
- **Documents within the same collection can have different fields and values**.
- **Values can be embedded or stored as arrays**.
- **Fields can hold multiple data types** (e.g., **a string in one document and a date in another**).

## Key Benefits
### Simplicity
MongoDB’s **flexibility allows more data to be stored in a single collection**, reducing the need for complex queries:
- **Simpler queries** lead to **reduced complexity**.
- **Applications working with MongoDB benefit from easier data reading and writing processes**.

### Polymorphic Nature
- **Polymorphic data model** allows for **storing various types of data**.
- **Collections can evolve over time** without needing strict schemas.

### Schemaless
MongoDB is **schemaless**, meaning:
- **Fewer restrictions** on data structure.
- **Easier updates and modifications** to data fields.

### Maintenance
- **Easier maintenance** compared to relational databases.
- **No foreign key constraints**.
- **No need to manage relationships across multiple tables**.

## Scalability
### Horizontal Scaling
MongoDB **supports horizontal scaling**:
- **Easily add more instances (nodes) to your cluster** as **data volume grows**.
- **Data can be distributed across multiple servers**.

### Big Data Handling
- **Handles large volumes of data** efficiently.
- **Meets modern data demands** for performance and scalability.

## Conclusion
MongoDB’s **flexible document model**, **schemaless nature**, and **horizontal scalability** make it **a robust solution** for **handling complex and evolving data needs**. These **benefits simplify data management** and **enhance application performance** in **today’s big data landscape**.

# Communicating with MongoDB Databases

## Mongo Query Language (MQL)
To communicate with MongoDB databases, you can use **Mongo Query Language (MQL)**.

### Key Points About MQL:
- **Imperative Language:** MQL is an **imperative language**, meaning **you explicitly tell MongoDB what actions to perform**.
- **Ease of Learning:** It **isn't difficult to pick up**, and we will **cover it soon in this course**.
- **Designed for Simple Queries:** MQL is **primarily designed for performing simple queries across single collections**.

## Aggregation Pipeline
For **more complex queries**, such as **aggregating data**, you can use the **MongoDB Aggregation Pipeline**.

### How the Aggregation Pipeline Works:
- **Stage-Based Processing:** The pipeline **breaks operations into stages**, with **each stage processing the data and passing the results to the next stage**.
- **Sequential Operations:** Operations **are executed in a specific sequence**.

### Example:
Imagine you want to **filter your results first** and **then group them**:
1. **First Stage:** Filter the results.
2. **Second Stage:** Group the results.

Each **stage processes the data before passing it to the next stage**, enabling **efficient data transformations**.



