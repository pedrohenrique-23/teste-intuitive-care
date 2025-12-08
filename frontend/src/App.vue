<!-- <script setup>
import { ref } from 'vue'

const searchTerm = ref('')
const operadoras = ref([])
const loading = ref(false)
const error = ref('')
const hasSearched = ref(false)

const buscarOperadoras = async () => {
  loading.value = true
  error.value = ''
  operadoras.value = []
  hasSearched.value = true

  try {
    const response = await fetch(`http://localhost:5000/operadoras?q=${searchTerm.value}`)
    
    if (!response.ok) throw new Error('Erro ao conectar com o servidor')
    
    operadoras.value = await response.json()
  } catch (e) {
    error.value = 'Erro ao buscar dados. Verifique se o "python src/api.py" está rodando.'
    console.error(e)
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="container">
    <header>
      <h1>🔍 Busca de Operadoras</h1>
      <p>Teste Técnico - Intuitive Care</p>
    </header>

    <div class="search-box">
      <input 
        v-model="searchTerm" 
        @keyup.enter="buscarOperadoras"
        placeholder="Digite o nome da operadora (ex: Unimed)..." 
        type="text"
      />
      <button @click="buscarOperadoras" :disabled="loading">
        {{ loading ? 'Buscando...' : 'Pesquisar' }}
      </button>
    </div>

    <div v-if="error" class="error">{{ error }}</div>

    <div v-if="!loading && operadoras.length > 0" class="results">
      <p class="count">Encontrados {{ operadoras.length }} resultados</p>
      <table>
        <thead>
          <tr>
            <th>Registro ANS</th>
            <th>CNPJ</th>
            <th>Razão Social</th>
            <th>Nome Fantasia</th>
            <th>Modalidade</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="op in operadoras" :key="op.Registro_ANS">
            <td>{{ op.Registro_ANS }}</td>
            <td>{{ op.CNPJ }}</td>
            <td>{{ op.Razao_Social }}</td>
            <td>{{ op.Nome_Fantasia || '-' }}</td> <td>{{ op.Modalidade }}</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-else-if="hasSearched && !loading && operadoras.length === 0" class="no-results">
      Nenhuma operadora encontrada para "{{ searchTerm }}".
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #333;
}

header {
  text-align: center;
  margin-bottom: 2rem;
}

h1 { color: #2c3e50; margin-bottom: 0.5rem; }

.search-box {
  display: flex;
  gap: 10px;
  margin-bottom: 2rem;
}

input {
  flex: 1;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
  outline: none;
}

input:focus { border-color: #42b983; }

button {
  padding: 12px 24px;
  background-color: #42b983; 
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.3s;
}

button:hover { background-color: #3aa876; }
button:disabled { background-color: #ccc; cursor: not-allowed; }

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  border-radius: 8px;
  overflow: hidden;
}

th, td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #eee;
}

th {
  background-color: #2c3e50;
  color: white;
  font-weight: 600;
}

tr:hover { background-color: #f1f1f1; }

.error {
  color: #721c24;
  background-color: #f8d7da;
  border-color: #f5c6cb;
  padding: 1rem;
  border-radius: 4px;
  margin-bottom: 1rem;
}

.count { color: #666; font-size: 0.9rem; text-align: right; margin-bottom: 0.5rem; }
.no-results { text-align: center; color: #666; margin-top: 2rem; font-style: italic; }
</style> -->

<script setup>
import { ref } from 'vue'

const searchTerm = ref('')
const operadoras = ref([])
const loading = ref(false)
const error = ref('')
const hasSearched = ref(false)

const buscarOperadoras = async () => {
  loading.value = true
  error.value = ''
  operadoras.value = []
  hasSearched.value = true

  try {
    const response = await fetch(`http://localhost:5000/operadoras?q=${searchTerm.value}`)
    
    if (!response.ok) throw new Error('Erro ao conectar com o servidor')
    
    operadoras.value = await response.json()
  } catch (e) {
    error.value = 'Erro ao buscar dados. Verifique se o "python src/api.py" está rodando.'
    console.error(e)
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="container">
    <header>
      <h1>🔍 Busca de Operadoras</h1>
      <p>Teste Técnico - Intuitive Care</p>
    </header>

    <div class="search-box">
      <input 
        v-model="searchTerm" 
        @keyup.enter="buscarOperadoras"
        placeholder="Digite o nome da operadora (ex: Unimed)..." 
        type="text"
      />
      <button @click="buscarOperadoras" :disabled="loading">
        {{ loading ? 'Buscando...' : 'Pesquisar' }}
      </button>
    </div>

    <div v-if="error" class="error">{{ error }}</div>

    <div v-if="!loading && operadoras.length > 0" class="results">
      <p class="count">Encontrados {{ operadoras.length }} resultados</p>
      
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Registro ANS</th>
              <th>CNPJ</th>
              <th>Razão Social</th>
              <th>Nome Fantasia</th>
              <th>Modalidade</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="op in operadoras" :key="op.Registro_ANS">
              <td>{{ op.Registro_ANS }}</td>
              <td>{{ op.CNPJ }}</td>
              <td>{{ op.Razao_Social }}</td>
              <td>{{ op.Nome_Fantasia || '-' }}</td> 
              <td>{{ op.Modalidade }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div v-else-if="hasSearched && !loading && operadoras.length === 0" class="no-results">
      Nenhuma operadora encontrada para "{{ searchTerm }}".
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 900px;
  margin: 0 auto;
  padding: 2rem;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #333;
}

header {
  text-align: center;
  margin-bottom: 2rem;
}

h1 { color: #2c3e50; margin-bottom: 0.5rem; }

.search-box {
  display: flex;
  gap: 10px;
  margin-bottom: 2rem;
}

input {
  flex: 1;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
  outline: none;
}

input:focus { border-color: #42b983; }

button {
  padding: 12px 24px;
  background-color: #42b983; 
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  white-space: nowrap;
  transition: background 0.3s;
}

button:hover { background-color: #3aa876; }
button:disabled { background-color: #ccc; cursor: not-allowed; }

.table-wrapper {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

table {
  width: 100%;
  border-collapse: collapse;
  min-width: 600px;
}

th, td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #eee;
  white-space: nowrap;
}

th {
  background-color: #2c3e50;
  color: white;
  font-weight: 600;
}

tr:hover { background-color: #f1f1f1; }

.error {
  color: #721c24;
  background-color: #f8d7da;
  border-color: #f5c6cb;
  padding: 1rem;
  border-radius: 4px;
  margin-bottom: 1rem;
}

.count { color: #666; font-size: 0.9rem; text-align: right; margin-bottom: 0.5rem; }
.no-results { text-align: center; color: #666; margin-top: 2rem; font-style: italic; }

@media (max-width: 600px) {
  .container {
    padding: 1rem;
  }

  .search-box {
    flex-direction: column;
  }

  button {
    width: 100%;
    padding: 14px;
  }

  h1 { font-size: 1.5rem; }
}
</style>