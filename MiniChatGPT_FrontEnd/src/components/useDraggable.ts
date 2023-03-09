import { ref, onMounted, onUnmounted } from 'vue'

export default function useDraggable() {
    const isDragging = ref(false)
    const startX = ref(0)
    const startY = ref(-30)
    const dragX = ref(0)
    const dragY = ref(-30)

    const handleMouseDown = (e: MouseEvent) => {
        isDragging.value = true
        startX.value = e.clientX
        startY.value = e.clientY
    }

    const handleMouseMove = (e: MouseEvent) => {
        if (isDragging.value) {
            dragX.value += e.clientX - startX.value
            dragY.value += e.clientY - startY.value
            startX.value = e.clientX
            startY.value = e.clientY
        }
    }

    const handleMouseUp = () => {
        isDragging.value = false
    }

    const enableDragging = () => {
        window.addEventListener('mousedown', handleMouseDown)
        window.addEventListener('mousemove', handleMouseMove)
        window.addEventListener('mouseup', handleMouseUp)
    }

    const disableDragging = () => {
        window.removeEventListener('mousedown', handleMouseDown)
        window.removeEventListener('mousemove', handleMouseMove)
        window.removeEventListener('mouseup', handleMouseUp)
    }

    onMounted(() => {
        enableDragging()
    })

    onUnmounted(() => {
        disableDragging()
    })

    return {
        isDragging,
        dragX,
        dragY,
        enableDragging,
        disableDragging,
    }
}
